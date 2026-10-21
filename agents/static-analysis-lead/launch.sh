#!/usr/bin/env bash
# Launch script for Code Style, Semgrep Rules & Static Analysis Lead (static-analysis-lead)
set -e

echo "=== Initializing Specialist: Code Style, Semgrep Rules & Static Analysis Lead [static-analysis-lead] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="static-analysis-lead"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
