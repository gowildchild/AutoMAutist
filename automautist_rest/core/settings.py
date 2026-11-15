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

import os
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================================================
# 1. PRIVATE EXTERNAL JSON CONFIG LOADER (/config/automautist-rest-django.conf)
# =========================================================================
CONF_PATHS = [
    Path('/homeassistant/automautist-rest-django.conf'),
    Path('/config/automautist-rest-django.conf'),
    Path('/app/storage/automautist-rest-django.conf'),
]
CUSTOM_CONF = {}
for conf_path in CONF_PATHS:
    if conf_path.is_file():
        try:
            with open(conf_path, 'r', encoding='utf-8') as f:
                CUSTOM_CONF = json.load(f)
            print(f"[AutoMAutist:CONF] Loaded private config from {conf_path}")
            break
        except Exception as conf_err:
            print(f"[AutoMAutist:CONF] Warning: Could not parse {conf_path}: {conf_err}")

def _get_json_list(env_name, conf_key):
    items = []
    raw_env = os.environ.get(env_name, '[]')
    try:
        parsed = json.loads(raw_env)
        if isinstance(parsed, list):
            items.extend(parsed)
    except (json.JSONDecodeError, TypeError):
        pass
    conf_val = CUSTOM_CONF.get(conf_key)
    if isinstance(conf_val, list):
        items.extend(conf_val)
    return items

# Core Security Keys (Private JSON file takes priority over .secrets.env / env vars)
SECRET_KEY = (
    CUSTOM_CONF.get('secret_key')
    or os.environ.get('SUPERVISOR_SECRET_KEY')
    or os.environ.get('DJANGO_SECRET_KEY')
    or 'django-insecure-fallback-automatic-key-AutoMAutist-2026'
)
ENCRYPTION_SALT = (
    CUSTOM_CONF.get('encryption_salt')
    or os.environ.get('SUPERVISOR_ENCRYPTION_SALT')
    or 'django-insecure-fallback-salt-key-AutoMAutist-2026'
)
DEBUG = bool(CUSTOM_CONF.get('debug', os.environ.get('SUPERVISOR_DEBUG', 'False') == 'True'))

RUNTIME_MODE = os.environ.get('AUTOMAUTIST_RUNTIME_MODE', 'STANDALONE')
APP_VERSION = os.environ.get('AUTOMAUTIST_VERSION', '0.1.12-dashboard')

# Allow Django to accept requests forwarded via Home Assistant Ingress & direct LAN IP
ALLOWED_HOSTS = CUSTOM_CONF.get('allowed_hosts', ['*'])

# Explicitly trust the internal proxy headers forwarded by the Supervisor
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

# Ensure Django doesn't block cross-origin iframe embedding used by the HASS UI frame
X_FRAME_OPTIONS = 'ALLOWALL'

# Allow session/CSRF cookies to work on BOTH direct HTTP (ip:19761) and HA Ingress
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = False

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8123',
    'http://homeassistant.local:8123',
    'https://*.nabu.casa',
]
for origin in _get_json_list('HA_TRUSTED_ORIGINS_JSON', 'csrf_trusted_origins'):
    if isinstance(origin, str) and origin.strip():
        CSRF_TRUSTED_ORIGINS.append(origin.strip())
CSRF_TRUSTED_ORIGINS = list(dict.fromkeys(CSRF_TRUSTED_ORIGINS))

TRUSTED_NETWORKS = list(dict.fromkeys(
    net.strip() for net in _get_json_list('TRUSTED_NETWORKS_JSON', 'trusted_networks')
    if isinstance(net, str) and net.strip()
))
DEFAULT_SCENES = _get_json_list('DEFAULT_SCENES_JSON', 'default_scenes')

# Core Framework Application Definitions
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'core.mood.apps.MoodConfig',
    'core.assist.apps.AssistConfig',
    'core.domotica.apps.DomoticaConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'core.views.HomeAssistantIngressMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

DATABASE_ENV_PATH = os.environ.get("DATABASE_PATH")
if DATABASE_ENV_PATH:
    if os.path.isdir(DATABASE_ENV_PATH) or DATABASE_ENV_PATH.endswith('/'):
        DATABASE_FILE_PATH = os.path.join(DATABASE_ENV_PATH, "db.sqlite3")
    else:
        DATABASE_FILE_PATH = DATABASE_ENV_PATH
else:
    DATABASE_FILE_PATH = os.path.join(BASE_DIR, "db.sqlite3")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_FILE_PATH,
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'core', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'core.views.ingress_context',
            ],
        },
    },
]

# Static Assets Management (CSS / JavaScript Framework Delivery)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
WHITENOISE_STATIC_PREFIX = '/static/'


storage_backend = CUSTOM_CONF.get(
    'staticfiles_storage_backend',
    os.environ.get('STATICFILES_STORAGE_BACKEND', 'whitenoise.storage.StaticFilesStorage')
)
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": storage_backend,
    },
}
STATICFILES_STORAGE = storage_backend

OIDC_ENABLED = bool(CUSTOM_CONF.get('oidc_enabled', os.environ.get('OIDC_ENABLED', 'false').lower() == 'true'))
if OIDC_ENABLED:
    OIDC_OP_ISSUER = CUSTOM_CONF.get('oidc_op_issuer', os.environ.get('OIDC_OP_ISSUER', ''))
    OIDC_RP_CLIENT_ID = CUSTOM_CONF.get('oidc_client_id', os.environ.get('OIDC_CLIENT_ID', ''))
    OIDC_RP_CLIENT_SECRET = CUSTOM_CONF.get('oidc_client_secret', os.environ.get('OIDC_CLIENT_SECRET', ''))
    OIDC_REDIRECT_URL = CUSTOM_CONF.get('oidc_redirect_url', os.environ.get('OIDC_REDIRECT_URL', ''))

    AUTHENTICATION_BACKENDS = (
        'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
else:
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
