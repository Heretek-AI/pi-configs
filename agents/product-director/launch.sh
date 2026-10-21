#!/usr/bin/env bash
# Launch script for Product Director & Strategic PRD Author (product-director)
set -e

echo "=== Initializing Specialist: Product Director & Strategic PRD Author [product-director] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="product-director"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
