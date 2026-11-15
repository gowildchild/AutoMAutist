#!/usr/bin/env bash
set -e

REPO_DIR="/share/automautist_repo"
SRC_DIR="${REPO_DIR}/automautist_rest"
DEV_DIR="/addons/local/automautist_rest"
DEV_SLUG="local_automautist_rest"

# Auto-detect the GitHub-installed add-on slug (e.g. a1b2c3d4_automautist_rest)
PROD_SLUG=$(ha apps list --raw-json 2>/dev/null | jq -r '.data.addons[] | select(.slug | endswith("_automautist_rest")) | .slug' | head -n 1 || true)

usage() {
    echo "Usage: $0 --dev <command> [arguments]"
    echo ""
    echo "Commands:"
    echo "  --dev copy              Sync repo to /addons/local/automautist_rest and reload store"
    echo "  --dev start             Stop production add-on, rebuild & start local DEV add-on"
    echo "  --dev stop              Stop local DEV add-on and restart production add-on"
    echo "  --dev commit \"msg\"      Stage, commit, and push changes in ${REPO_DIR} to GitHub"
    echo "  --dev audit             Creates an audit file of the current build"
    exit 1
}

if [ "$1" != "--dev" ] || [ -z "$2" ]; then
    usage
fi

ACTION="$2"

case "$ACTION" in
    audit)
        echo "[DEV] Auditing ${SRC_DIR}..."
        files-to-prompt "${REPO_DIR}" --ignore "*.db" --ignore "*.log" --ignore "__pycache__" --ignore "*.md" --ignore "LICENSE" -o "${REPO_DIR}/../automautist_rest_audit.txt"
        ;;


    copy)
        echo "[DEV] Copying ${SRC_DIR} -> ${DEV_DIR}..."
        rm -rf "$DEV_DIR"
        cp -r "$SRC_DIR" "$DEV_DIR"
        # Label local config.yaml so it is clearly marked (DEV) in the Home Assistant UI
        sed -i 's/^name: "AutoMAutist REST server"/name: "AutoMAutist REST server (DEV)"/' "${DEV_DIR}/config.yaml"
        echo "[DEV] Reloading Home Assistant Add-on Store..."
        ha store reload
        echo "[DEV] Copy complete."
        ;;

    start)
        if [ -n "$PROD_SLUG" ]; then
            echo "[DEV] Stopping production app (${PROD_SLUG}) to free port 19761..."
            ha apps stop "$PROD_SLUG" || true
        fi
        echo "[DEV] Updating/rebuilding and starting ${DEV_SLUG}..."
        # Try 'update' first (if config.yaml version changed), otherwise 'rebuild'
        ha apps update "$DEV_SLUG" 2>/dev/null || ha apps rebuild "$DEV_SLUG" || true
        ha apps start "$DEV_SLUG"
        echo "[DEV] Local DEV app is now running on port 19761."
        ;;

    stop)
        echo "[DEV] Stopping local DEV app (${DEV_SLUG})..."
        ha apps stop "$DEV_SLUG" || true
        if [ -n "$PROD_SLUG" ]; then
            echo "[DEV] Starting production app (${PROD_SLUG})..."
            ha apps start "$PROD_SLUG"
            echo "[DEV] Production app is back online."
        else
            echo "[DEV] Warning: Could not auto-detect GitHub production app slug. Start it manually in Settings -> Add-ons."
        fi
        ;;


    commit)
        COMMIT_MSG="$3"
        if [ -z "$COMMIT_MSG" ]; then
            echo "[ERROR] Please provide a commit message: $0 --dev commit \"Your message\""
            exit 1
        fi
        cd "$REPO_DIR"
        echo "[GIT] Checking status..."
        git status -s
        git add .
        git commit -m "$COMMIT_MSG"
        git push
        echo "[GIT] Pushed cleanly to GitHub."
        ;;

    *)
        usage
        ;;
esac
