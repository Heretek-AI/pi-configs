#!/usr/bin/env bash
# Launch script for Automated SemVer Lockfile Patcher & Vulnerability Remediation (dependency-patcher)
set -e

echo "=== Initializing Specialist: Automated SemVer Lockfile Patcher & Vulnerability Remediation [dependency-patcher] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="dependency-patcher"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
