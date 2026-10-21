# pi-configs

> **Autonomous Specialist Fleet Architecture & Forensic Ecosystem Audit for `@mariozechner/pi-coding-agent` (Pi v1.2.0+)**

---

## 1. Executive Summary

`pi-configs` provides a production-grade, local-first specialist fleet architecture for the **Pi coding agent** ecosystem. Unlike legacy multi-agent frameworks (such as Heretek-Crew under Paperclip/OpenCode) that rely on heavy Docker sidecars and fragile shell shims, `pi-configs` implements **70 self-contained, ultra-narrow local specialist agents**.

Every specialist in this fleet is completely isolated, operating under the **Principle of Least Privilege (PoLP)** with deterministic `exit code 2` hook guards, automated typecheck/linter correction loops, on-demand lazy MCP adapters, and structured AST/LSP code intelligence.

---

## 2. Core Architectural Pillars

```
+-----------------------------------------------------------------------------------+
|                            Pi Coding Agent (v1.2.0+)                              |
+-----------------------------------------------------------------------------------+
        |                      |                      |                      |
        v                      v                      v                      v
+---------------+      +---------------+      +---------------+      +---------------+
|  1. HOOKS     |      |  2. MCP       |      |  3. CODE INT  |      |  4. CRITIQUE  |
| pi-yaml-hooks |      | pi-mcp-adapter|      | ast-grep      |      | agent-browser |
| Exit code 2   |      | 200-tok proxy |      | ripwire       |      | taste-skill   |
| Auto-linter   |      | QuickJS mode  |      | CodeGraph     |      | agent-vision  |
| pi-warden     |      | Lazy spawns   |      | pi-lsp-adapter|      | stagehand     |
+---------------+      +---------------+      +---------------+      +---------------+
```

1. **Deterministic Guardrails & Hooks**:
   - Built on `Pi-YAML-Hooks` and `@gotgenes/pi-permission-system`.
   - Tool pre-execution gates (`tool.before.*`) intercept unauthorized operations and immediately abort with bash exit code `2`.
   - Post-mutation gates (`file.changed`) deterministically trigger language-specific formatters and static linters (`biome`, `ruff`, `cargo check`, `clang-format`).
   - Anti-stall and integrity enforcers (`DevMortimer/pi-warden`) prevent fake "done" declarations and break infinite conversational loops.

2. **Lazy, Proxy-Mode MCP Runtime**:
   - Standardized on `nicobailon/pi-mcp-adapter` (v5.4.0+), collapsing monolithic tool schemas into an efficient ~200-token proxy tool.
   - Child-process MCP servers are spawned on-demand and reaped on idle.
   - In-process QuickJS-WASI Code Mode (`mcpScript`) allows multi-step tool calls in a single turn without intermediate token bleed.

3. **High-Fidelity Code Intelligence & AST Hygiene**:
   - Surgical structural queries and dry-run rewrites via `@juvio15/pi-ast-grep` across 28 languages.
   - Zero-token structural signatures and blast-radius call graphs via `redhat-et/ripwire` (saving ~75% input tokens).
   - Multi-language AST knowledge graph traversal via `CodeGraphContext`.
   - Paginated, read-only LSP inspection via `nikmmd/pi-lsp-adapter` preventing unmanaged diagnostic dumps.

4. **Multi-Agent Orchestration & Subagent Context Isolation**:
   - In-process child-process RPC worker teams via `KristjanPikhof/Pi-Agents-Team`.
   - Context explosion prevented by discarding raw worker transcripts and extracting only deterministic `<final_answer>` blocks.
   - Task tracking and anti-drift reminders via `@tintinweb/pi-tasks` and `pi-goal-x`.

5. **Visual Critique, Game Testing & Anti-Slop**:
   - Zero-token headless browser inspection via `vercel-labs/agent-browser` (Rust CDP engine).
   - Machine-graded visual defect verdicts via `amitpatole/agent-vision` (WCAG relative luminance math, DOM geometry).
   - In-engine Godot 4.3+ viewport frame diffing via `mrf/godot-stagehand`.
   - Tone and language humanization via `jyooi/agent-simple-english` (stripping robotic buzzwords and marketing filler).

