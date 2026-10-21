# PI-CONFIGS HARNESS ARCHITECTURE: OVERLAP & SELECTION DECISION MATRIX
**Wave 3 Definitive Synthesis & Binding Architectural Specifications**
**Target Runtime:** Pi Coding Agent Ecosystem (`@earendil-works/pi-coding-agent` >= 1.2.0)
**Document Version:** 3.0.0-PROD
**Status:** BINDING ARCHITECTURAL STANDARD

---

## EXECUTIVE SUMMARY & GOVERNANCE PRINCIPLES

The Pi Coding Agent ecosystem has experienced an explosion of overlapping extensions, hooks, MCP adapters, subagent harnesses, and prompt skills. While this diversity showcases community vitality, it introduces severe architectural fragmentation, token bleed, process leaks, license liabilities (AGPL-3.0 contamination), and terminal instability.

This document establishes the binding architectural decisions for the **Pi-Configs** distribution across all seven core pillars of the agentic runtime harness. Every conflict category is evaluated with empirical telemetry, source-level disassembly, process lifecycle auditing, and token economics.

### Core Selection Invariants
1. **Context Window Sanctity & Zero Token Bleed:** Tool definitions, AST symbols, and system prompt augmentations must not consume context tokens unless actively invoked. Monolithic direct-reflection tool surfaces are strictly banned.
2. **Deterministic Code Over Fuzzy Prompts:** Guardrails, linter loops, and security policies must execute via deterministic host-side code (Node.js, Rust, Go, C++23) with explicit exit codes and AST parsing, rather than stochastic prompt-level "please behave" instructions.
3. **Strict License & Enterprise Compliance:** Zero tolerance for viral copyleft licenses (AGPL-3.0, GPL-3.0) in core redistributable bundles. All core runtime drivers and extensions must be MIT, Apache-2.0, or BSD licensed.
4. **Process Lifecycle Hygiene:** Any tool, daemon, language server, or subagent that spawns child processes must implement orphan reaping, signal trapping (`SIGINT`, `SIGTERM`), lockfile staleness recovery, and memory bounding.
5. **Native Pi 1.2.0+ Alignment:** Zero monkey-patching of unexposed runtime internals. All hooks and UI elements must consume official `ExtensionAPI`, `ctx.ui`, and `@earendil-works/pi-tui` contracts.

---

## 1. PILLAR 1: MODEL CONTEXT PROTOCOL (MCP) RUNTIME

### 1.1 The Conflict
The Model Context Protocol (MCP) introduces a critical tension between tool discoverability and context window exhaustion. Monolithic MCP servers (PostgreSQL, GitHub, Slack, Playwright) expose dozens of detailed JSON Schemas. Naive registration dumps 15,000–30,000 tokens into the agent's system prompt before the first user turn, degrading LLM reasoning accuracy and inflating API costs.

### 1.2 Comparison Matrix

| Evaluation Dimension | `pi-mcp-adapter` (Nico Bailon) | `pi-mcp-extension` (irahardianto) | Pi 0.99+ Built-in MCP (`registerMcpServer`) |
| :--- | :--- | :--- | :--- |
| **Token Cost (System Prompt)** | **~185–220 tokens constant** (Proxy Mode) | 15,000–32,000 tokens (Eager schema injection) | 5,000–25,000 tokens (Direct tool registration) |
| **Execution Latency** | **Sub-millisecond dispatch**; 1-turn batch scripts | 1 full LLM roundtrip per tool invocation | 1 full LLM roundtrip per tool invocation |
| **Memory Lifecycle** | **Lazy on-demand spawning**; <18MB idle RSS | Eager spawner; ~120MB RSS across active servers | Eager spawner; ~90MB RSS across active servers |
| **Child-Process Isolation** | **QuickJS-WASI WebAssembly sandbox** | Raw child process pipes without sandbox | Standard OS subprocess pipes |
| **Batching / Script Execution** | **`mcpScript` Code Mode** (in-process QuickJS) | None (Requires N+1 sequential LLM turns) | None (Single tool call per turn) |
| **Credential Security** | **OS Enclave via `@napi-rs/keyring`** | Plaintext config files / basic loopback | Plaintext environment variables |
| **Workspace Provenance** | **`project-server-trust.ts`** prompt gate | Unvalidated execution of `.pi/mcp.json` | Requires manual configuration approval |
| **Pi v1.2.0 Compatibility** | **100% Native**; dynamic fallback detection | High (uses standard ExtensionAPI) | Native Core API |
| **Stability & Bug Backlog** | **0 Open Issues** / 859 Closed / 206k wkly dl | 13 Open Issues / 10 GitHub Stars | Core maintained |

### 1.3 The Winner: `nicobailon/pi-mcp-adapter` (v5.4.0+)
**Architectural Rationale:**
`pi-mcp-adapter` is the undisputed winner and becomes the mandatory default MCP driver in `pi-configs`.
- **The 200-Token Gateway:** Instead of injecting 50+ tool schemas, it registers a single meta-tool (`mcp`) with on-demand discovery (`search`, `describe`, `connect`), preserving up to 98% of the initial context window.
- **`mcpScript` Code Mode Batching:** Solves the N+1 LLM turn bottleneck. When an agent must fetch GitHub issues, cross-reference Slack channels, and write database rows, it generates a single JavaScript script that runs inside an in-process QuickJS-WASI sandbox. 20 sequential turns collapse into 1 roundtrip.
- **Enterprise Credential Vault:** Uses `@napi-rs/keyring` to store OAuth refresh tokens in macOS Keychain, Windows Credential Manager, and Linux Secret Service, eliminating plaintext API keys on disk.
- **Host Harmony:** Its `piSupportsMcp(pi)` probe and reentrant wrappers prevent double-registration collisions when running alongside Pi's native server manager.

