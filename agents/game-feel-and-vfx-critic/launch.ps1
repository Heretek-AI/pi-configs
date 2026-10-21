# Launch script for Game Feel, VFX & Juiciness Critic (game-feel-and-vfx-critic)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: Game Feel, VFX & Juiciness Critic [game-feel-and-vfx-critic] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "game-feel-and-vfx-critic"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for game-feel-and-vfx-critic..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
