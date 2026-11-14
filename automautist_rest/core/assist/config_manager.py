import json
from pathlib import Path
from core.assist.flags import (
    mental_states,
    NeuroCognitiveState,
    ExpressiveInteraction,
    OverloadContext,
    ProtectionDirectives,
)

CARD_CONFIG_PATHS = [
    Path('/homeassistant/automautist-assist-cards.json'),
    Path('/share/automautist_db/automautist-assist-cards.json'),
    Path('/app/storage/automautist-assist-cards.json'),
]

DEFAULT_EXPORT_PATH = (
    Path('/share/automautist_db/automautist-assist-cards.json')
    if Path('/share').is_dir()
    else Path('/app/storage/automautist-assist-cards.json')
)

BASELINE_PRESETS = {
    "MOOD_FINE": {
        "label": "Fine",
        "color_hex": "#198754",
        "cognitive": ["COGNITIVE_OK", "MEMORY_OK", "FOCUS_OK"],
        "interaction": ["INTERACT_NONE"],
        "context": ["COPING_OK"],
        "protection": ["PROTECT_NONE"],
    },
    "MOOD_NERVOUS": {
        "label": "Nervous",
        "color_hex": "#ffc107",
        "cognitive": ["COGNITIVE_NERVOUS", "COGNITIVE_ANXIOUS", "BARRIER_HUMOR_NO_SARCASM"],
        "interaction": ["RESPONSE_DELAYED"],
        "context": ["COPING_ANNOYED", "SENSORY_EASY_AGGRAVATION"],
        "protection": ["STAY_CALM_AND_RELAXED", "DO_TALK_CLEARLY_ONLY"],
    },
    "MOOD_COPING": {
        "label": "Coping",
        "color_hex": "#fd7e14",
        "cognitive": ["COGNITIVE_TUNNEL_VISION", "FOCUS_LESS", "BARRIER_NO_HIDDEN_MESSAGES", "BARRIER_NO_SOCIAL_CUES"],
        "interaction": ["RESPONSE_DELAYED", "EXPRESSION_CONCISE"],
        "context": ["COPING_DIFFICULT", "SENSORY_HYPERACUSIS", "SENSORY_PHOTO_AVERSION"],
        "protection": ["STAY_CALM_AND_RELAXED", "DO_TALK_SLOWLY", "DO_TALK_LOW_VOLUME", "DO_NOT_PRESSURE"],
    },
    "MOOD_BAILOUT": {
        "label": "Bailout",
        "color_hex": "#e65c00",
        "cognitive": ["COGNITIVE_FOGGY", "FOCUS_INITIATION_DIFFICULT", "BARRIER_NO_TOUCHING", "BARRIER_NO_AGGRO_OR_CAPTIVE"],
        "interaction": ["RESPONSE_INTERMITTENT", "EXPRESSION_REDUCED", "STIMMING_TOOLS_FEEDBACK"],
        "context": ["COPING_TERRIBLE", "SENSORY_SPATIAL_DISTRESS", "SENSORY_REDIRECTION"],
        "protection": ["DO_NOT_TOUCH", "DO_NOT_PRESSURE", "DO_TALK_REQUIRED_NEEDS", "HELP_FIND_CALM_SPOT", "HELP_FIND_EXIT_ASAP", "WARN_RESPONSE_VOLATILITY"],
    },
    "MOOD_MELTDOWN": {
        "label": "Meltdown",
        "color_hex": "#dc3545",
        "cognitive": ["COGNITIVE_LOST_TIMESPACE", "FOCUS_EXECUTIVE_DISASTER", "BARRIER_NO_TOUCHING", "BARRIER_NO_AGGRO_OR_CAPTIVE"],
        "interaction": ["RESPONSE_UNRESPONSIVE", "EXPRESSION_FAIL_MUTISM", "EXPRESSION_FAIL_UNDERSTAND", "STIMMING_TOOLS_PRESSURE"],
        "context": ["COPING_FIGHT_OR_FLIGHT", "COPING_NEAR_MELTDOWN", "SENSORY_HYPERACUSIS", "SENSORY_PHOTO_AVERSION"],
        "protection": ["DO_NOT_TOUCH", "DO_NOT_AGITATE", "DO_NOT_TRIGGER", "DO_TALK_REQUIRED_NEEDS", "HELP_FIND_SAFE_SPOT", "HELP_TO_COMMUNICATE", "WARN_MALADAPTIVE_DECISIONS", "WARN_RESPONSE_VOLATILITY"],
    },
    "MOOD_CRASH": {
        "label": "Crash",
        "color_hex": "#0d6efd",
        "cognitive": ["COGNITIVE_FOGGY", "MEMORY_CRASHING", "FOCUS_COGNITIVE_INERTIA", "BARRIER_NO_TOUCHING"],
        "interaction": ["RESPONSE_UNRESPONSIVE", "EXPRESSION_REDUCED"],
        "context": ["COPING_DIFFICULT", "TRIGGER_COPING_EXHAUSTION", "TRIGGER_COPING_TIRED"],
        "protection": ["STAY_CALM_AND_RELAXED", "DO_NOT_TOUCH", "DO_NOT_PRESSURE", "HELP_FIND_RESTING_SPOT", "HELP_FIND_MY_HOME"],
    },
}


def names_to_mask(enum_cls, names_list) -> int:
    mask = 0
    for name in (names_list or []):
        member = getattr(enum_cls, str(name).strip(), None)
        if member is not None:
            mask |= int(member.value)
    return mask


def load_assist_card_config() -> dict:
    for path in CARD_CONFIG_PATHS:
        if path.is_file():
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                data['_source_path'] = str(path)
                return data
            except Exception as err:
                print(f"[AutoMAutist:ASSIST] Error reading {path}: {err}")
    return {
        "locked": False,
        "lock_message": "",
        "custom_phrases": {},
        "cards": BASELINE_PRESETS,
        "_source_path": "built-in-defaults",
    }


def export_baseline_json(target_path: Path = DEFAULT_EXPORT_PATH) -> dict:
    payload = {
        "locked": False,
        "lock_message": "Set 'locked' to true so a caregiver or assistant can lock these settings.",
        "custom_phrases": {},
        "available_flags_reference": {
            "cognitive": [f.name for f in NeuroCognitiveState if f.value != 0],
            "interaction": [f.name for f in ExpressiveInteraction if f.value != 0],
            "context": [f.name for f in OverloadContext if f.value != 0],
            "protection": [f.name for f in ProtectionDirectives if f.value != 0],
        },
        "cards": BASELINE_PRESETS,
    }
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)
    return payload