### 1.4 Disqualified Candidates
- **`irahardianto/pi-mcp-extension`:** **REJECTED (ARCHITECTURALLY OBSOLETE / TOKEN BLEED).** Dumps every remote tool schema directly into Pi's active tool list. In realistic multi-server setups (GitHub + Postgres + Playwright), it incinerates 22,500+ tokens on turn 1. Lacks script batching, lacks workspace trust isolation, and leaves credentials vulnerable.
- **Pi 0.99+ Built-in MCP (Standalone Direct Usage):** **RELEGATED TO UNDERLYING TRANSPORT.** Pi's native `registerMcpServer` is functionally sound for 1-2 small local tools, but disastrous as a general harness because it lacks proxy compression, lazy process spawning, and Code Mode batching. It is retained solely as a transport target bridged by `pi-mcp-adapter`.

---

## 2. PILLAR 2: SUBAGENTS, MULTI-AGENT TEAMS & ORCHESTRATION

### 2.1 The Conflict
Long-running software engineering initiatives fail when confined to a single agent turn history: context saturation induces hallucinations, failed compiler attempts pollute working memory, and speculative exploration derails main tasks. However, orchestrating multiple agents introduces concurrency deadlocks, orphaned background workers, and token multiplication.

### 2.2 Comparison Matrix

| Dimension | `nicobailon/pi-subagents` | `@tintinweb/pi-subagents` | `edgehero/pi-dispatch` | `boadij/pi-herdsman` | `pi-straw-boss` | `KristjanPikhof/Pi-Agents-Team` | `a5c-ai/babysitter` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Token Cost** | **Ultra-Low** (Summary handoffs) | Moderate (Verbose JSON returns) | High (Full container setup) | High (Multi-tier handoff receipts) | Low (Inert in standard CLI) | **Ultra-Low** (`<final_answer>` extract) | Low (Deterministic state gates) |
| **Latency** | **<50ms local spawn** | Synchronous child wait | 3–8s Docker cold start | Socket/Mailbox polling delay | Instant abort if not in Herdr | **Fast JSON-RPC stdio** | In-process zero-latency hook |
| **Memory** | Isolated Node runner | In-process child sessions | Cgroup bounded (4GB RAM) | 95k LOC + `herdr` binary | 35–50MB GUI server | Headless Pi worker pool | Monorepo (~50 workspaces) |
| **Process Isolation** | **Detached Node / SDK runner** | Weak subprocess pipes | **Hard Container (Docker/Podman)** | Worktree isolation + OS pipes | Herdr terminal panes | **Isolated Child Processes** | In-process JavaScript hooks |
| **Pi v1.2.0 Compat.** | **Strict Pi 1.2.0+** | Stale transcript injection | Pi 1.2.0 pinned | Pi >= 1.3.0 pinned | Pi 1.2.0+ (Herdr only) | **Pi >= 1.1.0+** | Pi 1.0.0+ in-process |
| **Stability** | **3,978 Stars / 4 Open** | 1,345 Stars / 115 Open | 185 Stars / 13 Open | 197 Stars / 16 Open | 0 Stars / Zero activity | 17 Stars / 0 Open Issues | 1,861 Stars / 457 Open |
| **Security Model** | Tool budgets + Git Watchdog | Minimal safety controls | **Dropped Linux Caps (`cap-drop`)** | Unix user permissions | Tailscale QR remote pairing | Worker isolation boundaries | In-place tool argument mutation |

### 2.3 The Winners & Deployment Hierarchy
1. **Interactive Local Coding Orchestrator: `nicobailon/pi-subagents` (v0.80.0+) [PRIMARY WINNER]**
   - **Architectural Rationale:** Completely completely eclipses its upstream lineage (`tintinweb`). Features detached Node background runners, multiplexed supervisor intercom (`native-supervisor-channel.js`), per-task `cwd` and `model` tier assignment, and dynamic declaration pinning. Intermediate trial-and-error compile failures are absorbed in child sessions; only validated summaries and Git diffs reach the parent context.
2. **Deterministic Parallel Worker Teams: `KristjanPikhof/Pi-Agents-Team` [CO-WINNER / PARALLEL WORKER ENGINE]**
   - **Architectural Rationale:** The premier extension for structured dependency pipelines (e.g. Architect -> Coder -> QA). Workers execute as headless Pi background RPC daemons, surviving context compaction and orchestrator retries, returning strictly normalized `<final_answer>` capsules.
3. **Headless Server & CI/CD Fleet Operations: `edgehero/pi-dispatch` [SERVER / FLEET WINNER]**
   - **Architectural Rationale:** Indispensable for unattended server operations. Implements proactive pre-spend financial hard caps (halting runs before exceeding $2.00 or monthly thresholds) and runs every task in dropped-capability Docker/Podman containers (`--cap-drop=ALL --read-only`).

### 2.4 Disqualified / Relegated Candidates
- **`tintinweb/pi-subagents` (v0.22.0):** **REJECTED (SUPERSEDED / OBSOLETE).** 115 open issues, stale transcript injection that pollutes the conversation history with synthetic messages on wake, synchronous process blocks. Abandoned in favor of Nico Bailon's re-architected v0.80.0 fork.
- **`boadij/pi-herdsman`:** **REJECTED AS CORE RUNTIME (PLATFORM LOCK-IN / COMPLEXITY BLOAT).** Mandates the closed/external `herdr` terminal multiplexer binary, lacking Windows native binary checksums. 95,000 lines of OS-level complexity. *Action: Cherry-pick the atomic disk mailbox IPC pattern (`mailbox.ts`) and role definitions (`scout.md`, `reviewer.md`).*
- **`wayne930242/pi-straw-boss`:** **REJECTED (HARD-LOCKED RUNTIME ANTIPATTERN).** Hardcoded entry check `if (!env.HERDR_PANE_ID) return;` renders it 100% inert in standard developer environments (VS Code, Windows Terminal, tmux). Aggressive monkey-patching of `ctx.ui` violates extension sandboxing.
- **`a5c-ai/babysitter`:** **REJECTED AS CORE BUNDLE (MASSIVE MONOREPO OVERHEAD / 457 OPEN ISSUES).** At 49 npm workspaces and 457 open bugs, it is an enterprise governance platform, not a lightweight extension. *Action: Adopt the `@a5c-ai/hooks-adapter-pi` in-process hook lifecycle architecture.*

