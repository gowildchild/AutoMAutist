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
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

from core.mood.models import MoodLogEntry, MentalStateProfile
from core.assist.models import NeuroProfile
from core.assist.engine import compile_auticoach_profile

from core.assist.flags import (
    mental_states,
    NeuroCognitiveState as C,
    ExpressiveInteraction as I,
    OverloadContext as CTX,
    ProtectionDirectives as P,
)

# Baseline flags applied automatically when a mood state has no custom sub-masks set
MOOD_DEFAULT_MASKS = {
    mental_states.MOOD_FINE.value: (
        C.COGNITIVE_OK | C.MEMORY_OK | C.FOCUS_OK,
        I.INTERACT_NONE,
        CTX.COPING_OK,
        P.PROTECT_NONE,
    ),
    mental_states.MOOD_NERVOUS.value: (
        C.COGNITIVE_NERVOUS | C.COGNITIVE_ANXIOUS | C.BARRIER_HUMOR_NO_SARCASM,
        I.RESPONSE_DELAYED,
        CTX.COPING_ANNOYED | CTX.SENSORY_EASY_AGGRAVATION,
        P.STAY_CALM_AND_RELAXED | P.DO_TALK_CLEARLY_ONLY,
    ),
    mental_states.MOOD_COPING.value: (
        C.COGNITIVE_TUNNEL_VISION | C.FOCUS_LESS | C.BARRIER_NO_HIDDEN_MESSAGES | C.BARRIER_NO_SOCIAL_CUES,
        I.RESPONSE_DELAYED | I.EXPRESSION_CONCISE,
        CTX.COPING_DIFFICULT | CTX.SENSORY_HYPERACUSIS | CTX.SENSORY_PHOTO_AVERSION,
        P.STAY_CALM_AND_RELAXED | P.DO_TALK_SLOWLY | P.DO_TALK_LOW_VOLUME | P.DO_NOT_PRESSURE,
    ),
    mental_states.MOOD_BAILOUT.value: (
        C.COGNITIVE_FOGGY | C.FOCUS_INITIATION_DIFFICULT | C.BARRIER_NO_TOUCHING | C.BARRIER_NO_AGGRO_OR_CAPTIVE,
        I.RESPONSE_INTERMITTENT | I.EXPRESSION_REDUCED | I.STIMMING_TOOLS_FEEDBACK,
        CTX.COPING_TERRIBLE | CTX.SENSORY_SPATIAL_DISTRESS | CTX.SENSORY_REDIRECTION,
        P.DO_NOT_TOUCH | P.DO_NOT_PRESSURE | P.DO_TALK_REQUIRED_NEEDS | P.HELP_FIND_CALM_SPOT | P.HELP_FIND_EXIT_ASAP | P.WARN_RESPONSE_VOLATILITY,
    ),
    mental_states.MOOD_MELTDOWN.value: (
        C.COGNITIVE_LOST_TIMESPACE | C.FOCUS_EXECUTIVE_DISASTER | C.BARRIER_NO_TOUCHING | C.BARRIER_NO_AGGRO_OR_CAPTIVE,
        I.RESPONSE_UNRESPONSIVE | I.EXPRESSION_FAIL_MUTISM | I.EXPRESSION_FAIL_UNDERSTAND | I.STIMMING_TOOLS_PRESSURE,
        CTX.COPING_FIGHT_OR_FLIGHT | CTX.COPING_NEAR_MELTDOWN | CTX.SENSORY_HYPERACUSIS | CTX.SENSORY_PHOTO_AVERSION,
        P.DO_NOT_TOUCH | P.DO_NOT_AGITATE | P.DO_NOT_TRIGGER | P.DO_TALK_REQUIRED_NEEDS | P.HELP_FIND_SAFE_SPOT | P.HELP_TO_COMMUNICATE | P.WARN_MALADAPTIVE_DECISIONS | P.WARN_RESPONSE_VOLATILITY,
    ),
    mental_states.MOOD_CRASH.value: (
        C.COGNITIVE_FOGGY | C.MEMORY_CRASHING | C.FOCUS_COGNITIVE_INERTIA | C.BARRIER_NO_TOUCHING,
        I.RESPONSE_UNRESPONSIVE | I.EXPRESSION_REDUCED,
        CTX.COPING_DIFFICULT | CTX.TRIGGER_COPING_EXHAUSTION | CTX.TRIGGER_COPING_TIRED,
        P.STAY_CALM_AND_RELAXED | P.DO_NOT_TOUCH | P.DO_NOT_PRESSURE | P.HELP_FIND_RESTING_SPOT | P.HELP_FIND_MY_HOME,
    ),
}


