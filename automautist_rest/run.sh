#!/usr/bin/env bash
set -e

BOOT_DATE=$(date '+%Y-%m-%d %H:%M:%S %Z')
ADDON_VERSION="standalone"
ADDON_SLUG="standalone"
RUNTIME_MODE="STANDALONE"
INGRESS_PORT="19761"
HOST_PORT="${PORT:-19761}"

if [ -f "/data/options.json" ] || [ -n "${SUPERVISOR_TOKEN:-}" ]; then
    DB_DIR="/share/automautist_db"
    SECRET_STORE="/share/automautist_db/.secrets.env"
    OPTIONS_FILE="/data/options.json"

    if [ -n "${SUPERVISOR_TOKEN:-}" ] && command -v curl >/dev/null 2>&1 && command -v jq >/dev/null 2>&1; then
        SELF_INFO=$(curl -s -H "Authorization: Bearer ${SUPERVISOR_TOKEN}" http://supervisor/addons/self/info 2>/dev/null || true)
        if [ -n "$SELF_INFO" ]; then
            ADDON_VERSION=$(echo "$SELF_INFO" | jq -r '.data.version // "unknown"')
            ADDON_SLUG=$(echo "$SELF_INFO" | jq -r '.data.slug // "unknown"')
            INGRESS_PORT=$(echo "$SELF_INFO" | jq -r '.data.ingress_port // 19761')
            MAPPED_PORT=$(echo "$SELF_INFO" | jq -r '.data.network["19761/tcp"] // empty')
            [ -n "$MAPPED_PORT" ] && HOST_PORT="$MAPPED_PORT"
        fi
    fi

    if [[ "$ADDON_SLUG" == local_* ]]; then
        RUNTIME_MODE="HA-DEV"
    else
        RUNTIME_MODE="HA-PROD"
    fi
else
    DB_DIR="/app/storage"
    SECRET_STORE="/app/storage/.secrets.env"
    OPTIONS_FILE=""
    RUNTIME_MODE="STANDALONE"
fi

export AUTOMAUTIST_RUNTIME_MODE="$RUNTIME_MODE"
export AUTOMAUTIST_VERSION="$ADDON_VERSION"
export AUTOMAUTIST_ADDON_SLUG="$ADDON_SLUG"
echo "[AutoMAutist ${RUNTIME_MODE}] ${ADDON_SLUG} v${ADDON_VERSION} (${DB_DIR} active)"
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

VERSION_STAMP="${DB_DIR}/.last_migrated_version"
LAST_VER=$(cat "$VERSION_STAMP" 2>/dev/null || echo "")

if [ "$RUNTIME_MODE" = "HA-DEV" ] || [ "$ADDON_VERSION" != "$LAST_VER" ]; then
    echo "[AutoMAutist:DB] Make Migrations Database v${LAST_VER:-none} -> v${ADDON_VERSION} - ${RUNTIME_MODE}.."
    python3 /app/manage.py makemigrations core domotica assist mood --noinput
    echo "$ADDON_VERSION" > "$VERSION_STAMP"
fi

echo "[AutoMAutist:DB] Migrating Django Database"
python3 /app/manage.py migrate --noinput

echo "[AutoMAutist:TIME] ${BOOT_DATE}"
echo "============================================================================"
echo " AutoMAutist REST v${ADDON_VERSION} | Copyright (c) 2009-2026 Gunther Voet"
echo " License: PolyForm Noncommercial 1.0.0 (Non-Commercial Use Only)"
echo " Source:  https://github.com/gowildchild/AutoMAutist"
echo "============================================================================"
echo "[AutoMAutist:RUN] Running Web Application on Port ${INGRESS_PORT} | Host Port ${HOST_PORT}"
exec gunicorn core.wsgi:application --chdir /app --bind "0.0.0.0:${INGRESS_PORT}" --workers 2 --threads 2 --timeout 60 --preload
