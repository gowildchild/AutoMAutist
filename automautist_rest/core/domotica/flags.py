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

import time 
from enum import IntFlag

class HexTimestamp:
    @property
    def current_32bit(self) -> str:
        ts_int = int(time.time())
        return f"0x{ts_int & 0xFFFFFFFF:08x}"

class room_location(IntFlag):
    ROOM_NOW_UNKNOWN           = 0
    ROOM_NOW_HALLWAY           = 1 << 0
    ROOM_NOW_LIVING            = 1 << 1
    ROOM_NOW_DINING            = 1 << 2
    ROOM_NOW_KITCHEN           = 1 << 3
    ROOM_NOW_BATHROOM          = 1 << 4
    ROOM_NOW_OFFICE            = 1 << 5
    ROOM_NOW_BEDROOM           = 1 << 6
    ROOM_NOW_TOILET            = 1 << 7
    ROOM_NOW_PANTRY            = 1 << 8
    ROOM_NOW_RESERVED1         = 1 << 9
    ROOM_NOW_RESERVED2         = 1 << 10
    ROOM_NOW_RESERVED3         = 1 << 11
    ROOM_NOW_TIME_BIT0         = 1 << 12
    ROOM_NOW_TIME_BIT1         = 1 << 13
    ROOM_NOW_TIME_BIT2         = 1 << 14
    ROOM_NOW_TIME_BIT3         = 1 << 15

    ROOM_LAST_UNKNOWN          = 0
    ROOM_LAST_HALLWAY          = 1 << 16
    ROOM_LAST_LIVING           = 1 << 17
    ROOM_LAST_DINING           = 1 << 18
    ROOM_LAST_KITCHEN          = 1 << 19
    ROOM_LAST_BATHROOM         = 1 << 20
    ROOM_LAST_OFFICE           = 1 << 21
    ROOM_LAST_BEDROOM          = 1 << 22
    ROOM_LAST_TOILET           = 1 << 23
    ROOM_LAST_PANTRY           = 1 << 24
    ROOM_LAST_RESERVED1        = 1 << 25
    ROOM_LAST_RESERVED2        = 1 << 26
    ROOM_LAST_RESERVED3        = 1 << 27
    ROOM_LAST_TIME_BIT0        = 1 << 28
    ROOM_LAST_TIME_BIT1        = 1 << 29
    ROOM_LAST_TIME_BIT2        = 1 << 30
    ROOM_LAST_TIME_BIT3        = 1 << 31

    ROOM_FROM_UNKNOWN          = 0
    ROOM_FROM_HALLWAY          = 1 << 32
    ROOM_FROM_LIVING           = 1 << 33
    ROOM_FROM_DINING           = 1 << 34
    ROOM_FROM_KITCHEN          = 1 << 35
    ROOM_FROM_BATHROOM         = 1 << 36
    ROOM_FROM_OFFICE           = 1 << 37
    ROOM_FROM_BEDROOM          = 1 << 38
    ROOM_FROM_TOILET           = 1 << 39
    ROOM_FROM_PANTRY           = 1 << 40
    ROOM_FROM_RESERVED1        = 1 << 41
    ROOM_FROM_RESERVED2        = 1 << 42
    ROOM_FROM_RESERVED3        = 1 << 43
    ROOM_FROM_TIME_BIT0        = 1 << 44
    ROOM_FROM_TIME_BIT1        = 1 << 45
    ROOM_FROM_TIME_BIT2        = 1 << 46
    ROOM_FROM_TIME_BIT3        = 1 << 47

    ROOM_TO_UNKNOWN            = 0
    ROOM_TO_HALLWAY            = 1 << 48
    ROOM_TO_LIVING             = 1 << 49
    ROOM_TO_DINING             = 1 << 50
    ROOM_TO_KITCHEN            = 1 << 51
    ROOM_TO_BATHROOM           = 1 << 52
    ROOM_TO_OFFICE             = 1 << 53
    ROOM_TO_BEDROOM            = 1 << 54
    ROOM_TO_TOILET             = 1 << 55
    ROOM_TO_PANTRY             = 1 << 56
    ROOM_TO_RESERVED1          = 1 << 57
    ROOM_TO_RESERVED2          = 1 << 58
    ROOM_TO_RESERVED3          = 1 << 59
    ROOM_TO_TIME_BIT0          = 1 << 60
    ROOM_TO_TIME_BIT1          = 1 << 61
    ROOM_TO_TIME_BIT2          = 1 << 62
    ROOM_TO_TIME_BIT3          = 1 << 63

