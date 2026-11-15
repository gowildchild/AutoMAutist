# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.paginator import Paginator
from django.utils import timezone
from core.mood.models import (
    MoodLogEntry,
    MentalStateProfile,
    EmotionalMoodTag,
    SystemControlState,
)
from core.assist.engine import compile_auticoach_profile
from core.assist.flags import mental_states

@csrf_exempt
def ingest_mood_telemetry(request):
    """
    POST /api/mood/log
    Minimal footprint ingestion endpoint for ESPHome/Home Assistant or local widgets.
    Stores mood, reason_summary, color, and bitmasks, returning current + last 10 entries.
    """
    if request.method == 'POST':
        try:
            body = json.loads(request.body) if request.body else {}
        except Exception:
            body = request.POST.dict()

        entity_id = body.get('entity_id', 'user.primary')
        m_mask = int(body.get('mood_mask', body.get('state_mask', 1)))
        c_mask = int(body.get('cognitive_mask', 0))
        i_mask = int(body.get('interaction_mask', 0))
        ctx_mask = int(body.get('context_mask', 0))
        p_mask = int(body.get('protection_mask', 0))
        reason = str(body.get('reason_summary', body.get('reason', ''))).strip()
        emotional_mood = str(body.get('emotional_mood', '')).strip()
        notes = str(body.get('clinician_notes', '')).strip()
        skip_log = str(body.get('skip_log', 'false')).lower() in ('true', '1', 'yes', 'on')

        label = "Fine"
        color = "#198754"
        try:
            profile = MentalStateProfile.objects.get(state_mask=m_mask)
            label = profile.label
            color = profile.ui_color_hex
        except MentalStateProfile.DoesNotExist:
            for s in mental_states:
                if s.value and (m_mask & s.value):
                    label = s.name.replace("MOOD_", "").title()
                    break


        ctrl, _ = SystemControlState.objects.get_or_create(entity_id=entity_id)
        ctrl.active_mood_mask = m_mask
        ctrl.active_mood_label = label
        ctrl.active_color_hex = color
        ctrl.active_emotional_mood = emotional_mood
        ctrl.active_reason = reason
        ctrl.save()

        entry_id = None
        now_iso = timezone.now().isoformat()
        if not skip_log:
            entry = MoodLogEntry.objects.create(
                entity_id=entity_id,
                mood_mask=m_mask,
                cognitive_mask=c_mask,
                interaction_mask=i_mask,
                context_mask=ctx_mask,
                protection_mask=p_mask,
                mood_label=label,
                ui_color_hex=color,
                emotional_mood=emotional_mood,
                reason_summary=reason,
                clinician_notes=notes,
            )
            entry_id = entry.id
            now_iso = entry.timestamp.isoformat()

        last_10 = list(MoodLogEntry.objects.filter(entity_id=entity_id, is_active=True)[:10].values(
            'timestamp', 'mood_label', 'emotional_mood', 'ui_color_hex', 'reason_summary'
        ))
        return JsonResponse({
            'status': 'updated_unlogged' if skip_log else 'logged',
            'logged': not skip_log,
            'id': entry_id,
            'cast_assist_enabled': ctrl.cast_assist_enabled,
            'current': {
                'timestamp': now_iso,
                'mood_mask': m_mask,
                'mood_label': label,
                'emotional_mood': emotional_mood,
                'color_hex': color,
                'reason_summary': reason,
            },
            'last_10': last_10
        }, status=201)


@csrf_exempt
def toggle_cast_assist(request):
    """POST /api/cast/toggle/ — Temporarily mute or enable Cast Assist alerts."""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        body = json.loads(request.body) if request.body else {}
    except Exception:
        body = request.POST.dict()

    entity_id = body.get('entity_id', 'user.primary')
    ctrl, _ = SystemControlState.objects.get_or_create(entity_id=entity_id)
    if 'enabled' in body:
        ctrl.cast_assist_enabled = str(body['enabled']).lower() in ('true', '1', 'yes', 'on')
    else:
        ctrl.cast_assist_enabled = not ctrl.cast_assist_enabled
    ctrl.save(update_fields=['cast_assist_enabled', 'updated_at'])

    return JsonResponse({
        'status': 'ok',
        'cast_assist_enabled': ctrl.cast_assist_enabled,
    })


@csrf_exempt
def manage_emotional_tags(request):
    """POST /api/mood/tags/ — Add or delete everyday emotional diary moods."""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        body = json.loads(request.body) if request.body else {}
    except Exception:
        body = request.POST.dict()

    action = body.get('action', 'add')
    if action == 'delete':
        tag_id = body.get('id')
        EmotionalMoodTag.objects.filter(id=tag_id).delete()
    else:
        name = str(body.get('name', '')).strip()
        emoji = str(body.get('emoji', '🙂')).strip() or '🙂'
        if not name:
            return JsonResponse({'error': 'Mood name is required'}, status=400)
        EmotionalMoodTag.objects.get_or_create(
            name__iexact=name,
            defaults={'name': name, 'emoji': emoji, 'is_default': False},
        )

    tags = list(EmotionalMoodTag.objects.all().values('id', 'name', 'emoji', 'is_default'))
    return JsonResponse({'status': 'ok', 'tags': tags})


def _format_duration(delta) -> str:
    total_mins = max(0, int(delta.total_seconds() // 60))
    if total_mins < 1:
        return "<1m"
    days, rem = divmod(total_mins, 1440)
    hours, mins = divmod(rem, 60)
    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if mins or not parts:
        parts.append(f"{mins}m")
    return " ".join(parts)


def public_mood_dashboard(request):
    """GET /mood/monitor/ — Compact Mood Diary & Clinical Archive with human-readable durations."""
    entity_id = request.GET.get('entity_id', 'user.primary')
    qs = list(MoodLogEntry.objects.filter(entity_id=entity_id, is_active=True)[:250])
    now = timezone.now()

    enriched = []
    for idx, entry in enumerate(qs):
        end_time = now if idx == 0 else qs[idx - 1].timestamp
        dur_str = "Active (" + _format_duration(end_time - entry.timestamp) + ")" if idx == 0 else _format_duration(end_time - entry.timestamp)
        rep = compile_auticoach_profile(
            entry.mood_mask, entry.cognitive_mask, entry.interaction_mask,
            entry.context_mask, entry.protection_mask
        )
        enriched.append({
            'id': entry.id,
            'timestamp': entry.timestamp,
            'timestamp_short': entry.timestamp.strftime('%Y-%m-%d %H:%M'),
            'mood_label': entry.mood_label,
            'emotional_mood': entry.emotional_mood,
            'color_hex': entry.ui_color_hex,
            'reason_summary': entry.reason_summary,
            'clinician_notes': entry.clinician_notes,
            'duration': dur_str,
            'assist_summary': rep.get('status_title', 'Stable'),
        })

    latest = qs[0] if qs else None
    current_assist = None
    if latest:
        current_assist = compile_auticoach_profile(
            latest.mood_mask, latest.cognitive_mask, latest.interaction_mask,
            latest.context_mask, latest.protection_mask
        )

    paginator = Paginator(enriched, 25)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'dashboard_mood.html', {
        'entity_id': entity_id,
        'current_entry': latest,
        'current_assist': current_assist,
        'last_10': enriched[:10],
        'page_obj': page_obj,
    })
