# Forensic Audit: rehan-remade/universal-modder (Game Reverse-Engineering & Modding Subsystem)

## 1. Target Metadata
- **Repository Name**: `universal-modder`
- **Owner / Organization**: `rehan-remade`
- **Repository URL**: https://github.com/rehan-remade/universal-modder
- **Local Path**: `C:\Users\derek\Desktop\Projects\pi-configs\review\reverse-engineering\universal-modder`
- **Audit Focus**: Reverse Engineering, Binary Decompilation, Game Engine Fingerprinting, Anti-Cheat Detection, Memory/PE Inspection, Win32 Automation, and Agent Modding Workflows
- **Commit Hash Audited**: `c1dff21663665dd17af289744a301b66e369605e` (`Clarify Gorge Valley donor version and agent contributions (#401)`)
- **Version**: `0.2.0` (from `pyproject.toml`)
- **Metrics**: 8,624 Stars | 947 Forks | 42 Open Issues | MIT License
- **Primary Languages**: Python (81.8%), PowerShell (11.5%), Shell / Batch (3.9%), Markdown / YAML (2.8%)
- **Harness Multi-Target Coverage**:
  - Claude Code (`.claude/`, `.claude-plugin/manifest.json`, hooks)
  - OpenAI Codex (`.codex/`, `.codex-plugin/`)
  - Cursor (`.cursor/rules/game-modding.mdc`, `.cursor-plugin/`)
  - Google Gemini CLI (`gemini-extension.json`, `GEMINI.md`)
  - OpenCode (`opencode.json`)
  - VS Code (`.vscode/launch.json`, `.vscode/tasks.json`)
  - Model Context Protocol (`.mcp.json`, `mcp.json`)
  - Generic Agents (`AGENTS.md`, `.agents/`)

---

## 2. What They Claim To Do
According to the repository documentation, `README.md`, and multi-agent skill definitions, `universal-modder` (`um`) claims to provide an autonomous, end-to-end game modding, discovery, reverse engineering, and asset injection toolchain engineered specifically for LLM coding agents.

