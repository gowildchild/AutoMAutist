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
from django.utils import timezone
import time
from typing import Dict, Any, Union
from core.domotica.flags import (
    room_location,
    trigger_location,
    room_occupancy,
    room_timing,
    room_during,
    room_brightness,
    trigger_priority,
    device_action,
    device_delays,
    device_powered,
)

def extract_raw_hex_segments(state_data: Union[Any, Dict[str, Any]]) -> Dict[str, str]:
    """
    Extracts and formats the raw 22-segment hex string components directly from 
    your finished bitmask structures without modifying any enum definitions.
    Accepts either a dict or a model object with matching attribute keys.
    """
    is_dict = isinstance(state_data, dict)

    def get_int(key: str, default: int = 0) -> int:
        val = state_data.get(key, default) if is_dict else getattr(state_data, key, default)
        try:
            return int(val or 0)
        except (ValueError, TypeError):
            return default

    # 0. Timestamp (32-bit uppercase)
    ts = f"{int(time.time()) & 0xFFFFFFFF:08X}"

    # 1. TRIG ROOM + Time (64-bit field broken out into four 16-bit blocks)
    rl = get_int("room_location", 0)
    tr_now = f"{rl & 0xFFFF:04X}"
    tr_last = f"{(rl >> 16) & 0xFFFF:04X}"
    tr_from = f"{(rl >> 32) & 0xFFFF:04X}"
    tr_to = f"{(rl >> 48) & 0xFFFF:04X}"

    # 2. ROOMOCCU (24-bit field represented as 8 characters: 00000000)
    ro = f"{get_int('room_occupancy', 0) & 0xFFFFFF:08X}"

    # 3. ROOM TIME split block layout (AABB-CCDD structural layout mapping)
    rt = get_int("room_timing", 0)
    rd = get_int("room_during", 0) & 0xFF
    rb = get_int("room_brightness", 0) & 0xFF
    rt_min = f"{rt & 0xFFFF:04X}"
    rt_max = f"{(rt >> 16) & 0xFFFF:04X}"
    rd_str = f"{rd:02X}"
    rb_str = f"{rb:02X}"

    # 4. TRIG LOC (32-bit boundary tracking separated into two 16-bit units)
    tl = get_int("trigger_location", 0)
    tl_from = f"{tl & 0xFFFF:04X}"
    tl_to = f"{(tl >> 16) & 0xFFFF:04X}"

    # 5. TR-PRIOR (16-bit layout)
    tp = f"{get_int('trigger_priority', 0) & 0xFFFF:04X}"

    # 6. DEVICE ACTION (32-bit field)
    da = f"{get_int('device_action', 0) & 0xFFFFFFFF:08X}"

    # 7. DEVICE DELAYS (64-bit field broken out exactly into 0xAB-CDEFGH-IJ-KLMNOP format)
    dd = get_int("device_delays", 0)
    ab = f"0x{(dd & 0xFF):02X}"
    cdefgh = f"{(dd >> 8) & 0xFFFFFF:06X}"
    ij = f"{(dd >> 32) & 0xFF:02X}"
    klmnop = f"{(dd >> 40) & 0xFFFFFF:06X}"

    # 8. POWERED (4-bit field / single character width)
    dp = f"{get_int('device_powered', 0) & 0xF:X}"

    # Checkdigits XOR calculation over the exact segment pool order
    checksum_pool = [
        ts, tr_now, tr_last, tr_from, tr_to, ro,
        rt_min, rt_max, rd_str, rb_str, tl_from, tl_to,
        tp, da, ab, cdefgh, ij, klmnop, dp
    ]
    chk = 0
    for segment in checksum_pool:
        clean = segment.replace("0x", "").replace("0X", "").replace("-", "")
        if clean:
            try:
                chk ^= int(clean, 16)
            except ValueError:
                pass
    checkdigits = f"{chk & 0xFFFF:04X}"

    return {
        "ts": ts,
        "tr_now": tr_now,
        "tr_last": tr_last,
        "tr_from": tr_from,
        "tr_to": tr_to,
        "ro": ro,
        "rt_min": rt_min,
        "rt_max": rt_max,
        "rd_str": rd_str,
        "rb_str": rb_str,
        "tl_from": tl_from,
        "tl_to": tl_to,
        "tp": tp,
        "da": da,
        "ab": ab,
        "cdefgh": cdefgh,
        "ij": ij,
        "klmnop": klmnop,
        "dp": dp,
        "checkdigits": checkdigits,
    }


