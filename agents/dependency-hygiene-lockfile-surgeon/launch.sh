#!/usr/bin/env bash
# Launch script for Lockfile Deduplication & Deep Dependency Surgeon (dependency-hygiene-lockfile-surgeon)
set -e

echo "=== Initializing Specialist: Lockfile Deduplication & Deep Dependency Surgeon [dependency-hygiene-lockfile-surgeon] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="dependency-hygiene-lockfile-surgeon"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
