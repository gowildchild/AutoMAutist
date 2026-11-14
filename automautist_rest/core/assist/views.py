#################### ########### ######## ####### ####### ###### ## * . 
####### AutoMAutist - Digital Autism Assistant, Coach and Caretaker       d  
######       .                                                        *  d8  
##### e            d8 *            e    e  .   e        +   8   ,e  d8   d8 *
#### d8b   88__88_d88__ e88~-_    d8b  d8b    d8b__ 88 ____d8____"_d88 __d8__
### /Y88b  88  88 888  d888   i  d888bdY88b  /Y8b   88  88 88   88 C8    88 .
## /  Y88b 88  88 888  8888   | / Y88Y Y888b/  Y8b  88  88 88   88 Y8b   88 *
# /____Y88b88  88 888  Y888   '/   YY   Y8b/____Y8b 88  88 88   88  88D  88 .
#/      Y88"8_-88 "88_/ "88_-~/      *   Y/8b    \Yb"8_-88 "8_/ 8\_8P   "8_/
#        \        +          /           /       
#
#        +                       https://github.com/gowildchild/AutoMAutist
#               Copyright (c)2009-2026 by Gunther Voet, All Rights Reserved
############################################################## #  #   #  *  .
# Released under strict Non-Commercial Open-Source License Terms.
import base64
import json
import zlib
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.utils import timezone
from core.mood.models import MoodLogEntry, MentalStateProfile
from core.assist.models import NeuroProfile
from core.assist.flags import (
    mental_states,
    NeuroCognitiveState,
    ExpressiveInteraction,
    OverloadContext,
    ProtectionDirectives,
)
from core.assist.config_manager import (
    load_assist_card_config,
    names_to_mask,
    export_baseline_json,
    BASELINE_PRESETS,
)
from core.assist.translations import get_available_languages, get_language_pack


def encode_card_token(cards_dict: dict) -> str:
    """Compresses a cards configuration dictionary into a compact URL-safe token."""
    raw = json.dumps(cards_dict, separators=(',', ':')).encode('utf-8')
    compressed = zlib.compress(raw, level=9)
    return base64.urlsafe_b64encode(compressed).decode('ascii').rstrip('=')


def decode_card_token(token_str: str) -> dict | None:
    """Decodes a URL-safe card token back into a cards dictionary without needing a DB."""
    if not token_str:
        return None
    try:
        padded = token_str + '=' * (-len(token_str) % 4)
        compressed = base64.urlsafe_b64decode(padded.encode('ascii'))
        raw = zlib.decompress(compressed).decode('utf-8')
        data = json.loads(raw)
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def _build_localized_report(m_mask: int, c_mask: int, i_mask: int, ctx_mask: int, p_mask: int, lang_pack: dict, custom_phrases: dict) -> dict:
    """Translates active IntFlag bitmasks into localized card sections."""
    flags_text = lang_pack.get("flags", {})

    def phrase_for(flag_name: str) -> str:
        return custom_phrases.get(flag_name) or flags_text.get(flag_name) or flag_name.replace("_", " ").title()

    warnings = []
    caregiver = []
    cognitive = []
    communication = []
    stimming = []
    triggers = []

    for flag in ProtectionDirectives:
        if flag.value != 0 and (p_mask & flag.value):
            txt = phrase_for(flag.name)
            if flag.name.startswith("WARN_"):
                warnings.append(txt)
            else:
                caregiver.append(txt)

    for flag in NeuroCognitiveState:
        if flag.value != 0 and (c_mask & flag.value):
            if flag.name.endswith("_OK"):
                continue
            cognitive.append(phrase_for(flag.name))

    for flag in ExpressiveInteraction:
        if flag.value != 0 and (i_mask & flag.value):
            txt = phrase_for(flag.name)
            if flag.name.startswith("STIMMING_"):
                stimming.append(txt)
            else:
                communication.append(txt)

    for flag in OverloadContext:
        if flag.value != 0 and (ctx_mask & flag.value):
            if flag.name == "COPING_OK":
                continue
            triggers.append(phrase_for(flag.name))

    return {
        "high_priority_warnings": warnings,
        "caregiver_instructions": caregiver,
        "cognitive_limitations": cognitive,
        "communication_profile": communication,
        "active_stimming_behaviors": stimming,
        "crisis_context_triggers": triggers,
    }


