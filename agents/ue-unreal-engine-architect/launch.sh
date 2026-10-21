#!/usr/bin/env bash
# Launch script for Unreal Engine 5 C++ & Gameplay Architecture Specialist (ue-unreal-engine-architect)
set -e

echo "=== Initializing Specialist: Unreal Engine 5 C++ & Gameplay Architecture Specialist [ue-unreal-engine-architect] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="ue-unreal-engine-architect"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
