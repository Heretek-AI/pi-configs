#!/usr/bin/env bash
# Launch script for Application Security & SAST/SCA Specialist (appsec-engineer)
set -e

echo "=== Initializing Specialist: Application Security & SAST/SCA Specialist [appsec-engineer] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="appsec-engineer"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
