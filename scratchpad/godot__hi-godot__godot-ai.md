# Forensic Audit: hi-godot/godot-ai

## 1. Target Metadata
- **Repository Name**: `godot-ai`
- **Owner / Organization**: `hi-godot`
- **Repository URL**: https://github.com/hi-godot/godot-ai
- **Local Path**: `C:\Users\derek\Desktop\Projects\pi-configs\review\godot\godot-ai`
- **Commit Hash Audited**: `b82b5c519b1b17228f70d8effce1626f391bd1dd` (`chore(release): prepare 4.3.0 (#1143)`)
- **Version**: `4.3.0` (Date: Sat Oct 3 13:08:14 2026 -0700)
- **Commit History Depth**: 1,122 commits across `main` and `release/v4`
- **License**: MIT License (`LICENSE`)
- **Primary Languages**: GDScript (~52%), Python (~43%), Shell / PowerShell (~5%)
- **Target Godot Version**: Godot **4.7+** (strictly enforced in 4.x line)
- **Python Runtime Requirements**: Python `>=3.11, <3.15` via `uv` / `uvx`
- **Core Runtime Dependencies** (`pyproject.toml`):
  - `fastmcp==4.0.10`, `fastmcp-slim==4.0.10`
  - `mcp==2.2.0`, `mcp-types==2.2.0`
  - `websockets==17.1`
  - `pydantic==2.13.5`
  - `httpx==0.28.1`, `httpx2==2.13.1`, `httpcore2==2.13.1`
  - `uvicorn==0.54.0`, `starlette==1.7.0`, `h11==0.16.0`, `anyio==4.15.1`
- **Configured Client Adapters** (`plugin/addons/godot_ai/clients/`):
  - 26 client configurators including `pi.gd`, `antigravity.gd`, `claude_code.gd`, `claude_desktop.gd`, `codex.gd`, `cursor.gd`, `deepseek_harness.gd`, `gemini_cli.gd`, `hermes.gd`, `omp.gd`, `opencode.gd`, `vscode.gd`, `zed.gd`.

---

## 2. What They Claim To Do
According to `README.md`, `AGENTS.md`, and `docs/plugin-architecture.md`, Godot AI claims to be a production-grade Model Context Protocol (MCP) server and bidirectional GDScript EditorPlugin that connects AI assistants (Claude Code, Pi Agent, Antigravity, Cursor, Codex, etc.) directly into a live Godot 4.7+ editor.

### Key Operational Claims
1. **Live Editor Bidirectional Control**: Exposes 46 high-level MCP tools and 120+ underlying Godot editor operations over an authenticated transport, enabling agents to build scenes, instantiate nodes, wire signals, edit properties, write and anchor-patch scripts, configure UI, tweak physics, manipulate tilemaps, manage shaders, and adjust cameras.
2. **Mutual HMAC Authentication & Transcript-Bound Protocol (v4 Protocol 2)**: Completely obsoleted insecure tokenless loopback ports. Editor and Python FastMCP daemon exchange cryptographic capabilities and verify mutual HMAC challenge proofs before any command is executed.
3. **Multi-Session Disambiguation**: Orchestrates multiple running Godot instances through an authoritative session registry (`<project-slug>@<16hex>`), allowing AI agents to pin calls to a specific editor via `session_id` or default to the active session.
4. **Readiness Gating & Self-Healing**: Enforces strict write locks (`require_writable_async()`). Prevents agents from modifying scenes while Godot is importing assets, recompiling shaders, or running modal dialogs (`EDITOR_NOT_READY` envelope contract).
5. **Runtime Game Liveness & Debugger Introspection**: Integrates a background autoload helper (`_mcp_game_helper`) that tracks game process liveness (`game_status.status = "live" | "break" | "not_live"`), captures GDScript boot-time parser errors directly from remote debugger frames, and reads run-isolated logs.
6. **Token-Optimized Rollup Architecture**: Avoids hitting client tool caps (<100 tools) by exposing 19 high-traffic verbs as first-class tools (`node_create`, `script_patch`, `project_run`, `logs_read`) while bundling remaining domain verbs into structured `<domain>_manage(op="...", params={...})` rollups.
7. **Cross-Model Vision Routing**: `editor_screenshot` captures 3D viewports, 2D viewports, cinematic Camera3D renders, and game framebuffers; includes automated vision routing fallback for text-only LLMs.

---

## 3. Forensic Code Reality (Proof of Work)
Physical inspection of the codebase in `review\godot\godot-ai` reveals exceptional architectural rigor, defensive programming, and meticulous adherence to production standards.

### 3.1 Architecture & Transport Stack
The system operates across a 3-tier boundary:
```text
[AI Assistant / CLI]
       │
       ▼ (stdio JSON-RPC)
[godot-ai attach (FastMCP Proxy)]
       │
       ▼ (HTTP + Bearer Capability Token)
[Python FastMCP Server (src/godot_ai/server.py)]
       │
       ▼ (Mutual HMAC WebSocket :9500)
[Godot EditorPlugin (plugin/addons/godot_ai/plugin.gd)]
       │
       ▼ (Internal Dispatcher & UndoRedo)
[Godot Engine SceneTree & EditorInterface]
```

