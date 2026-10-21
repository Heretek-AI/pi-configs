#!/usr/bin/env bash
# Launch script for Distributed Cache & Event Streaming Engineer (cache-streaming-eng)
set -e

echo "=== Initializing Specialist: Distributed Cache & Event Streaming Engineer [cache-streaming-eng] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="cache-streaming-eng"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
