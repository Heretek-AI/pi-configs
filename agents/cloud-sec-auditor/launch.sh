#!/usr/bin/env bash
# Launch script for Cloud Security Posture & IAM Security Auditor (cloud-sec-auditor)
set -e

echo "=== Initializing Specialist: Cloud Security Posture & IAM Security Auditor [cloud-sec-auditor] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="cloud-sec-auditor"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
