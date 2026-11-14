# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.paginator import Paginator

from core.mood.models import MoodLogEntry, MentalStateProfile
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
        reason = body.get('reason_summary', body.get('reason', ''))
        notes = body.get('clinician_notes', '')

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

        entry = MoodLogEntry.objects.create(
            entity_id=entity_id,
            mood_mask=m_mask,
            cognitive_mask=c_mask,
            interaction_mask=i_mask,
            context_mask=ctx_mask,
            protection_mask=p_mask,
            mood_label=label,
            ui_color_hex=color,
            reason_summary=reason,
            clinician_notes=notes
        )

        last_10 = list(MoodLogEntry.objects.filter(entity_id=entity_id)[:10].values(
            'timestamp', 'mood_label', 'ui_color_hex', 'reason_summary'
        ))
        return JsonResponse({
            'status': 'logged',
            'id': entry.id,
            'current': {
                'timestamp': entry.timestamp.isoformat(),
                'mood_label': entry.mood_label,
                'color_hex': entry.ui_color_hex,
                'reason_summary': entry.reason_summary
            },
            'last_10': last_10
        }, status=201)

    # GET request returns current + last 10 as JSON
    entity_id = request.GET.get('entity_id', 'user.primary')
    qs = MoodLogEntry.objects.filter(entity_id=entity_id)
    latest = qs.first()
    last_10 = list(qs[:10].values('timestamp', 'mood_label', 'ui_color_hex', 'reason_summary', 'mood_mask'))
    
    current_data = None
    if latest:
        report = compile_auticoach_profile(
            latest.mood_mask, latest.cognitive_mask, latest.interaction_mask,
            latest.context_mask, latest.protection_mask
        )
        current_data = {
            'timestamp': latest.timestamp.isoformat(),
            'mood_label': latest.mood_label,
            'color_hex': latest.ui_color_hex,
            'reason_summary': latest.reason_summary,
            'assist_report': report
        }

    return JsonResponse({'current': current_data, 'last_10': last_10})


def public_mood_dashboard(request):
    """
    GET /mood/monitor/
    Minimal-footprint webpage showing Current Mood, Last 10 Moods timeline,
    and a paginated clinical audit table for doctors/psychiatrists.
    """
    entity_id = request.GET.get('entity_id', 'user.primary')
    qs = MoodLogEntry.objects.filter(entity_id=entity_id)
    latest = qs.first()
    last_10_qs = qs[:10]

    current_assist = None
    if latest:
        current_assist = compile_auticoach_profile(
            latest.mood_mask, latest.cognitive_mask, latest.interaction_mask,
            latest.context_mask, latest.protection_mask
        )

    paginator = Paginator(qs, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    last_10_items = []
    for item in last_10_qs:
        rep = compile_auticoach_profile(
            item.mood_mask, item.cognitive_mask, item.interaction_mask,
            item.context_mask, item.protection_mask
        )
        last_10_items.append({
            'timestamp': item.timestamp.strftime('%Y-%m-%d %H:%M'),
            'mood_label': item.mood_label,
            'color_hex': item.ui_color_hex,
            'reason_summary': item.reason_summary,
            'assist_summary': rep.get('status_title', 'Stable')
        })

    return render(request, 'mood_dashboard.html', {
        'entity_id': entity_id,
        'current_entry': latest,
        'current_assist': current_assist,
        'last_10': last_10_items,
        'page_obj': page_obj
    })
