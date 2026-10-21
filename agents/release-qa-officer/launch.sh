#!/usr/bin/env bash
# Launch script for Release Verification & Acceptance Gatekeeper (release-qa-officer)
set -e

echo "=== Initializing Specialist: Release Verification & Acceptance Gatekeeper [release-qa-officer] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="release-qa-officer"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