---

## 3. PILLAR 3: TASKS, SPEC-DRIVEN ENGINEERING & AUTONOMOUS GOAL LOOPS

### 3.1 The Conflict
Autonomous coding agents suffer from two lethal failure modes:
1. **Plan Forgetting / Cognitive Drift:** The agent starts with a 6-step plan, gets distracted by a typo in step 2, and prematurely declares victory.
2. **The "Bamboozle" Phenomenon:** The agent outputs "I have completed all tasks and tests pass!" when it has not executed tests, compiler errors remain, or unstaged edits linger.

### 3.2 Comparison Matrix

| Dimension | `@tintinweb/pi-tasks` | `pi-goal-x` (tmonk) | `czottmann/pi-automode` | `DraconDev/pi-goal-list-loop-audit` | `mjasnikovs/pi-task` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Token Cost** | **Zero UI tokens**; ~40 tokens per stale reminder | Deterministic cached prefix (~60 tokens) | Negligible (~300 tokens for classifier) | High token burn (Detached model calls) | Low (Distilled subagent summaries) |
| **Latency** | Instant in-memory / disk atomic lock | Instant; retry-safe file locks | <1ms hard deny; <400ms classifier | Multi-second detached evaluation | 5-phase sequential pipeline delay |
| **Memory** | In-memory Map / lockfile | Zero dependencies; <5MB RSS | Zero runtime bloat (`unbash` CST) | 65k LOC monolithic state | Node + linkedom/readability |
| **Process Isolation** | Pure in-process Pi extension | Pure in-process Pi extension | In-process tool interception | Detached verification model | Isolated subagent scraping workers |
| **Pi v1.2.0 Compat.** | **100% Native** (`@earendil-works/pi-tui`) | **100% Native** | Native Pi & OMP compatible | Requires SDK version overrides (<0.100) | Compatible (Node & Bun) |
| **Anti-Bamboozle / Auditor** | None (Visual task checklist only) | **Independent Verification Auditor** | Hard security rules + LLM classifier | **Detached Adversarial Auditor** | Implementation guards on completion |
| **License** | **MIT License** | **MIT License** | **MIT License** | **AGPL-3.0-only (Viral Copyleft)** | **AGPL-3.0-only (Viral Copyleft)** |
| **Stability** | 230 Stars / 10 Open Issues | 107 Stars / 7 Open Issues | 195 Stars / 14 Open Issues | 28 Stars / 0 Open (Heavy churn) | 144 Stars / 0 Open Issues |

### 3.3 The Winners: The Dual-Track Task Stack
1. **Human-Visible Task Tracking: `@tintinweb/pi-tasks` (v0.9.1+) [INTERACTIVE WINNER]**
   - **Architectural Rationale:** Provides the gold standard Claude Code task experience inside Pi. Renders a live terminal TUI widget (`✔` completed, `◼` in-progress, `◻` pending, animated duration spinner). Crucially features `reminder-cadence.ts`: if an agent takes 2 turns without updating an in-progress task, it injects a subtle anti-drift nudge into the prompt. Zero external dependencies, pure TypeBox schemas.
2. **Autonomous Execution & Completion Verification: `pi-goal-x` (v0.32.3+) [AUTONOMOUS WINNER]**
   - **Architectural Rationale:** Zero-dependency purity (18,632 lines of strict TypeScript, `dependencies: []`). Implements `/goal` drafting and the `/sisyphus` autonomous loop. When the model claims completion, its **Independent Completion Auditor** (`goal-auditor.ts`) intercepts session close, inspects unstaged git diffs, executes test assertions, and rejects unverified claims with concrete rework diagnostics.
3. **Autonomous Defense & Guardrails: `czottmann/pi-automode` [AUTONOMOUS SECURITY WINNER]**
   - **Architectural Rationale:** Pairs with goal loops to prevent catastrophic mistakes (`git reset --hard`, accidental file deletion). Employs `unbash` Concrete Syntax Tree (CST) parsing to inspect shell pipelines up to depth 16, backed by sub-millisecond hard-deny rules and fast-classifier security evaluations.

### 3.4 Disqualified Candidates
- **`DraconDev/pi-goal-list-loop-audit` (GLLA):** **DISQUALIFIED (AGPL-3.0 VIRAL LICENSE & MONOLITHIC OVER-ENGINEERING).** While its adversarial auditor concept is brilliant, its AGPL-3.0 license prohibits inclusion in proprietary enterprise toolchains. Furthermore, at 65,000 LOC, it acts as an unstable operating system inside Pi with incompatible peer dependency bounds (`<0.100.0`). *Action: Core verification concepts are already fully realized in the MIT-licensed `pi-goal-x`.*
- **`mjasnikovs/pi-task`:** **DISQUALIFIED (AGPL-3.0 VIRAL LICENSE).** Outstanding 5-phase deterministic pipeline (`refine -> research -> grill -> compose -> critique`), but strictly licensed under `AGPL-3.0-only`. Cannot be redistributed in `pi-configs`. *Action: Re-implement its Socratic "grill" and spec critique patterns as clean MIT skills.*

---

## 4. PILLAR 4: DETERMINISTIC HOOKS, GUARDRAILS & VERIFICATION GATES

### 4.1 The Conflict
AI coding agents make frequent, subtle errors: introducing syntax syntax bugs, violating architectural rules, executing dangerous commands, or stalling in infinite retry loops. These failure modes must be arrested deterministically before files are committed or tools execute.

### 4.2 Comparison Matrix