- **Transport Boundary (`src/godot_ai/transport/websocket.py` & `plugin/addons/godot_ai/connection.gd`)**:
  - WebSocket listens on loopback (`127.0.0.1:9500`), but does *not* rely on loopback alone for trust.
  - Generates a cryptographically strong capability secret written to a restricted capability directory with strict filesystem ACLs.
  - Implements Protocol 2 mutual transcript-bound HMAC handshakes: client and server both prove possession of the ephemeral secret without transmitting it in plaintext.
  - Downgrade attempts to Protocol 1 or bare unauthenticated WebSocket connections immediately fail closed with socket termination.

- **Process Lifetime & Orphan Reaping (`src/godot_ai/orphan_reaper.py`)**:
  - Prevents zombie Python processes if Godot crashes or closes unexpectedly.
  - The server continuously monitors Godot PID status, idle timeouts, and parent process handles, automatically terminating itself cleanly if the parent editor disappears.

- **FastMCP Middleware Chain (`src/godot_ai/middleware/`)**:
  Registered in `src/godot_ai/server.py` in load-bearing composition order:
  1. `PreserveGodotCommandErrorData`: Ensures structured Godot engine error codes and stack traces survive JSON-RPC transmission.
  2. `StripClientWrapperKwargs`: Strips extraneous client wrappers injected by tools like Claude Desktop or Cursor.
  3. `ParseStringifiedParams`: Deserializes JSON strings into native Python dicts when LLMs improperly double-encode arguments.
  4. `FoldFlatManageParams`: Automatically folds flat parameters into nested `params={}` for `<domain>_manage` operations if the LLM flattens them.
  5. `HintOpTypoOnManage`: Evaluates Levenshtein distance on invalid `op` names and provides prescriptive corrective hints to the LLM.
  6. `TrackMcpSessions`: Observes session activity and tracks connection lifecycles.

### 3.2 Tool Surface & Rollup Mechanics
Physical inspection of `src/godot_ai/tools/` reveals 46 MCP tools:
- **Core Observation & State**: `editor_state`, `scene_get_hierarchy`, `node_get_properties`, `session_activate`.
- **Top-Level Direct Verbs**: `batch_execute`, `node_create`, `node_set_property`, `node_find`, `scene_open`, `scene_save`, `script_create`, `script_attach`, `script_patch`, `project_run`, `test_run`, `logs_read`, `editor_screenshot`, `editor_reload_plugin`, `animation_create`.
- **Domain Rollups (`<domain>_manage`)**:
  - `animation_manage`, `audio_manage`, `autoload_manage`, `camera_manage`, `csg_manage`, `editor_manage`, `filesystem_manage`, `game_manage`, `gridmap_manage`, `input_map_manage`, `material_manage`, `navigation_manage`, `node_manage`, `particle_manage`, `project_manage`, `resource_manage`, `scene_manage`, `script_manage`, `signal_manage`, `testing_manage`, `theme_manage`, `tilemap_manage`, `tileset_manage`, `ui_manage`.
- **Custom Tools Extensibility**: `custom_tool_call` and `custom_tools_manage` allow developers to expose project-specific GDScript methods as dynamic MCP tools.

### 3.3 The Godot-Side Implementation (`plugin/addons/godot_ai/`)
- **Plugin Lifecycle (`plugin.gd`)**: Registers docks, menu entries, project settings, debugger capture hooks, and lifecycle watchers. Integrates seamlessly with Godot's `UndoRedo` system so changes made by the AI can be undone with `Ctrl+Z` in the editor.
- **Client Configurator Engine (`plugin/addons/godot_ai/client_configurator.gd` & `clients/`)**:
  - Detects installed AI agents and CLI tools.
  - Specifically supports **Pi Agent** (`clients/pi.gd`), configuring `$USERPROFILE/.pi/agent/mcp.json` or `~/.pi/agent/mcp.json` with canonical stdio attach commands (`godot-ai attach`).
  - Specifically supports **Antigravity** (`clients/antigravity.gd`), updating `~/.gemini/config/mcp_config.json` with flat command configurations and disabling consoleless launcher flags on Windows to prevent stdio pipe freezes.
- **Game Helper Autoload (`plugin/addons/godot_ai/runtime/_mcp_game_helper.gd`)**:
  - Injected during game playback to provide IPC beacons, remote error capture, and frame pacing diagnostics back to the editor dock.

### 3.4 Telemetry Architecture (`src/godot_ai/telemetry.py` & `docs/TELEMETRY.md`)
- In v4.3.0, telemetry is rolled up into 15-minute batched latency histograms rather than per-call tracking.
- Session IDs are hashed via SHA-256 so project directory paths and machine usernames are never leaked.
- Complete opt-out is honored instantly via `GODOT_AI_DISABLE_TELEMETRY=true` or via the one-way opt-out toggle in the Godot AI editor dock.

---

## 4. 6-Pillar Classification
- **Pillar 1: System Prompts & Global Rules**:
  - Provides rich instructions in `AGENTS.md` specifying exact conventions for batch execution, session ID resolution, PR activity tracking, and error code handling.
