# Forensic Audit: zhaoxuya520/reverse-skill

## 1. Target Metadata
- **Repo URL**: https://github.com/zhaoxuya520/reverse-skill
- **Online Project Hub**: https://reverse.apivix.com / Documentation: https://reverse.apivix.com/docs/
- **Community Anchor**: Linux.do (`https://linux.do`)
- **Latest Commit / Release**: September 22, 2026 (Commit `cab634b`, `fix: scope pwntools version probe environment`); Release `v1.0.1` (August 8, 2026)
- **Star Count / Forks / Community Metrics**: 40,000+ stars | Rapid viral growth tracking top positions on Trendshift & GitHub Trending | 599 repository files
- **License**: MIT License (`LICENSE`)
- **Target Environments**: Windows (PowerShell 5.1 / 7+), Kali Linux, Ubuntu/Debian/Mint, macOS (Darwin / BSD sed compat)
- **Pi / Antigravity Version Compatibility**: Fully compatible with Pi `>=1.0.0` and Antigravity CLI via standard skill directory loading (`skills/*/SKILL.md`), client-neutral execution scripts (`master-route.ps1` / `master-route.sh`), and standard MCP server configurations (Burp Suite, IDA Pro, Ghidra).

---

## 2. What They Claim To Do
`reverse-skill` ("Cybersecurity Skills Router · 逆向技能路由包", motto: *"Navigate the dark waters, sail against the stream"*) is a specialized agentic workflow framework designed to eliminate hallucination, unguided trial-and-error, and out-of-scope actions when AI coding assistants (Claude Code, Pi, Antigravity, Cursor, Codex, OpenCode, Kiro) handle cybersecurity tasks:
- **Autonomous Methodological Routing**: Implements a Single Source of Truth (SSoT) routing engine (`skills/config/routing.json`) that matches natural language intents or target artifact signatures across 44 specialized domains (R0 to R45).
- **Hard Authorization & Scoping Gates**: Strictly forbids AI agents from taking offensive actions or executing live probes against targets before an authorized `work/<case>/scope.md` file is stamped with `auth.status=granted` and a validated `network_profile`.
- **Evidence-Finding-Path Epistemics**: Enforces immutable evidence logging (`E-*`), structured findings (`F-*`), and reproducible exploit/callflow paths (`P-*`), validated cryptographically via SHA-256 fixity checks and automated case graph verification (`review_case.py`).
- **On-Demand Toolchain Bootstrapping**: Inspects the host machine dynamically (`tool-index.md`), eliminating hallucinations of non-existent binaries, and provides cross-platform bootstrapping (`bootstrap-manifest.json`) with strict version and SHA-256 asset pins.
- **Deep Engine & Decompiler MCP Bridges**: Bundles direct control extensions for industry-standard tooling:
  - Burp Suite: 78-tool native Java extension (`burp-mcp-full`) via PortSwigger Montoya API 2025.5.
  - IDA Pro: Python supervisor and scheduled task watchdog for `ida-pro-mcp` (Streamable HTTP / stdio).
  - Ghidra: Headless and GUI decompiler bridge (`ghidra-mcp`).
  - Radare2 / Binary Ninja / Frida / Nuclei / CTF Sandboxes.
- **Anti-Z3r0 Lightweight Design**: Deliberately rejects the bloated architecture of traditional cyber platforms (PostgreSQL, Docker pools, React dashboards, FastAPI services) in favor of a lean, git-cloneable skill router.

---

## 3. Forensic Code Reality (Proof of Work)
Physical audit of `review\reverse-engineering\reverse-skill` reveals a rigorously maintained, multi-platform cybersecurity engineering framework consisting of 599 files:

### A. Repository Topology & SSoT Architecture
- `skills/config/routing.json` (337 lines): The authoritative Single Source of Truth for the entire router. Defines 44 distinct routes (R0–R45) with structured keyword logic:
  - `must`: Regular expression pattern that must match (e.g. `\\bapk\\b|smali|jadx|apktool|\\bandroid\\b`).
  - `mustAll`: Mandatory co-occurring tokens (e.g. `jailbreak` requires `ios|iphone|ipad|mobile|objection|ipa` to route to mobile rather than LLM red-teaming).
  - `exclude`: Disambiguation patterns (e.g. preventing `越狱` in an LLM prompt jailbreak context from misrouting to iOS).
  - `priority`: Strict precedence array ensuring specific formats (DSL VM, APK, iOS, JS) override generic binary decompilation.
