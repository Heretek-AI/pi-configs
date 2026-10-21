#!/usr/bin/env bash
# Launch script for TypeScript / Node.js Fullstack Systems Engineer (ts-node-fullstack)
set -e

echo "=== Initializing Specialist: TypeScript / Node.js Fullstack Systems Engineer [ts-node-fullstack] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="ts-node-fullstack"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
