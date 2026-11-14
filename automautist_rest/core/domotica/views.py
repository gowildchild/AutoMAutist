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
import ipaddress
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.signing import BadSignature
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import TokenProtectedDevice
from .engine import compile_live_hex_packet

@csrf_exempt
def execute_token_auth_endpoint(request):
    """
    Validates connecting edge nodes by checking signatures, extracting profiles,
    and matching current incoming traffic states against embedded token rules.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'POST authentication workflow required'}, status=400)

    try:
        incoming_body = json.loads(request.body)
        provided_token = request.headers.get('Authorization', '').replace('Bearer ', '').strip()
        target_entity = incoming_body.get('entity_id')

        # STANDALONE FALLBACK MODE: If no token or entity is provided during a HASS outage,
        # allow direct ESPHome/local upsert without hard signature blocking.
        if not provided_token and target_entity:
            device, _ = TokenProtectedDevice.objects.update_or_create(
                entity_id=target_entity,
                defaults={
                    'is_active': incoming_body.get('state') == 'on',
                    'has_motion': incoming_body.get('motion_detected', False)
                }
            )
            return JsonResponse({
                'access_status': 'GRANTED_LOCAL_FALLBACK',
                'active_policy': 'STANDALONE_DIRECT',
                'hex_action_frame': compile_live_hex_packet(device)
            })

        if not provided_token or not target_entity:
            return JsonResponse({'error': 'Missing required access token parameters'}, status=400)

        device = get_object_or_404(TokenProtectedDevice, entity_id=target_entity)

        # 1. CRYPTOGRAPHIC SIGNATURE MATRIX MATCH
        embedded_rules = device.verify_and_decode_token(provided_token)

        # 2. TEMPORAL CONSTRAINT MATCH CHECK
        current_time = int(timezone.now().timestamp())
        if current_time > embedded_rules['exp']:
            return JsonResponse({'error': 'Token lifetime constraint expired.'}, status=401)

        # 3. CRASH-FREE NETWORK LOCATION SCOPE CHECK
        client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
        allowed_net = embedded_rules.get('net', '0.0.0.0/0')

        if allowed_net != "0.0.0.0/0":
            try:
                if ipaddress.ip_address(client_ip) not in ipaddress.ip_network(allowed_net, strict=False):
                    return JsonResponse({'error': f"Client IP space '{client_ip}' violates allowed token subnet scope."}, status=403)
            except ValueError:
                return JsonResponse({'error': "Invalid network address parameters processed."}, status=400)

        # 4. RUNTIME DATA SYNCHRONIZATION
        device.is_active = incoming_body.get('state') == 'on'
        device.has_motion = incoming_body.get('motion_detected', False)
        device.save()

        # 5. GENERATE REAL-TIME FALLBACK MATRIX PACKET
        generated_hex = compile_live_hex_packet(device)

        return JsonResponse({
            'access_status': 'GRANTED',
            'active_policy': embedded_rules['plc'],
            'hex_action_frame': generated_hex
        })

    except BadSignature as crypto_err:
        return JsonResponse({'access_status': 'DENIED', 'reason': str(crypto_err)}, status=401)
    except Exception as general_err:
        return JsonResponse({'access_status': 'ERROR', 'reason': str(general_err)}, status=500)
