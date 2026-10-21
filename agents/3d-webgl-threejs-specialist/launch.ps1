# Launch script for 3D WebGL / WebGPU & Three.js Graphics Specialist (3d-webgl-threejs-specialist)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: 3D WebGL / WebGPU & Three.js Graphics Specialist [3d-webgl-threejs-specialist] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "3d-webgl-threejs-specialist"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for 3d-webgl-threejs-specialist..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
