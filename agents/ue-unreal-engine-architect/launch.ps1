# Launch script for Unreal Engine 5 C++ & Gameplay Architecture Specialist (ue-unreal-engine-architect)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: Unreal Engine 5 C++ & Gameplay Architecture Specialist [ue-unreal-engine-architect] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "ue-unreal-engine-architect"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for ue-unreal-engine-architect..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
