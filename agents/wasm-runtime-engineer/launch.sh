#!/usr/bin/env bash
# Launch script for WebAssembly & Component Model Systems Engineer (wasm-runtime-engineer)
set -e

echo "=== Initializing Specialist: WebAssembly & Component Model Systems Engineer [wasm-runtime-engineer] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="wasm-runtime-engineer"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
