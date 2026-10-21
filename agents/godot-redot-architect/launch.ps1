# Launch script for Godot 4 / Redot Engine Architecture Specialist (godot-redot-architect)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: Godot 4 / Redot Engine Architecture Specialist [godot-redot-architect] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "godot-redot-architect"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Check for Godot / Redot CLI
if (Get-Command "godot" -ErrorAction SilentlyContinue) {
    Write-Host "[OK] Detected Godot CLI on PATH." -ForegroundColor Green
} elseif (Get-Command "redot" -ErrorAction SilentlyContinue) {
    Write-Host "[OK] Detected Redot CLI on PATH." -ForegroundColor Green
} else {
    Write-Host "[NOTE] Neither 'godot' nor 'redot' CLI binary found in PATH. Static analysis will run in fallback mode." -ForegroundColor Yellow
}

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for godot-redot-architect..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
