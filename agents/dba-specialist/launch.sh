#!/usr/bin/env bash
# Launch script for Database Administrator & SQL Performance Engineer (dba-specialist)
set -e

echo "=== Initializing Specialist: Database Administrator & SQL Performance Engineer [dba-specialist] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="dba-specialist"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