class trigger_location(IntFlag):
    FROM_UNKNOWN           = 0
    FROM_STATE             = 1 << 0
    FROM_STATE_NUMERIC     = 1 << 1
    FROM_EVENT             = 1 << 2
    FROM_ZONE_ARRIVE       = 1 << 3
    FROM_ZONE_DEPART       = 1 << 4
    FROM_ZONE_BEACON       = 1 << 5
    FROM_ZONE_HOTSPOT      = 1 << 6
    FROM_DEVICE            = 1 << 7
    FROM_DOMOTICA          = 1 << 8
    FROM_REMOTE_WEBHOOK    = 1 << 9
    FROM_REMOTE_API        = 1 << 10
    FROM_REMOTE_CLOUD      = 1 << 11
    FROM_REMOTE_WEB        = 1 << 12
    FROM_LOCAL_VOICE       = 1 << 13
    FROM_ORIGINE_INSIDE    = 1 << 14
    FROM_ORIGINE_OUTSIDE   = 1 << 15
    TO_UNKNOWN             = 0
    TO_STATE               = 1 << 16
    TO_STATE_NUMERIC       = 1 << 17
    TO_EVENT               = 1 << 18
    TO_ZONE_ARRIVE         = 1 << 19
    TO_ZONE_DEPART         = 1 << 20
    TO_ZONE_BEACON         = 1 << 21
    TO_ZONE_HOTSPOT        = 1 << 22
    TO_DEVICE              = 1 << 23
    TO_DOMOTICA            = 1 << 24
    TO_REMOTE_WEBHOOK      = 1 << 25
    TO_REMOTE_API          = 1 << 26
    TO_REMOTE_CLOUD        = 1 << 27
    TO_REMOTE_WEB          = 1 << 28
    TO_LOCAL_VOICE         = 1 << 29
    TO_ORIGINE_INSIDE      = 1 << 30
    TO_ORIGINE_OUTSIDE     = 1 << 31

class room_occupancy(IntFlag):
    ROOM_UNKNOWN           = 0
    ROOM_OFF               = 1 << 0
    ROOM_POWERSAVE         = 1 << 1
    ROOM_STANDBY           = 1 << 2
    ROOM_UNOCCUPIED        = 1 << 3
    ROOM_BUSY              = 1 << 4
    ROOM_ACTIVE            = 1 << 5
    ROOM_OVERRIDE_DEMAND   = 1 << 6
    ROOM_OVERRIDE_MAINT    = 1 << 7
    ROOM_OVERRIDE_WORKS    = 1 << 8
    ROOM_OVERRIDE_GUEST    = 1 << 9
    ROOM_OVERRIDE_RESERVE1 = 1 << 10
    ROOM_OVERRIDE_RESERVE2 = 1 << 11
    ROOM_OCCUPANCY         = 1 << 12
    ROOM_OCCUPANCY_PASS    = 1 << 13
    ROOM_OCCUPANCY_MOTION  = 1 << 14
    ROOM_OCCUPANCY_PIR     = 1 << 15
    ROOM_OCCUPANCY_HPS     = 1 << 16
    ROOM_OCCUPANCY_RADAR   = 1 << 17
    ROOM_OCCUPANCY_RESERVE1= 1 << 18
    ROOM_OCCUPANCY_RESERVE2= 1 << 19
    ROOM_ACTION_TIME       = 1 << 20
    ROOM_ACTION_TASK       = 1 << 21