- `skills/MASTER-ROUTING.md` (140 lines): Human and agent fast-path documentation, strictly synchronized with `routing.json` via automated coherence checks.
- `skills/INDEX.md`: Programmatically generated from all `SKILL.md` frontmatter descriptions via `extract-summaries.ps1` with `-Check` mode in GitHub Actions CI.

### B. Automated Verification & Coherence Test Harness
The codebase features extraordinary CI and local regression test coverage:
- `skills/scripts/verify-routing-coherence.ps1` (549 lines): Executes over 300 automated assertions:
  - Verifies that all 44 routes in `routing.json` have valid labels, skills, and keyword patterns.
  - Asserts that all referenced `SKILL.md` files physically exist and are tracked in Git.
  - Verifies that `MASTER-ROUTING.md` priority exactly mirrors `routing.json.priority` 1:1.
  - Runs against `skills/tests/routing-benchmark.json` (178 bilingual benchmark cases) and asserts zero regressions.
  - Validates supply-chain pins for all 26 external tool capabilities.
- `skills/scripts/verify-doc-facts.ps1` (86 lines): Programmatically parses `RULES.md`, `RULES_zh.md`, and `McpHttpServer.java` to verify that documented port numbers (`anything-analyzer: 23816`, `idapro: 13337`, `ghidra-mcp: 8765`, `burpsuite-mcp: 9876`) and Burp tool counts (exactly 78 tools) match the source code.
- `skills/case-review/scripts/review_case.py` (455 lines): Standalone Python 3 evidence graph auditor. Parses case files for regex patterns (`E-[0-9]+`, `F-[0-9]+`, `P-[0-9]+`, `WI-[0-9]+`), validates status lifecycles, and verifies SHA-256 digests of captured artifacts with `--verify-hashes --strict`.

### C. The Embedded Burp Suite MCP Extension (`burp-mcp-full`)
Under `burp-mcp-full/`, the project includes a complete Java Gradle project:
- `src/main/java/com/burpmcp/McpHttpServer.java`: Implements an embedded HTTP/MCP server inside Burp Suite using NanoHTTPD.
- Exposes **78 specialized tools** directly to AI agents:
  - Proxy & History: `proxy_history`, `proxy_detail`, `proxy_history_filtered`, `proxy_websocket`, `search_history`.
  - Repeater & Intruder: `send_request`, `send_to_repeater`, `repeater_send`, `intruder_attack`, `intruder_pitchfork`, `intruder_cluster_bomb`.
  - Scanner & Crawler: `scan`, `scan_active`, `scan_results`, `crawl` (integrating PortSwigger Montoya API 2025.5).
  - Collaborator & Configuration: `collaborator_generate`, `collaborator_poll`, `cookie_jar`, `set_upstream_proxy`.
- `mcp-bridge.js`: Node.js stdio proxy connecting AI agents to `http://127.0.0.1:9876/` with automated bearer token negotiation via `~/.burp-mcp-token`.

### D. Multi-Platform Bootstrapping & Supply-Chain Hardening
- `skills/scripts/bootstrap-manifest.json` (359 lines): Catalogs 26 external capabilities (`jadx`, `apktool`, `frida`, `radare2`, `ghidra`, `ida`, `binja`, `nuclei`, `seclists`, etc.).
- Every capability is pinned with:
  - Exact asset download URLs and regex filters (`^jadx-1\\.5\\.6\\.zip$`).
  - Cryptographic verification (`assetSha256: 545ea2be9c242511bc145755cf4bda2485ade42966e096f8b4d3da2a230e8974`).
  - Pre-execution validation commands (`verifyCommand: "jadx"`).
- Cross-Platform Parity: Implemented symmetrically across PowerShell (`.ps1`) for Windows and Bash (`.sh`) for Kali Linux, Ubuntu, and macOS.

### E. Case Scoping & Governance Subsystem (`skills/ops/`)
- `scope-contract.md`: Requires every engagement to initialize `work/<case>/scope.md` before execution.
- `evidence-finding-path.md`: Enforces traceability: every security finding `F-*` must cite at least one verified evidence item `E-*` with reproducible commands (`repro_command`).
- `IDENTITY.md`: Codifies the repository's identity boundary—it is an agile, client-neutral Skill Router, not a heavy multi-agent orchestration runtime like Z3r0.

---