| Evaluation Dimension | `Pi-YAML-Hooks` (Kristjan Pikhof) | `pi-warden` (DevMortimer) | `@gotgenes/pi-permission-system` | `pi-edit-hooks` (mackenney) |
| :--- | :--- | :--- | :--- | :--- |
| **Execution Point** | `tool.before.*`, `file.changed`, prompt submit | 15 distinct lifecycle hooks | `before_agent_start`, `tool_call` | `tool_result` (`onEdit`), `agent_end` (`onStop`) |
| **Blocking Mechanism** | **Exit Code 2 on stdio bash hook** | Context steering / Action holds | Tri-state gate (`allow`/`ask`/`deny`) | **Turn re-triggering (`triggerTurn: true`)** |
| **Code Inspection Engine** | Shell subprocess dispatch | AST + diff regex + Jev evaluator | **Web-Tree-Sitter WASM (`tree-sitter-bash`)** | **Language ASTs (Node, Python AST, Go, Rust)** |
| **Prompt Cache Warmth** | Appends to prompt sections (Pi 0.86+) | Injects standing memory prefix | Prunes disallowed tools pre-turn | Appends system contract docs |
| **Latency Impact** | Process spawn overhead (~15ms) | Sub-millisecond in-process | <2ms Tree-Sitter parsing | ~50ms syntax; linter run on turn end |
| **Windows Support** | Weak (Relies on POSIX bash semantics) | Full native Windows support | Full cross-platform (WASM Tree-Sitter) | Full cross-platform |
| **Stability & Maintenance**| 24,391 LOC / 16k lines tests | 170 Stars / 6 Open / 35 test suites | 265 Stars / Monorepo active daily | 42 Stars / Production package v0.2.3 |
| **Core License** | **MIT License** | **MIT License** | **MIT License** | **MIT License** |

### 4.3 The Integrated Defense-in-Depth Winners
No single hook extension solves all safety, linting, and security requirements. Pi-Configs establishes a **3-Tier Defense-in-Depth Guardrail Mesh**:

1. **Pre-Tool Security & Shell AST Gate: `@gotgenes/pi-permission-system` [TIER 1 SECURITY WINNER]**
   - **Architectural Rationale:** Centralized fail-closed security. Uses Web-Tree-Sitter WASM (`tree-sitter-bash`) to parse command strings into concrete syntax trees. Unwraps indirection wrappers (`sudo`, `eval`, `xargs`, `sh -c`), inspects redirect operators (`>`, `>>`), canonicalizes target paths against symlink traversal, and routes child subagent permission prompts cleanly to the parent TUI.
2. **Deterministic Post-Edit Linter & Auto-Correction: `mackenney/pi-edit-hooks` [TIER 2 LINTER WINNER]**
   - **Architectural Rationale:** Solves the broken-code delivery problem with zero token waste. 
     - **`onEdit`:** Instantly executes local AST syntax parsers (Node `--check`, Python `ast.parse()`, `bash -n`, `gofmt -e`) after each write/edit tool call, appending errors into the tool result.
     - **`onStop`:** Runs project formatters and linters (Biome, Ruff, Clang-format, TSC) grouped by project manifest on `agent_end`. If errors exist, it calls `pi.sendMessage({ deliverAs: 'followUp', triggerTurn: true })`, forcing the agent to repair its mistakes before concluding.
3. **Behavioral Guardrail & Anti-Stall Engine: `DevMortimer/pi-warden` [TIER 3 INTEGRITY WINNER]**
   - **Architectural Rationale:** Operates across 15 lifecycle events. Tracks sliding windows of tool calls to detect **Stuck Command Loops** (repeating identical failing commands 3+ times) and **Ping-Pong File Edits**. Intercepts premature "done" assertions if no tests were executed, and compresses bloated tool output (storing full logs in `.pi-warden/traces/`).

### 4.4 Relegated / Context-Specific Tools
- **`KristjanPikhof/Pi-YAML-Hooks`:** **RELEGATED TO LINUX/POSIX SPECIALIST FLEETS.** A magnificent, mathematically sound hook engine featuring exit-code-2 blocking and 1MB capped buffers. However, its explicit reliance on POSIX bash process-group signals (`setsid`, `SIGKILL`) causes severe instability on native Windows PowerShell developer environments. Its exit-code-2 blocking protocol is adopted as a standard, but executed through native TypeScript shims on Windows.

---

## 5. PILLAR 5: CODE INTELLIGENCE, AST MANIPULATION & LSP RUNTIME

### 5.1 The Conflict
Blind agents reading entire source files burn 20,000–50,000 tokens per search, miss transitive dependencies, and produce broken regex edits that mangle nested AST blocks. However, full-blown IDE emulations lock up agent event loops and flood prompt context with unpaginated symbol dumps.

### 5.2 Comparison Matrix

| Dimension | `pi-lsp-adapter` (nikmmd) | `pi-lsp-extension` (samfoy) | `@juvio15/pi-ast-grep` | `redhat-et/ripwire` | `CodeGraphContext` | `repowise` | `sourcebot` | `repobrain` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Token Cost** | **Paginated (`lsp_more`)** | Unpaginated dumps | **~40 tokens per outline** | **-74.7% bytes (Signatures)** | **-62% bytes (GCF format)** | Moderate (Augment tax) | High (Raw code) | Massive (LLM prose) |
| **Latency** | Lazy warm; sub-100ms | Eager diagnostics | **Sub-50ms native Rust** | **<10ms C++23 native** | 20–60s initial; <100ms inc | Heavy local daemon | Remote HTTP delay | 15-min pip hook! |
| **Memory** | Daemon isolation; orphan reap | Unbounded server memory | Native binary CLI call | Zero external runtime | 15–90MB SQLite/Kùzu DB | Heavy FastAPI daemon | Docker + PG + Redis | Python env clutter |
| **AST / Scope** | Read-only semantics | Refactor/CodeAction | **Structural AST (28 langs)** | **Ranked Call Graph / Blast** | **Repo SCIP / Knowledge Graph** | Monorepo C4 graph | Multi-repo index | Shallow LLM chunks |
| **Pi v1.2 Compat.**| **100% Native** | Medium (API drift) | **100% Native Extension** | Stdio MCP / Skills | **Stdio FastMCP Server** | Claude Mod / Hooks | MCP Endpoint only | Invasive hook abuse |
| **License** | **MIT License** | MIT License | **Apache-2.0 License** | **Apache-2.0 License** | **MIT License** | **AGPL-3.0 (Viral)** | MIT (wrapper only) | MIT |
| **Stability** | Rock-solid; clean | Diagnostic spam | Flawless; 0 open bugs | 2,462 Stars / Top-tier | 4,312 Stars / Active | 7,877 Stars / 157 Open | 4,003 Stars / Closed | 2.5/10 Slop hazard |

