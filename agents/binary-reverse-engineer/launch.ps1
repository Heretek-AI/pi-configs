# Launch script for Binary Disassembly & Headless Decompilation Specialist (binary-reverse-engineer)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: Binary Disassembly & Headless Decompilation Specialist [binary-reverse-engineer] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "binary-reverse-engineer"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for binary-reverse-engineer..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
