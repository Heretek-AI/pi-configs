#!/usr/bin/env bash
# Launch script for Universal PC Game Modding & Injection Specialist (universal-game-modder)
set -e

echo "=== Initializing Specialist: Universal PC Game Modding & Injection Specialist [universal-game-modder] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="universal-game-modder"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