def international_assist_card_view(request):
    """
    GET /assist/card/
    Supports DB state, local JSON overrides, stateless ?token= URLs, and ?lang=xx switching.
    """
    entity_id = request.GET.get('entity_id', 'user.primary')
    lang_code = request.GET.get('lang', 'en').lower().strip()
    lang_pack = get_language_pack(lang_code)

    cfg = load_assist_card_config()
    is_locked = bool(cfg.get("locked", False))
    custom_phrases = cfg.get("custom_phrases", {})

    # Check if a stateless ?token= was supplied in the URL
    url_token = request.GET.get('token', '').strip()
    token_cards = decode_card_token(url_token)
    active_cards = token_cards if token_cards else cfg.get("cards", BASELINE_PRESETS)

    # Determine active mood mask
    if request.GET.get('mood_mask'):
        m_mask = int(request.GET.get('mood_mask', 1))
    else:
        latest = MoodLogEntry.objects.filter(entity_id=entity_id).first()
        if latest:
            m_mask = latest.mood_mask
        else:
            np = NeuroProfile.objects.filter(neuro_id=entity_id).first()
            m_mask = np.mood_mask if np else 1

    # Match mood mask to enum name (e.g., MOOD_BAILOUT)
    mood_member = next((m for m in mental_states if m.value != 0 and (m_mask & m.value)), mental_states.MOOD_FINE)
    mood_key = mood_member.name
    entry = active_cards.get(mood_key) or BASELINE_PRESETS.get(mood_key) or BASELINE_PRESETS["MOOD_FINE"]

    # Resolve bitmasks (explicit query params override preset masks)
    c_mask = int(request.GET['cognitive_mask']) if 'cognitive_mask' in request.GET else names_to_mask(NeuroCognitiveState, entry.get("cognitive"))
    i_mask = int(request.GET['interaction_mask']) if 'interaction_mask' in request.GET else names_to_mask(ExpressiveInteraction, entry.get("interaction"))
    ctx_mask = int(request.GET['context_mask']) if 'context_mask' in request.GET else names_to_mask(OverloadContext, entry.get("context"))
    p_mask = int(request.GET['protection_mask']) if 'protection_mask' in request.GET else names_to_mask(ProtectionDirectives, entry.get("protection"))

    title_label = request.GET.get('label') or lang_pack["moods"].get(mood_key) or entry.get("label", mood_key)
    color_hex = request.GET.get('color') or entry.get("color_hex", "#198754")
    timestamp_str = timezone.now().strftime('%Y-%m-%d %H:%M UTC')

    report = _build_localized_report(m_mask, c_mask, i_mask, ctx_mask, p_mask, lang_pack, custom_phrases)
    share_token = url_token or encode_card_token(active_cards)

    # Build localized mood dropdown options without requiring DB entries
    mood_options = []
    for m in mental_states:
        if m.value == 0:
            continue
        preset = active_cards.get(m.name) or BASELINE_PRESETS.get(m.name, {})
        mood_options.append({
            "state_mask": m.value,
            "key": m.name,
            "label": lang_pack["moods"].get(m.name) or preset.get("label", m.name.replace("MOOD_", "").title()),
        })

    if request.GET.get('format') == 'json':
        return JsonResponse({
            'entity_id': entity_id,
            'lang': lang_code,
            'ui': lang_pack["ui"],
            'mood_options': mood_options,
            'timestamp': timestamp_str,
            'title_label': title_label,
            'color_hex': color_hex,
            'is_locked': is_locked,
            'share_token': share_token,
            'masks': {
                'mood': m_mask, 'cognitive': c_mask, 'interaction': i_mask,
                'context': ctx_mask, 'protection': p_mask
            },
            'report': report,
        })

    return render(request, 'assist_card.html', {
        'entity_id': entity_id,
        'active_lang': lang_code,
        'languages': get_available_languages(),
        'ui': lang_pack["ui"],
        'profiles': mood_options,
        'timestamp_str': timestamp_str,
        'title_label': title_label,
        'color_hex': color_hex,
        'is_locked': is_locked,
        'share_token': share_token,
        'report': report,
        'masks': {
            'mood_mask': m_mask, 'cognitive_mask': c_mask,
            'interaction_mask': i_mask, 'context_mask': ctx_mask,
            'protection_mask': p_mask
        }
    })


def export_assist_card_config_view(request):
    """
    GET /assist/card/export/
    Writes baseline JSON template to storage and downloads it for user customization.
    """
    cfg = load_assist_card_config()
    if cfg.get("locked"):
        return HttpResponseForbidden("Assist card profile is locked by caregiver/assistant.")

    payload = export_baseline_json()
    response = HttpResponse(json.dumps(payload, indent=2), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="automautist-assist-cards.json"'
    return response