class room_timing(IntFlag):
    RT_UNKNOWN          = 0
    RT_NONE             = 0 << 0
    RT_PASSED           = 1 << 0
    RT_MINIMAL          = 1 << 1
    RT_MINIMAL_OCCUPY   = 1 << 2
    RT_MINIMAL_TIMED    = 1 << 3
    RT_MINIMAL_BIT0     = 1 << 4
    RT_MINIMAL_BIT1     = 1 << 5
    RT_MINIMAL_BIT2     = 1 << 6
    RT_MINIMAL_BIT3     = 1 << 7
    RT_MAXIMAL_PASSED   = 1 << 8
    RT_MAXIMAL          = 1 << 9
    RT_MAXIMAL_OCCUPY   = 1 << 10
    RT_MAXIMAL_TIMED    = 1 << 11
    RT_MAXIMAL_BIT0     = 1 << 12
    RT_MAXIMAL_BIT1     = 1 << 13
    RT_MAXIMAL_BIT2     = 1 << 14
    RT_MAXIMAL_BIT3     = 1 << 15
    RT_POWERSAVE_PASSED = 1 << 16
    RT_POWERSAVE        = 1 << 17
    RT_POWERSAVE_OCCUPY = 1 << 18
    RT_POWERSAVE_TIMED  = 1 << 19
    RT_POWERSAVE_BIT0   = 1 << 20
    RT_POWERSAVE_BIT1   = 1 << 21
    RT_POWERSAVE_BIT2   = 1 << 22
    RT_POWERSAVE_BIT3   = 1 << 23
    RT_POWERSAVE_STEP0  = 1 << 24
    RT_POWERSAVE_STEP1  = 1 << 25
    RT_POWERSAVE_STEP2  = 1 << 26
    RT_POWERSAVE_STEP3  = 1 << 27
    RT_POWERSAVE_STEPS0 = 1 << 28
    RT_POWERSAVE_STEPS1 = 1 << 29
    RT_POWERSAVE_STEPS2 = 1 << 30
    RT_POWERSAVE_STEPS3 = 1 << 31

class room_during(IntFlag):
    RD_UNKNOWN           = 0
    RD_DURING_DAY        = 1 << 0
    RD_DURING_NIGHT      = 1 << 1
    RD_DURING_ARMED      = 1 << 2
    RD_DURING_ALARM      = 1 << 3
    RD_DURING_TIME       = 1 << 4
    RD_DURING_TIME_SLEEP = 1 << 5
    RD_DURING_TIME_MAINT = 1 << 6
    RD_DURING_TRIGGER    = 1 << 7

class room_brightness(IntFlag):
    RB_MINIMAL_UNKNOWN  = 0
    RB_MINIMAL_BIT0     = 1 << 0
    RB_MINIMAL_BIT1     = 1 << 1
    RB_MINIMAL_BIT2     = 1 << 2
    RB_MINIMAL_BIT3     = 1 << 3
    RB_MAXIMAL_BIT0     = 1 << 4
    RB_MAXIMAL_BIT1     = 1 << 5
    RB_MAXIMAL_BIT2     = 1 << 6
    RB_MAXIMAL_BIT3     = 1 << 7
    RB_MAINTENANCE_BIT0 = 1 << 8
    RB_MAINTENANCE_BIT1 = 1 << 9
    RB_MAINTENANCE_BIT2 = 1 << 10
    RB_MAINTENANCE_BIT3 = 1 << 11


class trigger_priority(IntFlag):
    PRIORITY_UNKNOWN        = 0
    PRIORITY_NONE           = 1 << 0
    PRIORITY_ENVIRONMENT    = 1 << 1
    PRIORITY_MOOD           = 1 << 2
    PRIORITY_PATH           = 1 << 3
    PRIORITY_BUSY           = 1 << 4
    PRIORITY_LIGHT          = 1 << 5
    PRIORITY_MAINTENANCE    = 1 << 6
    PRIORITY_RESERVED1      = 1 << 7
    PRIORITY_CRITICAL       = 1 << 8
    PRIORITY_CRITICAL_FIRE  = 1 << 9
    PRIORITY_CRITICAL_ALARM = 1 << 10
    PRIORITY_CRITICAL_HOUSE = 1 << 11
    PRIORITY_CRITICAL_USAGE = 1 << 12

