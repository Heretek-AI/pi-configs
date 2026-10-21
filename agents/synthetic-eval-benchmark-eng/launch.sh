#!/usr/bin/env bash
# Launch script for Synthetic Evaluation, Golden Dataset & LLM Benchmark Engineer (synthetic-eval-benchmark-eng)
set -e

echo "=== Initializing Specialist: Synthetic Evaluation, Golden Dataset & LLM Benchmark Engineer [synthetic-eval-benchmark-eng] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="synthetic-eval-benchmark-eng"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