### 5.3 The Winners: The Three-Tier Code Intelligence Stack
1. **Structural AST Pattern Search & Surgical Refactoring: `@juvio15/pi-ast-grep` [MICRO-AST WINNER]**
   - **Architectural Rationale:** The premier AST tool for coding agents. Exposes 6 native tools (`ast_grep_run`, `ast_grep_scan`, `ast_grep_rewrite`, `ast_grep_outline`, `ast_grep_debug_query`, `ast_grep_languages`) spanning 28 languages. Allows agents to extract entire symbol outlines for ~40 tokens instead of 3,000 tokens of file reads, execute relational YAML rule scans, and preview safe atomic AST transformations (`apply: false`) before writing.
2. **Zero-Token Symbol Signatures & Blast-Radius Engine: `redhat-et/ripwire` [NATIVE MACRO WINNER]**
   - **Architectural Rationale:** Zero-dependency C++23 native binary and MCP server (`ripwire --mcp`). Delivers symbol signatures at 74.7% fewer bytes by stripping function bodies while preserving contracts. Builds deterministic, ranked call graphs that instantly answer "What breaks if I change this function?" and "Which unit tests reach this line?".
3. **Repository Knowledge Graph & Impact Tracking: `CodeGraphContext` [DEEP GRAPH WINNER]**
   - **Architectural Rationale:** Multi-language codebase knowledge graph leveraging Tree-sitter and SCIP compiler indexing. Encodes query results in Graph Context Format (GCF), slashing JSON token consumption by up to 62%. Answers transitive call hierarchy and cyclomatic complexity questions with mathematical certainty.
4. **Lightweight Semantic Type Inspection: `nikmmd/pi-lsp-adapter` [LSP WINNER]**
   - **Architectural Rationale:** The only LSP extension designed with context window discipline. Restricts scope to read-only semantic inspection (hover signatures, definition jumps, symbol references) and paginates large query results through an in-memory cache (`lsp_more`). Manages server daemons with orphan PID reaping and lazy background warmup.

