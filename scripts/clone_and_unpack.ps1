$ErrorActionPreference = "Continue"

$skills = @(
    "https://github.com/mattpocock/skills",
    "https://github.com/vercel-labs/skills",
    "https://github.com/vercel-labs/agent-browser",
    "https://github.com/heygen-com/hyperframes",
    "https://github.com/designed-by-ai/skills",
    "https://github.com/magentosh/superpowers",
    "https://github.com/anthropics/skills",
    "https://github.com/leonxlnx/taste-skill",
    "https://github.com/github/awesome-copilot",
    "https://github.com/gamedev-skills/awesome-gamedev-agent-skills",
    "https://github.com/majidmanzarpour/threejs-game-skills",
    "https://github.com/wshobson/agents",
    "https://github.com/thedivergentai/game-dev-agentic-skills",
    "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill",
    "https://github.com/viettranx/3dviz-pro-max"
)

$projects = @(
    "https://github.com/Donchitos/Claude-Code-Game-Studios",
    "https://github.com/htdt/godogen",
    "https://github.com/rehan-remade/universal-modder",
    "https://github.com/morluto/rea",
    "https://github.com/GaganSD/pi-extensions",
    "https://github.com/AgiFlow/doompi",
    "https://github.com/Heretek-AI/optimized-prompts",
    "https://github.com/asgeirtj/system_prompts_leaks",
    "https://github.com/AgiFlow/aicode-toolkit",
    "https://github.com/a5c-ai/babysitter",
    "https://github.com/pranshuchittora/simvyn",
    "https://github.com/tintinweb/pi-tasks",
    "https://github.com/boadij/pi-herdsman",
    "https://github.com/czottmann/pi-automode",
    "https://github.com/edgehero/pi-dispatch",
    "https://github.com/DevMortimer/pi-warden",
    "https://github.com/MattDevy/pi-extensions",
    "https://github.com/mjasnikovs/pi-task",
    "https://github.com/ben-vargas/pi-packages",
    "https://github.com/lmilojevicc/pi-zentui",
    "https://github.com/mrclrchtr/supi",
    "https://github.com/mavam/pi-agents",
    "https://github.com/robzolkos/pi-slopchop",
    "https://github.com/philipbrembeck/pi-advisor",
    "https://github.com/alpertarhan/pi-smart-compact",
    "https://github.com/DraconDev/pi-goal-list-loop-audit",
    "https://github.com/nczz/pi-knowledge",
    "https://github.com/CinloDev/pi-sdd-profiles",
    "https://github.com/joematthews/pi-smart-web-search",
    "https://github.com/d3ara1n/pi-extensions",
    "https://github.com/repowise-dev/repowise",
    "https://github.com/sourcebot-dev/sourcebot",
    "https://github.com/redhat-et/ripwire",
    "https://github.com/aoci-spec/aoci-code",
    "https://github.com/proxysoul/Empryo",
    "https://github.com/study8677/repobrain",
    "https://github.com/KristjanPikhof/Pi-YAML-Hooks",
    "https://github.com/KristjanPikhof/Pi-Agents-Team"
)

$npmPackages = @(
    "pi-mcp-adapter",
    "billion-context",
    "pi-subagents",
    "pi-web-access",
    "@langfuse/pi-observability-plugin",
    "pi-mcp-extension",
    "openwiki",
    "pi-goal-x",
    "@dietrichgebert/ponytail",
    "pi-lens",
    "@onkernel/browser-loop",
    "pi-advisor-flow",
    "@gotgenes/pi-permission-system",
    "pi-straw-boss",
    "@companion-ai/feynman",
    "pi-lsp-adapter",
    "@tintinweb/pi-subagents",
    "pi-simplify",
    "gentle-pi"
)

Write-Host "=== CLONING SKILLS REPOS ==="
foreach ($repo in $skills) {
    $parts = $repo.Split('/')
    $owner = $parts[-2]
    $name = $parts[-1]
    $target = "review/skills/${owner}__${name}"
    if (-not (Test-Path $target)) {
        Write-Host "Cloning $repo -> $target"
        git clone --depth 1 "$repo.git" $target
    } else {
        Write-Host "Already cloned: $target"
    }
}

Write-Host "`n=== CLONING PROJECTS REPOS ==="
foreach ($repo in $projects) {
    $parts = $repo.Split('/')
    $owner = $parts[-2]
    $name = $parts[-1]
    $target = "review/Projects/${owner}__${name}"
    if (-not (Test-Path $target)) {
        Write-Host "Cloning $repo -> $target"
        git clone --depth 1 "$repo.git" $target
    } else {
        Write-Host "Already cloned: $target"
    }
}

Write-Host "`n=== UNPACKING NPM PACKAGES ==="
foreach ($pkg in $npmPackages) {
    $slug = $pkg.Replace("@", "").Replace("/", "__")
    $targetDir = "review/npm-packages/$slug"
    if (-not (Test-Path $targetDir)) {
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    }
    $extracted = Test-Path "$targetDir/package"
    if (-not $extracted) {
        Write-Host "Packing $pkg -> $targetDir"
        Push-Location $targetDir
        cmd.exe /c "npm pack $pkg"
        $tar = Get-ChildItem -Filter "*.tgz" | Select-Object -First 1
        if ($tar) {
            tar -xzf $tar.Name
            Write-Host "Extracted $tar"
        } else {
            Write-Warning "Failed to download $pkg"
        }
        Pop-Location
    } else {
        Write-Host "Already unpacked: $slug"
    }
}
Write-Host "=== BATCH DOWNLOAD COMPLETED ==="
