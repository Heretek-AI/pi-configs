#!/usr/bin/env bash
# Launch script for Semantic LSP & Code Knowledge Graph Navigator (lsp-type-graph-navigator)
set -e

echo "=== Initializing Specialist: Semantic LSP & Code Knowledge Graph Navigator [lsp-type-graph-navigator] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="lsp-type-graph-navigator"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