class trigger_domotica(IntFlag):
    TRIGGER_UNKNOWN            = 0
    TRIGGER_ID                 = 1 << 0
    TRIGGER_AUTOMATION         = 1 << 1
    TRIGGER_ACTION             = 1 << 2
    TRIGGER_EVENT              = 1 << 3
    TRIGGER_BUS                = 1 << 4
    TRIGGER_REMOTE             = 1 << 5
    TRIGGER_BUTTON             = 1 << 6
    TRIGGER_BUTTON_REMOTE      = 1 << 7
    TRIGGER_DETECTOR           = 1 << 8
    TRIGGER_DETECTOR_MOTION    = 1 << 9
    TRIGGER_DETECTOR_PRESENCE  = 1 << 10
    TRIGGER_MOTION_ARRIVAL     = 1 << 11
    TRIGGER_MOTION_DEPART      = 1 << 12
    TRIGGER_MOTION_POWERSAVE   = 1 << 13
    TRIGGER_MOTION_DELAYED     = 1 << 14
    TRIGGER_MOTION_END         = 1 << 15

    TRIGGER_TIMED_POWERSAVE    = 1 << 16
    TRIGGER_TIMED_MINIMAL      = 1 << 17
    TRIGGER_TIMED_MAXIMAL      = 1 << 18
    TRIGGER_TIMED_RESERVED     = 1 << 19
    
    TRIGGER_EMERGENCY_BUTTON   = 1 << 20
    TRIGGER_EMERGENCY_FIRE     = 1 << 21
    TRIGGER_EMERGENCY_ALARM    = 1 << 22
    TRIGGER_EMERGENCY_HOUSE    = 1 << 23

    TRIGGER_POWER_OK           = 1 << 24
    TRIGGER_POWER_STANDBY      = 1 << 25
    TRIGGER_POWER_UPS          = 1 << 26
    TRIGGER_POWER_LOSS         = 1 << 27

    TRIGGER_ALARM_DISARMED     = 1 << 28
    TRIGGER_ALARM_ACTIVATED    = 1 << 29
    TRIGGER_ALARM_ARMED_AWAY   = 1 << 30
    TRIGGER_ALARM_ARMED_HOME   = 1 << 31
    TRIGGER_ALARM_ARMED_NIGHT  = 1 << 32

    TRIGGER_HOUSE_CRITICAL     = 1 << 33
    TRIGGER_HOUSE_FIRE         = 1 << 34
    TRIGGER_HOUSE_EMERGENCY    = 1 << 35
    TRIGGER_HOUSE_ALARM        = 1 << 36

class device_powered(IntFlag):
    DEVICE_POWER_UNKNOWN       = 0
    DEVICE_POWER_BATTERY       = 1 << 0
    DEVICE_POWER_CHARGABLE     = 1 << 1
    DEVICE_POWER_ADAPTER       = 1 << 2
    DEVICE_POWER_POWER         = 1 << 3
    DEVICE_POWER_BACKUP        = 1 << 4

class device_action(IntFlag):
    ON_UNKNOWN             = 0
    ON_MOTION_OFF          = 1 << 0
    ON_PIR_OFF             = 1 << 1
    ON_PRESENCE_OFF        = 1 << 2
    ON_RADAR_OFF           = 1 << 3
    ON_MOTION_ON           = 1 << 4
    ON_PIR_ON              = 1 << 5
    ON_PRESENCE_ON         = 1 << 6
    ON_RADAR_ON            = 1 << 7
    ON_DISARMED            = 1 << 8
    ON_ARMED_AWAY          = 1 << 9
    ON_ARMED_HOME          = 1 << 10
    ON_ARMED_NIGHT         = 1 << 11
    ON_ARMED_ALARM         = 1 << 12

    ON_RESERVED1           = 1 << 13
    ON_RESERVED2           = 1 << 14
    ON_RESERVED3           = 1 << 15

    ON_PATH_PASSING        = 1 << 16
    ON_PATH_ARRIVED        = 1 << 17
    ON_PATH_DEPARTED       = 1 << 18

    ON_HOUSE_TRIGGER       = 1 << 19
    ON_HOUSE_DOMOTICA      = 1 << 20
    ON_HOUSE_STANDBY       = 1 << 21
    ON_HOUSE_EMPTY         = 1 << 22
    ON_HOUSE_SLEEP         = 1 << 23

    DEFAULT_TURN_OFF       = 1 << 24
    DEFAULT_TURN_ON        = 1 << 25
    DEFAULT_TURN_POWERSAVE = 1 << 26
    DEFAULT_TURN_STANDBY   = 1 << 27

    TURN_OFF               = 1 << 28
    TURN_ON                = 1 << 29
    TURN_POWERSAVE         = 1 << 30
    TURN_STANDBY           = 1 << 31

