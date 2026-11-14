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
from core.assist.flags import mental_states, NeuroCognitiveState, ExpressiveInteraction, OverloadContext, ProtectionDirectives

class NeuroProfile(models.Model):
    """
    Ecosystem Neuro-Cognitive Profile. Tracks situational executive functioning,
    communication barriers, and safety directives independently from hardware routing data.
    """

    neuro_id    = models.CharField(max_length=150, unique=True, help_text="Identifier")
    neuro_alias = models.CharField(max_length=100, blank=True, null=True, help_text="Friendly tracking alias")

    # 🧠 THE 4 MASTER CONSOLIDATED ADAPTIVE BITFIELDS
    mood_mask = models.BigIntegerField(default=mental_states.MOOD_FINE.value)
    cognitive_mask = models.BigIntegerField(default=NeuroCognitiveState.COGNITIVE_NONE.value)
    interaction_mask = models.BigIntegerField(default=ExpressiveInteraction.INTERACT_NONE.value)
    context_mask = models.BigIntegerField(default=OverloadContext.CONTEXT_NONE.value)
    protection_mask = models.BigIntegerField(default=ProtectionDirectives.PROTECT_NONE.value)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Neuro-Cognitive Assistance Profile"

    def __str__(self):
        return f"Profile: {self.neuro_alias or self.neuro_id}"
