#!/usr/bin/env bash
# Launch script for Binary Disassembly & Headless Decompilation Specialist (binary-reverse-engineer)
set -e

echo "=== Initializing Specialist: Binary Disassembly & Headless Decompilation Specialist [binary-reverse-engineer] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="binary-reverse-engineer"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
