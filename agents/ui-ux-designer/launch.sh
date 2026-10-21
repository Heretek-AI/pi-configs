#!/usr/bin/env bash
# Launch script for UI/UX Designer & Interactive Prototyper (ui-ux-designer)
set -e

echo "=== Initializing Specialist: UI/UX Designer & Interactive Prototyper [ui-ux-designer] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="ui-ux-designer"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
