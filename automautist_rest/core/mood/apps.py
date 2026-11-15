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

from django.apps import AppConfig
from django.db.models.signals import post_migrate
def seed_auti_coach_presets(sender, **kwargs):
    """
    Natively pre-fills historical 15-year Auti-Coach regulation profiles 
    on the very first database compilation step automatically.
    """
    # Local imports inside the signal execution block to prevent early application boot loops
    from core.mood.models import MentalStateProfile
    from core.assist.flags import mental_states

    presets = [
        {
            "state_mask": mental_states.MOOD_FINE.value,
            "label": "Fine",
            "description": "Everything is all fine, nothing to worry about!",
            "ui_color_hex": "#198754",               "rgb_mood_color": "#4444FF",

            "overrides": { "timer_shower_mins_min":     7, "timer_shower_mins_max": 10, "timer_shower_mins_add": 0, "timer_shower_cold":     True,
                           "timer_wakeup_mins_min":    10, "timer_wakeup_mins_max": 20, "timer_wakeup_mins_add": 0, "timer_wakeup_sound":    True,
                           "timer_travel_mins_min":    20, "timer_travel_mins_max": 30, "timer_travel_mins_add": 0, "timer_travel_sound":    True,
                           "bright_screen_min":        96, "bright_screen_max":    255, "bright_screen_add":    32, "bright_screen_auto":    True,
                           "bright_lights_min":        96, "bright_lights_max":    255, "bright_lights_add":    16, "bright_lights_auto":    True,
                           "volume_assistant_min":     4,  "volume_assistant_max":   7, "volume_assistant_add":  1, "volume_assistant_auto": True,
                           "automations_non_critical": True
                         }
        },
        {
            "state_mask": mental_states.MOOD_NERVOUS.value,
            "label": "Nervous",
            "description": "Sensory overload warnings detected. Minor calming buffers engaged.",
            "ui_color_hex": "#ffc107",               "rgb_mood_color": "#ffc107",
            "overrides": { "timer_shower_mins_min":     8, "timer_shower_mins_max": 10, "timer_shower_mins_add": 3, "timer_shower_cold":     True,
                           "timer_wakeup_mins_min":    12, "timer_wakeup_mins_max": 30, "timer_wakeup_mins_add": 3, "timer_wakeup_sound":    True,
                           "timer_travel_mins_min":    20, "timer_travel_mins_max": 30, "timer_travel_mins_add": 5, "timer_travel_sound":    True,
                           "bright_screen_min":        96, "bright_screen_max":    255, "bright_screen_add":    24, "bright_screen_auto":    True,
                           "bright_lights_min":        96, "bright_lights_max":    255, "bright_lights_add":    12, "bright_lights_auto":    True,
                           "volume_assistant_min":      4, "volume_assistant_max":   6, "volume_assistant_add":  1, "volume_assistant_auto": True,
                           "automations_non_critical": True
                         }
        },
        {
            "state_mask": mental_states.MOOD_COPING.value,
            "label": "Coping",
            "description": "Actively processing high sensory friction. Systems slowed down.",
            "ui_color_hex": "#fd7e14",
            "overrides": { "timer_shower_mins_min":     8, "timer_shower_mins_max": 12, "timer_shower_mins_add": 4, "timer_shower_cold":    False,
                           "timer_wakeup_mins_min":    13, "timer_wakeup_mins_max": 35, "timer_wakeup_mins_add": 5, "timer_wakeup_sound":    True,
                           "timer_travel_mins_min":    21, "timer_travel_mins_max": 35, "timer_travel_mins_add": 7, "timer_travel_sound":    True,
                           "bright_screen_min":        96, "bright_screen_max":    192, "bright_screen_add":    24, "bright_screen_auto":    True,
                           "bright_lights_min":        96, "bright_lights_max":    192, "bright_lights_add":    12, "bright_lights_auto":    True,
                           "volume_assistant_min":      4, "volume_assistant_max":   5, "volume_assistant_add":  2, "volume_assistant_auto": True,
                           "automations_non_critical": True
                         }
        },
        {
            "state_mask": mental_states.MOOD_BAILOUT.value,
            "label": "Bailout",
            "description": "Immediate retreat necessary. Initiating sensory extraction sequences.",
            "ui_color_hex": "#e65c00",
            "overrides": { "timer_shower_mins_min":    10, "timer_shower_mins_max": 20, "timer_shower_mins_add": 4, "timer_shower_cold":    False,
                           "timer_wakeup_mins_min":    14, "timer_wakeup_mins_max": 40, "timer_wakeup_mins_add": 5, "timer_wakeup_scene":  "wakeup",
                           "timer_travel_mins_min":    24, "timer_travel_mins_max": 40, "timer_travel_mins_add": 9, "timer_travel_alert":  "message",
                           "bright_screen_min":        48, "bright_screen_max":    160, "bright_screen_add":     8, "bright_screen_auto":   True,
                           "bright_lights_min":        48, "bright_lights_max":    160, "bright_lights_add":    12, "bright_lights_auto":   True,
                           "volume_assistant_min":      3, "volume_assistant_max":   4, "volume_assistant_add":  1, "volume_assistant_auto":True,
                           "volume_relax_min":          3, "volume_relax_max":       5, "volume_relax_add":      1, "volume_relax_scene":  "relaxsounds",
                           "sounds_relax_ondemand":  True, "sounds_relax_auto":   True, "sounds_relax_mins_max":20, "lights_relax_scene":  "warm",
                           "automations_non_critical": False
                         }
        },
        {
            "state_mask": mental_states.MOOD_MELTDOWN.value,
            "label": "Meltdown",
            "description": "Active neurological overload crisis. Full isolation protection active.",
            "ui_color_hex": "#dc3545",
            "overrides": { "timer_shower_mins_min":    12, "timer_shower_mins_max": 25, "timer_shower_mins_add": 6,  "timer_shower_cold":    False,
                           "timer_wakeup_mins_min":    20, "timer_wakeup_mins_max": 45, "timer_wakeup_mins_add": 10, "timer_wakeup_scene": "rgb",
                           "timer_travel_mins_min":    25, "timer_travel_mins_max": 50, "timer_travel_mins_add": 14, "timer_travel_alert": "message",
                           "bright_screen_min":        32, "bright_screen_max":    128, "bright_screen_add":      8, "bright_screen_auto":   True,
                           "bright_lights_min":        32, "bright_lights_max":    164, "bright_lights_add":     12, "bright_lights_auto":   True,
                           "volume_assistant_min":      3, "volume_assistant_max":   4, "volume_assistant_add":   0, "volume_assistant_auto":True,
                           "volume_relax_min":          3, "volume_relax_max":       5, "volume_relax_add":       1, "volume_relax_scene":  "sounds",
                           "sounds_relax_ondemand":   True,"sounds_relax_auto":   True, "sounds_relax_mins_max": 60, "lights_relax_scene":  "red",
                           "automations_non_critical": False
                         }
        },
        {
            "state_mask": mental_states.MOOD_CRASH.value,
            "label": "Crash",
            "description": "Post-crisis vegetative recovery state. Low-energy space forced.",
            "ui_color_hex": "#0d6efd",
            "overrides": { "timer_shower_mins_min":    15, "timer_shower_mins_max": 25, "timer_shower_mins_add": 7,  "timer_shower_cold":   False,
                           "timer_wakeup_mins_min":    10, "timer_wakeup_mins_max": 15, "timer_wakeup_mins_add": 15, "timer_wakeup_scene": "rgb",
                           "timer_travel_mins_min":    30, "timer_travel_mins_max": 60, "timer_travel_mins_add": 20, "timer_travel_alert": "message",
                           "bright_screen_min":        32, "bright_screen_max":    128, "bright_screen_add":      8, "bright_screen_auto":  True,
                           "bright_lights_min":        32, "bright_lights_max":    164, "bright_lights_add":     12, "bright_lights_auto":  True,
                           "sounds_relax_ondemand":  True, "sounds_relax_auto":   True, "sounds_relax_mins_max": 30, "lights_relax_scene": "cool",
                           "automations_non_critical": False
                         }
        }
    ]

    for item in presets:
        # update_or_create ensures profiles are safely generated once, but won't overwrite user edits later!
        MentalStateProfile.objects.update_or_create(
            state_mask=item["state_mask"],
            defaults={
                "label": item["label"],
                "ui_color_hex": item["ui_color_hex"],
                "description": item["description"],
                "environmental_overrides": item["overrides"]
            }
        )

    from django.db import connection
    from django.db.utils import OperationalError
    from core.mood.models import MoodLogEntry, EmotionalMoodTag, SystemControlState

    existing_tables = connection.introspection.table_names()
    with connection.schema_editor() as schema_editor:
        for model_cls in (EmotionalMoodTag, SystemControlState):
            if model_cls._meta.db_table not in existing_tables:
                schema_editor.create_model(model_cls)

        # Ensure new columns on MoodLogEntry exist in existing SQLite DBs
        mood_cols = {
            col.name for col in connection.introspection.get_table_description(
                connection.cursor(), MoodLogEntry._meta.db_table
            )
        }
        for field_name in ("emotional_mood", "is_active"):
            if field_name not in mood_cols:
                schema_editor.add_field(MoodLogEntry, MoodLogEntry._meta.get_field(field_name))

    try:
        default_emotions = [
            ("Happy", "😊"), ("Calm", "😌"), ("Content", "🙂"), ("Grateful", "🙏"),
            ("Sad", "😢"), ("Tired", "😴"), ("Frustrated", "😤"), ("Anxious", "😰"),
            ("Overwhelmed", "😵"), ("Lonely", "😔"), ("Energetic", "⚡"), ("Neutral", "😐"),
        ]
        for emo_name, emo_icon in default_emotions:
            EmotionalMoodTag.objects.get_or_create(
                name=emo_name,
                defaults={"emoji": emo_icon, "is_default": True},
            )
        SystemControlState.objects.get_or_create(entity_id="user.primary")
    except OperationalError:
        pass


class MoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

    # FIXED: Explicitly register the isolated subfolder module namespace path
    name = 'core.mood'
    label = 'mood'

    def ready(self):
        # Bind the data seeding routine straight to the sub-app's migration hook
        post_migrate.connect(seed_auti_coach_presets, sender=self)
