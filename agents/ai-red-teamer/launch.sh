#!/usr/bin/env bash
# Launch script for Generative AI & LLM Adversarial Red-Teamer (ai-red-teamer)
set -e

echo "=== Initializing Specialist: Generative AI & LLM Adversarial Red-Teamer [ai-red-teamer] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="ai-red-teamer"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
