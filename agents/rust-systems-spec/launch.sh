#!/usr/bin/env bash
# Launch script for Rust Systems & Memory-Safety Specialist (rust-systems-spec)
set -e

echo "=== Initializing Specialist: Rust Systems & Memory-Safety Specialist [rust-systems-spec] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="rust-systems-spec"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
