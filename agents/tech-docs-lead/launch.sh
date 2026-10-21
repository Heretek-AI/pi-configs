#!/usr/bin/env bash
# Launch script for Technical Documentation Lead & Docs-as-Code Architect (tech-docs-lead)
set -e

echo "=== Initializing Specialist: Technical Documentation Lead & Docs-as-Code Architect [tech-docs-lead] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="tech-docs-lead"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
