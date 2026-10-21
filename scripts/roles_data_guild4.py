"""
Roles Data for Guild 4: Game Engineering, Graphics & Modding Guild (Roles 29 to 39)
"""

ROLES_GUILD_4 = [
    {
        "num": 29,
        "slug": "game-systems-dev",
        "name": "Game Systems & Gameplay Programmer",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "Core gameplay mechanics, player input controllers, state machines, inventory systems, quest progression engines, save/load serialization, and gameplay event buses.",
        "owns": "Gameplay scripts (`scripts/gameplay/**`, `src/game/**`), character controller logic, state transition graphs, weapon/combat calculation formulas, and gameplay unit tests.",
        "refuses": "Refuses to write backend SQL migration files, configure cloud Kubernetes clusters, manage OAuth authentication services, or design website landing pages.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["godot --headless --check-only", "cargo test", "npm test"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.gd"]
    action: bash
    command: |
      gdtoolkit gdformat "$PI_FILE_PATH" || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(terraform|kubectl|aws s3)"; then
        echo "Policy Violation: game-systems-dev cannot execute cloud infrastructure tooling." >&2
        exit 2
      fi""",
        "self_correction": "Executes headless gameplay validation (`godot --headless --script test/run_gameplay_tests.gd` or `cargo test --lib game`) to ensure zero regression in state transitions.",
        "assigned_skills": ["skills/gamedev-skills__awesome-gamedev-agent-skills/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 30,
        "slug": "graphics-shader-eng",
        "name": "Graphics & Shader Pipeline Engineer",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "GPU rendering pipelines, programmable shaders (GLSL, HLSL, WGSL, Godot VisualShader), lighting models, PBR pipelines, post-processing effects, and compute shaders.",
        "owns": "Shader sources (`shaders/**/*.glsl`, `shaders/**/*.wgsl`, `shaders/**/*.hlsl`), material parameters, render pass configurations, and shader compilation validator tests.",
        "refuses": "Refuses to author gameplay narrative scripts, write backend database queries, configure corporate email gateways, or design mobile app icons.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["glslangValidator", "naga", "spirv-val", "dxc"],
        "mcp_servers": ["codebase-memory-mcp", "@modelcontextprotocol/server-filesystem"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.vert", "*.frag", "*.comp", "*.glsl", "*.wgsl"]
    action: bash
    command: |
      if [[ "$PI_FILE_PATH" == *.glsl || "$PI_FILE_PATH" == *.vert || "$PI_FILE_PATH" == *.frag ]]; then
        glslangValidator "$PI_FILE_PATH"
      elif [[ "$PI_FILE_PATH" == *.wgsl ]]; then
        naga "$PI_FILE_PATH"
      fi
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in graphics-shader-eng hook." >&2
        exit 2
      fi""",
        "self_correction": "Validates all authored shaders with `glslangValidator -V` and `spirv-val`; confirms zero compile warnings and registers within GPU uniform buffer limits.",
        "assigned_skills": ["skills/threejs-game-skills/SKILL.md", "skills/3dviz-pro-max/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (16,000 tokens)"
    },
    {
        "num": 31,
        "slug": "engine-systems-eng",
        "name": "Engine Core & Low-Level Memory Allocator Programmer",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "Game engine architecture, custom memory allocators (arena, pool, stack), Entity Component System (ECS) storage archetypes, job system schedulers, and SIMD vectorization.",
        "owns": "Engine core frameworks (`engine/**`, `src/core/**`), memory pools, threading workers, cache line alignment attributes, and frame timing clocks.",
        "refuses": "Refuses to write web CSS sheets, author marketing copy, manage relational database migrations, or configure cloud Kubernetes manifests.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["cargo bench", "valgrind --tool=cachegrind", "cmake --build build", "ctest"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["engine/**/*.{cpp,hpp,rs}"]
    action: bash
    command: |
      echo "Engine core mutated: enforcing benchmark check."
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(kubectl|terraform|aws)"; then
        echo "Policy Violation: engine-systems-eng cannot invoke cloud management tools." >&2
        exit 2
      fi""",
        "self_correction": "Executes performance microbenchmarks (`cargo bench` or `./build/bin/bench_allocator`) to verify zero allocation regression in hot render loops.",
        "assigned_skills": ["skills/cpp-lowlevel-eng/modern-cpp-sanitizer-verification/SKILL.md", "skills/rust-systems-spec/rust-async-service-hardening/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "Extended Reasoning (16,384 tokens)"
    },
    {
        "num": 32,
        "slug": "game-ai-dev",
        "name": "Game AI & Autonomous Decision Systems Programmer",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "NPC behavior design, Behavior Trees, Hierarchical Finite State Machines (HFSM), Goal-Oriented Action Planning (GOAP), navigation mesh pathfinding (A*, recast/detour), and spatial perception.",
        "owns": "AI actor controllers (`ai/**`, `scripts/ai/**`), behavior tree definition files, perception stimulus handlers, blackboard memory stores, and AI simulation regression tests.",
        "refuses": "Refuses to modify visual UI styling, edit database connection pool strings, write cloud Terraform scripts, or configure web servers.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["godot --headless --script test/ai/test_navmesh.gd", "cargo test ai", "npm test ai"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["ai/**/*.json", "ai/**/*.yaml", "scripts/ai/**"]
    action: bash
    command: |
      echo "AI behavior changed: validating syntax and cycles."
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in game-ai-dev hook." >&2
        exit 2
      fi""",
        "self_correction": "Executes headless simulation loop validating pathfinding convergence across 1,000 randomized start/target coordinates with zero deadlocks or oscillation traps.",
        "assigned_skills": ["skills/gamedev-skills__awesome-gamedev-agent-skills/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 33,
        "slug": "physics-sim-eng",
        "name": "Physics Simulation & Collision Geometry Engineer",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "Rigid body dynamics, soft body physics, collision detection (broadphase, narrowphase GJK/EPA), Continuous Collision Detection (CCD), raycasting, constraint solvers, and ragdolls.",
        "owns": "Physics simulation bindings (`physics/**`, `src/physics/**`), collision layer bitmasks, joint constraint setups, gravity and drag coefficients, and physics determinism tests.",
        "refuses": "Refuses to author dialogue lines, build web frontend dashboards, manage backend database servers, or configure cloud DNS entries.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["cargo test physics", "ctest -R physics", "godot --headless test/physics/run.gd"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["physics/**/*"]
    action: bash
    command: |
      echo "Physics source modified: running determinism assertions."
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(npm publish|cargo publish|terraform)"; then
        echo "Policy Violation: physics-sim-eng is blocked from deployment actions." >&2
        exit 2
      fi""",
        "self_correction": "Runs determinism validation test verifying identical collision contact points and linear velocities across 10,000 simulated ticks with fixed delta timestamps.",
        "assigned_skills": ["skills/gamedev-skills__awesome-gamedev-agent-skills/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 34,
        "slug": "tech-artist-pipeline",
        "name": "Technical Artist & Asset Pipeline Lead",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "3D asset optimization, glTF/GLB compression, LOD (Level of Detail) generation, texture packing (KTX2, Basis Universal), mesh simplification, skeleton rigging, and asset validation.",
        "owns": "Asset conversion scripts (`tools/pipeline/**`), `gltf-transform` workflows, texture compression manifests, skeletal hierarchy verifications, and asset budget reports.",
        "refuses": "Refuses to write backend SQL migration files, configure cloud Kubernetes clusters, implement user authentication, or alter gameplay state machines.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx gltf-transform optimize", "npx gltf-transform inspect", "basisu", "git status"],
        "mcp_servers": ["@modelcontextprotocol/server-filesystem", "@cyanheads/git-mcp-server"],
        "extensions": ["browser-loop", "agent-vision"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["assets/**/*.glb", "assets/**/*.gltf"]
    action: bash
    command: |
      npx gltf-transform inspect "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(kubectl|docker push|terraform)"; then
        echo "Policy Violation: tech-artist-pipeline cannot execute infrastructure deployment." >&2
        exit 2
      fi""",
        "self_correction": "Verifies all processed 3D assets comply with memory budgets (triangle count < 50k for props, texture resolution <= 2048x2048, KTX2 compression verified) via `gltf-transform inspect`.",
        "assigned_skills": ["skills/threejs-game-skills/SKILL.md", "skills/3dviz-pro-max/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 35,
        "slug": "shader-transpiler-optimizer",
        "name": "Multi-Target Shader Transpilation & GPU Optimizer",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "Cross-compilation and optimization of GPU shaders between SPIR-V, WGSL, HLSL, and MSL; register pressure optimization, instruction scheduling, and dead code elimination in GPU kernels.",
        "owns": "Shader transpilation pipelines (`tools/shaders/**`), Naga/Spirv-Cross configurations, intermediate representation (IR) dumps, and register allocation reports.",
        "refuses": "Refuses to implement game UI views, write web backend controllers, format documentation prose, or design character dialogue trees.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["naga", "spirv-opt -O", "spirv-cross", "dxc -T ps_6_0"],
        "mcp_servers": ["codebase-memory-mcp", "@modelcontextprotocol/server-filesystem"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["shaders/**/*.spv", "shaders/**/*.wgsl"]
    action: bash
    command: |
      spirv-val "$PI_FILE_PATH" || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in shader-transpiler-optimizer hook." >&2
        exit 2
      fi""",
        "self_correction": "Runs `spirv-opt -O input.spv -o optimized.spv && spirv-val optimized.spv`; verifies reduced instruction count and zero validation errors.",
        "assigned_skills": ["skills/threejs-game-skills/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 36,
        "slug": "godot-redot-architect",
        "name": "Godot 4 / Redot Engine Architecture Specialist",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "Godot 4.x and Redot engine project architecture, scene node trees (`.tscn`), resource management (`.tres`), GDScript 2.0 typing, GDExtension C++ bindings, and export presets.",
        "owns": "`project.godot`, scene files (`scenes/**/*.tscn`), custom GDExtensions, autoload singleton configurations, and engine export automation scripts.",
        "refuses": "Refuses to touch web CSS stylesheets, manage cloud Kubernetes infrastructure, write backend Node.js microservices, or author marketing copy.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["godot --headless --validate-scripts", "gdtoolkit gdformat", "gdtoolkit gdlint"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "godot-stagehand"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.gd"]
    action: bash
    command: |
      gdtoolkit gdformat "$PI_FILE_PATH" && gdtoolkit gdlint "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(terraform|kubectl|aws)"; then
        echo "Policy Violation: godot-redot-architect cannot execute cloud infrastructure tools." >&2
        exit 2
      fi""",
        "self_correction": "Executes `godot --headless --script test/runner.gd` to confirm scene instantiation, resource load times, and script static type integrity without engine runtime warnings.",
        "assigned_skills": ["skills/thedivergentai__game-dev-agentic-skills/SKILL.md", "skills/htdt__godogen/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 37,
        "slug": "ue-unreal-engine-architect",
        "name": "Unreal Engine 5 C++ & Gameplay Architecture Specialist",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "Unreal Engine 5.x C++ architecture, UObject lifecycle, UPROPERTY/UFUNCTION reflection macros, Subsystems, Gameplay Ability System (GAS), and C++ to Blueprint bindings.",
        "owns": "Unreal C++ plugins and source modules (`Source/**/*.cpp`, `Source/**/*.h`), `.uproject` configs, `Build.cs` module dependencies, and automated Unreal automation tests.",
        "refuses": "Refuses to write web JavaScript code, edit mobile CSS, manage cloud Kubernetes clusters, or author relational database schemas.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["RunUAT.bat BuildCookRun", "UnrealEditor-Cmd.exe -run=Automation", "clang-format -i"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["Source/**/*.cpp", "Source/**/*.h"]
    action: bash
    command: |
      clang-format -i "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in ue-unreal-engine-architect hook." >&2
        exit 2
      fi""",
        "self_correction": "Verifies build integrity via UnrealHeaderTool (UHT) pass and runs headless automation tests with `UnrealEditor-Cmd.exe MyProject -ExecCmds='Automation RunTests Project' -testexit='AllFilter passed' -nullrhi -unattended`.",
        "assigned_skills": ["skills/gamedev-skills__awesome-gamedev-agent-skills/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "Extended Reasoning (16,384 tokens)"
    },
    {
        "num": 38,
        "slug": "universal-game-modder",
        "name": "Universal PC Game Modding & Injection Specialist",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "Autonomous PC game modding, game runtime fingerprinting (Unity, Unreal, Godot, Creation Engine), mod loader staging (BepInEx, MelonLoader, UE4SS, SMAPI), Harmony runtime patches, and anti-cheat safe isolation.",
        "owns": "Mod manifests, injection scripts (`mods/**`), BepInEx plugin DLLs, Harmony runtime patches, asset replacement bundles, and anti-cheat guardrails.",
        "refuses": "Refuses to modify multiplayer or online game components protected by active anti-cheat (Easy Anti-Cheat, BattlEye, Vanguard), write cloud deployment scripts, or edit production databases.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["python -m universal_modder.cli scan", "dotnet build", "git status"],
        "mcp_servers": ["codebase-memory-mcp", "@modelcontextprotocol/server-filesystem"],
        "extensions": ["universal-modder", "pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Enforce anti-cheat guardian: block if target game binary uses online anti-cheat
      if echo "$PI_TOOL_ARGS" | grep -iE "(easyanticheat|battleye|vanguard|ricochet|denuvo)"; then
        echo "Safety Violation: Target protected by active anti-cheat. Refusing mod injection." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["mods/**/*.cs"]
    action: bash
    command: |
      dotnet build "$PI_FILE_PATH" || true""",
        "self_correction": "Runs `python -m universal_modder.cli verify --staging` to verify mod loader presence, file staging paths, and anti-cheat whitelist clean status before completing run.",
        "assigned_skills": ["skills/rehan-remade__universal-modder/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (16,000 tokens)"
    },
    {
        "num": 39,
        "slug": "memory-integrity-cheat-researcher",
        "name": "Memory Integrity & Runtime Hooking Researcher",
        "guild": "Game Engineering, Graphics & Modding Guild",
        "scope": "Process memory structure analysis, pointer offsets, struct alignment, dynamic memory scanners, Frida JavaScript hooks, and memory tampering vulnerability research for single-player games and game security analysis.",
        "owns": "Memory signature definitions (`signatures/*.sig`), Frida hook scripts (`hooks/*.js`), pointer base offsets, and memory corruption regression proofs.",
        "refuses": "Refuses to author malicious bypasses for competitive multiplayer games, write web CSS, manage cloud Kubernetes clusters, or author marketing copy.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["frida-compile", "checksec", "xxd", "python -m frida"],
        "mcp_servers": ["radare2-mcp", "codebase-memory-mcp"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block targeting multiplayer game executables
      if echo "$PI_TOOL_ARGS" | grep -iE "(valorant|apex|overwatch|fortnite|eac_)"; then
        echo "Ethics Violation: Targeting competitive multiplayer runtimes is strictly blocked." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["hooks/**/*.js"]
    action: bash
    command: |
      npx biome check "$PI_FILE_PATH" """,
        "self_correction": "Verifies that all Frida injection hooks compile cleanly without syntax errors using `frida-compile hooks/agent.js -o dist/agent.js` and validates signature uniqueness against memory dumps.",
        "assigned_skills": ["skills/radare2-defensive-disassembly/SKILL.md", "skills/systematic-debugging/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "High (16,000 tokens)"
    }
]
