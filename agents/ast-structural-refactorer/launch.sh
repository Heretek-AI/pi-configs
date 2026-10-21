#!/usr/bin/env bash
# Launch script for Tree-sitter Structural Search & AST Refactoring Specialist (ast-structural-refactorer)
set -e

echo "=== Initializing Specialist: Tree-sitter Structural Search & AST Refactoring Specialist [ast-structural-refactorer] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="ast-structural-refactorer"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