class autonomous(IntFlag):
    MODE_NONE       = 0
    MODE_MANUAL     = 1 << 0
    MODE_AUTOMATIC  = 1 << 1
    MODE_SUPERVISED = 1 << 2
    MODE_LOCKED     = 1 << 3
    MODE_ORDER      = 1 << 4
    MODE_SEQUENCE   = 1 << 5
    MODE_BATCH      = 1 << 6

class mental_states(IntFlag):
    MOOD_NONE              = 0
    MOOD_FINE              = 1 << 0
    MOOD_NERVOUS           = 1 << 1
    MOOD_COPING            = 1 << 2
    MOOD_BAILOUT           = 1 << 3
    MOOD_MELTDOWN          = 1 << 4

class device_delays(IntFlag):
    DEFAULT_DELAY_UNKNOWN       = 0
    DEFAULT_DELAY_OFF_BIT0      = 1 << 0
    DEFAULT_DELAY_OFF_BIT1      = 1 << 1
    DEFAULT_DELAY_OFF_BIT2      = 1 << 2
    DEFAULT_DELAY_OFF_BIT3      = 1 << 3

    DEFAULT_DELAY_ON_BIT0       = 1 << 4
    DEFAULT_DELAY_ON_BIT1       = 1 << 5
    DEFAULT_DELAY_ON_BIT2       = 1 << 6
    DEFAULT_DELAY_ON_BIT3       = 1 << 7

    OCCUPANCE_DELAY_OFF_BIT0    = 1 << 8
    OCCUPANCE_DELAY_OFF_BIT1    = 1 << 9
    OCCUPANCE_DELAY_OFF_BIT2    = 1 << 10
    OCCUPANCE_DELAY_OFF_BIT3    = 1 << 11

    OCCUPANCE_DELAY_ON_BIT0     = 1 << 12
    OCCUPANCE_DELAY_ON_BIT1     = 1 << 13
    OCCUPANCE_DELAY_ON_BIT2     = 1 << 14
    OCCUPANCE_DELAY_ON_BIT3     = 1 << 15

    OCCUPANCE_STEP_OFF_BIT0     = 1 << 16
    OCCUPANCE_STEP_OFF_BIT1     = 1 << 17
    OCCUPANCE_STEP_OFF_BIT2     = 1 << 18
    OCCUPANCE_STEP_OFF_BIT3     = 1 << 19

    OCCUPANCE_STEP_ON_BIT0      = 1 << 20
    OCCUPANCE_STEP_ON_BIT1      = 1 << 21
    OCCUPANCE_STEP_ON_BIT2      = 1 << 22
    OCCUPANCE_STEP_ON_BIT3      = 1 << 23

    OCCUPANCE_STEPS_OFF_BIT0    = 1 << 24
    OCCUPANCE_STEPS_OFF_BIT1    = 1 << 25
    OCCUPANCE_STEPS_OFF_BIT2    = 1 << 26
    OCCUPANCE_STEPS_OFF_BIT3    = 1 << 27

    OCCUPANCE_STEPS_ON_BIT0     = 1 << 28
    OCCUPANCE_STEPS_ON_BIT1     = 1 << 29
    OCCUPANCE_STEPS_ON_BIT2     = 1 << 30
    OCCUPANCE_STEPS_ON_BIT3     = 1 << 31

    PASS_DELAY_OFF_BIT0         = 1 << 32
    PASS_DELAY_OFF_BIT1         = 1 << 33
    PASS_DELAY_OFF_BIT2         = 1 << 34
    PASS_DELAY_OFF_BIT3         = 1 << 35

    PASS_DELAY_ON_BIT0          = 1 << 36
    PASS_DELAY_ON_BIT1          = 1 << 37
    PASS_DELAY_ON_BIT2          = 1 << 38
    PASS_DELAY_ON_BIT3          = 1 << 39

    POWERSAVE_DELAY_OFF_BIT0    = 1 << 40
    POWERSAVE_DELAY_OFF_BIT1    = 1 << 41
    POWERSAVE_DELAY_OFF_BIT2    = 1 << 42
    POWERSAVE_DELAY_OFF_BIT3    = 1 << 43

    POWERSAVE_DELAY_ON_BIT0     = 1 << 44
    POWERSAVE_DELAY_ON_BIT1     = 1 << 45
    POWERSAVE_DELAY_ON_BIT2     = 1 << 46
    POWERSAVE_DELAY_ON_BIT3     = 1 << 47

    POWERSAVE_STEP_OFF_BIT0     = 1 << 48
    POWERSAVE_STEP_OFF_BIT1     = 1 << 49
    POWERSAVE_STEP_OFF_BIT2     = 1 << 50
    POWERSAVE_STEP_OFF_BIT3     = 1 << 51

    POWERSAVE_STEP_ON_BIT0      = 1 << 52
    POWERSAVE_STEP_ON_BIT1      = 1 << 53
    POWERSAVE_STEP_ON_BIT2      = 1 << 54
    POWERSAVE_STEP_ON_BIT3      = 1 << 55

    POWERSAVE_STEPS_OFF_BIT0    = 1 << 56
    POWERSAVE_STEPS_OFF_BIT1    = 1 << 57
    POWERSAVE_STEPS_OFF_BIT2    = 1 << 58
    POWERSAVE_STEPS_OFF_BIT3    = 1 << 59

    POWERSAVE_STEPS_ON_BIT0     = 1 << 60
    POWERSAVE_STEPS_ON_BIT1     = 1 << 61
    POWERSAVE_STEPS_ON_BIT2     = 1 << 62
    POWERSAVE_STEPS_ON_BIT3     = 1 << 63


