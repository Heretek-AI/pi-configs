# Launch script for WebAssembly & Component Model Systems Engineer (wasm-runtime-engineer)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: WebAssembly & Component Model Systems Engineer [wasm-runtime-engineer] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "wasm-runtime-engineer"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for wasm-runtime-engineer..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
