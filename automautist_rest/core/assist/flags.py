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

from enum import IntFlag

class mental_states(IntFlag):
    MOOD_NONE              = 0
    MOOD_FINE              = 1 << 0
    MOOD_NERVOUS           = 1 << 1
    MOOD_COPING            = 1 << 2
    MOOD_BAILOUT           = 1 << 3
    MOOD_MELTDOWN          = 1 << 4
    MOOD_CRASH             = 1 << 5
    MOOD_BURNOUT           = 1 << 6
    MOOD_EXHAUSTED         = 1 << 7


class NeuroCognitiveState(IntFlag):
    """
    CATEGORY 1: INTERNAL BRAIN ENGINE (Capacity, Attention, Executive Function and barriers)
    Consolidates Cognitive Mode, Working Memory, barriers and Executive Dysfunction
    """
    COGNITIVE_NONE             = 0
    COGNITIVE_OK               = 1 << 0
    COGNITIVE_NERVOUS          = 1 << 1
    COGNITIVE_ANXIOUS          = 1 << 2
    COGNITIVE_HYPERACTIVE      = 1 << 3
    COGNITIVE_TUNNEL_VISION    = 1 << 4
    COGNITIVE_BLURRY           = 1 << 5
    COGNITIVE_FOGGY            = 1 << 6
    COGNITIVE_LOST_TIMESPACE   = 1 << 7

    MEMORY_OK                  = 1 << 8
    MEMORY_LONG_TERM_ONLY      = 1 << 9
    MEMORY_SHORT_TERM_ONLY     = 1 << 10
    MEMORY_FORGETFUL           = 1 << 11
    MEMORY_BLURRY              = 1 << 12
    MEMORY_FOGGY               = 1 << 13
    MEMORY_UNRESPONSIVE        = 1 << 14
    MEMORY_CRASHING            = 1 << 15

    FOCUS_HYPER                = 1 << 16
    FOCUS_OK                   = 1 << 17
    FOCUS_LESS                 = 1 << 18
    FOCUS_INITIATION_DIFFICULT = 1 << 19
    FOCUS_EXECUTIVE_DISASTER   = 1 << 20
    FOCUS_LOST                 = 1 << 21
    FOCUS_COGNITIVE_INERTIA    = 1 << 22
    FOCUS_PROCASTRINATING      = 1 << 23

    # REAL-TIME PROCESSING AND COMMUNICATION LIMITATIONS
    # especially regarding context, humor, and hidden subtext decoding.
    BARRIER_HUMOR_OK           = 1 << 24
    BARRIER_HUMOR_SUBTLE_ONLY  = 1 << 25
    BARRIER_HUMOR_DIFFICULT    = 1 << 26
    BARRIER_HUMOR_NO_SARCASM   = 1 << 27
    BARRIER_NO_HIDDEN_MESSAGES = 1 << 28
    BARRIER_NO_SOCIAL_CUES     = 1 << 29
    BARRIER_NO_TOUCHING        = 1 << 30
    BARRIER_NO_AGGRO_OR_CAPTIVE= 1 << 31


class ExpressiveInteraction(IntFlag):
    """
    CATEGORY 2: EXTERNAL INTERACTION (Communication, Language, & Motor Stimming)
    Consolidates your Speech, Response Latency, and Somatic Regulation parameters.
    """
    INTERACT_NONE               = 0
    # Response Latency properties
    RESPONSE_OK                 = 1 << 0
    RESPONSE_DELAYED            = 1 << 1
    RESPONSE_ERRATIC            = 1 << 2
    RESPONSE_INTERMITTENT       = 1 << 3
    RESPONSE_UNPREDICTABLE      = 1 << 4
    RESPONSE_CHAOTIC            = 1 << 5
    RESPONSE_UNRESPONSIVE       = 1 << 6
    RESPONSE_INADEQUATE         = 1 << 7

    # Expressive Communication / Mutism layers
    EXPRESSION_OK               = 1 << 8
    EXPRESSION_VERBOSE          = 1 << 9   # normal
    EXPRESSION_CONCISE          = 1 << 10  # short
    EXPRESSION_REDUCED          = 1 << 11  # less, slower
    EXPRESSION_FRAGMENTED       = 1 << 12  # fragments, missing words
    EXPRESSION_CHAOTIC          = 1 << 13  # chaotic consistency
    EXPRESSION_FAIL_COMMUNICATE = 1 << 14  # cannot access vocabulary, erratic chaos
    EXPRESSION_FAIL_UNDERSTAND  = 1 << 15  # cannot understand, misunderstanding
    EXPRESSION_FAIL_MUTISM      = 1 << 16  # communication impossible

    # Verbal Processing / Decoding blocks
    LANGUAGE_OK                 = 1 << 17
    LANGUAGE_SLOWER             = 1 << 18
    LANGUAGE_CHAOTIC            = 1 << 19
    LANGUAGE_NOT_UNDERSTAND     = 1 << 20
    LANGUAGE_MISUNDERSTAND      = 1 << 21
    LANGUAGE_MISSING_WORDS      = 1 << 22

    # Somatic Regulation / Stimming layers
    STIMMING_RUBBING_SOFT       = 1 << 23
    STIMMING_RUBBING_HARD       = 1 << 24
    STIMMING_HAIR_HEAD          = 1 << 25
    STIMMING_ARMS_LEGS          = 1 << 26
    STIMMING_MOVEMENT_ARMS      = 1 << 27
    STIMMING_MOVEMENT_LEGS      = 1 << 28
    STIMMING_HEAD_HAIR          = 1 << 29
    STIMMING_HEAD_DANGER        = 1 << 30
    STIMMING_TOOLS_FEEDBACK     = 1 << 31
    STIMMING_TOOLS_PRESSURE     = 1 << 32

