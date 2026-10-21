#!/usr/bin/env bash
# Launch script for API Contract & OpenAPI / Pact Verification Specialist (api-contract-tester)
set -e

echo "=== Initializing Specialist: API Contract & OpenAPI / Pact Verification Specialist [api-contract-tester] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="api-contract-tester"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
