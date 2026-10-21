# Launch script for Autonomous Linter & Code Formatting Enforcer (linter-formatter-enforcer)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: Autonomous Linter & Code Formatting Enforcer [linter-formatter-enforcer] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "linter-formatter-enforcer"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for linter-formatter-enforcer..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
