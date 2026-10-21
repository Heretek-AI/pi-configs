#!/usr/bin/env bash
# Launch script for Brand Voice, Copywriting & Microcopy Specialist (brand-copy-spec)
set -e

echo "=== Initializing Specialist: Brand Voice, Copywriting & Microcopy Specialist [brand-copy-spec] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="brand-copy-spec"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
