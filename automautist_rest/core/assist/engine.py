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

from __future__ import annotations
from typing import Any
"""
AutoMAutist Ecosystem - Dynamic Sentence & Hex Packet Compilation Engines
Translates consolidated multi-layered IntFlag integers into descriptive hypermedia payloads
and 22-segment localized fallback hex actions packets.
"""

from core.assist.flags import (
    mental_states,
    NeuroCognitiveState,
    ExpressiveInteraction,
    OverloadContext,
    ProtectionDirectives
)

def _safe_int(val: Any) -> int:
    try:
        return int(val or 0)
    except (ValueError, TypeError):
        return 0

def compile_auticoach_profile(mood_mask, cognitive_mask, interaction_mask, context_mask, protection_mask) -> dict:
    """
    Ecosystem Core Decoder: Translates consolidated multi-layered IntFlag bitwise integers
    into clean, localized, accessible markdown strings and operational parameters.
    """
    mood_mask = _safe_int(mood_mask)
    c = _safe_int(cognitive_mask)
    i = _safe_int(interaction_mask)
    ctx = _safe_int(context_mask)
    p = _safe_int(protection_mask)
    report = {
        "status_title": "Baseline Status: Stable",
        "color_hex": "#198754",
        "cognitive_limitations": [],
        "communication_profile": [],
        "active_stimming_behaviors": [],
        "crisis_context_triggers": [],
        "caregiver_instructions": [],
        "high_priority_warnings": []
    }

    # =========================================================================
    # 0. PARSE GLOBAL MENTAL STATE
    # =========================================================================
    if mood_mask & mental_states.MOOD_FINE.value:
        report["status_title"] = "Status: Fine & Stable"
        report["color_hex"] = "#198754"
    elif mood_mask & mental_states.MOOD_NERVOUS.value:
        report["status_title"] = "Status: Nervous / Sensory Saturation Warning"
        report["color_hex"] = "#ffc107"
    elif mood_mask & mental_states.MOOD_COPING.value:
        report["status_title"] = "Status: Coping / Processing Sensory Friction"
        report["color_hex"] = "#fd7e14"
    elif mood_mask & mental_states.MOOD_BAILOUT.value:
        report["status_title"] = "Status: Immediate Bailout Required"
        report["color_hex"] = "#e65c00"
    elif mood_mask & mental_states.MOOD_MELTDOWN.value:
        report["status_title"] = "Status: Active Autistic Meltdown Crisis"
        report["color_hex"] = "#dc3545"
    elif mood_mask & mental_states.MOOD_CRASH.value:
        report["status_title"] = "Status: Post-Crisis Neuro-Vegetative Crash"
        report["color_hex"] = "#0d6efd"
    elif mood_mask & mental_states.MOOD_BURNOUT.value:
        report["status_title"] = "Status: Chronic Autistic Burnout Phase"
        report["color_hex"] = "#6f42c1"
    elif mood_mask & mental_states.MOOD_EXHAUSTED.value:
        report["status_title"] = "Status: Absolute Exhaustion"
        report["color_hex"] = "#495057"

    # =========================================================================
    # 1. PARSE CATEGORY 1: INTERNAL BRAIN ENGINE (NeuroCognitiveState)
    # =========================================================================
    c = cognitive_mask
    # Cognitive / Attention / Executive Dysfunction
    if c & NeuroCognitiveState.COGNITIVE_NERVOUS.value: report["cognitive_limitations"].append("Nervous system running on edge.")
    if c & NeuroCognitiveState.COGNITIVE_ANXIOUS.value: report["cognitive_limitations"].append("High internal anxiety baseline limits concentration.")
    if c & NeuroCognitiveState.COGNITIVE_HYPERACTIVE.value: report["cognitive_limitations"].append("Brain is currently hyperactive; raw thought racing.")
    if c & NeuroCognitiveState.COGNITIVE_TUNNEL_VISION.value: report["cognitive_limitations"].append("Experiencing high-friction tunnel vision.")
    if c & NeuroCognitiveState.COGNITIVE_BLURRY.value: report["cognitive_limitations"].append("Cognitive input mapping is blurry.")
    if c & NeuroCognitiveState.COGNITIVE_FOGGY.value: report["cognitive_limitations"].append("Severe brain fog limits immediate task processing.")
    if c & NeuroCognitiveState.COGNITIVE_LOST_TIMESPACE.value: report["cognitive_limitations"].append("Lost track of time-space context completely.")

    if c & NeuroCognitiveState.MEMORY_LONG_TERM_ONLY.value: report["cognitive_limitations"].append("Working memory drop: can only access historical long-term data loops.")
    if c & NeuroCognitiveState.MEMORY_SHORT_TERM_ONLY.value: report["cognitive_limitations"].append("Can only retain immediate local short-term tasks.")
    if c & NeuroCognitiveState.MEMORY_FORGETFUL.value: report["cognitive_limitations"].append("Highly forgetful of ongoing steps right now.")
    if c & NeuroCognitiveState.MEMORY_UNRESPONSIVE.value: report["cognitive_limitations"].append("Memory retrieval gates are currently unresponsive.")
    if c & NeuroCognitiveState.MEMORY_CRASHING.value: report["cognitive_limitations"].append("Memory allocation failure: active mental exhaustion.")

    if c & NeuroCognitiveState.FOCUS_HYPER.value: report["cognitive_limitations"].append("Locked in deep hyperfocus; disengagement will cause high friction.")
    if c & NeuroCognitiveState.FOCUS_LESS.value: report["cognitive_limitations"].append("Attention span dropped significantly.")
    if c & NeuroCognitiveState.FOCUS_INITIATION_DIFFICULT.value: report["cognitive_limitations"].append("Experiencing massive difficulty with task initiation.")
    if c & NeuroCognitiveState.FOCUS_EXECUTIVE_DISASTER.value: report["cognitive_limitations"].append("CRITICAL: Complete executive dysfunction block active.")
    if c & NeuroCognitiveState.FOCUS_COGNITIVE_INERTIA.value: report["cognitive_limitations"].append("Stuck in absolute cognitive inertia.")
    if c & NeuroCognitiveState.FOCUS_PROCASTRINATING.value: report["cognitive_limitations"].append("Paralyzed in executive procrastination loops.")

    # Socio-Cognitive Barriers
    if c & NeuroCognitiveState.BARRIER_HUMOR_SUBTLE_ONLY.value: report["cognitive_limitations"].append("Can only interpret highly subtle, non-aggressive humor formats.")
    if c & NeuroCognitiveState.BARRIER_HUMOR_DIFFICULT.value: report["cognitive_limitations"].append("Processing humor or jokes is too exhausting right now.")
    if c & NeuroCognitiveState.BARRIER_HUMOR_NO_SARCASM.value: report["cognitive_limitations"].append("Sarcasm detection is completely offline. Take all words literally.")
    if c & NeuroCognitiveState.BARRIER_NO_HIDDEN_MESSAGES.value: report["cognitive_limitations"].append("Unable to parse hidden messages, double meanings, or social cues.")
    if c & NeuroCognitiveState.BARRIER_NO_SOCIAL_CUES.value: report["cognitive_limitations"].append("Completely blind to standard unwritten social cues or expectations.")
    if c & NeuroCognitiveState.BARRIER_NO_TOUCHING.value: report["cognitive_limitations"].append("Strict touch boundary: do not initiate physical contact.")
    if c & NeuroCognitiveState.BARRIER_NO_AGGRO_OR_CAPTIVE.value: report["cognitive_limitations"].append("Will perceive any shouting, capture, or cornering as a direct threat.")

    # =========================================================================
    # 2. PARSE CATEGORY 2: EXTERNAL INTERACTION (ExpressiveInteraction)
    # =========================================================================
    i = interaction_mask
    # Response Latency properties
    if i & ExpressiveInteraction.RESPONSE_DELAYED.value: report["communication_profile"].append("Responses and processing times will be significantly delayed.")
    if i & ExpressiveInteraction.RESPONSE_ERRATIC.value: report["communication_profile"].append("Reactions may seem erratic, jumpy, or out of sync.")
    if i & ExpressiveInteraction.RESPONSE_INTERMITTENT.value: report["communication_profile"].append("Communication gate is intermittent; answers will come and go.")
    if i & ExpressiveInteraction.RESPONSE_UNPREDICTABLE.value: report["communication_profile"].append("Autonomic responses are completely unpredictable right now.")
    if i & ExpressiveInteraction.RESPONSE_UNRESPONSIVE.value: report["communication_profile"].append("Slowly or completely unresponsive to verbal calls.")
    if i & ExpressiveInteraction.RESPONSE_INADEQUATE.value: report["communication_profile"].append("Response output may seem inadequate, short, or inappropriate.")

    # Expressive Communication / Mutism / Decoding layers
    if i & ExpressiveInteraction.EXPRESSION_VERBOSE.value: report["communication_profile"].append("Speech might become overly verbose, looping, or long-winded.")
    if i & ExpressiveInteraction.EXPRESSION_CONCISE.value: report["communication_profile"].append("Can only communicate in short, highly concise sentences.")
    if i & ExpressiveInteraction.EXPRESSION_REDUCED.value: report["communication_profile"].append("Verbal output is heavily reduced and physically slower.")
    if i & ExpressiveInteraction.EXPRESSION_FRAGMENTED.value: report["communication_profile"].append("Speech consists only of broken word fragments or single missing words.")
    if i & ExpressiveInteraction.EXPRESSION_CHAOTIC.value: report["communication_profile"].append("Consistency is chaotic; jumping wildly between unrelated speech topics.")
    if i & ExpressiveInteraction.EXPRESSION_FAIL_COMMUNICATE.value: report["communication_profile"].append("Cannot access internal vocabulary banks; erratic chaos when attempting to speak.")
    if i & ExpressiveInteraction.EXPRESSION_FAIL_UNDERSTAND.value: report["communication_profile"].append("Experiencing profound difficulty understanding incoming sentences; high risk of misunderstanding.")
    if i & ExpressiveInteraction.EXPRESSION_FAIL_MUTISM.value: report["communication_profile"].append("SITUATIONAL MUTISM ACTIVE: Communication is physically impossible right now.")

    # Somatic Regulation / Stimming layers
    if i & ExpressiveInteraction.STIMMING_RUBBING_SOFT.value: report["active_stimming_behaviors"].append("Soft tactile stimming active (rubbing fabrics/soft textures).")
    if i & ExpressiveInteraction.STIMMING_RUBBING_HARD.value:
        report["active_stimming_behaviors"].append("Hard high-friction stimming active (deep rubbing/pressure).")
    if i & ExpressiveInteraction.STIMMING_HAIR_HEAD.value:
        report["active_stimming_behaviors"].append("Proprioceptive tracking: touching head or hair.")
    if i & ExpressiveInteraction.STIMMING_ARMS_LEGS.value:
        report["active_stimming_behaviors"].append("Sensory balancing: movement in limbs detected.")
    if i & ExpressiveInteraction.STIMMING_MOVEMENT_ARMS.value:
        report["active_stimming_behaviors"].append("Sensory balancing: explicit movement in arms detected.")
    if i & ExpressiveInteraction.STIMMING_MOVEMENT_LEGS.value:
        report["active_stimming_behaviors"].append("Sensory balancing: explicit movement in legs detected.")
    if i & ExpressiveInteraction.STIMMING_HEAD_HAIR.value:
        report["active_stimming_behaviors"].append("Somatic tracking: hair manipulation behaviors active.")
    if i & ExpressiveInteraction.STIMMING_HEAD_DANGER.value:
        report["active_stimming_behaviors"].append("⚠️ HIGH FRICTION RISK: Dangerous or high-force head movements detected.")
    if i & ExpressiveInteraction.STIMMING_TOOLS_FEEDBACK.value:
        report["active_stimming_behaviors"].append("Utilizing external tactile tools or fidgets for nervous system regulation feedback.")
    if i & ExpressiveInteraction.STIMMING_TOOLS_PRESSURE.value:
        report["active_stimming_behaviors"].append("Seeking heavy deep-pressure feedback tools to stabilize somatic loading.")

    # =========================================================================
    # 3. PARSE CATEGORY 3: CRISIS CONTEXT (OverloadContext)
    # =========================================================================
    ctx = context_mask
    # Autonomic Nervous System Loading
    if ctx & OverloadContext.COPING_ANNOYED.value:
        report["crisis_context_triggers"].append("Nervous system is easily annoyed; minor friction feels amplified.")
    if ctx & OverloadContext.COPING_DIFFICULT.value:
        report["crisis_context_triggers"].append("Coping is highly difficult; internal sensory limits are reaching near-capacity.")
    if ctx & OverloadContext.COPING_TERRIBLE.value:
        report["crisis_context_triggers"].append("Nervous system load is terrible; severe sensory distress.")
    if ctx & OverloadContext.COPING_NIGHTMARE.value:
        report["crisis_context_triggers"].append("Autonomic processing running in a critical nightmare distress loop.")
    if ctx & OverloadContext.COPING_FIGHT_OR_FLIGHT.value:
        report["crisis_context_triggers"].append("🔥 AMYGDALA HIJACK: Body is locked in a raw, defensive fight-or-flight crisis layout.")
    if ctx & OverloadContext.COPING_NEAR_MELTDOWN.value:
        report["crisis_context_triggers"].append("🚨 CRITICAL BOUNDARY: On the absolute verge of an autistic meltdown failover.")
    if ctx & OverloadContext.COPING_NO_ESCAPE_POSSIBLE.value:
        report["crisis_context_triggers"].append("Trapped: experiencing acute panic because no physical escape route is possible.")

    # Environmental / Somatosensory Overload Triggers
    if ctx & OverloadContext.SENSORY_HYPERACUSIS.value:
        report["crisis_context_triggers"].append("Hyperacusis active: environmental noise, chattering, or background pitches cause physical pain.")
    if ctx & OverloadContext.SENSORY_PHOTO_AVERSION.value:
        report["crisis_context_triggers"].append("Photo-Aversion active: overhead lights, glare, or luminance fluctuations cause extreme distress.")
    if ctx & OverloadContext.SENSORY_SPATIAL_DISTRESS.value:
        report["crisis_context_triggers"].append("Spatial Distress: overwhelmed by busy movement arrays, clutter, or visual crowd density.")
    if ctx & OverloadContext.SENSORY_TACTILE_DEFENSE.value:
        report["crisis_context_triggers"].append("Tactile Defensiveness: clothing textures, tags, or fabric friction causing severe processing aversion.")
    if ctx & OverloadContext.SENSORY_GUSTATORY_AVERSION.value:
        report["crisis_context_triggers"].append("Gustatory Aversion: high aversion or direct physical rejection risk regarding specific food textures.")
    if ctx & OverloadContext.SENSORY_PROPRIOCEPTIVE_JAR.value:
        report["crisis_context_triggers"].append("Proprioceptive Jar: highly vulnerable to surprise physical touch or invasion of close personal boundaries.")
    if ctx & OverloadContext.SENSORY_EASY_AGGRAVATION.value:
        report["crisis_context_triggers"].append("Low Annoyance Cap: threshold has collapsed; easily aggravated by any sudden sensory shift.")
    if ctx & OverloadContext.SENSORY_REDIRECTION.value:
        report["crisis_context_triggers"].append("Active Sensory Redirection engaged: currently using headphones, shielding hands, or caps.")

    # Contextual Triggers
    if ctx & OverloadContext.TRIGGER_COPING_DIFFICULTIES.value: report["crisis_context_triggers"].append("Trigger Context: Accumulated compounding coping difficulties.")
    if ctx & OverloadContext.TRIGGER_COPING_LONGTERM.value: report["crisis_context_triggers"].append("Trigger Context: Processing heavy long-term psychological or environmental load.")
    if ctx & OverloadContext.TRIGGER_COPING_EXHAUSTION.value: report["crisis_context_triggers"].append("Trigger Context: Complete, profound exhaustion of internal mitigation reserves.")
    if ctx & OverloadContext.TRIGGER_COPING_GASLIGHTING.value: report["crisis_context_triggers"].append("Trigger Context: Subjected to invalidation, confusion, or gaslighting scripts.")
    if ctx & OverloadContext.TRIGGER_COPING_ENVIRONMENT.value: report["crisis_context_triggers"].append("Trigger Context: Friction originating straight from the current environment layout.")
    if ctx & OverloadContext.TRIGGER_COPING_CROWD.value: report["crisis_context_triggers"].append("Trigger Context: Overloaded by crowd scale or public noise saturation.")
    if ctx & OverloadContext.TRIGGER_COPING_SOCIAL.value: report["crisis_context_triggers"].append("Trigger Context: Exhausted by high-demand or forced social interaction expectations.")
    if ctx & OverloadContext.TRIGGER_COPING_TIRED.value: report["crisis_context_triggers"].append("Trigger Context: Severe, acute lack of sleep or biological physical rest.")
    if ctx & OverloadContext.TRIGGER_COPING_FOOD.value: report["crisis_context_triggers"].append("Trigger Context: Low baseline energy from missing meals or hydration drops.")
    if ctx & OverloadContext.TRIGGER_SHORT_TEMPER.value: report["crisis_context_triggers"].append("Trigger Context: Internal temper boundaries are critically compressed.")
    if ctx & OverloadContext.TRIGGER_IMPOSSIBLE_PEOPLE.value: report["crisis_context_triggers"].append("Trigger Context: Forced to navigate around toxic, confusing, or impossible people.")
    if ctx & OverloadContext.TRIGGER_SHORT_SPACE.value: report["crisis_context_triggers"].append("Trigger Context: Confined inside a restrictive, narrow, or claustrophobic spatial layout.")
    if ctx & OverloadContext.TRIGGER_ENVIRONMENT.value: report["crisis_context_triggers"].append("Trigger Context: Unfavorable environmental triggers active.")
    if ctx & OverloadContext.TRIGGER_VIOLENCE.value: report["crisis_context_triggers"].append("Trigger Context: Encountered hostility, aggression, or structural violence.")
    if ctx & OverloadContext.TRIGGER_SHOCK_OR_TRAUMA.value: report["crisis_context_triggers"].append("Trigger Context: Stunned by a traumatic event or direct psychological shock block.")
    if ctx & OverloadContext.TRIGGER_SHOUTING.value: report["crisis_context_triggers"].append("Trigger Context: Stressed by sharp, close-quarters vocal shouting or high volume.")

    # =========================================================================
    # 4. PARSE CATEGORY 4: INTERVENTION MAP (ProtectionDirectives)
    # =========================================================================
    p = protection_mask
    # Caregiver Grounding Instructions
    if p & ProtectionDirectives.STAY_CALM_AND_RELAXED.value:
        report["caregiver_instructions"].append("Please stay completely relaxed, calm, and neutral.")
    if p & ProtectionDirectives.STAY_AROUND_ME.value:
        report["caregiver_instructions"].append("Stay near me for behavioral anchoring, but do not crowd my physical circle.")
    if p & ProtectionDirectives.DO_NOT_AGITATE.value:
        report["caregiver_instructions"].append("DO NOT agitate, argue, correct, or trigger me.")
    if p & ProtectionDirectives.DO_NOT_TRIGGER.value:
        report["caregiver_instructions"].append("DO NOT present active triggers or complex tasks.")
    if p & ProtectionDirectives.DO_NOT_INSECURITIES.value:
        report["caregiver_instructions"].append("DO NOT challenge my security or make me feel uncertain.")
    if p & ProtectionDirectives.DO_NOT_TOUCH.value:
        report["caregiver_instructions"].append("DO NOT touch me under any circumstances right now.")
    if p & ProtectionDirectives.DO_NOT_AGGRESS_OR_ABUSE.value:
        report["caregiver_instructions"].append("CRITICAL: Cease all forms of authority abuse, demand compliance, or aggression.")
    if p & ProtectionDirectives.DO_NOT_PRESSURE.value:
        report["caregiver_instructions"].append("DO NOT put additional pressure or time-sensitive expectations on me.")

    # Caregiver Vocal Processing Modifiers
    if p & ProtectionDirectives.DO_TALK_SLOWLY.value:
        report["caregiver_instructions"].append("Speak very slowly to allow my processing filters to map your words.")
    if p & ProtectionDirectives.DO_TALK_RELAXED.value:
        report["caregiver_instructions"].append("Keep your vocal tone completely un-rushed and quiet.")
    if p & ProtectionDirectives.DO_TALK_LOW_VOLUME.value:
        report["caregiver_instructions"].append("Lower your speaking volume significantly.")
    if p & ProtectionDirectives.DO_TALK_CLEARLY_ONLY.value:
        report["caregiver_instructions"].append("Use strictly clear, plain sentences. Zero sarcasm, subtext, or hints.")
    if p & ProtectionDirectives.DO_TALK_REAFFIRM.value:
        report["caregiver_instructions"].append("Offer simple, calm, repetitive reassurance.")
    if p & ProtectionDirectives.DO_TALK_CONFIRM.value:
        report["caregiver_instructions"].append("Confirm understanding explicitly without demanding long answers.")
    if p & ProtectionDirectives.DO_TALK_REQUIRED_NEEDS.value:
        report["caregiver_instructions"].append("Limit speech exclusively to basic needs (water, quiet space, safety exits).")
    if p & ProtectionDirectives.DO_TALK_GET_CALM.value:
        report["caregiver_instructions"].append("Focus on grounding communication loops to restore internal calm.")

    # High-Priority Protective Action Prompts (Customs / Travel Safeguards / Warnings)
    if p & ProtectionDirectives.HELP_FIND_SAFE_SPOT.value:
        report["caregiver_instructions"].append("Help me locate a physically secure fallback spot.")
    if p & ProtectionDirectives.HELP_FIND_CALM_SPOT.value:
        report["caregiver_instructions"].append("Guide me toward a quiet space to de-escalate and relax.")
    if p & ProtectionDirectives.HELP_FIND_RESTING_SPOT.value:
        report["caregiver_instructions"].append("Assist me in finding an uncrowded zone to sit down and rest.")
    if p & ProtectionDirectives.HELP_FIND_EXIT_ASAP.value:
        report["caregiver_instructions"].append("Help me identify and navigate to the nearest clear exit immediately.")
    if p & ProtectionDirectives.HELP_FIND_MY_HOME.value:
        report["caregiver_instructions"].append("Assist me with transport arrays, directions, or routes to find my way home safely.")
    if p & ProtectionDirectives.HELP_TO_TRAVEL.value:
        report["caregiver_instructions"].append("Take over active transit logistics execution (managing tickets, checkpoints, queues).")
    if p & ProtectionDirectives.HELP_TO_COMMUNICATE.value:
        report["caregiver_instructions"].append("Act as a communication shield; interpret or speak on my behalf if required.")
    if p & ProtectionDirectives.HELP_ME_UNDERSTAND.value:
        report["caregiver_instructions"].append("Help me decode what is happening in the current situation into explicit, basic steps.")
    if p & ProtectionDirectives.HELP_ME_CHOOSE_TO_DECIDE.value:
        report["caregiver_instructions"].append("Help me choose by stripping away complicated options or branching possibilities.")
    if p & ProtectionDirectives.HELP_ME_CONSULT_TO_DECIDE.value:
        report["caregiver_instructions"].append("Consult with my designated trusted circle before finalizing any major decisions.")

    # High-Priority System & Transit Alerts
    if p & ProtectionDirectives.WARN_MALADAPTIVE_DECISIONS.value:
        report["high_priority_warnings"].append("⚠️ CRITICAL SAFETY ALERT: Internal cognitive evaluation gates are compromised. I am highly vulnerable to making fast choices that are counter-productive, unsafe, or harmful to my well-being. Intercept or delay critical decisions immediately.")
    if p & ProtectionDirectives.WARN_RESPONSE_VOLATILITY.value:
        report["high_priority_warnings"].append("⚠️ OFFICIAL TRANSIT / CUSTOMS NOTICE: Processing channels are completely saturated. My responses to official staff, security agents, or passport control may be significantly delayed, fragmented, non-verbal, or look unpredictable/volatile. This is an involuntary, biological survival breakdown—NOT an act of intentional malice, hostility, or non-compliance.")
    if p & ProtectionDirectives.WARN_IMPULSE_CONTROL.value:
        report["high_priority_warnings"].append("⚠️ WARNING: Internal behavioral impulse control filters are running offline.")
    if p & ProtectionDirectives.WARN_DANGERS.value:
        report["high_priority_warnings"].append("⚠️ SAFETY WARNING: Experiencing acute difficulty identifying immediate physical dangers or environmental hazards. Maintain proxy watch on my behalf.")
    if p & ProtectionDirectives.WARN_OTHERS_AROUND_ME.value:
        report["high_priority_warnings"].append("⚠️ NOTICE: High vulnerability to being overwhelmed or panicked by the behaviors of nearby individuals.")

    return report
