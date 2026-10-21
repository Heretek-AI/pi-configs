#!/usr/bin/env bash
# Launch script for Technical Artist & Asset Pipeline Lead (tech-artist-pipeline)
set -e

echo "=== Initializing Specialist: Technical Artist & Asset Pipeline Lead [tech-artist-pipeline] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="tech-artist-pipeline"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