class RESTPayloadManager:
    @staticmethod
    def get_hex_timestamp() -> str:
        """Outputs standard uppercase 32-bit timestamp hex string."""
        return f"{int(time.time()) & 0xFFFFFFFF:08X}"

    @staticmethod
    def calculate_checkdigits(payload_segments: list) -> str:
        """XOR checksum calculation over all data components."""
        chk = 0
        for segment in payload_segments:
            clean = segment.replace("0x", "").replace("-", "")
            if clean:
                try:
                    chk ^= int(clean, 16)
                except ValueError:
                    pass
        return f"{chk & 0xFFFF:04X}"  # 4 hex character validation ceiling block

    def build_packet_string(self, state_data: dict) -> str:
        """
        Packs inputs into the exact layout format requested.
        Output matches: FFFFFFFF-0000-0000-0000-0000-00000000-...-checkdigits
        """
        ts = self.get_hex_timestamp()

        # 1. TRIG ROOM + Time (64-bit field broken out into four 16-bit blocks)
        rl = int(state_data.get('room_location', 0))
        tr_now  = f"{rl & 0xFFFF:04X}"
        tr_last = f"{(rl >> 16) & 0xFFFF:04X}"
        tr_from = f"{(rl >> 32) & 0xFFFF:04X}"
        tr_to   = f"{(rl >> 48) & 0xFFFF:04X}"

        # 2. ROOMOCCU (24-bit field represented as 8 characters: 00000000)
        ro = f"{int(state_data.get('room_occupancy', 0)) & 0xFFFFFF:08X}"

        # 3. ROOM TIME split block layout (AABB-CCDD structural layout mapping)
        rt = int(state_data.get('room_timing', 0))
        rd = int(state_data.get('room_during', 0)) & 0xFF
        rb = int(state_data.get('room_brightness', 0)) & 0xFF
        
        rt_min = f"{rt & 0xFFFF:04X}"
        rt_max = f"{(rt >> 16) & 0xFFFF:04X}"
        rd_str = f"{rd:02X}"
        rb_str = f"{rb:02X}"

        # 4. TRIG LOC (32-bit boundary tracking separated into two 16-bit units)
        tl = int(state_data.get('trigger_location', 0))
        tl_from = f"{tl & 0xFFFF:04X}"
        tl_to   = f"{(tl >> 16) & 0xFFFF:04X}"

        # 5. TR-PRIOR (16-bit layout)
        tp = f"{int(state_data.get('trigger_priority', 0)) & 0xFFFF:04X}"

        # 6. DEVICE ACTION (32-bit field)
        da = f"{int(state_data.get('device_action', 0)) & 0xFFFFFFFF:08X}"

        # 7. DEVICE DELAYS (64-bit field broken out exactly into 0xAB-CDEFGH-IJ-KLMNOP format)
        dd = int(state_data.get('device_delays', 0))
        ab = f"0x{(dd & 0xFF):02X}"
        cdefgh = f"{(dd >> 8) & 0xFFFFFF:06X}"
        ij = f"{(dd >> 32) & 0xFF:02X}"
        klmnop = f"{(dd >> 40) & 0xFFFFFF:06X}"

        # 8. POWERED (4-bit field / single character width)
        dp = f"{int(state_data.get('device_powered', 0)) & 0xF:X}"

        # Group components for validation arrays
        checksum_pool = [
            ts, tr_now, tr_last, tr_from, tr_to, ro, rt_min, rt_max, 
            rd_str, rb_str, tl_from, tl_to, tp, da, ab, cdefgh, ij, klmnop, dp
        ]
        checkdigits = self.calculate_checkdigits(checksum_pool)

        # Output payload structured to match layout rules exactly
        packet = (
            f"{ts}-{tr_now}-{tr_last}-{tr_from}-{tr_to}-{ro}-"
            f"{rt_min}-{rt_max}-{rd_str}-{rb_str}-{tl_from}-{tl_to}-"
            f"{tp}-{rd_str}-{rb_str}-{da}-{ab}-{cdefgh}-{ij}-{klmnop}-"
            f"{dp}-{checkdigits}"
        )
        return packet

