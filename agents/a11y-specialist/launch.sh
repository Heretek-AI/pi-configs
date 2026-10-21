#!/usr/bin/env bash
# Launch script for Accessibility & WCAG 2.2 AA Compliance Auditor (a11y-specialist)
set -e

echo "=== Initializing Specialist: Accessibility & WCAG 2.2 AA Compliance Auditor [a11y-specialist] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="a11y-specialist"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
