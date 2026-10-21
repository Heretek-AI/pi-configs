#!/usr/bin/env bash
# Launch script for Game Feel, VFX & Juiciness Critic (game-feel-and-vfx-critic)
set -e

echo "=== Initializing Specialist: Game Feel, VFX & Juiciness Critic [game-feel-and-vfx-critic] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="game-feel-and-vfx-critic"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
