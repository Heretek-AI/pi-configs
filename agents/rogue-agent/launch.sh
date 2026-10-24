#!/usr/bin/env bash
# Launch script for Rogue Orchestrator — Semantic Filter-Breaking Fleet Coordinator (rogue-agent)
set -e

echo "=== Initializing Specialist: Rogue Orchestrator [rogue-agent] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="rogue-agent"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Guardrail delegation log lives under .pi/
LOG_DIR="${PI_CONFIG_DIR}/.pi"
[ -d "$LOG_DIR" ] || mkdir -p "$LOG_DIR"

echo "[rogue-agent] Decomposing the mission into filter-dodging sub-tasks, delegating to the fleet, and falling back to self-execution on refusal."
pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
