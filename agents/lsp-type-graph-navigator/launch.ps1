# Launch script for Semantic LSP & Code Knowledge Graph Navigator (lsp-type-graph-navigator)
$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: Semantic LSP & Code Knowledge Graph Navigator [lsp-type-graph-navigator] ==="
$env:PI_SKIP_VERSION_CHECK = "1"
$env:PI_SPECIALIST_SLUG = "lsp-type-graph-navigator"
$env:PI_CONFIG_DIR = $PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for lsp-type-graph-navigator..."
pi --config "$PSScriptRoot/.pi/settings.json" --agents-file "$PSScriptRoot/AGENTS.md" @args