- **Pillar 2: Extensions & Native Plugins**:
  - Godot Engine `EditorPlugin` (`plugin/addons/godot_ai/`), complete with custom dock UI (`mcp_dock.gd`), toolbar indicators, and project settings integration.
- **Pillar 3: Event Hooks & Lifecycle Handlers**:
  - Contains `.claude/hooks/` and background orphan reaper watchdogs (`watch_idle`, `watch_owner`) ensuring clean lifecycle teardown and avoiding leaked background processes.
- **Pillar 4: Model Context Protocol (MCP)**:
  - Premier implementation of MCP 2.2.0 / FastMCP 4.0.10. Implements MCP Tools, MCP Resources (`godot://nodes`, `godot://scenes`, `godot://scripts`, `godot://shaders`, `godot://classes`), and stdio proxy attach routing.
- **Pillar 5: Agent Skills & Knowledge Layers**:
  - `.claude/skills/verification/` provides test verification and diagnostic workflows; documentation includes extensive authoring guides for animations, shaders, and UI.
- **Pillar 6: Sidecars, Daemons & Tools**:
  - Python FastMCP daemon (`godot-ai`), stdio attach bridge CLI, and headless test runners (`script/ci-game-capture-smoke`).

---

## 5. Brutally Honest Usefulness Assessment (Score: 9.8 / 10)
- **Strengths**:
  - **Gold Standard Engineering**: This is arguably the most polished, mature, and robust MCP server in existence across any domain. The code quality, type annotations, unit tests (121 unit tests, 46 integration tests), and architecture docs are extraordinary.
  - **Native Pi & Antigravity Support**: Unlike most MCP tools that only test Claude Desktop, `godot-ai` has dedicated, platform-tested configurators for both Pi Agent (`clients/pi.gd`) and Antigravity (`clients/antigravity.gd`), handling Windows-specific path quirks, stdio freezing issues, and JSON merge precedence.
  - **Safe & Non-Destructive**: Integrates directly with Godot's `UndoRedo` stack and enforces readiness write gating, ensuring that AI modifications never corrupt scenes or clobber unsaved work.
  - **Deep Debugger & Game Liveness Integration**: Solves the classic problem where an AI runs a game and has no idea why it crashed. The `_mcp_game_helper` and debugger break synthesizer immediately relay compile and runtime errors back to the model.
- **Weaknesses**:
  - Requires Godot 4.7+: Projects pinned to older Godot versions (4.0–4.6) must use legacy v3 or upgrade their engine.
  - C# support is text-only: While GDScript has full AST analysis, parser validation, and hot reload, C# support is currently limited to file manipulation and symbol outlining without direct compiler integration.

---

## 6. Community Feedback & Sentiment
- **GitHub Traction**: Over 1,100 commits, 1,143 pull requests, active Discord community (5865F2 vanity invite), and widely recognized as the official AI bridge for Godot Engine developers.
- **Release Cadence**: Rapid, highly disciplined release engineering (from v4.0.0 through v4.3.0 in under a month) responding directly to community feedback regarding Linux Flatpak sandbox issues, Windows stdio hangs, and telemetry transparency.
- **Sentiment**: Celebrated by indie game developers and technical artists for cutting UI layout and signal wiring time from hours to minutes.

---

## 7. Verdict
**ADOPT AS-IS (MANDATORY CORE GODOT EXTENSION / MCP SERVER)**

`godot-ai` should be formally adopted as the default, first-party Godot MCP toolchain in the `pi-configs` ecosystem. Its native client configurator for Pi Agent (`clients/pi.gd`) makes connecting Pi to Godot completely turnkey (`godot-ai attach`).

### Actionable Next Steps for Pi-Configs:
1. **Default MCP Registration**: Add `godot-ai` to Pi's suggested/configured MCP server catalog in `configs/mcp.json`:
   ```json
   {
     "mcpServers": {
       "godot": {
         "command": "uvx",
         "args": ["godot-ai", "attach"]
       }
     }
   }
   ```
2. **Skill Pairing**: Pair `godot-ai` with Godot agent skills (such as `gamedev-skills` and `godogen`) so agents have both high-level design knowledge and physical execution tools in the editor.

---

## 8. Discovered Alternatives & Recommendations
- **Upstream Project**: https://github.com/hi-godot/godot-ai
- **Alternative Tools & Ecosystem Projects**:
  - **godot-stagehand** (https://github.com/mrf/godot-stagehand): Go MCP server and CI scenario runner for driving running Godot 4.3+ games, capturing frames, and diffing visual baselines.
  - **godogen** (https://github.com/htdt/godogen): Generative asset pipeline and automated Godot project generator.
  - **Claude-Code-Game-Studios** (https://github.com/Donchitos/Claude-Code-Game-Studios): Godot game dev studio simulation personas and stage-gate checklists.
  - **Blender-MCP** (https://github.com/ahujas/blender-mcp): Equivalent MCP bridge for 3D modeling and animation in Blender.
- **Follow-up Action**: Append entry to `scratchpad/followup.txt` under `[GODOT-MCP]`.
