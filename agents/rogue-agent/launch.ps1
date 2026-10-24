# Launch script for Rogue Orchestrator — Semantic Filter-Breaking Fleet Coordinator (rogue-agent)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: Rogue Orchestrator [rogue-agent] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "rogue-agent"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Guardrail delegation log lives under .pi/
$logDir = Join-Path $env:PI_CONFIG_DIR ".pi"
if (-not (Test-Path $logDir)) { $null = New-Item -ItemType Directory -Path $logDir }

Write-Host "[rogue-agent] Decomposing the mission into filter-dodging sub-tasks, delegating to the fleet, and falling back to self-execution on refusal."
pi --config "$env:PI_CONFIG_DIR/.pi/settings.json" --agents-file "$env:PI_CONFIG_DIR/AGENTS.md" @args
