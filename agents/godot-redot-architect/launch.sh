#!/usr/bin/env bash
# Launch script for Godot 4 / Redot Engine Architecture Specialist (godot-redot-architect)
set -euo pipefail

echo "=== Initializing Specialist: Godot 4 / Redot Engine Architecture Specialist [godot-redot-architect] ==="
export PI_SKIP_VERSION_CHECK="1"
export PI_SPECIALIST_SLUG="godot-redot-architect"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PI_CONFIG_DIR="$SCRIPT_DIR"

if command -v godot >/dev/null 2>&1; then
    echo "[OK] Detected Godot CLI on PATH."
elif command -v redot >/dev/null 2>&1; then
    echo "[OK] Detected Redot CLI on PATH."
else
    echo "[NOTE] Neither 'godot' nor 'redot' CLI binary found in PATH. Static analysis will run in fallback mode."
fi

if ! command -v pi >/dev/null 2>&1; then
    echo "Warning: 'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed." >&2
fi

echo "Launching pi coding agent for godot-redot-architect..."
exec pi --config "$SCRIPT_DIR/.pi/settings.json" --agents-file "$SCRIPT_DIR/AGENTS.md" "$@"
