# Launch script for Mobile Web & Responsive Layout Engineer (mobile-web-eng)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: Mobile Web & Responsive Layout Engineer [mobile-web-eng] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "mobile-web-eng"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for mobile-web-eng..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
