#!/usr/bin/env bash
# Launch script for SBOM, Software License & Regulatory Compliance Auditor (compliance-auditor)
set -e

echo "=== Initializing Specialist: SBOM, Software License & Regulatory Compliance Auditor [compliance-auditor] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="compliance-auditor"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
