#!/usr/bin/env bash
# Launch script for Memory Integrity & Runtime Hooking Researcher (memory-integrity-cheat-researcher)
set -e

echo "=== Initializing Specialist: Memory Integrity & Runtime Hooking Researcher [memory-integrity-cheat-researcher] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="memory-integrity-cheat-researcher"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
