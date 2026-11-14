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

from django.db import models
from django.utils import timezone

def get_default_coaching_overrides():
    """
    Provides a standardized fallback schema dictionary for non-programmed 
    environmental values to prevent mutable state sharing bugs in JSONFields.
    """
    return {
        "shower_timeout_minutes": 15,
        "wakeup_buffer_minutes": 10,
        "smart_screen_brightness": 100,
        "voice_assistant_volume": 70,
        "allow_non_critical_automations": True
    }

class MentalStateProfile(models.Model):
    """
    Universal Auti-Coach Cognitive Profile. Uses an open-ended JSONField 
    to pass arbitrary environmental variables down the REST line seamlessly.
    """
    state_mask = models.BigIntegerField(unique=True, help_text="The internal IntFlag bitmask integer value.")
    label = models.CharField(max_length=50, help_text="Friendly name shown on user screens.")
    ui_color_hex = models.CharField(max_length=7, default="#198754", help_text="Visual dashboard color scheme.")
    description = models.TextField(help_text="Clear explanation of the nervous system state.")

    environmental_overrides = models.JSONField(
        default=get_default_coaching_overrides,
        help_text="Universal key-value map for adaptive environmental tweaks."
    )

    class Meta:
        verbose_name = "Auti-Coach State Regulation Profile"
        ordering = ['state_mask']

    def __str__(self):
        return f"{self.label} (Mask: {self.state_mask})"

class MoodLogEntry(models.Model):
    """
    Minimal-footprint immutable time-series log for clinical review & trend analysis.
    Stores raw bitmasks + text snapshots so cards/reports render offline without recomputation.
    """
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    entity_id = models.CharField(max_length=150, default="user.primary", db_index=True)

    # Snapshot of states at log time
    mood_mask = models.BigIntegerField(default=1)
    cognitive_mask = models.BigIntegerField(default=0)
    interaction_mask = models.BigIntegerField(default=0)
    context_mask = models.BigIntegerField(default=0)
    protection_mask = models.BigIntegerField(default=0)

    # Human-readable contextual summary & clinician notes
    mood_label = models.CharField(max_length=50, default="Fine")
    ui_color_hex = models.CharField(max_length=7, default="#198754")
    reason_summary = models.TextField(blank=True, default="", help_text="Triggers/circumstances (crowds, fatigue, etc.)")
    clinician_notes = models.TextField(blank=True, default="")

    class Meta:
        verbose_name = "Clinical Mood Telemetry Log"
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['entity_id', '-timestamp']),
        ]

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.entity_id} - {self.mood_label}"
