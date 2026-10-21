#!/usr/bin/env bash
# Launch script for Godot 4 / Redot Engine Architecture Specialist (godot-redot-architect)
set -e

echo "=== Initializing Specialist: Godot 4 / Redot Engine Architecture Specialist [godot-redot-architect] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="godot-redot-architect"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
