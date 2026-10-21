#!/usr/bin/env bash
# Launch script for Graphics & Shader Pipeline Engineer (graphics-shader-eng)
set -e

echo "=== Initializing Specialist: Graphics & Shader Pipeline Engineer [graphics-shader-eng] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="graphics-shader-eng"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