def international_assist_card_view(request):
    entity_id = request.GET.get('entity_id', 'user.primary')

    if 'mood_mask' in request.GET and request.GET.get('mood_mask'):
        m_mask = int(request.GET.get('mood_mask', 1))
        c_mask = int(request.GET.get('cognitive_mask', 0))
        i_mask = int(request.GET.get('interaction_mask', 0))
        ctx_mask = int(request.GET.get('context_mask', 0))
        p_mask = int(request.GET.get('protection_mask', 0))

        profile_obj = MentalStateProfile.objects.filter(state_mask=m_mask).first()
        title_label = request.GET.get('label') or (profile_obj.label if profile_obj else 'Custom Override')
        color_hex = request.GET.get('color') or (profile_obj.ui_color_hex if profile_obj else '#dc3545')
        timestamp_str = timezone.now().strftime('%Y-%m-%d %H:%M UTC')
    else:
        latest = MoodLogEntry.objects.filter(entity_id=entity_id).first()
        if latest:
            m_mask = latest.mood_mask
            c_mask = latest.cognitive_mask
            i_mask = latest.interaction_mask
            ctx_mask = latest.context_mask
            p_mask = latest.protection_mask
            title_label = latest.mood_label
            color_hex = latest.ui_color_hex
            timestamp_str = latest.timestamp.strftime('%Y-%m-%d %H:%M UTC')
        else:
            np = NeuroProfile.objects.filter(neuro_id=entity_id).first()
            if np:
                m_mask, c_mask, i_mask, ctx_mask, p_mask = (
                    np.mood_mask, np.cognitive_mask, np.interaction_mask, np.context_mask, np.protection_mask
                )
                title_label = "Active Profile"
                color_hex = "#198754"
            else:
                m_mask, c_mask, i_mask, ctx_mask, p_mask = 1, 0, 0, 0, 0
                title_label = "Fine"
                color_hex = "#198754"
            timestamp_str = timezone.now().strftime('%Y-%m-%d %H:%M UTC')

    # Fill in baseline cognitive/interaction/context/protection masks if none were explicitly provided
    if (c_mask | i_mask | ctx_mask | p_mask) == 0 and m_mask in MOOD_DEFAULT_MASKS:
        def_c, def_i, def_ctx, def_p = MOOD_DEFAULT_MASKS[m_mask]
        c_mask, i_mask, ctx_mask, p_mask = int(def_c), int(def_i), int(def_ctx), int(def_p)

    report = compile_auticoach_profile(m_mask, c_mask, i_mask, ctx_mask, p_mask)

    if request.GET.get('format') == 'json':
        return JsonResponse({
            'entity_id': entity_id,
            'timestamp': timestamp_str,
            'title_label': title_label,
            'color_hex': color_hex,
            'masks': {
                'mood': m_mask, 'cognitive': c_mask, 'interaction': i_mask,
                'context': ctx_mask, 'protection': p_mask
            },
            'report': report
        })

    return render(request, 'assist_card.html', {
        'entity_id': entity_id,
        'profiles': MentalStateProfile.objects.all().order_by('state_mask'),
        'timestamp_str': timestamp_str,
        'title_label': title_label,
        'color_hex': color_hex,
        'report': report,
        'masks': {
            'mood_mask': m_mask, 'cognitive_mask': c_mask,
            'interaction_mask': i_mask, 'context_mask': ctx_mask,
            'protection_mask': p_mask
        }
    })
