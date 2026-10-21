#!/usr/bin/env bash
# Launch script for Multi-Target Shader Transpilation & GPU Optimizer (shader-transpiler-optimizer)
set -e

echo "=== Initializing Specialist: Multi-Target Shader Transpilation & GPU Optimizer [shader-transpiler-optimizer] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="shader-transpiler-optimizer"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