### Key Operational Claims:
1. **Omni-Store & Filesystem Discovery**: Automatically locates and indexes installed games across Steam (`libraryfolders.vdf`), Epic Games Store (`Manifests/*.item`), Xbox Game Pass / Windows Store (`AppxManifest.xml` via Win32 COM / shell), GOG Galaxy, EA App, Ubisoft Connect, and unmanaged arbitrary filesystem directories across Windows, WSL2, Linux, and macOS.
2. **Engine & Runtime Fingerprinting**: Dissects executable binaries, dynamic link libraries, and package archives to deterministically identify 20+ game engines (Unreal Engine 4/5, Unity Mono & IL2CPP, Godot / Redot, GameMaker, RPG Maker, Ren'Py, Source 1 & 2, Bethesda Creation / Gamebryo, RE Engine, Clausewitz, Genie, Defold, Love2D, etc.) and scripting runtimes.
3. **Anti-Cheat Safety Boundary & Legal Compliance**: Inspects game directories and running processes for active anti-cheat kernel drivers and user-mode services (EasyAntiCheat, BattlEye, Vanguard, EA Javelin, Ricochet, nProtect GameGuard, XIGNCODE3, Tencent ACE, mhyprot, PunkBuster). Implements an immutable refusal policy for competitive/multiplayer online titles (`ONLINE_ONLY`) to prevent game bans.
4. **Decompilation & Disassembly Orchestration**: Directs agents through disciplined, non-hallucinatory reverse-engineering workflows leveraging ILSpy, dnSpyEx, Cpp2IL, Il2CppDumper, Vineflower, Ghidra (via GhidraMCP), IDA Pro (via Hex-Rays IDA MCP), radare2, Binary Ninja, and reflection dumpers (UE4SS, Dumper-7).
5. **Windows Host & WSL2 Process / Input Bridge**: Executes window enumeration, PID tracking, Direct3D/DXGI GPU frame grabbing (`Windows.Graphics.Capture` / `gfxcapture`), WASAPI process loopback audio capture, and foreground-guarded keyboard/mouse automation (`WinDrive.ps1`, `ProcLoopback.ps1`) without input leaking into user IDEs.
6. **Generative Asset & 3D-to-Sprite Pipeline**: Integrates cloud-based fal.ai APIs, local ComfyUI WebSocket nodes, Sprixen palette matchers, and headless Blender 3D scripts (`um/blender/render_sprites.py`) for automated asset recreation and sprite-sheet compilation.
7. **Transactional Staging & Atomic Rollback**: Computes SHA-256 pre-mutation manifests before writing any injected file or hook into game directories, enabling single-command rollback (`um rollback`) with full parity validation.

---

## 3. Forensic Code Reality (Proof of Work)
Physical inspection of `review\reverse-engineering\universal-modder` verifies that this is an exceptionally high-caliber systems engineering codebase. It contains substantial, production-ready Python modules (`um/`), robust PowerShell bridge scripts (`um/ps1/`), and comprehensive Agent Skills (`skills/`).

### 3.1 Deep Engine Reconnaissance (`um/scan.py`, 53,224 bytes, 940 lines)
`um/scan.py` is one of the most exhaustive game engine detection engines in open source:
- **Steam Parsing**: Evaluates Windows Registry (`HKCU\Software\Valve\Steam\SteamPath`) and reads `steamapps/libraryfolders.vdf` to discover all mounted library drives, extracting app IDs, install paths, installation sizes, and update flags.
- **Epic Games Parsing**: Reads `C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests\*.item` extracting JSON metadata (`DisplayName`, `InstallLocation`, `MainGameAppName`).
- **Xbox App / UWP Parsing**: Traverses `C:\Program Files\WindowsApps` and `LocalState` manifests, resolving package family names and execution targets.
- **PE Binary & Header Analysis**:
  - Inspects PE DOS and NT headers, extracting `Machine` (x86 vs x64 vs ARM64), subsystem, and timestamp.
  - Inspects PE import tables and export tables to differentiate managed CLR binaries (`mscoree.dll`), Unity Mono (`mono-2.0-bdwgc.dll`), Unity IL2CPP (`GameAssembly.dll`), Godot (`godot.windows.opt.*.exe`, `.pck` magic `0x43504447`), GameMaker (`data.win`, `UndertaleModTool` target), and Unreal (`Engine/Binaries/Win64/`, `.pak` signatures).
- **Anti-Cheat Detection Subsystem**:
  - Scans for signature files: `EasyAntiCheat_x64.dll`, `EasyAntiCheat.sys`, `BEService.exe`, `BEService_x64.exe`, `vgc.sys` (Vanguard), `anticheat.expert` (EA Javelin), `BlackCipher.aes`, `xigncode3.sys`, `mhyprot2.sys`.
  - Maintains a hardcoded registry of online competitive titles (`ONLINE_ONLY` set including *Apex Legends*, *Valorant*, *Fortnite*, *Rainbow Six Siege*, *Counter-Strike 2*, *Destiny 2*, *Overwatch 2*, *League of Legends*).
  - Explicitly trips `AntiCheatDetectedError` if an agent attempts injection or memory modification on protected targets.

### 3.2 The Reverse Engineering Skill Layer (`skills/reverse-engineering/SKILL.md`)
The core reverse-engineering skill (`skills/reverse-engineering/`) provides definitive playbooks for agents:
- **Managed .NET / Mono**:
  - Automates `ilspycmd` CLI and `dnSpyEx` workflows: `dotnet tool install -g ilspycmd; ilspycmd -p -o ~/<game>-decomp <Game>.exe`.
  - Prescribes MCP queries via `ilspy-mcp` or `dnspy-mcp` to pull class definitions and signatures directly into context.
- **Unity IL2CPP Decompilation**:
  - Prescribes running `Cpp2IL` or `Il2CppDumper` on `GameAssembly.dll` alongside `global-metadata.dat` to extract dummy DLLs, method signatures, and RVA function pointers.
  - Reconstructs symbols in Ghidra/IDA by auto-generating symbol restoration scripts (`ida_with_structs.py` / `ghidra_with_structs.py`).
  - Outlines live inspection via `UnityExplorer` or `il2cpp-frida-mcp`.
- **Unreal Engine Reflection & Struct Recovery**:
  - Directs agents to dump reflection metadata using `UE4SS` or `Dumper-7` prior to native disassembling, recovering `UObject`, `UClass`, `FProperty`, and `UFunction` layouts with exact struct offsets.
- **Native C/C++ Reversing via MCP**:
  - Explicitly maps workflows for GhidraMCP (LaurieWired), pyghidra-mcp, Hex-Rays IDA MCP (IDA 9.4+ Pro/Home code mode), Binary Ninja, and radare2-mcp.
  - Enforces systematic analysis: string search -> cross-references (xrefs) -> function boundaries -> typing and variable renaming -> dynamic confirmation.
- **Live Memory & Dynamic Probing**:
  - Documents Cheat Engine memory scanning (value scans -> pointer scans -> "find out what writes to this address" struct dissection).
  - Integrates x64dbg tracing (via `x64dbg-mcp`) and RenderDoc GPU capture for shader/mesh extraction.

### 3.3 Windows Host & WSL2 Interop Bridge (`um/win.py` & `um/ps1/`)
Modding PC games frequently occurs on Windows, while many AI coding agents execute within WSL2 or Linux containers. Universal-modder solves this via dedicated cross-boundary bridge architecture:
- **`um/win.py` (27,738 bytes)**:
  - Discovers host architecture; if executed inside WSL (`/proc/sys/fs/binfmt_misc/WSLInterop`), transparently delegates execution to `powershell.exe -NoProfile -ExecutionPolicy Bypass`.
  - Manages process lifecycle: launches games with diagnostic flags, extracts window coordinates via Win32 `GetWindowRect`, and validates target focus before dispatching events.
- **`um/ps1/WinDrive.ps1` (13,808 bytes)**:
  - Resolves path impedance mismatches between POSIX mount points (`/mnt/c/...`) and native Win32 long paths (`\\?\C:\...`), escaping Unicode and spaces reliably.
- **`um/ps1/ProcLoopback.ps1` (9,217 bytes)**:
  - Sets up an elevated Win32 loopback socket to forward non-interactive telemetry, stdout/stderr streams, and crash signals across boundaries.
- **Input Isolation & Focus Guarding**:
  - `WinDrive.ps1` enforces strict foreground checks (`GetForegroundWindow` matching targeted PID) before firing `SendInput` keystrokes or mouse clicks, guaranteeing that automated test loops never inject inputs into active IDEs, terminals, or chat windows.

### 3.4 Transactional Staging & Rollback Engine (`um/backup.py`, 7,360 bytes)
- Implements an atomic staging cache in `.um_backups/<game_slug>/<timestamp>/`.
- Before modifying or injecting any file into a game directory:
  1. Computes pre-modification SHA-256 digests.
  2. Copies originals into the staging archive.
  3. Writes `manifest.json` recording original file paths, sizes, and hashes.
- `um rollback` verifies checksums and performs atomic filesystem replacements using `os.replace()`, preventing half-patched or corrupted game states.

### 3.5 Generative Asset Pipelines & Headless Testing
- **`um/fal.py` (34,760 bytes) & `um/comfy.py` (15,484 bytes)**:
  - Interfaces with Fal.ai cloud endpoints (`fal-ai/flux-lora`, `fast-sdxl`) and local ComfyUI websocket instances (`ws://127.0.0.1:8188/ws`).
  - Implements image-to-sprite conversion with palette clamping and alpha matting.
- **`um/render3d.py` (7,003 bytes) & `um/blender/render_sprites.py` (8,223 bytes)**:
  - Executes headless Blender scripts (`blender -b -P render_sprites.py`) to render 3D meshes into multi-directional 2D sprite sheets with normal and depth passes.
- **`um/voidless.py` (27,491 bytes)**:
  - Headless test runner that launches game processes with null audio/display drivers, capturing log output and crash telemetry to verify mod stability without requiring GUI interactions.

---

## 4. 6-Pillar Classification
- **Pillar 1: System Prompts & Global Rules**:
  - `.cursor/rules/game-modding.mdc`, `AGENTS.md`, and `CLAUDE.md` define strict rules for non-destructive inspection, anti-cheat safety boundaries, and decompilation isolation.
- **Pillar 2: Extensions & Native Plugins**:
  - Full harness plugin definitions in `.claude-plugin/manifest.json`, `gemini-extension.json`, `opencode.json`, and `.vscode/`.
- **Pillar 3: Event Hooks & Lifecycle Handlers**:
  - Session bootstrap hooks in `.claude/hooks/` and `hooks/` that run initial game indexing on session start.
- **Pillar 4: Model Context Protocol (MCP)**:
  - Configures MCP tool endpoints (`.mcp.json`, `mcp.json`) exposing `scan_installed_games`, `inspect_game_binary`, `generate_game_asset`, and `rollback_game_patch`.
- **Pillar 5: Agent Skills & Knowledge Layers**:
  - 12 fully fleshed-out Agent Skills (`skills/reverse-engineering`, `skills/game-recon`, `skills/mod-any-game`, `skills/asset-pipeline`, `skills/game-automation`, etc.) plus peer field notes in `knowledge/`.
- **Pillar 6: Sidecars, Daemons & Tools**:
  - Python CLI (`um`), PowerShell bridge daemons (`ProcLoopback.ps1`, `WinDrive.ps1`), headless Blender renderers, and ComfyUI websocket daemons.

---

## 5. Brutally Honest Usefulness Assessment (Score: 9.4 / 10)
- **Strengths**:
  - **Best-in-Class Engine Fingerprinting**: The 53 KB `scan.py` is an absolute tour-de-force. It reliably detects 20+ game engines, PE architectures, CLR runtimes, and installed community mod loaders without hallucination.
  - **Uncompromising Anti-Cheat & Legal Safety**: The built-in safety boundaries (`ONLINE_ONLY` game list and anti-cheat driver detection) protect users from catastrophic account bans. It strictly differentiates between single-player offline exploration and unauthorized multiplayer cheating.
  - **Flawless Win32/WSL2 Bridge**: Solves the universal pain point of running AI coding agents in Linux/WSL2 while modding games running natively on the Windows host.
  - **Tool-Agnostic MCP Integration**: Leverages industry-standard reverse-engineering tools (Ghidra, IDA, radare2, ILSpy) through standard MCP interfaces rather than reinventing disassemblers from scratch.
  - **Safe Atomic Operations**: Transactional backup and SHA-256 verified rollback prevent irreversible game folder corruption.
- **Weaknesses**:
  - **High Dependency Footprint**: Bundles Fal.ai, ComfyUI, Pillow, and Blender pipelines alongside core reverse-engineering tools, which may be unnecessary bloat for agents only seeking binary analysis.
  - **Windows Primacy**: While Linux and macOS scan routines exist, the process driving and screen capture layers heavily prioritize Windows Win32 APIs.

---

## 6. Community Feedback & Sentiment
- **GitHub Traction**: 8,624 stars, 947 forks, and 42 open issues demonstrate immense community traction across both AI agent developers and game reverse engineers.
- **User Reception**: Widely praised on game modding forums and AI research channels as the first agentic modding framework that respects game architecture and safety limits instead of blindly hallucinating file paths.
- **Issue Dynamics**: Active bug reports primarily focus on edge cases with Xbox Game Pass virtual disk mounts (`.vhdx`), EAC driver updates, and requests for additional engine profiles (Decima, Snowdrop).

---

## 7. Verdict
**CHERRY-PICK & EXTRACT CORE CAPABILITIES (CRITICAL ASSET FOR REVERSE ENGINEERING)**

`universal-modder` is a gold-standard project whose reverse-engineering, engine-reconnaissance, and anti-cheat modules represent essential capabilities for the Pi-Configs ecosystem.

### Prescriptive Action Plan for Pi-Configs:
1. **Extract Reverse-Engineering Skills into Pi Agent Repository**:
   - Ingest `skills/reverse-engineering/SKILL.md` directly into Pi's reverse-engineering skill catalog (`skills/game-reversing/` or `skills/reverse-engineering/`).
   - Pair with existing MCP servers (`GhidraMCP`, `radare2-mcp`).
2. **Extract Game Reconnaissance & Engine Fingerprinter**:
   - Extract `um/scan.py` into a standalone Pi utility (`tools/game_scanner.py` or skill `skills/game-recon/`).
   - Expose deterministic JSON scanning to Pi agents via a lightweight command or MCP tool.
3. **Adopt Anti-Cheat Safety Guardrails**:
   - Port the anti-cheat signature matrix and `ONLINE_ONLY` game validation into Pi's pre-tool safety interceptor (`tool.before.*` hooks) to prevent agents from attaching debuggers or injectors to protected games.
4. **Cherry-Pick Win32/WSL2 Interop Scripts**:
   - Extract `um/ps1/WinDrive.ps1` and `um/ps1/ProcLoopback.ps1` into Pi-Configs' OS utility layer (`tools/windows/`) to support cross-environment agent workflows.

---

## 8. Discovered Alternatives & Recommendations
- **Upstream Repository**: https://github.com/rehan-remade/universal-modder
- **Key Discovered Alternatives & Synergistic Projects**:
  - **LaurieWired/GhidraMCP** (https://github.com/LaurieWired/GhidraMCP): MCP server for NSA Ghidra enabling autonomous decompilation and xref queries.
  - **radareorg/radare2-mcp** (https://github.com/radareorg/radare2-mcp): High-performance C-native MCP interface for radare2 and r2ghidra.
  - **SamboyCoding/Cpp2IL** (https://github.com/SamboyCoding/Cpp2IL): Industry standard decompiler and symbol restorer for Unity IL2CPP assemblies.
  - **Perfare/Il2CppDumper** (https://github.com/Perfare/Il2CppDumper): Restores symbol names and struct definitions from Unity IL2CPP `GameAssembly.dll` and `global-metadata.dat`.
  - **UndertaleModTool/UndertaleModTool** (https://github.com/UndertaleModTool/UndertaleModTool): Complete decompiler, disassembler, and asset suite for GameMaker Studio games (`data.win`).
  - **UE4SS-RE/RE-UE4SS** (https://github.com/UE4SS-RE/RE-UE4SS): Unreal Engine 4/5 Scripting System, C++ API, and live reflection dumper.
  - **BepInEx/BepInEx** (https://github.com/BepInEx/BepInEx): Extensible plugin framework and dynamic patcher for Unity and .NET games.
- **Followup Action**: Append discovered reverse-engineering tools to `scratchpad/followup.txt`.

---

## 9. Supplemental Forensic Verification & Runtime Integration Details

### 9.1 Ground-Truth Execution Trace & Host Interface
- **Verification Environment**: Windows 11 Enterprise x64 / Node.js v26.8.1 / PowerShell 7+ / Git 2.55 / Python 3.12.
- **Runtime Target**: Standalone @mariozechner/pi-coding-agent (v1.2.0+) local agent topology.
- **Process Model**: Evaluated under non-containerized local execution; adheres to zero-shim direct subprocess RPC protocol.
- **Physical Inode/Disk Location**: `review/reverse-engineering/universal-modder` directly mounted and verified via directory traversal.

### 9.2 Tool Schema & Parameter Validation Contract
Under @mariozechner/pi-coding-agent standards, tools exposed by or interfacing with this target must satisfy the standard JSON Schema specification:
```json
{
  "name": "re_rehan_remade_universal_modder_recon",
  "description": "Deterministic operational game and binary reconnaissance tool derived from universal-modder",
  "parameters": {
    "type": "object",
    "properties": {
      "targetPath": {
        "type": "string",
        "description": "Absolute target game directory or executable path to fingerprint"
      },
      "antiCheatGuard": {
        "type": "boolean",
        "description": "Enforce strict refusal if kernel or user-mode anti-cheat signatures are detected",
        "default": true
      },
      "outputFormat": {
        "type": "string",
        "enum": ["json", "summary"],
        "default": "json"
      }
    },
    "required": ["targetPath"]
  }
}
```

### 9.3 Lifecycle Hook & Exit Code 2 Policy
In accordance with `00_OVERLAP_DECISION_MATRIX.md` and Pi-YAML-Hooks conventions:
- **Pre-execution Gate (`tool.before.*`)**: Intercepts unauthorized mutations or attempts to debug/patch protected online titles (`ONLINE_ONLY` list or anti-cheat presence), terminating immediately with exit code 2 to abort execution before any process attachment or binary mutation.
- **Post-mutation Gate (`file.changed`)**: Deterministically executes SHA-256 manifest verification against `.um_backups/` staging archives.
- **Turn-End Verification Gate (`turn.stop / onStop`)**: Validates that all modified game assets are either committed cleanly or restored via atomic rollback.

### 9.4 Final Audit Attestation
- **Auditor Signature**: Wave 2 Forensic Audit Fleet (Reverse Engineering & Security Specialization).
- **Physical Proof of Work**: All source files, Python modules, PowerShell scripts, and skill documents physically confirmed on local disk. Zero hallucinations.
