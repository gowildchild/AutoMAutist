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

import ipaddress
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.urls import set_script_prefix
from core.domotica.models import TokenProtectedDevice
from core.domotica.flags import room_location
from core.mood.models import MentalStateProfile, MoodLogEntry
from core.assist.engine import compile_auticoach_profile


import re

INGRESS_PREFIX_RE = re.compile(r'^(/api/hassio_ingress/[^/]+)')

class HomeAssistantIngressMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ingress_path = request.headers.get('X-Ingress-Path') or request.META.get('HTTP_X_INGRESS_PATH')
        if not ingress_path:
            match = INGRESS_PREFIX_RE.match(request.path)
            if match:
                ingress_path = match.group(1)

        if ingress_path:
            base_prefix = ingress_path.rstrip('/')
            request.ingress_prefix = base_prefix
            set_script_prefix(base_prefix)
            if request.path.startswith(base_prefix):
                normalized_path = request.path[len(base_prefix):]
                if not normalized_path.startswith('/'):
                    normalized_path = '/' + normalized_path
                request.path_info = normalized_path
                request.path = normalized_path
        else:
            request.ingress_prefix = ''
            set_script_prefix('/')
        return None


def ingress_context(request):
    return {'ingress_prefix': getattr(request, 'ingress_prefix', '')}

def admin_dashboard(request):
    devices = TokenProtectedDevice.objects.all()
    profiles = MentalStateProfile.objects.all().order_by('state_mask')
    latest_mood = MoodLogEntry.objects.filter(entity_id='user.primary').first()

    # Determine active mood mask (defaults to Fine = 1)
    active_mask = latest_mood.mood_mask if latest_mood else 1
    active_profile = profiles.filter(state_mask=active_mask).first() or profiles.first()

    # Build JSON map of all mood presets for instant client-side previewing
    profiles_json = json.dumps({
        str(p.state_mask): {
            "label": p.label,
            "color": p.ui_color_hex,
            "description": p.description,
            "overrides": p.environmental_overrides,
        }
        for p in profiles
    })

    policy_choices = TokenProtectedDevice.POLICY_CHOICES
    room_choices = [
        (r.value, r.name.replace("ROOM_NOW_", "").replace("_", " ").title())
        for r in room_location
        if "NOW" in r.name and "UNKNOWN" not in r.name and "TIME" not in r.name and "RESERVED" not in r.name
    ]

    return render(request, 'dashboard.html', {
        'devices': devices,
        'active_devices_count': devices.filter(is_active=True).count(),
        'profiles': profiles,
        'active_mask': active_mask,
        'active_profile': active_profile,
        'latest_mood': latest_mood,
        'profiles_json': profiles_json,
        'policy_choices': policy_choices,
        'room_choices': room_choices,
    })


def mount_new_policy_token(request):
    """
    Endpoint enabling administrators to mint structural token rules from UI forms.
    """
    if request.method == 'POST':
        entity = request.POST.get('entity_id', '').strip()
        alias = request.POST.get('friendly_name', '').strip()
        policy = request.POST.get('assigned_policy', 'ROUTING_ONLY')
        subnet = request.POST.get('allowed_ip_subnet', '0.0.0.0/0').strip() or '0.0.0.0/0'

        try:
            max_calls = int(request.POST.get('max_daily_calls') or 100)
            days = int(request.POST.get('expiration_days') or 365)
            room_mask = int(request.POST.get('room_now_mask') or 0)
        except ValueError:
            messages.error(request, "Numeric fields (calls, days, or room mask) must be valid integers.")
            return redirect('admin-dashboard')

        try:
            ipaddress.ip_network(subnet, strict=False)
        except ValueError:
            messages.error(request, f"Invalid CIDR subnet format: '{subnet}'. Example: 192.168.1.0/24")
            return redirect('admin-dashboard')

        if entity:
            device, _ = TokenProtectedDevice.objects.update_or_create(
                entity_id=entity,
                defaults={
                    'friendly_name': alias,
                    'assigned_policy': policy,
                    'max_daily_calls': max_calls,
                    'allowed_ip_subnet': subnet,
                    'expiration_days': days,
                    'room_now_mask': room_mask
                }
            )
            device.generate_secure_policy_token()
            messages.success(request, f"Successfully provisioned token configuration profiles for {entity}!")
        else:
            messages.warning(request, "Entity ID is required to provision a device token.")

    return redirect('admin-dashboard')
