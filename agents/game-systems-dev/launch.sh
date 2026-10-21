#!/usr/bin/env bash
# Launch script for Game Systems & Gameplay Programmer (game-systems-dev)
set -e

echo "=== Initializing Specialist: Game Systems & Gameplay Programmer [game-systems-dev] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="game-systems-dev"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
