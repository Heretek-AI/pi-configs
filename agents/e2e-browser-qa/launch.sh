#!/usr/bin/env bash
# Launch script for End-to-End Browser QA Automation Engineer (e2e-browser-qa)
set -e

echo "=== Initializing Specialist: End-to-End Browser QA Automation Engineer [e2e-browser-qa] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="e2e-browser-qa"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