class OverloadContext(IntFlag):
    """
    CATEGORY 3: CRISIS CONTEXT (System Load & Active Sensory Vulnerabilities)
    Consolidates your Coping Levels and environmental texture/oral triggers.
    """
    CONTEXT_NONE              = 0
    # Autonomic Nervous System Loading
    COPING_OK                 = 1 << 0
    COPING_ANNOYED            = 1 << 1
    COPING_DIFFICULT          = 1 << 2
    COPING_TERRIBLE           = 1 << 3
    COPING_NIGHTMARE          = 1 << 4
    COPING_FIGHT_OR_FLIGHT    = 1 << 5
    COPING_NEAR_MELTDOWN      = 1 << 6
    COPING_NO_ESCAPE_POSSIBLE = 1 << 7

    # Environmental / Somatosensory Overload triggers
    SENSORY_HYPERACUSIS        = 1 << 8  # Noise
    SENSORY_PHOTO_AVERSION     = 1 << 9  # Light
    SENSORY_SPATIAL_DISTRESS   = 1 << 10  # Busy/Crowds
    SENSORY_TACTILE_DEFENSE    = 1 << 11 # Touch/Fabrics
    SENSORY_GUSTATORY_AVERSION = 1 << 12 # Food Textures
    SENSORY_PROPRIOCEPTIVE_JAR = 1 << 13 # Proximity Shock
    SENSORY_EASY_AGGRAVATION   = 1 << 14 # Low Annoyance Cap
    SENSORY_REDIRECTION        = 1 << 15 # Use of headphone/hands

    # Triggers
    TRIGGER_COPING_DIFFICULTIES = 1 << 16
    TRIGGER_COPING_LONGTERM     = 1 << 17
    TRIGGER_COPING_EXHAUSTION   = 1 << 18
    TRIGGER_COPING_GASLIGHTING  = 1 << 19
    TRIGGER_COPING_ENVIRONMENT  = 1 << 20
    TRIGGER_COPING_CROWD        = 1 << 21
    TRIGGER_COPING_SOCIAL       = 1 << 22
    TRIGGER_COPING_TIRED        = 1 << 23
    TRIGGER_COPING_FOOD         = 1 << 24
    TRIGGER_SHORT_TEMPER        = 1 << 25
    TRIGGER_IMPOSSIBLE_PEOPLE   = 1 << 26
    TRIGGER_SHORT_SPACE         = 1 << 27
    TRIGGER_ENVIRONMENT         = 1 << 28
    TRIGGER_VIOLENCE            = 1 << 29
    TRIGGER_SHOCK_OR_TRAUMA     = 1 << 30
    TRIGGER_SHOUTING            = 1 << 31

class ProtectionDirectives(IntFlag):
    """
    CATEGORY 4: INTERVENTION MAP (Caregiver Rules & Travel/Customs Safety Prompts)
    Consolidates your Caregiver bounding directives and high-priority transit help tags.
    """
    PROTECT_NONE              = 0
    # Caregiver Grounding Instructions
    STAY_CALM_AND_RELAXED     = 1 << 0
    STAY_AROUND_ME            = 1 << 1
    DO_NOT_AGITATE            = 1 << 2
    DO_NOT_TRIGGER            = 1 << 3
    DO_NOT_INSECURITIES       = 1 << 4
    DO_NOT_TOUCH              = 1 << 5
    DO_NOT_AGGRESS_OR_ABUSE   = 1 << 6
    DO_NOT_PRESSURE           = 1 << 7

    DO_TALK_SLOWLY            = 1 << 8
    DO_TALK_RELAXED           = 1 << 9
    DO_TALK_LOW_VOLUME        = 1 << 10
    DO_TALK_CLEARLY_ONLY      = 1 << 11
    DO_TALK_REAFFIRM          = 1 << 12
    DO_TALK_CONFIRM           = 1 << 13
    DO_TALK_REQUIRED_NEEDS    = 1 << 14
    DO_TALK_GET_CALM          = 1 << 15

    # High-Priority Protective Supports (Customs / Travel Failovers)
    HELP_FIND_SAFE_SPOT        = 1 << 16
    HELP_FIND_CALM_SPOT        = 1 << 17
    HELP_FIND_RESTING_SPOT     = 1 << 18
    HELP_FIND_EXIT_ASAP        = 1 << 19
    HELP_FIND_MY_HOME          = 1 << 20

    HELP_TO_TRAVEL             = 1 << 21
    HELP_TO_COMMUNICATE        = 1 << 22
    HELP_ME_UNDERSTAND         = 1 << 23
    HELP_ME_CHOOSE_TO_DECIDE   = 1 << 24
    HELP_ME_CONSULT_TO_DECIDE  = 1 << 25

    WARN_MALADAPTIVE_DECISIONS = 1 << 26
    WARN_RESPONSE_VOLATILITY   = 1 << 27
    WARN_IMPULSE_CONTROL       = 1 << 28
    WARN_DANGERS               = 1 << 29
    WARN_OTHERS_AROUND_ME      = 1 << 30