def render_hex_packet(
    segments: Dict[str, str],
    template_format: str = (
        "{ts}-{tr_now}-{tr_last}-{tr_from}-{tr_to}-{ro}-"
        "{rt_min}-{rt_max}-{rd_str}-{rb_str}-{tl_from}-{tl_to}-"
        "{tp}-{rd_str}-{rb_str}-{da}-{ab}-{cdefgh}-{ij}-{klmnop}-"
        "{dp}-{checkdigits}"
    ),
) -> str:
    """
    Composes the final 22-segment string using any customizable format template.
    Preserves your exact default order:
    FFFFFFFF-tr_now-tr_last-tr_from-tr_to-ro-rt_min-rt_max-rd_str-rb_str-tl_from-tl_to-tp-rd_str-rb_str-da-ab-cdefgh-ij-klmnop-dp-checkdigits
    """
    return template_format.format(**segments)


def compile_live_hex_packet(device_or_dict: Union[Any, Dict[str, Any]]) -> str:
    """
    Drop-in compatibility engine function for views and ESPHome payload endpoints.
    """
    segments = extract_raw_hex_segments(device_or_dict)
    return render_hex_packet(segments)

def compile_live_hex_packet_prototype(device) -> str:
    """
    Dynamically generates your exact custom 22-segment hex template layout map
    by matching the active database model properties against IntFlags.
    Output matches: FFFFFFFF-0000-0000-0000-0000-00000000-...-checkdigits
    """
    ts = f"{int(timezone.now().timestamp()) & 0xFFFFFFFF:08X}"

    # 1. TRIG ROOM + Time (64-bit field broken out into four 16-bit blocks)
    rl = int(device.room_now_mask)
    tr_now  = f"{rl & 0xFFFF:04X}"
    tr_last = f"{(rl >> 16) & 0xFFFF:04X}"
    tr_from = f"{(rl >> 32) & 0xFFFF:04X}"
    tr_to   = f"{(rl >> 48) & 0xFFFF:04X}"

    # 2. ROOMOCCU (24-bit field represented as 8 characters: 00000000)
    ro_flag = 0
    if device.is_active:
        ro_flag |= room_occupancy.ROOM_ACTIVE.value
    if device.has_motion:
        ro_flag |= room_occupancy.ROOM_OCCUPANCY_MOTION.value
    ro = f"{ro_flag & 0xFFFFFF:08X}"

    # 3. ROOM TIME split block layout spacer configurations
    rt_min, rt_max, rd_str, rb_str = "0000", "0000", "00", "00"
    tl_from, tl_to, tp = "0000", "0000", "0000"

    # 4. DEVICE ACTION (32-bit field)
    da_val = device_action.TURN_ON.value if device.is_active else device_action.TURN_OFF.value
    da = f"{da_val & 0xFFFFFFFF:08X}"

    # 5. DEVICE DELAYS & POWERED (4-bit field / single character width)
    ab, cdefgh, ij, klmnop = "0x00", "000000", "00", "000000"
    dp = f"{int(device.power_type_mask) & 0xF:X}"

    # 6. Checkdigits XOR Calculation Loop over all text blocks
    pool = [ts, tr_now, tr_last, tr_from, tr_to, ro, rt_min, rt_max, rd_str, rb_str, tl_from, tl_to, tp, da, ab, cdefgh, ij, klmnop, dp]
    chk = 0
    for segment in pool:
        clean = segment.replace("0x", "")
        if clean:
            chk ^= int(clean, 16)
    checkdigits = f"{chk & 0xFFFF:04X}"

    return (
        f"{ts}-{tr_now}-{tr_last}-{tr_from}-{tr_to}-{ro}-"
        f"{rt_min}-{rt_max}-{rd_str}-{rb_str}-{tl_from}-{tl_to}-"
        f"{tp}-{rd_str}-{rb_str}-{da}-{ab}-{cdefgh}-{ij}-{klmnop}-"
        f"{dp}-{checkdigits}"
    )
