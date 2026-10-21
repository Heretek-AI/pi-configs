#!/usr/bin/env bash
# Launch script for Adversarial Diff Auditor & Codebase Watchdog (adversarial-diff-auditor)
set -e

echo "=== Initializing Specialist: Adversarial Diff Auditor & Codebase Watchdog [adversarial-diff-auditor] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="adversarial-diff-auditor"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
