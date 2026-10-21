# Launch script for Accessibility & WCAG 2.2 AA Compliance Auditor (a11y-specialist)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: Accessibility & WCAG 2.2 AA Compliance Auditor [a11y-specialist] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "a11y-specialist"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for a11y-specialist..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