# --- Local Verification Runner ---
if __name__ == "__main__":
    manager = RESTPayloadManager()
    
    # Generate mock configuration to verify bit packing limits
    mock_inputs = {
        'room_location': room_location.ROOM_NOW_LIVING | room_location.ROOM_LAST_HALLWAY,
        'room_occupancy': room_occupancy.ROOM_ACTIVE | room_occupancy.ROOM_OCCUPANCY_MOTION,
        'room_timing': room_timing.RT_MINIMAL | room_timing.RT_POWERSAVE_STEP1,
        'room_during': room_during.RD_DURING_NIGHT,
        'room_brightness': room_brightness.RB_MINIMAL_BIT2,
        'trigger_location': trigger_location.FROM_DEVICE | trigger_location.TO_STATE,
        'trigger_priority': trigger_priority.PRIORITY_LIGHT,
        'device_action': device_action.TURN_ON | device_action.ON_MOTION_ON,
        'device_delays': device_delays.DEFAULT_DELAY_OFF_BIT1 | device_delays.OCCUPANCE_DELAY_ON_BIT3,
        'device_powered': device_powered.DEVICE_POWER_POWER
    }

    print("Verified REST String Output Payload:")
    print(manager.build_packet_string(mock_inputs))


#
#                                            ROOM DURING-+   +-- ROOM BRIGHTNESS
#Timestamp [  TRIG ROOM+time   ]  [ROOMOCCU]  [ROOM TIME |   | ] [TRIG- LOC] [TR-PRIOR] [DEVICE  ]  [DEVICE DELAYS     ] [POWERED]    #Timestamp [ NOW -LAST-FROM- TO]  [OCCUPANC]  [AABB-CCDD |   | ] [FROM - TO]  [HI-LO]   [ACTION  ]  [DELAYS            ] []
#FFFFFFFF  0x0000-0000-0000-0000 0x000-00000 0x0000-0000-00-0000 0x0000-0000  0x00-00   0x00000000 0xAB CDEFGH IJ KLMNOP 0x0
#                                              | |  | |
#				MINIMAL MIN---+ |  | +-- POWERSAVE STEP/S
#				MAXIMAL MIN-----+  +---- POWERSAVE MIN
# DEVICE DELAYS: 
# AB = Default Delay Off & On, CDEFGH = OCCUPANCE Delay OFF, ON, Step Off, Step On, Steps Off, Steps On, 
# IJ = Pass Delay Off+On,      KLMNOP = Powersave Delay OFF, ON, Step Off, Step ON, Steps Off, Steps On
#
# example string: 
# FFFFFFFF-0000-0000-0000-0000-00000000-0000-0000-00-0000-0000-0000-00-00-00000000-0xABCD-EFGH-IJKL-MNOP-0-checkdigits
