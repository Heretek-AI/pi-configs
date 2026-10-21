#!/usr/bin/env bash
# Launch script for Threat Modeling & Zero-Trust Architecture Engineer (threat-modeler)
set -e

echo "=== Initializing Specialist: Threat Modeling & Zero-Trust Architecture Engineer [threat-modeler] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="threat-modeler"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
