#!/usr/bin/env bash
# Launch script for Creative Narrative Director & Worldbuilding Architect (creative-narrative-director)
set -e

echo "=== Initializing Specialist: Creative Narrative Director & Worldbuilding Architect [creative-narrative-director] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="creative-narrative-director"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
