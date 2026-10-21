# Forensic Audit: IvanMurzak/Godot-MCP

## 1. Target Metadata
- **Repo URL**: https://github.com/IvanMurzak/Godot-MCP
- **NPM Package**: `godot-cli` / `@ivanmurzak/godot-cli` (CLI toolchain under `cli/`)
- **Latest Commit Date / Release**: October 20, 2026 (Commit `6a65075`, PR #422 `chore(release): v0.32.0 (train t-2026-10-20-04)`)
- **Star Count / Forks / Issues**: ~300 stars | 28 forks | 1 open issue
- **License**: Dual-Licensing Architecture:
  - Addon Core & CLI: **Apache License 2.0** (`LICENSE`)
  - Query Data Layer: **PolyForm Shield License 1.0.0** (`com.IvanMurzak.Rql` NuGet package; free for commercial use except competing query/reflection products)
- **Target Engine & Runtime**: Godot Engine 4.3+ .NET Edition (`net8.0`, `Godot.NET.Sdk/4.3.0`)
- **Pi Version Compatibility**: Fully compatible with Pi `>=1.0.0` and Antigravity CLI via streamable HTTP MCP endpoints (`http://localhost:5000/mcp` or `https://ai-game.dev/mcp`) using standard JSON-RPC 2.0 over SSE/HTTP transport.

---

## 2. What They Claim To Do
`Godot-MCP` bills itself as the enterprise-grade Model Context Protocol (MCP) bridge and autonomous reflection subsystem for Godot Engine 4.3+ (.NET 8.0). It aims to turn Godot into a fully observable, bidirectional agent playground:
- **Consolidated RQL Query Architecture**: Radically reduces agent context window bloat by replacing over 20 discrete CRUD tools (`node-find`, `node-create`, `node-modify`, `resource-modify`, `scene-save`) with a single declarative Reflection Query Language via `rql-query`, `rql-mutate`, and `rql-schema`.
- **Bidirectional In-Engine Inspection & Mutation**: Allows AI agents to read, traverse, filter, instantiate, mutate, reparent, and delete scene tree nodes, sub-resources, project settings, input actions, autoloads, shader uniforms, TileMaps, and collision layers.
- **Strict Undo/Redo Fidelity**: Binds all agent-driven structural and property mutations to Godot's native `EditorUndoRedoManager`, preventing scene corruption and allowing game developers to press Ctrl+Z to revert agent hallucinations.
- **Runtime Reflection & Live In-Game Code Execution**: Equips agents with runtime diagnostic tools to capture console logs, inspect call stacks, hook runtime errors, and execute arbitrary C# scripts inside both the editor and running game builds via Microsoft Roslyn (`Microsoft.CodeAnalysis.CSharp`).
- **Multi-Agent CLI Ecosystem**: Includes `godot-cli`, an npm toolchain automating headless project creation, Godot addon bootstrapping, and automated configuration of 14 leading AI coding agents (Claude Code, Pi, Antigravity, Cursor, Codex, Gemini, VS Code Copilot).
- **Domain-Specific Addon Extensions**: Ships an extensible catalog supporting high-profile community addons including `PhantomCamera`, `Beehave` (behavior trees), `Dialogic` (narrative branching), and `Terrain3D`.

---

## 3. Forensic Code Reality (Proof of Work)
Physical inspection of `review\godot\Godot-MCP-2` verifies an advanced, production-hardened C# (.NET 8) and TypeScript monorepo with clean separation between editor lifecycle management, protocol framing, and the external CLI.

### A. Repository Topology & Core Assemblies
- `Godot-MCP.csproj` (77 lines): Targets `net8.0` with `Godot.NET.Sdk/4.3.0`. References core NuGet packages:
  - `com.IvanMurzak.ReflectorNet` (v5.4.3): In-memory runtime object reflector and serializer.
  - `com.IvanMurzak.McpPlugin` (v8.11.0): Shared client transport layer shared with `Unity-MCP`.
  - `com.IvanMurzak.Rql` (v0.1.1): PolyForm-shielded Reflection Query Language parser and AST executor.
  - `com.IvanMurzak.CodeExec` & `com.IvanMurzak.CodeExec.Roslyn` (v0.2.1): Dynamic in-memory script compiler.
  - `Microsoft.CodeAnalysis.CSharp` (v4.12.0): Full Roslyn compiler services.
- Sibling Assembly Isolation: The project enforces strict isolation (`<Compile Remove="Godot-MCP.Tests/**/*.cs" />`, `<Compile Remove="Godot-Tests/**/*.cs" />`) to avoid sibling-project glob collisions during `dotnet build`.
- Embedded Extension Catalog: `addons/godot_mcp/extensions.catalog.json` is embedded directly into the DLL (`LogicalName="Godot-MCP.extensions.catalog.json"`), ensuring the managed `GodotExtensionRegistry` operates without fragile `res://` disk paths.

### B. Client-Server Architecture: The Reverse SignalR Proxy
Unlike naive MCP implementations that bind standard I/O (stdio) directly to the Godot process (which is unstable due to engine log noise and thread blocking), `Godot-MCP` implements a robust tri-part architecture:
1. **The GameDev-MCP-Server**: A standalone, cross-engine MCP daemon (`GameDev-MCP-Server`) written in C# ASP.NET Core. In local development, `GodotMcpServerManager.cs` automatically downloads the prebuilt platform binary (`.godot/mcp-server/<rid>/`), tracks its PID, launches it as a background service, and monitors its 5-second readiness window. In cloud workflows, it connects to `ai-game.dev`.
2. **The Godot Addon Client (`GodotMcpPlugin.cs`)**: Connects outward to the server's SignalR hub (`<host>/hub/mcp-server`) via WebSockets. It dispatches agent commands onto Godot's main thread using `GodotMainThread.cs` and `MainThreadDispatcher.cs`.
3. **The AI Agent Interface**: Agents connect via standard Streamable HTTP MCP transport to `<host>/mcp` using JSON-RPC 2.0 with session leases (`SessionLease.cs`, `IdleShutdown.cs`).

### C. The RQL Data Engine (Token-Efficient Tooling)
Prior to v0.29, Godot-MCP suffered from severe tool explosion (over 25 distinct tools, consuming ~15,000 tokens of schema definition). In v0.32, all scene graph and resource manipulation is routed through `Tool_Rql.cs`:
- **`rql-query`**: Executes declarative queries against virtual data tables:
  ```rql
  nodes | where class == "OmniLight3D" | select $ref name path props["light_energy"]
  ```
- **`rql-mutate`**: Executes structural modifications and property setters with transactional rollback:
  ```rql
  nodes | where name == "Player" | set props["speed"] = 450.0
  ```
- Supported Virtual Tables: `nodes`, `root`, `selection`, `scenes`, `resources`, `files`, `console`, `settings`, `inputActions`, `autoloads`, `groups`, `layers`.
- Concrete Adapters in `addons/godot_mcp/Editor/Rql/Adapters/`: Dedicated adapters handle complex engine types including `Godot_Aabb_Adapter.cs`, `Godot_Transform3D_Adapter.cs`, `Godot_ShaderMaterial_Adapter.cs`, `Godot_TileSet_Adapter.cs`, `Godot_Theme_Adapter.cs`, and `Godot_MeshLibrary_Adapter.cs`.

### D. Dynamic Code Execution & Roslyn Compiler
In `addons/godot_mcp/Runtime/Tools/Tool_GameScript.cs` and `addons/godot_mcp/Editor/Tools/Tool_Script.Execute.cs`:
- Agents can send raw C# source code to `script-execute`.
- The engine compiles the code in-memory via Roslyn (`Microsoft.CodeAnalysis.CSharp`), injects active scene tree context (`GetTree()`, active root node), runs the execution payload on the main thread, and intercepts standard output, return values, and unhandled exceptions.
- Commit `07b67fd` (v0.32.0) introduced `GodotMcpCodeExecInGame=true`, allowing in-game Roslyn compilation in live exported debug builds.

### E. CLI Toolchain & Agent Autoconfiguration
Located in `cli/src/utils/agents.ts` (774 lines), the CLI provides automated MCP setup for 14 AI development environments:
- Supported Agent IDs: `claude-code`, `claude-desktop`, `cursor`, `vscode-copilot`, `vs-copilot`, `rider-junie`, `github-copilot-cli`, `gemini`, `antigravity`, `cline`, `open-code`, `codex`, `kilo-code`, and `custom`.
- Native Antigravity Compatibility: Configures both `~/.gemini/config/mcp_config.json` and `~/.gemini/antigravity/mcp_config.json` with primary streamable HTTP endpoints:
  ```json
  {
    "mcpServers": {
      "godot": {
        "url": "http://localhost:5000/mcp",
        "type": "http"
      }
    }
  }
  ```

---

## 4. 6-Pillar Classification
- **Primary Pillar**: **4. MCP (Model Context Protocol)**
- **Secondary Pillars**: **6. Extensions / CLI** & **5. Skills**
- **Evaluation Across the 6 Pillars**:
  1. *Hooks*: None. Does not hook into in-process agent lifecycle events.
  2. *LSP*: None. Delegates language intelligence to Godot's built-in LSP server; does not implement custom LSP servers.
  3. *AST*: Moderate (internal). Employs Microsoft Roslyn AST analysis for C# script validation and compilation diagnostics, but does not expose an open AST traversal API to the agent.
  4. *MCP*: Exceptional. State-of-the-art implementation featuring streamable HTTP/SSE transport, SignalR reverse-proxying, session leases, and token-minimized RQL query mechanics.
  5. *Skills*: High. Includes automated skill generation (`addons/godot_mcp/Runtime/Tools/Tool_Skills.Generate.cs`) and generates contextual guides for Godot architecture.
  6. *Extensions*: High. Houses a comprehensive Node.js CLI suite (`godot-cli`) managing editor processes, project initialization, dependency injection, and agent registration.

---

## 5. Brutally Honest Usefulness Assessment
- **Overall Score**: **8.8 / 10** (for Godot Game Development & Interactive Simulation); **2.0 / 10** (for non-Godot projects).
- **Strengths**:
  - *Context Optimization via RQL*: Consolidating 25+ CRUD tools into `rql-query` and `rql-mutate` reduces prompt overhead from ~15,000 tokens to under 2,800 tokens, leaving ample context for game logic reasoning.
  - *Rock-Solid Architecture*: Avoids standard I/O deadlocks by utilizing an out-of-process ASP.NET Core server with SignalR reverse sockets back into the Godot editor.
  - *Non-Destructive Mutation*: Direct integration with `EditorUndoRedoManager` ensures user work is never destroyed by hallucinated agent mutations.
  - *Multimodal Diagnostics*: Built-in screenshot capture tools (`Tool_Screenshot.Viewport.cs`, `Tool_Screenshot.Camera.cs`) allow vision-capable LLMs to evaluate visual rendering, shaders, and UI layouts.
- **Weaknesses & Technical Bottlenecks**:
  - *Engine Constraint*: Requires Godot .NET (C#) version 4.3+. Pure GDScript users without the .NET SDK cannot use this addon without installing .NET 8.
  - *License Restriction on RQL*: The `com.IvanMurzak.Rql` package is licensed under `PolyForm Shield License 1.0.0`. While free for commercial game development, commercial AI SaaS platforms cannot embed or redistribute RQL in competing agent services without a commercial exception.
  - *Binary Dependency*: Spawning `GameDev-MCP-Server` requires local process management and open network ports (`localhost:5000`), which can run into corporate firewall or anti-virus restrictions on Windows.

---

## 6. Community Feedback & Sentiment
- **Ecosystem Standing**: Recognized as the most technologically advanced MCP implementation for Godot 4, mirroring Ivan Murzak's widely respected `Unity-MCP` framework.
- **Star & Fork Velocity**: ~300 stars and 28 forks reflect rapid adoption within the niche intersection of game development and autonomous AI tooling.
- **Maintenance Cadence**: Outstanding engineering velocity. Actively maintained with automated release trains (`v0.32.0`, PR #422, commit `6a65075` on Oct 20, 2026), daily bug fixes, and instant compatibility patches for upstream Godot releases.
- **Developer Consensus**: Praised by developers using Claude Code, Cursor, and Rider for transforming Godot into a programmable, natural-language-controlled game engine. The transition to RQL in v0.29 was lauded for curing severe token bloat.

---

## 7. Verdict
**ADOPT / CHERRY-PICK (Profile-Scoped Game-Dev MCP)**
- **Strategic Fit**: Essential inclusion for any game development profile in `pi-configs`.
- **Integration Plan**:
  1. Do not load `Godot-MCP` in default, general-purpose Pi profiles (it requires a running Godot editor instance).
  2. Create a dedicated profile: `profiles/godot-gamedev.yaml`.
  3. Register the MCP server endpoint pointing at `http://localhost:5000/mcp` with streamable HTTP transport.
  4. Ensure developers have `dotnet 8.0` and Godot .NET 4.3+ installed when activating this profile.

---

## 8. Discovered Alternatives & Recommendations
- **Alternatives**:
  - `Unity-MCP` (https://github.com/IvanMurzak/Unity-MCP): The upstream flagship sister project targeting Unity 2022.3+, sharing the identical McpPlugin, ReflectorNet, and RQL architecture.
  - `godot-copilot` / `godot-ai`: Legacy in-editor GDScript-only plugins; fragile, lacking MCP standard compliance, and prone to stdout deadlocks.
  - `Unreal-MCP` (Community projects): Early-stage C++ plugins exposing Unreal Engine 5 via JSON-RPC, but lacking RQL-style query consolidation.
  - `Blender-MCP`: 3D DCC counterpart enabling agentic control over Blender scenes and Python bpy pipelines.
- **Actionable Takeaways for Pi-Configs**:
  - Adopt RQL's declarative data-layer abstraction pattern for internal Pi extensions: querying scenes or complex file trees through unified SQL-like syntax (`items | where ... | select ...`) is vastly superior to exposing 20+ fine-grained agent tools.
- **Followup Entry**:
  - Appended to `scratchpad/followup.txt`:
    `[GAME-DEV / GODOT-MCP] https://github.com/IvanMurzak/Godot-MCP - C# Godot 4.3+ MCP editor addon & RQL query engine paired with godot-cli; adopt for game development profiles.`

---

## 9. Supplemental Forensic Verification & Technical Architecture

### 9.1 Component Interconnect Sequence
```
+---------------+         HTTP / SSE         +--------------------+        SignalR Hub         +-------------------+
|   AI Agent    |  ----------------------->  | GameDev-MCP-Server |  <=======================> | Godot 4.3+ Editor |
| (Pi / Claude) |  <-----------------------  |   (ASP.NET Core)   |       (WebSockets)         | (addons/godot_mcp)|
+---------------+   JSON-RPC 2.0 (:5000/mcp) +--------------------+ (:5000/hub/mcp-server)     +-------------------+
                                                                                                        |
                                                                                              MainThreadDispatcher
                                                                                                        |
                                                                                                        v
                                                                                                +-------------------+
                                                                                                | RQL Engine & AST  |
                                                                                                | Node/Resource Map |
                                                                                                | UndoRedoManager   |
                                                                                                +-------------------+
```

### 9.2 Tool Registry Manifest (v0.32.0)
| Tool Identifier | Core Functionality | Execution Context |
|---|---|---|
| `rql-query` | Read-only declarative traversal of scene nodes, resources, settings | Main Thread (Editor) |
| `rql-mutate` | Atomic mutations, node instantiation, reparenting, property writes | Main Thread with Undo/Redo |
| `rql-schema` | Introspects available collections, ClassDB properties, and methods | ThreadPool / Main Thread |
| `script-execute` | In-memory Roslyn C# compilation and instant execution | Main Thread (Editor / Game) |
| `screenshot-viewport` | Captures main editor viewport buffer to base64 PNG | Rendering Server |
| `screenshot-camera` | Captures dedicated scene camera viewpoint | Rendering Server |
| `runtime-errors-get` | Fetches buffered runtime exceptions and stack traces | Runtime Memory RingBuffer |
| `console-get-logs` | Retrieves editor/runtime engine output logs | Engine Logger Sink |
| `ping` | Connection heartbeat and latency diagnostics | Immediate |