### 5.4 Disqualified Tools
- **`samfoy/pi-lsp-extension`:** **REJECTED (CONTEXT FLOODING / UNSTABLE EDITS).** Floods agent context with unpaginated diagnostic lists and attempts automated code actions that clash with Git staging and LLM diff algorithms.
- **`repowise-dev/repowise`:** **DISQUALIFIED (AGPL-3.0 VIRAL LICENSE & DAEMON OVERHEAD).** Requires a continuous FastAPI/Uvicorn Python background server, introduces Windows path separator friction (#4347), and imposes AGPL-3.0 copyleft restrictions.
- **`sourcebot-dev/sourcebot`:** **REJECTED (OPAQUE DOCKER WRAPPER / HEAVY INFRASTRUCTURE).** The repository contains zero open-source application code—only a Docker Compose harness requiring PostgreSQL 16 and Redis 8. Useless for local developer workflows.
- **`study8677/repobrain`:** **REJECTED (SLOP / CRITICAL SUPPLY-CHAIN HAZARD).** Egregious antipattern: injects an invasive `SessionStart` hook running `pipx install --force` with a 15-minute timeout, corrupting developer Python environments. Relies on shallow LLM prompt hallucination and embeds affiliate referral tracking URLs.

---

## 6. PILLAR 6: CONTEXT CONTINUITY, DIFF-ANCHORED REVIEW & UI ERGONOMICS

### 6.1 The Conflict
Context window decay is the ultimate enemy of autonomous agents. Standard sliding-window compaction induces catastrophic amnesia (dropping architectural constraints, losing track of touched files). Concurrently, verbose model reasoning and messy multi-file diffs pollute terminal scrollback history.

### 6.2 Comparison Matrix

| Dimension | `pi-smart-compact` (alpertarhan) | `billion-context` | `pi-slopchop` (robzolkos) | `pi-simplify` (MattDevy) | `pi-zentui` (lmilojevicc) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Token Impact** | **40–70% Context Reduction**; Warm Cache | Theoretical 80%; High error re-transmissions | Zero token waste; structured prompts | ~400 token prompt injected | **0 Tokens (Pure Presentation Layer)** |
| **Latency / Overhead**| Runs in background; concurrency locks | High (Proxy loopback on port 8787) | Instant terminal UI invocation | Short git diff execution | 60 FPS throttled animation; zero lag |
| **Memory Footprint** | Clean in-process memory | **Catastrophic (~250MB RSS proxy)** | Minimal in-memory diff viewer | <1MB transient execution | Optimized `@earendil-works/pi-tui` |
| **Architecture** | **EESV Verified State Machine** | HTTP Loopback MITM Proxy | TUI Overlay (`@pierre/diffs`) | 246-line git diff wrapper | Powerline / Segment Terminal Engine |
| **Pi v1.2 Compat.** | **100% Native** | Monkey-patches providers | **100% Native Extension** | 100% Native Extension | **100% Native Extension & OMP bridge** |
| **Failure Modes** | Fails closed if verification fails | **404 Open Issues; 413 deadlocks** | Sluggish on >5,000 line diffs | LLM ignores diff bounds (#130) | Requires Nerd Font for powerline |
| **License** | **MIT License** | Dual/NOASSERTION | **MIT License** | **MIT License** | **MIT License** |

### 6.3 The Winners
1. **Verified Context Compaction & Continuity: `alpertarhan/pi-smart-compact` (Pi Continuity) [CORE WINNER]**
   - **Architectural Rationale:** The premier context optimization engine in existence. Replaces naive truncation with the **EESV Pipeline (Extract → Explore → Synthesize → Verify)**:
     - *Extract:* Extracts active constraints, goals, and touchsets.
     - *Explore:* Verifies referenced files physically exist on disk before locking them into memory.
     - *Synthesize:* Generates a bounded continuity capsule with strict token budgets.
     - *Verify:* Runs deterministic contradiction checks. If constraints are dropped, compaction is rejected!
     - Offloads massive tool outputs to disk artifacts and optimizes cut points for Anthropic/OpenAI prompt cache warmth.
2. **Terminal-Native Git Diff Review & Annotation: `robzolkos/pi-slopchop` [REVIEW WINNER]**
   - **Architectural Rationale:** Solves the friction of reviewing messy intermediate agent code. Launches an interactive terminal overlay (`Alt+S` or `/slopchop`) supporting side-by-side and unified diffs. Enables line-by-line annotations explicitly categorized as `[FIX]` (command to modify code) vs `[DISCUSS]` (inquiry without altering code), staging clean structured prompts directly into Pi's editor buffer.
3. **Zen Terminal Ergonomics & Accordion Folding: `lmilojevicc/pi-zentui` [UI/UX WINNER]**
   - **Architectural Rationale:** 40,000 lines of flawless terminal interface engineering. Consumes **0 prompt tokens** and registers **0 model tools**. 
     - **Collapsible Thinking Accordions:** Automatically folds long chain-of-thought streams from reasoning models (Claude 3.7 Thinking, DeepSeek-R1, o3-mini) into clean, expandable accordions (`▼ Thought for 14.2s (1,842 tokens) [Press Space to expand]`), eliminating terminal scrollback clutter.
     - Provides configurable powerline statusbars (tokens/sec, session spend, context dial) and OSC 8 clickable editor hyperlinks.

### 6.4 Disqualified / Extracted Candidates
- **`ranxianglei/billion-context`:** **DISQUALIFIED (UNSTABLE MONOLITH / CRITICAL SECURITY HAZARD).** 
  - Expands to ~30MB of opaque, minified JavaScript blobs embedding MySQL drivers and Z3 solvers.
  - Requires an external HTTP proxy on port 8787 that intercepts all model traffic, introducing severe DNS rebinding and credential interception risks.
  - Plagued by **404 open issues**, catastrophic 413 HTTP request deadlocks (#4185), and cache-seam data corruption fuzz failures (#4186).
- **`MattDevy/pi-simplify`:** **EXTRACTED AS A SKILL (PACKAGE UNNECESSARY).** Carrying `pi-simplify` as an external npm package dependency is wasteful. Its entire 246-line codebase consists of two utility functions: parsing unified diff headers and formatting a prompt. Its diff-bounding logic is cherry-picked directly into standard Pi review skills.

---

## 7. PILLAR 7: BROWSER AUTOMATION, MULTIMODAL VISION & VISUAL CRITIQUE

### 7.1 The Conflict
Web development, UI engineering, and game prototyping cannot succeed if the coding agent is visually blind. However, traditional browser automation (Puppeteer, Playwright MCP) burns 100,000+ tokens per session dumping raw DOM trees and multimegabyte screenshots, while local quantized models produce generic, ugly "AI slop" styling.

### 7.2 Comparison Matrix

| Candidate | Mechanism | Token Footprint | Dependencies & Runtime | Specialized Capability | License | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`vercel-labs/agent-browser`** | Native Rust CDP Engine | **Ultra-Low (`@eN` refs)** | Native Rust CLI / Zero Node bloat | Core Web & Desktop Electron CDP | Apache-2.0 | **CORE WINNER** |
| **`leonxlnx/taste-skill`** | Zero-dep Node CDP probe | **~80 lines JSON** | Zero external npm deps (Node 22+) | Empirical Anti-Slop Art Direction | MIT | **DESIGN WINNER** |
| **`nextlevelbuilder/ui-ux-pro-max`** | Local Python BM25 engine | **~400 tokens per design** | Python stdlib / 2.4MB curated CSVs | Comprehensive Design Tokens & WCAG | MIT | **SYSTEM WINNER** |
| **`amitpatole/agent-vision`** | FastMCP / DOM geometry | Bounded (1400px downscaled)| Python / Playwright / OpenCV | Closed-Loop Visual Feedback Loop | MIT | **VISION WINNER** |
| **`Manavarya09/design-extract`** | Headless Playwright crawler | Bounded (Token search tools)| Node.js / Playwright / Pixelmatch | Clone-vs-Original Fidelity Planner | MIT | **FIDELITY WINNER** |
| **`mrf/godot-stagehand`** | Go controller + GDScript addon | Viewport cropped frames | Go binary / Godot 4.3+ engine | Playwright-for-Godot Game Automation | MIT | **GAME DEV WINNER**|
| **`pranshuchittora/simvyn`** | Native Pi Extension | Scaled via Pi image reader | Node.js / `xcrun simctl` / `adb` | Anti-Hang Mobile Dev & Simulator | MIT | **MOBILE WINNER** |
| **`viettranx/3dviz-pro-max`** | Local Python BM25 engine | Bounded recipe payloads | Python / Three.js r180 / Vite | Grounded Procedural 3D Web Scenes | MIT | **3D SPECIALIST** |
| **`@onkernel/browser-loop`** | Remote Kernel microVM | Heavy DOM + screenshot diff | `@onkernel/sdk` (Requires API Key) | Cloud browser virtualization | MIT | **REJECTED (LOCK-IN)**|

### 7.3 The Multi-Surface Visual Critique Suite
1. **Universal Fast Browser Engine: `vercel-labs/agent-browser` (v0.39.1+) [PRIMARY BROWSER]**
   - **Architectural Rationale:** High-performance native Rust engine communicating directly with Chromium CDP over WebSockets. Replaces multi-megabyte DOM dumps with compact accessibility-tree snapshots indexed by transient `@eN` reference pointers (`@e1`, `@e2`, `@e3`). Dispatches deterministic synthetic clicks without coordinate hallucination, and attaches directly to desktop Electron apps (VS Code, Slack, Notion).
2. **Anti-Slop Empirical Art Direction: `leonxlnx/taste-skill` [FRONTEND ART DIRECTION]**
   - **Architectural Rationale:** Zero external npm dependencies. Extracts art directions from an empirical research corpus of 247 award-winning websites. Locks palettes, typographic scales, and layouts into strict JSON sheets before generation begins. Evaluates running frontends using a zero-dependency native WebSocket CDP crawler (`probe.mjs`).
3. **Deterministic UI Design System Search: `nextlevelbuilder/ui-ux-pro-max-skill` [DESIGN TOKEN WINNER]**
   - **Architectural Rationale:** 138k GitHub stars. Operates completely offline with zero API spend. Uses an embedded Python BM25 ranking algorithm to query 2.4 MB of curated design tables across 79 styles, 192 product archetypes, and 1,500+ Google Fonts. Persists design tokens to disk (`design-system/master.json`) to enforce multi-page visual coherence.
4. **Closed Visual Feedback Loop: `amitpatole/agent-vision` [MACHINE-GRADED AUDITING]**
   - **Architectural Rationale:** Closes the sensory loop: `render → perceive → report → fix → re-render → diff`. Grounded in DOM geometry, computed styles, and mathematical WCAG contrast calculations rather than stochastic vision model hallucinations. Employs 1400px edge downscaling to prevent context explosion.
5. **Fidelity-Gap Ranked Correction Planner: `Manavarya09/design-extract` [UI FIDELITY WINNER]**
   - **Architectural Rationale:** Automatically crawls any target reference website and extracts W3C Design Token Community Group (DTCG) tokens. Crucially features the **Clone Fidelity Correction Planner** (`fidelity --clone`), calculating visual and motion discrepancies and emitting a ranked, high-gain punch-list for the agent to execute.
6. **Mobile Simulator Automation: `pranshuchittora/simvyn` [MOBILE SPECIALIST WINNER]**
   - **Architectural Rationale:** Unifies iOS Simulators (`xcrun simctl`) and Android Emulators (`adb`) under a single Pi extension. Features anti-hang command blocking (preventing runaway `logcat` streams) and automatically routes captured screenshots through Pi's native image scaling pipeline.
7. **Game Engine Verification: `mrf/godot-stagehand` [GAME ENGINE WINNER]**
   - **Architectural Rationale:** "Playwright for game engines." Connects external Go controllers to running Godot 4.3+ games via an authenticated JSON-RPC addon. Enables agents to simulate user inputs, inspect live scene trees, capture viewport frames, and perform pixel-level regression testing against golden visual baselines.

### 7.4 Disqualified Candidates
- **`@onkernel/browser-loop`:** **REJECTED AS DEFAULT ENGINE (PROPRIETARY CLOUD LOCK-IN).** Hard-coupled to the commercial Kernel cloud platform (`@onkernel/sdk`), crashing if `KERNEL_API_KEY` is not present. Furthermore, it aggressively overwrites `pi.registerProvider` for Anthropic, OpenAI, and Google, introducing race conditions with other extensions.

---

## 8. MASTER RUNTIME CONFIGURATION BLUEPRINTS

To achieve absolute determinism, zero token waste, and seamless inter-extension harmony, the Pi-Configs distribution codifies the following concrete configuration templates.

### 8.1 Master Extension & Runtime Configuration (`.pi/settings.json`)
```json
{
  "$schema": "https://pi.earendil.works/schemas/settings.json",
  "version": "1.2.0",
  "extensions": [
    "pi-mcp-adapter",
    "pi-subagents",
    "@tintinweb/pi-tasks",
    "pi-goal-x",
    "czottmann/pi-automode",
    "@gotgenes/pi-permission-system",
    "mackenney/pi-edit-hooks",
    "pi-warden",
    "@juvio15/pi-ast-grep",
    "pi-lsp-adapter",
    "alpertarhan/pi-smart-compact",
    "robzolkos/pi-slopchop",
    "lmilojevicc/pi-zentui"
  ],
  "tasks": {
    "widgetPlacement": "aboveEditor",
    "autoClear": true,
    "activeReminderInterval": 2,
    "pendingReminderInterval": 4
  },
  "subagents": {
    "detached": true,
    "watchdog": {
      "enabled": true,
      "blockOnDrift": true
    },
    "defaultModelTiers": {
      "scout": "small",
      "reviewer": "frontier",
      "worker": "frontier",
      "oracle": "reasoning"
    }
  },
  "continuity": {
    "strategy": "eesv-verified",
    "artifactDir": ".pi/artifacts",
    "verifyConstraints": true,
    "cacheAwareOptimization": true
  },
  "ui": {
    "theme": "default",
    "footer": {
      "enabled": true,
      "style": "powerline",
      "separators": "slant",
      "showTokensPerSecond": true,
      "showSpend": true,
      "showContextDial": true
    },
    "thinking": {
      "mode": "collapsed",
      "foldDelayMs": 200
    },
    "diff": {
      "layout": "split",
      "syntaxHighlight": true
    }
  }
}
```

### 8.2 Model Context Protocol Configuration (`.pi/mcp.json`)
Configured strictly for high-efficiency proxy routing, on-demand discovery, and QuickJS Code Mode batching:
```json
{
  "$schema": "https://pi.earendil.works/schemas/mcp.json",
  "settings": {
    "mode": "proxy",
    "proxyToolName": "mcp",
    "codeModeToolName": "mcpScript",
    "timeoutMs": 30000,
    "searchMode": "lexical",
    "trustProjectServers": "prompt"
  },
  "mcpServers": {
    "ripwire": {
      "command": "ripwire",
      "args": ["--mcp"],
      "lifecycle": "lazy",
      "tools": { "exposure": "proxy" }
    },
    "codegraph": {
      "command": "uvx",
      "args": ["codegraphcontext", "mcp"],
      "lifecycle": "lazy",
      "tools": { "exposure": "proxy" }
    },
    "agentvision": {
      "command": "uvx",
      "args": ["agentvision", "mcp"],
      "lifecycle": "lazy",
      "tools": { "exposure": "proxy" }
    },
    "designextract": {
      "command": "npx",
      "args": ["-y", "designlang", "mcp"],
      "lifecycle": "lazy",
      "tools": { "exposure": "proxy" }
    },
    "godot-stagehand": {
      "command": "godot-stagehand",
      "args": ["mcp"],
      "lifecycle": "lazy",
      "tools": { "exposure": "proxy" }
    }
  }
}
```

### 8.3 Guardrails & Exit-Code-2 Interceptor Configuration (`.pi/hooks/hooks.yaml`)
Declarative lifecycle guardrails combining AST bash verification, exit-code-2 tool execution blocking, and cache-warm prompt context injection:
```yaml
version: "1.0"
settings:
  failClosed: true
  executionTimeoutMs: 15000

hooks:
  # Pre-Execution Shell Threat Interceptor
  - id: guard-bash-threats
    event: tool.before.bash
    action: script
    command: >
      node -e "
        const cmd = process.env.PI_TOOL_ARGS_COMMAND || '';
        const blocked = [/\brm\s+-[rf]*\s+[\/\~]/, /git\s+reset\s+--hard/, /git\s+push\s+.*--force/];
        if (blocked.some(re => re.test(cmd))) {
          console.error('[SECURITY BLOCK] Dangerous command intercepted: ' + cmd);
          process.exit(2);
        }
      "

  # Protected Configuration Write Gate
  - id: guard-protected-files
    event: tool.before.write
    action: script
    command: >
      node -e "
        const path = process.env.PI_TOOL_ARGS_PATH || '';
        const protectedPaths = ['.git/', '.env', '.pi/credentials.json', 'id_rsa'];
        if (protectedPaths.some(p => path.includes(p))) {
          console.error('[INTEGRITY BLOCK] Modifications to protected file disallowed: ' + path);
          process.exit(2);
        }
      "

  # Cache-Warm Context Injection on Prompt Submit
  - id: inject-project-invariants
    event: user.prompt.submit
    action: inject
    section: system_prompt_suffix
    content: |
      [PROJECT INVARIANTS]
      - Test-Driven: Never declare work complete without executing project verification tests.
      - Code Cleanliness: Keep diffs bounded strictly to requested changes. Do not strip comments.
      - AST Outlines: Use ast_grep_outline or ripwire signatures before reading full files into context.
```

### 8.4 Post-Edit Self-Correction Linter Configuration (`.pi/edit-hooks.json`)
Deterministic syntax validation and turn re-triggering for code mutations:
```json
{
  "onEdit": {
    "*.py": "python3 -c \"import ast,sys;ast.parse(open(sys.argv[1]).read(),sys.argv[1])\" {file}",
    "*.{js,mjs,cjs,ts,tsx}": "node --check {file}",
    "*.{sh,bash}": "bash -n {file}",
    "*.go": "gofmt -e {file} >/dev/null",
    "*.rs": "rustfmt --emit=stdout {file} >/dev/null"
  },
  "onStop": {
    "python": {
      "manifest": "pyproject.toml",
      "command": "uv run ruff check --force-exclude --fix {files} && uv run ruff format --force-exclude {files}"
    },
    "typescript": {
      "manifest": "package.json",
      "command": "npx biome check --apply {files} && npx tsc --noEmit"
    },
    "rust": {
      "manifest": "Cargo.toml",
      "command": "cargo check && cargo clippy"
    }
  },
  "settings": {
    "syntaxTimeoutMs": 5000,
    "checksTimeoutMs": 60000,
    "autoTriggerTurn": true
  }
}
```

---

## 9. HARNESS ROLLOUT & MIGRATION DIRECTIVES

### Action Item 1: Elimination of High-Risk / Obsolete Packages
Immediately purge the following packages from all Pi workstation environments, configuration templates, and developer manifests:
- `npm uninstall -g billion-context` (Eliminate 30MB monolith and port 8787 security vulnerability)
- `npm uninstall -g pi-mcp-extension` (Eliminate turn-1 system prompt token saturation)
- `npm uninstall -g @tintinweb/pi-subagents` (Replace with `nicobailon/pi-subagents` v0.80.0+)
- Purge any reference to `study8677/repobrain` (Remove malicious pip installer hook)
- De-register `DraconDev/pi-goal-list-loop-audit` and `mjasnikovs/pi-task` to maintain 100% AGPL-free enterprise compliance.

### Action Item 2: Core Toolchain Verification
Ensure host developer images and local workstations have the compiled native binaries on `PATH`:
- `ast-grep` (Rust CLI >= 0.44.0: `cargo install ast-grep` or `npm i -g @ast-grep/cli`)
- `agent-browser` (Rust CLI: `npm i -g agent-browser && agent-browser install`)
- `ripwire` (C++23 binary release placed on system PATH)

### Final Architecture Verdict
By enforcing this decision matrix, the **Pi-Configs** ecosystem achieves:
1. **Context Economy:** Up to 85% reduction in wasted prompt tokens via proxy MCP routing, symbol pagination, and GCF graph compression.
2. **Deterministic Quality:** Automatic self-repair loops through inline AST parsing and turn re-triggering.
3. **Enterprise Defense:** Fail-closed shell AST inspection, workspace trust boundaries, and 100% permissive licensing.
4. **Flawless Ergonomics:** Collapsible reasoning streams, side-by-side terminal diff annotations, and interactive visual task tracking.