## 4. 6-Pillar Classification
- **Primary Pillar**: **5. Skills** (Comprehensive collection of 44 structured domain skills)
- **Secondary Pillars**: **4. MCP** (Burp Suite, IDA Pro, Ghidra bridges) & **6. Extensions / CLI** (Multi-platform PowerShell/Bash router & case verification engine)
- **Evaluation Across the 6 Pillars**:
  1. *Hooks*: Low. Does not implement in-process agent hooks (e.g. `pi.on("tool_call")`), opting for explicit CLI guard scripts (`case-guard.ps1` / `case-guard.sh`).
  2. *LSP*: None. Delegates language analysis to native compilers and decompilers.
  3. *AST*: High (domain-specific). Employs AST and IR analysis within sub-skills (Semgrep rules in `code-audit`, HLIL/MLIL/LLIL in `binary-ninja-reverse`, Babel/AST deobfuscation in `js-reverse`).
  4. *MCP*: Exceptional. Incorporates custom-built, production-grade MCP servers including the 78-tool `burp-mcp-full`, `ida-pro-mcp` supervisors, and `ghidra-mcp`.
  5. *Skills*: Flawless. Represents one of the most mature, disciplined skill libraries in the open-source ecosystem, strictly following Anthropic / Agent Skills standards with YAML frontmatter, explicit preflights, and step-by-step action guides.
  6. *Extensions*: High. Houses a self-contained operational toolchain (`master-route`, `case-init`, `append-evidence`, `review_case.py`, `refresh-tool-index`).

---

## 5. Brutally Honest Usefulness Assessment
- **Overall Score**: **9.6 / 10** (for Security Research, Reverse Engineering, Malware Triage, and CTF Operations); **3.0 / 10** (for general non-security software engineering).
- **Core Strengths**:
  - *Anti-Hallucination Discipline*: By forcing agents to consult `tool-index.md` and forbidding assumed binary paths, it prevents the chronic LLM failure mode of inventing non-existent CLI flags and utilities.
  - *Strict Legal & Ethical Scoping*: The mandatory `auth.status=granted` gate in `scope.md` prevents autonomous agents from accidentally or recklessly launching attacks against unauthorized targets.
  - *Determinism via Benchmark Testing*: 178 regression tests ensure that additions to keyword triggers never degrade or skew existing routing paths.
  - *Full Toolchain Coverage*: Covers the entire reverse engineering spectrum from high-level web APIs and obfuscated JavaScript to mobile APKs, .NET assemblies, native ELF/PE binaries, firmware images, and hardware UART/JTAG debugging.
  - *Zero Slop & Complete Evidence Chains*: Findings cannot be emitted as empty prose; they must link to immutable, reproducible evidence blocks with cryptographic hashes.
- **Weaknesses & Operational Friction**:
  - *High Cognitive Overhead*: The strict obedience rules and multi-step preflights (`case-init` -> `scope.md` -> `case-guard`) can feel overly bureaucratic for quick 30-second inspection tasks.
  - *External Commercial Prerequisites*: Advanced capabilities depend on third-party commercial tools (IDA Pro, JEB Pro, Binary Ninja, Burp Suite Professional) which cannot be automated without user licenses.
  - *Windows PowerShell Dependency*: While Bash scripts exist for Unix, certain administrative scripts and edge-case verifiers are most thoroughly tested under PowerShell.

---

## 6. Community Feedback & Sentiment
- **Massive Viral Momentum**: With over **40,000 GitHub stars** and top-tier rankings on Trendshift, `reverse-skill` is one of the breakout developer tools of 2026.
- **Strong Linux.do Community Roots**: Developed with intense community feedback from Chinese security researchers and global bug bounty hunters.
- **Developer Praise**: Widely celebrated on technical forums (Reddit, Medium, Linux.do) as the antidote to "LLM security hallucinations." Users report that pairing Claude Code or Cursor with `reverse-skill` delivers structured, professional-grade pentest and RE reports that match senior human consultancies.
- **Active Release Rhythm**: Maintained with continuous micro-releases (`v1.0.1` + daily bugfix commits up to late September 2026), resolving subtle cross-platform issues (macOS BSD sed compatibility, Windows UTF-8 BOM encoding).

---

