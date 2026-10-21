# Launch script for Creative Narrative Director & Worldbuilding Architect (creative-narrative-director)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: Creative Narrative Director & Worldbuilding Architect [creative-narrative-director] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "creative-narrative-director"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for creative-narrative-director..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
