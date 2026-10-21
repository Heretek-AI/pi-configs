#!/usr/bin/env bash
# Launch script for Performance Load & k6 Stress Testing Engineer (load-stress-tester)
set -e

echo "=== Initializing Specialist: Performance Load & k6 Stress Testing Engineer [load-stress-tester] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="load-stress-tester"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