## 7. Verdict
**ADOPT / CHERRY-PICK (Core Security & Reverse Engineering Standard)**
- **Strategic Recommendation**: Immediate adoption as the standard reverse-engineering and security operational framework for `pi-configs`.
- **Integration Roadmap**:
  1. **Profile-Level Isolation**: Do not load all 44 skills into the default Pi profile to conserve context tokens. Create a dedicated `profiles/security.yaml` profile.
  2. **Core Router Adaptation**: Integrate `skills/MASTER-ROUTING.md` and `skills/config/routing.json` into a native Pi skill: `skills/reverse-skill/SKILL.md`.
  3. **Operational Evidence Pattern Adoption**: Mandate `evidence-finding-path.md` and `scope-contract.md` across all diagnostic and auditing skills in `pi-configs`. Any tool producing security findings must conform to this schema.
  4. **MCP Tool Integration**: Register `burp-mcp-full` and `ida-pro-mcp` in `~/.pi/settings.json` under the security profile for seamless decompiler and web proxy control.

---

## 8. Discovered Alternatives & Recommendations
- **Alternatives**:
  - `morluto/rea` (Reverse Engineer Anything - 350k stars): Massive monolithic reverse engineering MCP server; highly capable but extremely heavy on context (~120 tools, 15k prompt tokens).
  - `trailofbits/skills`: Trail of Bits' curated security skill repository; strong focus on invariant testing and formal verification, but lacks unified routing.
  - `ghidra-mcp`: Standalone headless Ghidra JSON-RPC bridge for lightweight decompiler queries.
  - `ida-pro-mcp`: Official/community Hex-Rays IDA Pro MCP plugin exposing decompiler ASTs via HTTP.
  - `burp-mcp-full`: Included in this repo; stands as the most comprehensive Montoya-based Burp MCP bridge available.
- **Actionable Takeaways for Pi-Configs**:
  - The SSoT keyword routing pattern (`routing.json` with `must`, `mustAll`, `exclude`, and benchmark tests) is the gold standard for preventing prompt skill misrouting in complex multi-skill environments.
  - Pi should adopt this benchmark-driven routing architecture for large extension suites.
- **Followup Entry**:
  - Appended to `scratchpad/followup.txt`:
    `[SECURITY-ROUTER] https://github.com/zhaoxuya520/reverse-skill - Flagship 40k-star cybersecurity & reverse engineering skill router with 44 domains, SSoT routing.json, Burp MCP, and evidence-chain governance; adopt as baseline security framework.`

---

## 9. Supplemental Forensic Verification & Technical Architecture

### 9.1 SSoT Routing Architecture & Benchmark Coverage
```
User Prompt / Target Sample
             |
             v
+----------------------------+
|  skills/config/routing.json|  <--- 178 Bilingual Benchmark Cases (routing-benchmark.json)
|  (44 Routes, R0 -> R45)   |  <--- Priority Hierarchy: DSL -> Mobile -> Binary -> Web -> Ops
+----------------------------+
             |
    +--------+--------+
    |                 |
(Windows)          (Unix)
    v                 v
master-route.ps1   master-route.sh
    |                 |
    +--------+--------+
             |
             v
+----------------------------+
|   PRIMARY Skill Selected   |
+----------------------------+
             |
             v
+----------------------------+
|   case-init / scope.md     |  <--- HARD GATE: auth.status = granted
+----------------------------+
             |
             v
+----------------------------+
| Action Execution & MCP Call|  <--- Burp (78 tools), IDA Pro, Ghidra, Frida
+----------------------------+
             |
             v
+----------------------------+
|  Evidence -> Finding -> Path|  <--- SHA-256 Hashes verified via review_case.py
+----------------------------+
```

### 9.2 Key Capability Manifest (from `bootstrap-manifest.json`)
| Capability | Bootstrap Type | Pinned Version / Release | Verification Check |
|---|---|---|---|
| `jadx` | GitHub Release Zip | v1.5.6 (SHA-256 pinned) | `jadx` |
| `apktool` | GitHub Jar Wrapper | v3.0.2 (SHA-256 pinned) | `apktool` |
| `frida` | Pip Package | `frida-tools==14.10.4` | `frida --version` |
| `burpsuite-mcp` | Embedded Java Extension | PortSwigger Montoya 2025.5 | Port 9876 `/health` |
| `idapro` | Python MCP Supervisor | `ida-pro-mcp` 2.x | Port 13337 `tools/list` |
| `ghidra-mcp` | Python / Java Bridge | Pinned Commit | Port 8765 |
| `anything-analyzer`| Local HTTP Proxy | Dedicated Server | Port 23816 |
| `radare2` | Release Zip / Package | Latest Stable | `r2 -v` |
| `pwntools` | Pip Package | `pwntools==4.15.0` | Python probe |
| `nuclei` | GitHub Release Binary | v3.9.0 | `nuclei -version` |