---

## 3. Directory Layout

```text
pi-configs/
|-- agents/                             # 70 Standalone Specialist Directories
|   |-- <agent-slug>/
|   |   |-- AGENTS.md                   # Operational charter, domain boundaries & DoD
|   |   |-- launch.ps1                  # One-click Windows PowerShell launcher
|   |   |-- launch.sh                   # One-click POSIX Bash launcher
|   |   `-- .pi/
|   |       |-- settings.json           # Model tier, thinking level, tool whitelist
|   |       |-- mcp.json                # Scoped lazy MCP server declarations
|   |       |-- mcp-adapter.json        # pi-mcp-adapter proxy runtime configuration
|   |       |-- hook/
|   |       |   `-- hooks.yaml          # Declarative exit-code-2 blocking guards
|   |       |-- extensions/
|   |       |   `-- index.ts            # Typed Pi extension lifecycle hooks
|   |       `-- skills/
|   |           `-- <skill-name>/
|   |               `-- SKILL.md        # Refactored, non-truncated execution skill
|-- scratchpad/                         # Forensic Audit & Architecture Outputs
|   |-- 00_OVERLAP_DECISION_MATRIX.md   # Binding judgment matrix across all 7 pillars
|   |-- 01_SPECIALIST_ROSTER_SPEC.md    # Master specification for all 70 specialists
|   |-- followup.txt                    # 109 verified wild alternatives cataloged
|   `-- *.md                            # 85 comprehensive per-repo forensic audit reports
|-- scripts/                            # Scaffolding, Generator & Verification Tooling
|   |-- build_specialist_fleet.js       # Node.js generator for all 70 specialist configs
|   |-- verify_mission_completion.js    # Deterministic 3-gate automated verification suite
|   |-- clone_and_unpack.ps1            # Staging downloader for skills, repos & npm tarballs
|   `-- expand_scratchpad.ps1           # Forensic audit expansion and verification script
`-- README.md                           # Master architectural documentation
```

---

## 4. The 70 Specialist Fleet Roster

The fleet is organized into 8 departmental guilds:

### Guild 1: Executive, Product & Documentation
| Slug | Title | Primary Tools | Recommended Model |
|---|---|---|---|
| [`exec-director`](agents/exec-director/) | Fleet Executive Director & OKR Governor | `git log`, `gh release list`, `codebase-memory-mcp` | Claude 3.7 Sonnet (16k thinking) |
| [`product-director`](agents/product-director/) | Product Director & Strategic PRD Author | `gh issue create`, `gh milestone list` | Claude 3.7 Sonnet (12k thinking) |
| [`tpm-scrum-lead`](agents/tpm-scrum-lead/) | Technical Product Manager & Agile Scrum Lead | `gh project`, `gh issue comment`, `pi-task` | Claude 3.5 Sonnet (6k thinking) |
| [`system-architect`](agents/system-architect/) | Enterprise System Architect & ADR Owner | `spectral lint`, `codebase-memory-mcp` | Claude 3.7 Sonnet (24k thinking) |
| [`tech-docs-lead`](agents/tech-docs-lead/) | Technical Documentation Lead & Docs Architect | `markdownlint-cli2`, `typedoc` | Claude 3.5 Sonnet (8k thinking) |
| [`ux-research-analyst`](agents/ux-research-analyst/) | UX Telemetry & Feedback Analyst | `duckdb`, `jq`, `mcp-server-duckdb` | Claude 3.5 Sonnet (6k thinking) |
| [`brand-copy-spec`](agents/brand-copy-spec/) | Brand Voice, Copywriting & Microcopy Specialist | `i18n-ally-cli`, `jq` | Claude 3.5 Sonnet (6k thinking) |
| [`api-spec-doc-specialist`](agents/api-spec-doc-specialist/) | OpenAPI, AsyncAPI & Protobuf API Doc Specialist | `spectral lint`, `redocly` | Claude 3.5 Sonnet (8k thinking) |
| [`creative-narrative-director`](agents/creative-narrative-director/) | Creative Narrative Director & Worldbuilder | `jq`, `git log`, narrative trees | Claude 3.7 Sonnet (12k thinking) |
| [`humanizer-and-tone-editor`](agents/humanizer-and-tone-editor/) | Natural Tone, Voice & Humanization Editor | `agent-simple-english`, `git diff` | Claude 3.7 Sonnet (12k thinking) |

### Guild 2: Visual, Aesthetic & Design Systems
| Slug | Title | Primary Tools | Recommended Model |
|---|---|---|---|
| [`gui-visual-critic`](agents/gui-visual-critic/) | GUI Visual Critic & Anti-AI-Slop Inspector | `agent-vision`, `taste-skill`, Playwright | Claude 3.7 Sonnet (16k thinking) |
| [`game-feel-and-vfx-critic`](agents/game-feel-and-vfx-critic/) | Game Feel, VFX & Juiciness Critic | `godot-stagehand`, `ffmpeg`, `ffprobe` | Claude 3.7 Sonnet (12k thinking) |
| [`ui-ux-designer`](agents/ui-ux-designer/) | UI/UX Designer & Interactive Prototyper | `tailwindcss`, `taste-skill`, `ui-ux-pro-max` | Claude 3.7 Sonnet (12k thinking) |
| [`design-system-eng`](agents/design-system-eng/) | Design Systems & Component Token Engineer | `test-storybook`, `style-dictionary` | Claude 3.5 Sonnet (8k thinking) |
| [`a11y-specialist`](agents/a11y-specialist/) | Accessibility & WCAG 2.2 AA Compliance Auditor | `@axe-core/cli`, `pa11y-ci` | Claude 3.5 Sonnet (8k thinking) |
| [`fe-perf-eng`](agents/fe-perf-eng/) | Frontend Performance & Core Web Vitals Engineer | `lighthouse-ci`, `vite-bundle-visualizer` | Claude 3.5 Sonnet (8k thinking) |
| [`mobile-web-eng`](agents/mobile-web-eng/) | Mobile Web & Responsive Layout Engineer | `playwright test --project=Mobile_Safari` | Claude 3.5 Sonnet (6k thinking) |
| [`3d-webgl-threejs-specialist`](agents/3d-webgl-threejs-specialist/) | 3D WebGL / WebGPU & Three.js Specialist | `gltf-transform`, Three.js r170+, WebGPU | Claude 3.7 Sonnet (16k thinking) |

### Guild 3: Core Language & Systems Engineering
| Slug | Title | Primary Tools | Recommended Model |
|---|---|---|---|
| [`ts-node-fullstack`](agents/ts-node-fullstack/) | TypeScript / Node.js Fullstack Systems Engineer | `tsc --noEmit`, `vitest`, `biome` | Claude 3.7 Sonnet (12k thinking) |
| [`rust-systems-spec`](agents/rust-systems-spec/) | Rust Systems & Memory-Safety Specialist | `cargo check`, `cargo clippy`, `cargo test` | Claude 3.7 Sonnet (16k thinking) |
| [`go-backend-eng`](agents/go-backend-eng/) | Go High-Concurrency Backend Engineer | `golangci-lint`, `go test -race` | Claude 3.7 Sonnet (12k thinking) |
| [`python-backend-spec`](agents/python-backend-spec/) | Python Async Backend & FastAPI Specialist | `ruff check`, `mypy --strict`, `pytest` | Claude 3.7 Sonnet (12k thinking) |
| [`cpp-lowlevel-eng`](agents/cpp-lowlevel-eng/) | C++23 Low-Level Systems & Memory Engineer | `clang-tidy`, `cmake --build`, `valgrind` | Claude 3.7 Sonnet (16k thinking) |
| [`java-kotlin-eng`](agents/java-kotlin-eng/) | Modern Java 21+ & Kotlin Backend Specialist | `./gradlew check`, `ktlintCheck` | Claude 3.7 Sonnet (12k thinking) |
| [`ios-mobile-spec`](agents/ios-mobile-spec/) | iOS Native Swift & SwiftUI Specialist | `xcodebuild test`, `swiftlint`, `simvyn` | Claude 3.7 Sonnet (12k thinking) |
| [`android-mobile-spec`](agents/android-mobile-spec/) | Android Native Kotlin & Jetpack Specialist | `./gradlew testDebugUnitTest`, `simvyn` | Claude 3.7 Sonnet (12k thinking) |
| [`embedded-rtos-firmware-eng`](agents/embedded-rtos-firmware-eng/) | Embedded C, RTOS & Bare-Metal HAL Engineer | `arm-none-eabi-gcc`, Zephyr / FreeRTOS | Claude 3.7 Sonnet (16k thinking) |
| [`wasm-runtime-engineer`](agents/wasm-runtime-engineer/) | WebAssembly & WASI Systems Specialist | `wasm-opt`, `wasm-tools validate`, `wasmtime`| Claude 3.7 Sonnet (12k thinking) |

### Guild 4: Game Engineering, Graphics & Modding
| Slug | Title | Primary Tools | Recommended Model |
|---|---|---|---|
| [`game-systems-dev`](agents/game-systems-dev/) | Game Systems & Gameplay Programmer | `godot --headless`, `cargo test` | Claude 3.7 Sonnet (12k thinking) |
| [`graphics-shader-eng`](agents/graphics-shader-eng/) | Graphics & Shader Pipeline Engineer | `glslangValidator`, `naga`, SPIR-V | Claude 3.7 Sonnet (16k thinking) |
| [`engine-systems-eng`](agents/engine-systems-eng/) | Engine Core & Memory Allocator Programmer | `cargo bench`, `valgrind --tool=cachegrind` | Claude 3.7 Sonnet (16k thinking) |
| [`game-ai-dev`](agents/game-ai-dev/) | Game AI & Autonomous Decision Systems Programmer | `godot --headless --script test/ai`, navmesh | Claude 3.7 Sonnet (12k thinking) |
| [`physics-sim-eng`](agents/physics-sim-eng/) | Physics Simulation & Collision Engineer | `cargo test physics`, `ctest -R physics` | Claude 3.7 Sonnet (12k thinking) |
| [`tech-artist-pipeline`](agents/tech-artist-pipeline/) | Technical Artist & Asset Pipeline Lead | `gltf-transform`, Blender CLI, sprite tools | Claude 3.5 Sonnet (8k thinking) |
| [`shader-transpiler-optimizer`](agents/shader-transpiler-optimizer/) | Multi-Target Shader Transpiler & Optimizer | `naga`, `spirv-opt -O`, WGSL / HLSL | Claude 3.7 Sonnet (12k thinking) |
| [`godot-redot-architect`](agents/godot-redot-architect/) | Godot 4 / Redot Engine Architect | `godot --headless --validate-scripts` | Claude 3.7 Sonnet (12k thinking) |
| [`ue-unreal-engine-architect`](agents/ue-unreal-engine-architect/) | Unreal Engine 5 C++ & Gameplay Architect | `RunUAT.bat BuildCookRun`, UE5 UHT/UBT | Claude 3.7 Sonnet (16k thinking) |
| [`universal-game-modder`](agents/universal-game-modder/) | Universal PC Game Modding Specialist | `universal-modder`, BepInEx, Harmony, SMAPI | Claude 3.7 Sonnet (16k thinking) |
| [`memory-integrity-cheat-researcher`](agents/memory-integrity-cheat-researcher/) | Memory Integrity & Runtime Hooking Researcher | `frida-compile`, `checksec`, `radare2-mcp` | Claude 3.7 Sonnet (16k thinking) |

### Guild 5: Architecture, Cloud & Infrastructure
| Slug | Title | Primary Tools | Recommended Model |
|---|---|---|---|
| [`cloud-platform-eng`](agents/cloud-platform-eng/) | Cloud Platform & OpenTofu / IaC Engineer | `tofu fmt -check`, `tofu validate`, AWS MCP | Claude 3.7 Sonnet (12k thinking) |
| [`k8s-orchestrator`](agents/k8s-orchestrator/) | Kubernetes Platform & Helm Orchestrator | `kubeconform -strict`, `helm lint` | Claude 3.5 Sonnet (8k thinking) |
| [`dba-specialist`](agents/dba-specialist/) | Database Administrator & SQL Perf Engineer | `sqlfluff lint`, `pg_format`, Postgres MCP | Claude 3.7 Sonnet (12k thinking) |
| [`cache-streaming-eng`](agents/cache-streaming-eng/) | Distributed Cache & Event Streaming Engineer | `redis-cli ping`, `kcat -L`, Kafka MCP | Claude 3.5 Sonnet (8k thinking) |
| [`sre-incident-eng`](agents/sre-incident-eng/) | SRE & Incident Commander | `promtool check rules`, Sentry MCP | Claude 3.7 Sonnet (12k thinking) |
| [`observability-eng`](agents/observability-eng/) | Observability & OpenTelemetry Engineer | `promtool check config`, OTEL collector | Claude 3.5 Sonnet (8k thinking) |
| [`git-drift-coord`](agents/git-drift-coord/) | Git Worktree & Branch Drift Coordinator | `git status`, `git worktree list` | Claude 3.5 Sonnet (6k thinking) |

### Guild 6: Quality Assurance & Verification
| Slug | Title | Primary Tools | Recommended Model |
|---|---|---|---|
| [`e2e-browser-qa`](agents/e2e-browser-qa/) | E2E Browser QA Automation Engineer | `npx playwright test`, Playwright MCP | Claude 3.7 Sonnet (12k thinking) |
| [`api-contract-tester`](agents/api-contract-tester/) | API Contract & Pact Verification Specialist | `schemathesis run`, OpenAPI validation | Claude 3.5 Sonnet (8k thinking) |
| [`load-stress-tester`](agents/load-stress-tester/) | Performance Load & k6 Stress Testing Engineer | `k6 run tests/load/scenario.js` | Claude 3.5 Sonnet (8k thinking) |
| [`sabotage-qa-tester`](agents/sabotage-qa-tester/) | Mutation Testing & Chaos Sabotage Tester | `npx stryker run`, `cargo mutants` | Claude 3.7 Sonnet (12k thinking) |
| [`release-qa-officer`](agents/release-qa-officer/) | Release QA Officer & Deployment Gatekeeper | `git diff --stat`, release sanity probes | Claude 3.7 Sonnet (12k thinking) |

### Guild 7: Defensive Security, Binary Forensics & AI Red-Teaming
| Slug | Title | Primary Tools | Recommended Model |
|---|---|---|---|
| [`appsec-engineer`](agents/appsec-engineer/) | Application Security & SAST/DAST Engineer | `semgrep scan --config p/security-audit` | Claude 3.7 Sonnet (16k thinking) |
| [`cloud-sec-auditor`](agents/cloud-sec-auditor/) | Cloud Security & IAM Permissions Auditor | `checkov -d .`, `trivy config .` | Claude 3.7 Sonnet (12k thinking) |
| [`binary-reverse-engineer`](agents/binary-reverse-engineer/) | Binary Reverse Engineer & Disassembly Specialist | `radare2-mcp`, `GhidraMCP`, `objdump` | Claude 3.7 Sonnet (16k thinking) |
| [`firmware-sec-analyst`](agents/firmware-sec-analyst/) | Firmware Security & Hardware Attack Analyst | `binwalk -e`, `checksec`, entropy scans | Claude 3.7 Sonnet (16k thinking) |
| [`threat-modeler`](agents/threat-modeler/) | STRIDE Threat Modeler & Architecture Auditor | `pytm`, STRIDE / DREAD threat trees | Claude 3.7 Sonnet (12k thinking) |
| [`compliance-auditor`](agents/compliance-auditor/) | SOC2 / ISO 27001 / HIPAA Compliance Auditor | `osqueryi`, CIS benchmark checklists | Claude 3.5 Sonnet (8k thinking) |
| [`ai-red-teamer`](agents/ai-red-teamer/) | AI Model Red-Teamer & Prompt Injection Auditor | `garak`, adversarial jailbreak fuzzers | Claude 3.7 Sonnet (16k thinking) |

### Guild 8: Data, Machine Learning & Code Hygiene
| Slug | Title | Primary Tools | Recommended Model |
|---|---|---|---|
| [`data-pipeline-eng`](agents/data-pipeline-eng/) | Data Pipeline, Spark & dbt Engineer | `dbt run --select`, `dbt test` | Claude 3.7 Sonnet (12k thinking) |
| [`vector-rag-spec`](agents/vector-rag-spec/) | Vector Database & Hybrid RAG Specialist | Qdrant / LanceDB client, ONNX embeddings | Claude 3.7 Sonnet (12k thinking) |
| [`mlops-serving-eng`](agents/mlops-serving-eng/) | Model Serving, Triton & vLLM MLOps Engineer | `triton`, `docker compose -f triton.yml` | Claude 3.7 Sonnet (12k thinking) |
| [`analytics-metrics-eng`](agents/analytics-metrics-eng/) | Product Analytics & Event Tracking Engineer | `duckdb`, event taxonomy validators | Claude 3.5 Sonnet (8k thinking) |
| [`synthetic-eval-benchmark-eng`](agents/synthetic-eval-benchmark-eng/) | Synthetic Data & LLM Eval Benchmark Engineer | `deepeval test run`, Ragas / deepeval | Claude 3.7 Sonnet (16k thinking) |
| [`ast-structural-refactorer`](agents/ast-structural-refactorer/) | AST Structural Search & Safe Refactorer | `@juvio15/pi-ast-grep` (6 native tools) | Claude 3.7 Sonnet (16k thinking) |
| [`linter-formatter-enforcer`](agents/linter-formatter-enforcer/) | Deterministic Multi-Language Linter Enforcer | `biome`, `ruff`, `cargo clippy`, `hooks.yaml` | Claude 3.5 Haiku (4k thinking) |
| [`dependency-hygiene-lockfile-surgeon`](agents/dependency-hygiene-lockfile-surgeon/) | Lockfile Deduplication & Supply-Chain Surgeon | `npm dedupe`, `cargo tree --duplicates` | Claude 3.7 Sonnet (12k thinking) |
| [`dependency-patcher`](agents/dependency-patcher/) | Upstream Library Patcher & `patch-package` Eng | `npx patch-package`, `git apply --check` | Claude 3.7 Sonnet (12k thinking) |
| [`lsp-type-graph-navigator`](agents/lsp-type-graph-navigator/) | Semantic LSP & Code Knowledge Graph Navigator | `pi-lsp-adapter`, `CodeGraphContext` | Claude 3.7 Sonnet (16k thinking) |
| [`adversarial-diff-auditor`](agents/adversarial-diff-auditor/) | Adversarial Diff Auditor & Codebase Watchdog | `git diff`, `pi-slopchop` watchdog review | Claude 3.7 Sonnet (16k thinking) |
| [`static-analysis-lead`](agents/static-analysis-lead/) | Code Style, Semgrep Rules & Static Analysis Lead | `semgrep --validate --config rules/` | Claude 3.7 Sonnet (12k thinking) |

---

## 5. Quick Start & Launcher Guide

### 5.1 Launching an Agent
Each specialist can be launched independently using its scoped launcher script. The launcher verifies the host environment, enforces local configuration bindings, and launches `pi` scoped to that agent's charter:

**On Windows PowerShell:**
```powershell
./agents/gui-visual-critic/launch.ps1
```

**On Linux / macOS Bash:**
```bash
./agents/gui-visual-critic/launch.sh
```

### 5.2 Deterministic Verification Suite
Run the automated verification suite to validate all 85 forensic audit reports, the alternatives register, and all 70 specialist configurations:

```bash
node scripts/verify_mission_completion.js
```

---

## 6. License

MIT License. All tools, scripts, and specialist configurations in this repository are open source and free for commercial and private use.
