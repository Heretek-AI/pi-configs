#!/usr/bin/env bash
# Launch script for Natural Tone, Voice & Humanization Editor (humanizer-and-tone-editor)
set -e

echo "=== Initializing Specialist: Natural Tone, Voice & Humanization Editor [humanizer-and-tone-editor] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="humanizer-and-tone-editor"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
