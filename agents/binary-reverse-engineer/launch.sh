#!/usr/bin/env bash
# Launch script for Binary Disassembly & Headless Decompilation Specialist (binary-reverse-engineer)
set -euo pipefail

echo "=== Initializing Specialist: Binary Disassembly & Headless Decompilation Specialist [binary-reverse-engineer] ==="
export PI_SKIP_VERSION_CHECK="1"
export PI_SPECIALIST_SLUG="binary-reverse-engineer"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PI_CONFIG_DIR="$SCRIPT_DIR"

# Check for Disassembly & Reverse Engineering Tooling
for tool in r2 rabin2 objdump ghidra frida; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "[OK] Detected '$tool' in PATH."
    else
        echo "[INFO] '$tool' not detected in PATH. Specialist will use Node/TypeScript fallback inspection."
    fi
done

if ! command -v pi >/dev/null 2>&1; then
    echo "Warning: 'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed." >&2
fi

echo "Launching pi coding agent for binary-reverse-engineer..."
exec pi --config "$SCRIPT_DIR/.pi/settings.json" --agents-file "$SCRIPT_DIR/AGENTS.md" "$@"
