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
import json
from pathlib import Path

USER_LANG_DIRS = [
    Path('/homeassistant'),
    Path('/share/automautist_db'),
    Path('/app/storage'),
]

BUILTIN_TRANSLATIONS = {
    "en": {
        "lang_name": "English",
        "ui": {
            "card_header": "AUTISTIC SUPPORT / EMERGENCY CARD",
            "current_state": "CURRENT STATE",
            "locked_badge": "Locked",
            "warnings_title": "Critical Notice (Read First)",
            "help_title": "How to Help Right Now",
            "cognitive_title": "Executive & Communication",
            "sensory_title": "Sensory & Stimming",
            "default_help": "Calm, plain, respectful communication.",
            "default_comm": "Standard communication active.",
            "console_btn": "Console",
            "export_btn": "Export JSON",
            "print_btn": "Print",
        },
        "moods": {
            "MOOD_FINE": "Fine",
            "MOOD_NERVOUS": "Nervous",
            "MOOD_COPING": "Coping",
            "MOOD_BAILOUT": "Bailout",
            "MOOD_MELTDOWN": "Meltdown",
            "MOOD_CRASH": "Crash",
        },
        "flags": {
            "COGNITIVE_OK": "Cognitive processing is clear and stable.",
            "COGNITIVE_NERVOUS": "Heightened nervous system tension.",
            "COGNITIVE_ANXIOUS": "Elevated anxiety; keep interactions predictable.",
            "COGNITIVE_TUNNEL_VISION": "Tunnel vision active; cannot process multiple inputs.",
            "COGNITIVE_FOGGY": "Severe brain fog; thinking and decision-making are slowed.",
            "COGNITIVE_LOST_TIMESPACE": "Disoriented in time or space; needs calm grounding.",
            "MEMORY_OK": "Short-term memory functioning normally.",
            "MEMORY_CRASHING": "Short-term memory overload; write down important details.",
            "FOCUS_OK": "Focus and attention are stable.",
            "FOCUS_LESS": "Reduced attention span; keep sentences short.",
            "FOCUS_INITIATION_DIFFICULT": "Task initiation blocked; gentle step-by-step prompts help.",
            "FOCUS_EXECUTIVE_DISASTER": "Executive function offline; cannot plan or organize right now.",
            "FOCUS_COGNITIVE_INERTIA": "Cognitive inertia; transitioning between tasks is very hard.",
            "BARRIER_HUMOR_NO_SARCASM": "Take words literally; avoid sarcasm, idioms, or jokes.",
            "BARRIER_NO_HIDDEN_MESSAGES": "Be direct and explicit; do not rely on hints or subtext.",
            "BARRIER_NO_SOCIAL_CUES": "Cannot read facial expressions or body language cues.",
            "BARRIER_NO_TOUCHING": "Physical touch causes distress or panic.",
            "BARRIER_NO_AGGRO_OR_CAPTIVE": "Loud voices, confrontation, or blocking exits triggers fight-or-flight.",
            "RESPONSE_DELAYED": "Delayed verbal response; allow 5-10 seconds to answer.",
            "RESPONSE_INTERMITTENT": "Speech is intermittent; may nod, point, or type instead.",
            "RESPONSE_UNRESPONSIVE": "Temporarily non-speaking (situational mutism); still hears and understands.",
            "EXPRESSION_CONCISE": "Communicating in short, direct phrases only.",
            "EXPRESSION_REDUCED": "Severely reduced verbal output; use yes/no questions.",
            "EXPRESSION_FAIL_MUTISM": "Cannot speak right now; use written text or cards.",
            "EXPRESSION_FAIL_UNDERSTAND": "Difficulty processing spoken speech; show written text.",
            "STIMMING_TOOLS_FEEDBACK": "Using sensory/stimming tools to self-regulate; this is safe.",
            "STIMMING_TOOLS_PRESSURE": "Needs deep pressure or sensory tool to stabilize.",
            "COPING_OK": "Coping well with current environment.",
            "COPING_ANNOYED": "Growing sensory irritation; reduce background noise.",
            "COPING_DIFFICULT": "Struggling to filter sensory input.",
            "COPING_TERRIBLE": "Sensory overload threshold reached; immediate exit needed.",
            "COPING_FIGHT_OR_FLIGHT": "Acute nervous system fight-or-flight response active.",
            "COPING_NEAR_MELTDOWN": "On the verge of a neurological meltdown.",
            "SENSORY_EASY_AGGRAVATION": "High sensitivity to sudden sounds or interruptions.",
            "SENSORY_HYPERACUSIS": "Sound sensitivity (hyperacusis); lower voice and minimize noise.",
            "SENSORY_PHOTO_AVERSION": "Light sensitivity; dim bright lights or screens.",
            "SENSORY_SPATIAL_DISTRESS": "Crowds and tight spaces cause acute spatial distress.",
            "SENSORY_REDIRECTION": "Needs quiet, low-stimulation environment immediately.",
            "TRIGGER_COPING_EXHAUSTION": "Severe post-overload exhaustion.",
            "TRIGGER_COPING_TIRED": "Deep fatigue; needs rest without demands.",
            "STAY_CALM_AND_RELAXED": "Speak in a calm, steady, unhurried tone.",
            "DO_TALK_CLEARLY_ONLY": "Use clear, literal, single-step instructions.",
            "DO_TALK_SLOWLY": "Speak slowly and pause between sentences.",
            "DO_TALK_LOW_VOLUME": "Keep your voice quiet and gentle.",
            "DO_TALK_REQUIRED_NEEDS": "Only ask essential safety or basic-need questions.",
            "DO_NOT_TOUCH": "DO NOT TOUCH without explicit permission.",
            "DO_NOT_PRESSURE": "Do not rush, pressure, or demand immediate answers.",
            "DO_NOT_AGITATE": "Do not raise your voice, argue, or crowd personal space.",
            "DO_NOT_TRIGGER": "Remove bright lights, alarms, or loud chatter nearby.",
            "HELP_FIND_CALM_SPOT": "Help guide to a quiet, low-light waiting area.",
            "HELP_FIND_EXIT_ASAP": "Assist in finding the nearest quiet exit immediately.",
            "HELP_FIND_SAFE_SPOT": "Ensure a safe, enclosed, quiet space to recover.",
            "HELP_FIND_RESTING_SPOT": "Provide a quiet place to sit or lie down undisturbed.",
            "HELP_FIND_MY_HOME": "Help arrange safe transport home or contact trusted support.",
            "HELP_TO_COMMUNICATE": "Offer paper, phone text, or yes/no cards to communicate.",
            "WARN_RESPONSE_VOLATILITY": "WARNING: Stress reactions are involuntary neurological responses, not aggression.",
            "WARN_MALADAPTIVE_DECISIONS": "WARNING: Cannot reliably sign legal documents or make complex decisions right now.",
        },
    },

    "nl": {
        "lang_name": "Nederlands",
        "ui": {
            "card_header": "AUTISME ONDERSTEUNING / NOODKAART",
            "current_state": "HUIDIGE STATUS",
            "locked_badge": "Vergrendeld",
            "warnings_title": "Belangrijke Melding (Eerst Lezen)",
            "help_title": "Hoe Nu Te Helpen",
            "cognitive_title": "Cognitie & Communicatie",
            "sensory_title": "Prikkels & Stimming",
            "default_help": "Rustige, duidelijke en respectvolle communicatie.",
            "default_comm": "Standaard communicatie actief.",
            "console_btn": "Paneel",
            "export_btn": "Exporteer JSON",
            "print_btn": "Afdrukken",
        },
        "moods": {
            "MOOD_FINE": "Goed",
            "MOOD_NERVOUS": "Gespannen",
            "MOOD_COPING": "Overprikkeld",
            "MOOD_BAILOUT": "Terugtrekken",
            "MOOD_MELTDOWN": "Meltdown",
            "MOOD_CRASH": "Crash / Uitputting",
        },
        "flags": {
            "COGNITIVE_OK": "Cognitieve verwerking is helder en stabiel.",
            "COGNITIVE_NERVOUS": "Verhoogde spanning in het zenuwstelsel.",
            "COGNITIVE_ANXIOUS": "Verhoogde angst; houd interacties voorspelbaar.",
            "COGNITIVE_TUNNEL_VISION": "Tunnelvisie actief; kan geen meerdere prikkels tegelijk verwerken.",
            "COGNITIVE_FOGGY": "Zware hersenmist; denken en beslissen gaat traag.",
            "COGNITIVE_LOST_TIMESPACE": "Gedesoriënteerd in tijd of ruimte; rustige houvast nodig.",
            "MEMORY_OK": "Kortetermijngeheugen werkt normaal.",
            "MEMORY_CRASHING": "Kortetermijngeheugen overbelast; schrijf belangrijke info op.",
            "FOCUS_OK": "Focus en aandacht zijn stabiel.",
            "FOCUS_LESS": "Verminderde aandachtsspanne; houd zinnen kort.",
            "FOCUS_INITIATION_DIFFICULT": "Taakstart geblokkeerd; rustige stap-voor-stap hulp helpt.",
            "FOCUS_EXECUTIVE_DISASTER": "Executieve functies uitgevallen; kan nu niet plannen of organiseren.",
            "FOCUS_COGNITIVE_INERTIA": "Cognitieve inertie; schakelen tussen taken is erg moeilijk.",
            "BARRIER_HUMOR_NO_SARCASM": "Neem woorden letterlijk; vermijd sarcasme of grapjes.",
            "BARRIER_NO_HIDDEN_MESSAGES": "Wees direct en duidelijk; geen hints of dubbele bodems.",
            "BARRIER_NO_SOCIAL_CUES": "Kan gezichtsuitdrukkingen of lichaamstaal niet lezen.",
            "BARRIER_NO_TOUCHING": "Fysieke aanraking veroorzaakt paniek of stress.",
            "BARRIER_NO_AGGRO_OR_CAPTIVE": "Luide stemmen, confrontatie of uitgangen blokkeren wekt vluchtreactie op.",
            "RESPONSE_DELAYED": "Vertraagde reactie; geef 5-10 seconden tijd om te antwoorden.",
            "RESPONSE_INTERMITTENT": "Spraak is beperkt; kan knikken, wijzen of typen.",
            "RESPONSE_UNRESPONSIVE": "Tijdelijk niet-sprekend (mutisme); hoort en begrijpt alles nog wel.",
            "EXPRESSION_CONCISE": "Communiceert alleen in korte, directe woorden.",
            "EXPRESSION_REDUCED": "Sterk verminderde spraak; stel ja/nee-vragen.",
            "EXPRESSION_FAIL_MUTISM": "Kan nu niet spreken; gebruik tekst of deze kaart.",
            "EXPRESSION_FAIL_UNDERSTAND": "Moeite met gesproken taal verwerken; toon geschreven tekst.",
            "STIMMING_TOOLS_FEEDBACK": "Gebruikt prikkel-/stimminghulpmiddelen om te kalmeren; dit is veilig.",
            "STIMMING_TOOLS_PRESSURE": "Heeft diepe druk of prikkelhulpmiddel nodig om te stabiliseren.",
            "COPING_OK": "Gaat goed om met de huidige omgeving.",
            "COPING_ANNOYED": "Toenemende prikkelgevoeligheid; verminder achtergrondgeluid.",
            "COPING_DIFFICULT": "Moeite om omgevingsprikkels te filteren.",
            "COPING_TERRIBLE": "Grens van overprikkeling bereikt; direct vertrekken nodig.",
            "COPING_FIGHT_OR_FLIGHT": "Acute vecht-of-vluchtreactie van het zenuwstelsel.",
            "COPING_NEAR_MELTDOWN": "Op het randje van een neurologische meltdown.",
            "SENSORY_EASY_AGGRAVATION": "Hoge gevoeligheid voor plotselinge geluiden of onderbrekingen.",
            "SENSORY_HYPERACUSIS": "Geluidsgevoeligheid (hyperacusis); praat zacht en beperk lawaai.",
            "SENSORY_PHOTO_AVERSION": "Lichtgevoeligheid; dim felle lichten of schermen.",
            "SENSORY_SPATIAL_DISTRESS": "Drukte en krappe ruimtes veroorzaken acute stress.",
            "SENSORY_REDIRECTION": "Heeft direct een rustige, prikkelarme omgeving nodig.",
            "TRIGGER_COPING_EXHAUSTION": "Zware uitputting na overprikkeling.",
            "TRIGGER_COPING_TIRED": "Diepe vermoeidheid; rust nodig zonder eisen.",
            "STAY_CALM_AND_RELAXED": "Spreek op een rustige, kalme en gelijkmatige toon.",
            "DO_TALK_CLEARLY_ONLY": "Gebruik duidelijke, letterlijke instructies van één stap.",
            "DO_TALK_SLOWLY": "Spreek langzaam en pauzeer tussen zinnen.",
            "DO_TALK_LOW_VOLUME": "Houd uw stem zacht en vriendelijk.",
            "DO_TALK_REQUIRED_NEEDS": "Stel alleen noodzakelijke vragen over veiligheid of basisbehoeften.",
            "DO_NOT_TOUCH": "NIET AANRAKEN zonder uitdrukkelijke toestemming.",
            "DO_NOT_PRESSURE": "Niet haasten, pushen of directe antwoorden eisen.",
            "DO_NOT_AGITATE": "Verhef uw stem niet en houd voldoende persoonlijke ruimte.",
            "DO_NOT_TRIGGER": "Beperk fel licht, alarmen of luid gepraat in de buurt.",
            "HELP_FIND_CALM_SPOT": "Help naar een rustige, prikkelarme wachtruimte.",
            "HELP_FIND_EXIT_ASAP": "Help direct de dichtstbijzijnde rustige uitgang te vinden.",
            "HELP_FIND_SAFE_SPOT": "Zorg voor een veilige, afgesloten en rustige plek.",
            "HELP_FIND_RESTING_SPOT": "Bied een rustige plek om ongestoord te zitten of liggen.",
            "HELP_FIND_MY_HOME": "Help veilig vervoer naar huis regelen of bel vertrouwd contact.",
            "HELP_TO_COMMUNICATE": "Bied papier, telefoontekst of ja/nee-kaarten aan.",
            "WARN_RESPONSE_VOLATILITY": "WAARSCHUWING: Stressreacties zijn onvrijwillige neurologische reacties, geen agressie.",
            "WARN_MALADAPTIVE_DECISIONS": "WAARSCHUWING: Kan nu geen juridische documenten tekenen of complexe keuzes maken.",
        },
    },

    "fr": {
        "lang_name": "Français",
        "ui": {
            "card_header": "CARTE DE SOUTIEN / URGENCE AUTISME",
            "current_state": "ÉTAT ACTUEL",
            "locked_badge": "Verrouillé",
            "warnings_title": "Avis Critique (À Lire en Premier)",
            "help_title": "Comment Aider Maintenant",
            "cognitive_title": "Cognition & Communication",
            "sensory_title": "Sensoriel & Stimming",
            "default_help": "Communication calme, claire et respectueuse.",
            "default_comm": "Communication standard active.",
            "console_btn": "Console",
            "export_btn": "Exporter JSON",
            "print_btn": "Imprimer",
        },
        "moods": {
            "MOOD_FINE": "Calme",
            "MOOD_NERVOUS": "Tendu",
            "MOOD_COPING": "Surcharge",
            "MOOD_BAILOUT": "Retrait Urgence",
            "MOOD_MELTDOWN": "Meltdown",
            "MOOD_CRASH": "Épuisement",
        },
        "flags": {
            "COGNITIVE_FOGGY": "Brouillard cérébral sévère ; la réflexion est ralentie.",
            "COGNITIVE_TUNNEL_VISION": "Vision tunnel ; impossible de traiter plusieurs informations à la fois.",
            "BARRIER_HUMOR_NO_SARCASM": "Prenez les mots au sens littéral ; évitez le sarcasme.",
            "BARRIER_NO_TOUCHING": "Le contact physique provoque de la détresse ou de la panique.",
            "RESPONSE_DELAYED": "Réponse verbale différée ; laissez 5 à 10 secondes pour répondre.",
            "RESPONSE_UNRESPONSIVE": "Mutisme situationnel temporaire ; entend et comprend toujours.",
            "EXPRESSION_FAIL_MUTISM": "Impossible de parler maintenant ; utilisez l'écrit ou cette carte.",
            "SENSORY_HYPERACUSIS": "Hypersensibilité au bruit ; baissez la voix et réduisez le bruit.",
            "SENSORY_PHOTO_AVERSION": "Sensibilité à la lumière ; tamisez les lumières vives.",
            "DO_NOT_TOUCH": "NE PAS TOUCHER sans permission explicite.",
            "DO_NOT_PRESSURE": "Ne pas presser ni exiger de réponse immédiate.",
            "DO_TALK_SLOWLY": "Parlez lentement avec des phrases courtes.",
            "DO_TALK_LOW_VOLUME": "Parlez à voix basse et calme.",
            "HELP_FIND_CALM_SPOT": "Aidez à rejoindre un endroit calme et peu éclairé.",
            "HELP_FIND_EXIT_ASAP": "Aidez à trouver la sortie calme la plus proche.",
            "WARN_RESPONSE_VOLATILITY": "ATTENTION : Les réactions de stress sont neurologiques et involontaires, pas de l'agressivité.",
            "WARN_MALADAPTIVE_DECISIONS": "ATTENTION : Impossible de signer des documents légaux ou de prendre des décisions complexes.",
        },
    },
    "de": {
        "lang_name": "Deutsch",
        "ui": {
            "card_header": "AUTISMUS-UNTERSTÜTZUNGS- / NOTFALLKARTE",
            "current_state": "AKTUELLER ZUSTAND",
            "locked_badge": "Gesperrt",
            "warnings_title": "Wichtiger Hinweis (Zuerst Lesen)",
            "help_title": "Wie Sie Jetzt Helfen Können",
            "cognitive_title": "Kognition & Kommunikation",
            "sensory_title": "Sensorik & Stimming",
            "default_help": "Ruhige, klare und respektvolle Kommunikation.",
            "default_comm": "Standardkommunikation aktiv.",
            "console_btn": "Konsole",
            "export_btn": "JSON Export",
            "print_btn": "Drucken",
        },
        "moods": {
            "MOOD_FINE": "Stabil",
            "MOOD_NERVOUS": "Angespannt",
            "MOOD_COPING": "Reizüberflutet",
            "MOOD_BAILOUT": "Rückzug Nötig",
            "MOOD_MELTDOWN": "Meltdown",
            "MOOD_CRASH": "Erschöpfung",
        },
        "flags": {
            "COGNITIVE_FOGGY": "Starker Gehirnnebel; Denken und Entscheiden sind verlangsamt.",
            "COGNITIVE_TUNNEL_VISION": "Tunnelblick aktiv; mehrere Reize können nicht gleichzeitig verarbeitet werden.",
            "BARRIER_HUMOR_NO_SARCASM": "Worte wörtlich nehmen; Sarkasmus und Ironie vermeiden.",
            "BARRIER_NO_TOUCHING": "Körperliche Berührung löst Stress oder Panik aus.",
            "RESPONSE_DELAYED": "Verzögerte Antwort; bitte 5-10 Sekunden Zeit lassen.",
            "RESPONSE_UNRESPONSIVE": "Vorübergehender Mutismus; hört und versteht weiterhin alles.",
            "EXPRESSION_FAIL_MUTISM": "Sprechen ist gerade nicht möglich; bitte Text oder diese Karte nutzen.",
            "SENSORY_HYPERACUSIS": "Geräuschempfindlichkeit; bitte leise sprechen und Lärm reduzieren.",
            "SENSORY_PHOTO_AVERSION": "Lichtempfindlichkeit; grelles Licht oder Bildschirme dimmen.",
            "DO_NOT_TOUCH": "NICHT BERÜHREN ohne ausdrückliche Erlaubnis.",
            "DO_NOT_PRESSURE": "Keinen Zeitdruck ausüben und keine sofortige Antwort fordern.",
            "DO_TALK_SLOWLY": "Bitte langsam und in kurzen, klaren Sätzen sprechen.",
            "DO_TALK_LOW_VOLUME": "Bitte leise und ruhig sprechen.",
            "HELP_FIND_CALM_SPOT": "Bitte zu einem ruhigen, reizarmen Ort begleiten.",
            "HELP_FIND_EXIT_ASAP": "Bitte sofort den nächsten ruhigen Ausgang zeigen.",
            "WARN_RESPONSE_VOLATILITY": "ACHTUNG: Stressreaktionen sind unwillkürliche neurologische Reaktionen, keine Aggression.",
            "WARN_MALADAPTIVE_DECISIONS": "ACHTUNG: Kann derzeit keine rechtlichen Dokumente unterschreiben oder komplexe Entscheidungen treffen.",
        },
    },
    "es": {
        "lang_name": "Español",
        "ui": {
            "card_header": "TARJETA DE APOYO / EMERGENCIA AUTISMO",
            "current_state": "ESTADO ACTUAL",
            "locked_badge": "Bloqueado",
            "warnings_title": "Aviso Crítico (Leer Primero)",
            "help_title": "Cómo Ayudar Ahora Mismo",
            "cognitive_title": "Cognición y Comunicación",
            "sensory_title": "Sensorial y Stimming",
            "default_help": "Comunicación tranquila, clara y respetuosa.",
            "default_comm": "Comunicación estándar activa.",
            "console_btn": "Consola",
            "export_btn": "Exportar JSON",
            "print_btn": "Imprimir",
        },
        "moods": {
            "MOOD_FINE": "Bien",
            "MOOD_NERVOUS": "Nervioso",
            "MOOD_COPING": "Sobrecarga",
            "MOOD_BAILOUT": "Retirada Urgente",
            "MOOD_MELTDOWN": "Meltdown",
            "MOOD_CRASH": "Agotamiento",
        },
        "flags": {
            "COGNITIVE_OK": "El procesamiento cognitivo es claro y estable.",
            "COGNITIVE_NERVOUS": "Tensión elevada en el sistema nervioso.",
            "COGNITIVE_ANXIOUS": "Ansiedad elevada; mantenga las interacciones predecibles.",
            "COGNITIVE_TUNNEL_VISION": "Visión de túnel activa; no puede procesar múltiples estímulos a la vez.",
            "COGNITIVE_FOGGY": "Niebla mental severa; pensar y tomar decisiones es muy lento.",
            "COGNITIVE_LOST_TIMESPACE": "Desorientado en tiempo o espacio; necesita calma y orientación.",
            "MEMORY_OK": "La memoria a corto plazo funciona con normalidad.",
            "MEMORY_CRASHING": "Sobrecarga de memoria a corto plazo; escriba los datos importantes.",
            "FOCUS_OK": "La concentración y la atención son estables.",
            "FOCUS_LESS": "Atención reducida; use frases cortas.",
            "FOCUS_INITIATION_DIFFICULT": "Dificultad para iniciar tareas; ayude paso a paso con calma.",
            "FOCUS_EXECUTIVE_DISASTER": "Función ejecutiva bloqueada; no puede planificar ni organizar ahora.",
            "FOCUS_COGNITIVE_INERTIA": "Inercia cognitiva; cambiar de actividad es muy difícil.",
            "BARRIER_HUMOR_NO_SARCASM": "Toma las palabras literalmente; evite el sarcasmo o las bromas.",
            "BARRIER_NO_HIDDEN_MESSAGES": "Sea directo y explícito; no use indirectas ni dobles sentidos.",
            "BARRIER_NO_SOCIAL_CUES": "No puede interpretar expresiones faciales ni lenguaje corporal.",
            "BARRIER_NO_TOUCHING": "El contacto físico provoca angustia o pánico.",
            "BARRIER_NO_AGGRO_OR_CAPTIVE": "Voces altas, confrontación o bloquear salidas activan respuesta de huida.",
            "RESPONSE_DELAYED": "Respuesta verbal lenta; espere de 5 a 10 segundos para que responda.",
            "RESPONSE_INTERMITTENT": "El habla es intermitente; puede asentir, señalar o escribir.",
            "RESPONSE_UNRESPONSIVE": "Mutismo situacional temporal; sigue escuchando y comprendiendo todo.",
            "EXPRESSION_CONCISE": "Se comunica solo con frases cortas y directas.",
            "EXPRESSION_REDUCED": "Habla muy reducida; haga preguntas de sí o no.",
            "EXPRESSION_FAIL_MUTISM": "No puede hablar ahora mismo; use texto escrito o esta tarjeta.",
            "EXPRESSION_FAIL_UNDERSTAND": "Dificultad para procesar el habla; muestre texto escrito.",
            "STIMMING_TOOLS_FEEDBACK": "Usa herramientas sensoriales para autorregularse; es seguro.",
            "STIMMING_TOOLS_PRESSURE": "Necesita presión profunda o herramienta sensorial para estabilizarse.",
            "COPING_OK": "Se adapta bien al entorno actual.",
            "COPING_ANNOYED": "Irritación sensorial creciente; reduzca el ruido de fondo.",
            "COPING_DIFFICULT": "Dificultad para filtrar estímulos sensoriales.",
            "COPING_TERRIBLE": "Límite de sobrecarga alcanzado; necesita salir inmediatamente.",
            "COPING_FIGHT_OR_FLIGHT": "Respuesta aguda de lucha o huida activa.",
            "COPING_NEAR_MELTDOWN": "Al borde de una crisis neurológica (meltdown).",
            "SENSORY_EASY_AGGRAVATION": "Alta sensibilidad a sonidos repentinos o interrupciones.",
            "SENSORY_HYPERACUSIS": "Sensibilidad al sonido (hiperacusia); baje la voz y reduzca el ruido.",
            "SENSORY_PHOTO_AVERSION": "Sensibilidad a la luz; atenúe luces brillantes o pantallas.",
            "SENSORY_SPATIAL_DISTRESS": "Las multitudes y espacios cerrados causan angustia aguda.",
            "SENSORY_REDIRECTION": "Necesita un entorno tranquilo y sin estímulos de inmediato.",
            "TRIGGER_COPING_EXHAUSTION": "Agotamiento severo tras sobrecarga sensorial.",
            "TRIGGER_COPING_TIRED": "Fatiga profunda; necesita descanso sin exigencias.",
            "STAY_CALM_AND_RELAXED": "Hable con un tono tranquilo, pausado y neutral.",
            "DO_TALK_CLEARLY_ONLY": "Use instrucciones claras, literales y de un solo paso.",
            "DO_TALK_SLOWLY": "Hable despacio y haga pausas entre frases.",
            "DO_TALK_LOW_VOLUME": "Mantenga la voz baja y suave.",
            "DO_TALK_REQUIRED_NEEDS": "Haga solo preguntas esenciales de seguridad o necesidades básicas.",
            "DO_NOT_TOUCH": "NO TOCAR sin permiso explícito.",
            "DO_NOT_PRESSURE": "No apure, presione ni exija respuestas inmediatas.",
            "DO_NOT_AGITATE": "No levante la voz, no discuta ni invada el espacio personal.",
            "DO_NOT_TRIGGER": "Aleje luces brillantes, alarmas o ruido fuerte cercano.",
            "HELP_FIND_CALM_SPOT": "Ayude a ir a una zona de espera tranquila y con poca luz.",
            "HELP_FIND_EXIT_ASAP": "Ayude a encontrar la salida tranquila más cercana de inmediato.",
            "HELP_FIND_SAFE_SPOT": "Facilite un espacio seguro, cerrado y tranquilo para recuperarse.",
            "HELP_FIND_RESTING_SPOT": "Ofrezca un lugar tranquilo para sentarse o recostarse sin molestias.",
            "HELP_FIND_MY_HOME": "Ayude a organizar transporte seguro a casa o contacte a su apoyo.",
            "HELP_TO_COMMUNICATE": "Ofrezca papel, texto en el móvil o tarjetas de sí/no.",
            "WARN_RESPONSE_VOLATILITY": "AVISO: Las reacciones de estrés son respuestas neurológicas involuntarias, no agresión.",
            "WARN_MALADAPTIVE_DECISIONS": "AVISO: No puede firmar documentos legales ni tomar decisiones complejas ahora.",
        },
    },
}


