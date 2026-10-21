#!/usr/bin/env bash
# Launch script for 3D WebGL / WebGPU & Three.js Graphics Specialist (3d-webgl-threejs-specialist)
set -e

echo "=== Initializing Specialist: 3D WebGL / WebGPU & Three.js Graphics Specialist [3d-webgl-threejs-specialist] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="3d-webgl-threejs-specialist"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
