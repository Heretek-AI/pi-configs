#!/usr/bin/env bash
# Launch script for Enterprise System Architect & ADR Owner (system-architect)
set -e

echo "=== Initializing Specialist: Enterprise System Architect & ADR Owner [system-architect] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="system-architect"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
