#!/usr/bin/env bash
# Launch script for Kubernetes Platform & Helm Orchestrator (k8s-orchestrator)
set -e

echo "=== Initializing Specialist: Kubernetes Platform & Helm Orchestrator [k8s-orchestrator] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="k8s-orchestrator"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
