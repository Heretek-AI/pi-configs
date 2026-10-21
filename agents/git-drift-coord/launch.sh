#!/usr/bin/env bash
# Launch script for Git Worktree, Merge & Branch Drift Coordinator (git-drift-coord)
set -e

echo "=== Initializing Specialist: Git Worktree, Merge & Branch Drift Coordinator [git-drift-coord] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="git-drift-coord"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
