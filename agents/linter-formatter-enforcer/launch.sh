#!/usr/bin/env bash
# Launch script for Autonomous Linter & Code Formatting Enforcer (linter-formatter-enforcer)
set -e

echo "=== Initializing Specialist: Autonomous Linter & Code Formatting Enforcer [linter-formatter-enforcer] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="linter-formatter-enforcer"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
