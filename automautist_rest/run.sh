#!/usr/bin/env bash
set -e

# 1. Standalone vs Home Assistant OS Path Detection
if [ -d "/share" ]; then
    DB_DIR="/share/automautist_db"
    SECRET_STORE="/share/automautist_db/.secrets.env"
    OPTIONS_FILE="/data/options.json"
    echo "[AutoMAutist:ENV] Mode: Home Assistant Add-on detected (/share active)."
else
    DB_DIR="/app/storage"
    SECRET_STORE="/app/storage/.secrets.env"
    OPTIONS_FILE=""
    echo "[AutoMAutist:ENV] Mode: Standalone Server detected (/app/storage active)."
fi

echo "[AutoMAutist:INIT] System Database Engine..."
mkdir -p "$DB_DIR"
export DATABASE_PATH="${DB_DIR}/db.sqlite3"

echo "[AutoMAutist:SUPERVISOR] Reading JSON Options..."
HA_ORIGINS_JSON="[]"
EXPORT_TRUSTED_NETWORKS="[]"
EXPORT_DEFAULT_SCENES="[]"
EXPORT_STATIC_STORAGE="whitenoise.storage.StaticFilesStorage"
EXPORT_OIDC_ENABLED="false"
EXPORT_OIDC_ISSUER=""
EXPORT_OIDC_CLIENT_ID=""
EXPORT_OIDC_CLIENT_SECRET=""
EXPORT_OIDC_REDIRECT_URL=""
EXPORT_DEBUG="False"

if [ -n "$OPTIONS_FILE" ] && [ -f "$OPTIONS_FILE" ] && command -v jq >/dev/null 2>&1; then
    HA_ORIGINS_JSON=$(jq -c '.csrf_trusted_origins // []' "$OPTIONS_FILE" 2>/dev/null || echo "[]")
    EXPORT_TRUSTED_NETWORKS=$(jq -c '.trusted_networks // []' "$OPTIONS_FILE" 2>/dev/null || echo "[]")
    EXPORT_DEFAULT_SCENES=$(jq -c '.default_scenes // []' "$OPTIONS_FILE" 2>/dev/null || echo "[]")
    EXPORT_STATIC_STORAGE=$(jq -r '.staticfiles_storage_backend // "whitenoise.storage.StaticFilesStorage"' "$OPTIONS_FILE" 2>/dev/null || echo "whitenoise.storage.StaticFilesStorage")
    EXPORT_OIDC_ENABLED=$(jq -r '.oidc_enabled // false' "$OPTIONS_FILE" 2>/dev/null || echo "false")
    EXPORT_OIDC_ISSUER=$(jq -r '.oidc_op_issuer // ""' "$OPTIONS_FILE" 2>/dev/null || echo "")
    EXPORT_OIDC_CLIENT_ID=$(jq -r '.oidc_client_id // ""' "$OPTIONS_FILE" 2>/dev/null || echo "")
    EXPORT_OIDC_CLIENT_SECRET=$(jq -r '.oidc_client_secret // ""' "$OPTIONS_FILE" 2>/dev/null || echo "")
    EXPORT_OIDC_REDIRECT_URL=$(jq -r '.oidc_redirect_url // ""' "$OPTIONS_FILE" 2>/dev/null || echo "")
    RAW_DEBUG=$(jq -r '.debug // false' "$OPTIONS_FILE" 2>/dev/null || echo "false")
    if [ "$RAW_DEBUG" = "true" ]; then
        EXPORT_DEBUG="True"
    fi
fi

# Load persisted fallback secrets if generated on a previous boot
if [ -f "$SECRET_STORE" ]; then
    # shellcheck disable=SC1090
    source "$SECRET_STORE"
fi

# Security Nudging: Auto-generate fallback secrets if missing (used when /config/automautist-rest-django.conf has none)
EXPORT_SECRET="${AUTO_SECRET_KEY:-${DJANGO_SECRET_KEY:-}}"
EXPORT_SALT="${AUTO_ENCRYPTION_SALT:-${SUPERVISOR_ENCRYPTION_SALT:-}}"
NEED_SAVE=0

if [ -z "$EXPORT_SECRET" ]; then
    echo "[AutoMAutist:SECURITY] Auto-generating fallback Django SECRET_KEY..."
    EXPORT_SECRET=$(python3 -c "import secrets, string; print(''.join(secrets.choice(string.ascii_letters + string.digits + '!@#$%^&*(-_=+)') for _ in range(50)))")
    NEED_SAVE=1
fi

if [ -z "$EXPORT_SALT" ]; then
    echo "[AutoMAutist:SECURITY] Auto-generating fallback cryptographic signing SALT..."
    EXPORT_SALT=$(python3 -c "import secrets, string; print(''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32)))")
    NEED_SAVE=1
fi

if [ "$NEED_SAVE" -eq 1 ]; then
    cat <<EOF > "$SECRET_STORE"
AUTO_SECRET_KEY="$EXPORT_SECRET"
AUTO_ENCRYPTION_SALT="$EXPORT_SALT"
EOF
    chmod 600 "$SECRET_STORE"
    echo "[AutoMAutist:SECURITY] Persisted fallback credentials to $SECRET_STORE"
fi

# Export runtime environment variables for Django settings
export SUPERVISOR_DEBUG="$EXPORT_DEBUG"
export TRUSTED_NETWORKS_JSON="$EXPORT_TRUSTED_NETWORKS"
export DEFAULT_SCENES_JSON="$EXPORT_DEFAULT_SCENES"
export DJANGO_SECRET_KEY="$EXPORT_SECRET"
export SUPERVISOR_SECRET_KEY="$EXPORT_SECRET"
export SUPERVISOR_ENCRYPTION_SALT="$EXPORT_SALT"
export HA_TRUSTED_ORIGINS_JSON="$HA_ORIGINS_JSON"
export STATICFILES_STORAGE_BACKEND="$EXPORT_STATIC_STORAGE"
export OIDC_ENABLED="$EXPORT_OIDC_ENABLED"
export OIDC_OP_ISSUER="$EXPORT_OIDC_ISSUER"
export OIDC_CLIENT_ID="$EXPORT_OIDC_CLIENT_ID"
export OIDC_CLIENT_SECRET="$EXPORT_OIDC_CLIENT_SECRET"
export OIDC_REDIRECT_URL="$EXPORT_OIDC_REDIRECT_URL"

echo "[AutoMAutist:DB:SETUP] Database table sync migrations..."
python3 /app/manage.py migrate --noinput

echo "=================================================================="
echo " AutoMAutist REST Server | Copyright (c) 2009-2026 Gunther Voet"
echo " License: PolyForm Noncommercial 1.0.0 (Non-Commercial Use Only)"
echo " Source:  https://github.com/gowildchild/AutoMAutist"
echo "=================================================================="
echo "[AutoMAutist:RUN] Running Web Application on Port 19761..."
exec gunicorn core.wsgi:application --chdir /app --bind 0.0.0.0:19761 --workers 2 --threads 2 --timeout 60 --preload
