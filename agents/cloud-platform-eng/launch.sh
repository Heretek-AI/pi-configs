#!/usr/bin/env bash
# Launch script for Cloud Platform & OpenTofu / Infrastructure-as-Code Engineer (cloud-platform-eng)
set -e

echo "=== Initializing Specialist: Cloud Platform & OpenTofu / Infrastructure-as-Code Engineer [cloud-platform-eng] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="cloud-platform-eng"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
