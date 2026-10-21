# Launch script for iOS Swift / SwiftUI Native Mobile Specialist (ios-mobile-spec)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: iOS Swift / SwiftUI Native Mobile Specialist [ios-mobile-spec] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "ios-mobile-spec"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for ios-mobile-spec..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
