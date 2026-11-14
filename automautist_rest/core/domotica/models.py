#################### ########### ######## ####### ####### ###### ## * ..
####### AutoMAutist - Digital Autism Assistant, Coach and Caretaker       d..
######       .                                                        *  d8..
##### e            d8 *            e    e  .   e        +   8   ,e  d8   d8 *
#### d8b   88__88_d88__ e88~-_    d8b  d8b    d8b__ 88 ____d8____"_d88 __d8__
### /Y88b  88  88 888  d888   i  d888bdY88b  /Y8b   88  88 88   88 C8    88 .
## /  Y88b 88  88 888  8888   | / Y88Y Y888b/  Y8b  88  88 88   88 Y8b   88 *
# /____Y88b88  88 888  Y888   '/   YY   Y8b/____Y8b 88  88 88   88  88D  88 .
#/      Y88"8_-88 "88_/ "88_-~/      *   Y/8b    \Yb"8_-88 "8_/ 8\_8P   "8_/
#        \        +          /           /.......
#
#        +                       https://github.com/gowildchild/AutoMAutist
#               Copyright (c)2009-2026 by Gunther Voet, All Rights Reserved
############################################################## #  #   #  *  .
# Released under strict Non-Commercial Open-Source License Terms.

import json
import base64
import hashlib
import time
import os
from django.db import models
from django.core.signing import Signer, BadSignature
from django.utils import timezone
from django.conf import settings

from .flags import room_location, device_powered, device_action

class TokenDeviceRegister(models.Model):
    """
    Ecosystem Core Fallback Hardware Registry. Tracks local connectivity channels,
    token cache strings, and physical room location attributes only.
    """
    entity_id = models.CharField(max_length=150, unique=True, help_text="HASS Component Key")
    friendly_name = models.CharField(max_length=100, blank=True, null=True)
    generated_token_cache = models.TextField(blank=True, null=True)

    # 🏁 HARDWARE DOMOTICA TRACKERS ONLY
    room_now_mask = models.BigIntegerField(default=0)
    power_type_mask = models.BigIntegerField(default=4)
    is_active = models.BooleanField(default=False)
    has_motion = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Token Device Register"

    def generate_secure_policy_token(self):
        from django.core.signing import Signer
        signer = Signer(salt=os.environ.get('SUPERVISOR_ENCRYPTION_SALT', 'auto-salt-2026'))
        self.generated_token_cache = signer.sign(f"{self.entity_id}:{self.room_now_mask}")
        self.save()

    def __str__(self):
        return f"{self.friendly_name or 'Unnamed Node'} ({self.entity_id})"

class TokenProtectedDevice(models.Model):
    POLICY_CHOICES = [
        ('ROUTING_ONLY', 'Read Telemetry Only'),
        ('EXECUTE_RELAY', 'Full Bidirectional Action Override'),
        ('CRITICAL_FAILOVER', 'Emergency System Takeover'),
    ]

    entity_id = models.CharField(max_length=150, unique=True, help_text="HASS Component Tracker Key")
    friendly_name = models.CharField(max_length=100, blank=True, null=True)

    assigned_policy = models.CharField(max_length=20, choices=POLICY_CHOICES, default='ROUTING_ONLY')

    max_daily_calls = models.IntegerField(default=1000, help_text="Throttling constraint limit")
    allowed_ip_subnet = models.CharField(max_length=50, default="192.168.7.0/24", help_text="Network scope restriction boundary")
    expiration_days = models.IntegerField(default=365, help_text="Token lifetime constraint calculation metric")

    room_now_mask = models.BigIntegerField(
        default=0,
        choices=[(r.value, r.name.replace("ROOM_NOW_", "")) for r in room_location if "NOW" in r.name],
        help_text="Active location bitfield profile assignment"
    )
    power_type_mask = models.BigIntegerField(
        default=4,
        choices=[(p.value, p.name.replace("DEVICE_POWER_", "")) for p in device_powered],
        help_text="Device electrical hardware parameters input"
    )

    is_active = models.BooleanField(default=False, help_text="Current state tracker flag (On/Off)")
    has_motion = models.BooleanField(default=False, help_text="Current space occupancy state telemetry")

    encryption_salt = models.CharField(max_length=64, blank=True, help_text="Automated token generation seed value")
    generated_token_cache = models.TextField(blank=True, null=True, help_text="Last exported secure token string frame")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Token Protected Device Register"

    def generate_secure_policy_token(self) -> str:
        if not self.encryption_salt:
            self.encryption_salt = hashlib.sha256(f"{self.entity_id}-{time.time()}".encode()).hexdigest()

        expiration_timestamp = int(timezone.now().timestamp()) + (self.expiration_days * 86400)

        policy_payload = {
            "eid": self.entity_id,
            "plc": self.assigned_policy,
            "mdc": self.max_daily_calls,
            "net": self.allowed_ip_subnet,
            "exp": expiration_timestamp
        }

        serialized_json = json.dumps(policy_payload)
        active_salt = self.encryption_salt or getattr(settings, 'ENCRYPTION_SALT', 'default-salt-key')
        signer = Signer(salt=active_salt)
        signed_string = signer.sign(serialized_json)

        encoded_token = base64.urlsafe_b64encode(signed_string.encode()).decode()
        self.generated_token_cache = encoded_token
        self.save()
        return encoded_token

    def verify_and_decode_token(self, token_string: str) -> dict:
        try:
            decoded_bytes = base64.urlsafe_b64decode(token_string.encode())
            active_salt = self.encryption_salt or getattr(settings, 'ENCRYPTION_SALT', 'default-salt-key')
            signer = Signer(salt=active_salt)

            original_json = signer.unsign(decoded_bytes.decode())
            return json.loads(original_json)
        except (BadSignature, Exception):
            raise BadSignature("Cryptographic signature check failed. Token is corrupted or tampered with.")

    def __str__(self):
        return f"{self.friendly_name or self.entity_id} [{self.assigned_policy}]"
