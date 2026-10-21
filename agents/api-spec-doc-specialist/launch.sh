#!/usr/bin/env bash
# Launch script for OpenAPI, AsyncAPI & Protobuf API Documentation Specialist (api-spec-doc-specialist)
set -e

echo "=== Initializing Specialist: OpenAPI, AsyncAPI & Protobuf API Documentation Specialist [api-spec-doc-specialist] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="api-spec-doc-specialist"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