def get_available_languages() -> list:
    langs = {code: data["lang_name"] for code, data in BUILTIN_TRANSLATIONS.items()}
    for folder in USER_LANG_DIRS:
        if folder.is_dir():
            for file in folder.glob("automautist-lang-*.json"):
                code = file.stem.replace("automautist-lang-", "").lower()
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        custom = json.load(f)
                    langs[code] = custom.get("lang_name", code.upper())
                except Exception:
                    pass
    return [{"code": k, "name": v} for k, v in langs.items()]


def get_language_pack(lang_code: str) -> dict:
    code = (lang_code or "en").lower().strip()
    base = {
        "lang_name": BUILTIN_TRANSLATIONS["en"]["lang_name"],
        "ui": dict(BUILTIN_TRANSLATIONS["en"]["ui"]),
        "moods": dict(BUILTIN_TRANSLATIONS["en"]["moods"]),
        "flags": dict(BUILTIN_TRANSLATIONS["en"]["flags"]),
    }

    if code in BUILTIN_TRANSLATIONS and code != "en":
        selected = BUILTIN_TRANSLATIONS[code]
        base["lang_name"] = selected.get("lang_name", code.upper())
        base["ui"].update(selected.get("ui", {}))
        base["moods"].update(selected.get("moods", {}))
        base["flags"].update(selected.get("flags", {}))

    for folder in USER_LANG_DIRS:
        custom_file = folder / f"automautist-lang-{code}.json"
        if custom_file.is_file():
            try:
                with open(custom_file, "r", encoding="utf-8") as f:
                    custom = json.load(f)
                if "lang_name" in custom:
                    base["lang_name"] = custom["lang_name"]
                base["ui"].update(custom.get("ui", {}))
                base["moods"].update(custom.get("moods", {}))
                base["flags"].update(custom.get("flags", {}))
                break
            except Exception as err:
                print(f"[AutoMAutist:LANG] Failed loading {custom_file}: {err}")

    return base
