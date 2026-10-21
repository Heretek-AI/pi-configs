# Forensic Audit: Heretek-AI/Heretek-Crew

## 1. Target Metadata
- Repo URL / NPM URL: https://github.com/Heretek-AI/Heretek-Crew
- Latest Commit Date / Publish Date: 2026-10-19 (Commit `fe7fae8` - "ci(ocr): point review job at org reusable workflow (pinned)")
- Star Count / Forks / Issues: 0 stars / 0 forks / 2 issues
- License: Proprietary / Internal Enterprise Fleet Baseline (No open-source license declared)
- Pi Version Compatibility: Low direct runtime compatibility (built originally for `@opencode/cli@2.0.32` orchestrated by Paperclip `paperclipai/paperclip`); High conceptual and asset compatibility for migration to native Pi (`@earendil-works/pi-coding-agent`).

## 2. What They Claim To Do
Heretek-Crew specifies an enterprise autonomous agent fleet of 51 specialized roles:
- Orchestrated originally via Paperclip on top of OpenCode v2.
- Designed under the Principle of Least Privilege (PoLP): granular file, shell, and network permission policies per agent role.
- Divided into 9 functional departments:
  1. Executive & Product Governance (Roles 01-06)
  2. Game Development & Modding (Roles 07-12)
  3. Web & UI/UX Design (Roles 13-18)
  4. Language Engineers (Roles 19-26: Rust, Go, Python, C++, TS/Node, Java/Kotlin, Android, iOS)
  5. Cloud, Platform & SRE (Roles 27-32)
  6. Quality Assurance & Verification (Roles 33-38)
  7. Defensive Security, Binary Analysis & Forensics (Roles 39-44, 51)
  8. Data & AI Systems (Roles 45-48)
  9. Operations & Maintenance (Roles 49-50)
- Backed by an extensive Docker sidecar ecosystem providing headless browsers (Browserless), metasearch (SearXNG), reverse engineering (Ghidra, Radare2), database services (PostgreSQL 17, Redis, Neo4j, Qdrant), and LLM routing (LiteLLM/Bifrost).

## 3. Forensic Code Reality (Proof of Work)
Forensic inspection of the codebase, scripts, Docker configurations, and the adversarial audit report (`AUDIT_REPORT_FINDINGS.md`) reveals both profound architectural depth and severe integration friction:

### A. The 51 Roles Departmental Matrix (`roles-catalog/ROLE_CATALOG_50.md`)
Physical inspection of `roles/` verifies exactly 51 active role implementations across 9 core departments:

#### Department 1: Executive & Product Governance (Roles 01–06)
1. `exec-director` (Role 01): Director / CEO-Delegate. High-level OKRs, budget sign-offs, read-only repo mapping, system architecture approval.
2. `product-director` (Role 02): Head of Product. PRD authoring, user journey maps, feature prioritization, epic breakdown.
3. `tpm-scrum-lead` (Role 03): Technical Product Manager / Scrum Lead. Sprint ticket decomposition, Jira/GitHub milestone hygiene, definition of done (DoD) verification.
4. `system-architect` (Role 04): Enterprise System Architect. C4 architectural diagrams, ADR (Architecture Decision Record) authoring, interface contract enforcement.
5. `tech-docs-lead` (Role 05): Technical Documentation Lead. Docs-as-code curation, OpenAPI spec synchronization, markdown linter enforcement.
6. `ux-research-analyst` (Role 06): User Experience Research Analyst. Telemetry analysis via DuckDB, user journey friction audits, heuristic evaluations.

#### Department 2: Game Development & Modding (Roles 07–12)
7. `game-systems-dev` (Role 07): Gameplay & Engine Systems Programmer. Game loops, state machines, inventory/quest logic, headless unit test runs.
8. `graphics-shader-eng` (Role 08): Graphics & Shader Engineer. HLSL/GLSL/WGSL pipelines, SPIR-V validation, draw call batching, render target profiling.
9. `engine-systems-eng` (Role 09): Core Engine Programmer. Memory allocators, cache-conscious ECS (Entity Component System), frame budget benchmarking.
10. `game-ai-dev` (Role 10): Game AI Programmer. Behavior trees, utility AI, navmesh generation, dynamic avoidance systems.
11. `physics-sim-eng` (Role 11): Physics & Simulation Engineer. Rigid body dynamics, collision broadphase/narrowphase tuning, continuous collision detection (CCD).
12. `tech-artist-pipeline` (Role 12): Technical Artist & Asset Pipeline Lead. GLTF transform pipelines, texture compression (KTX2/Basis), asset baking validation.

#### Department 3: Web & UI/UX Design (Roles 13–18)
13. `ui-ux-designer` (Role 13): UI/UX Designer & Prototyper. Visual wireframes, responsive CSS layouts, Tailwind styling, accessibility foundations.
14. `design-system-eng` (Role 14): Design System Engineer. W3C DTCG design tokens, component library invariants, Storybook test runner validation.
15. `a11y-specialist` (Role 15): Accessibility Specialist. WCAG 2.2 AA audits, `axe-core` headless sweeps, ARIA attribute validation, keyboard navigation testing.
16. `fe-perf-eng` (Role 16): Frontend Performance Engineer. Core Web Vitals optimization, bundle tree-shaking, LCP/INP diagnostic tracing.
17. `mobile-web-eng` (Role 17): Mobile Web & Responsive Layout Engineer. Viewport boundary validation (320px–4k), touch-target hitboxes, PWA manifests.
18. `brand-copy-spec` (Role 18): Brand & Creative Copy Specialist. Microcopy consistency, internationalization (i18n) key catalogs, tone-of-voice compliance.

#### Department 4: Specialized Language Engineers (Roles 19–26)
19. `rust-systems-spec` (Role 19): Rust Systems Specialist. Memory safety, Tokio async runtimes, `cargo clippy -D warnings`, zero-copy deserialization.
20. `go-backend-eng` (Role 20): Go Backend Engineer. High-concurrency goroutine services, `go test -race`, interface decoupling, minimal allocations.
21. `python-backend-spec` (Role 21): Python Backend & Systems Specialist. FastAPI/AsyncIO microservices, strict `mypy --strict`, Ruff formatting, Pytest fixtures.
22. `ts-node-fullstack` (Role 22): TypeScript / Node Fullstack Engineer. Next.js React Server Components, tRPC APIs, strict type safety, Vitest coverage.
23. `cpp-lowlevel-eng` (Role 23): C++ Systems Engineer. C++20/23 modern paradigms, CMake/Ninja builds, ASan/UBSan sanitizers, cacheline alignment.
24. `java-kotlin-eng` (Role 24): Java & Kotlin Enterprise Specialist. Spring Boot 3 virtual threads, Gradle Kotlin DSL, JVM garbage collection tuning.
25. `ios-mobile-spec` (Role 25): iOS Mobile Specialist. SwiftUI declarative architectures, Swift 6 concurrency, SwiftLint, CoreData/SwiftData.
26. `android-mobile-spec` (Role 26): Android Mobile Specialist. Jetpack Compose, Kotlin coroutines, ADB instrumentation via `docker-android`.

#### Department 5: Cloud, Platform & Site Reliability (Roles 27–32)
27. `cloud-platform-eng` (Role 27): Cloud Platform Engineer. OpenTofu/Terraform IaC, AWS/GCP IAM least-privilege policies, drift detection.
28. `k8s-orchestrator` (Role 28): Kubernetes & Container Orchestrator. Helm chart hardening, Kubeconform schema validation, NetworkPolicy isolation.
29. `sre-incident-eng` (Role 29): Site Reliability Engineer. PromQL alerting rules, SLO/SLI error budget monitoring, automated post-mortem drafts.
30. `observability-eng` (Role 30): Observability & Telemetry Engineer. OpenTelemetry tracing pipelines, Grafana dashboards, structured logging formats.
31. `dba-specialist` (Role 31): Database Administrator. PostgreSQL query plan optimization (`EXPLAIN ANALYZE`), index tuning, zero-downtime migrations.
32. `cache-streaming-eng` (Role 32): Cache & Streaming Systems Engineer. Redis cluster partitioning, Apache Kafka consumer group lag management.

#### Department 6: Quality Assurance & Verification (Roles 33–38)
33. `e2e-browser-qa` (Role 33): End-to-End Browser Automation Engineer. Headless Playwright test suites, visual snapshot regressions, network trace analysis.
34. `api-contract-tester` (Role 34): API & Contract Testing Specialist. OpenAPI/Swagger schema conformance, Schemathesis fuzzing, mock verification.
35. `load-stress-tester` (Role 35): Load & Performance Stress Tester. k6 distributed load testing scenarios, latency percentiles under load, saturation points.
36. `sabotage-qa-tester` (Role 36): Adversarial Sabotage & Mutation Tester. Mutation testing (`cargo mutants`, Stryker), test suite resilience benchmarking.
37. `static-analysis-lead` (Role 37): Static Analysis & Code Hygiene Lead. Semgrep rule crafting, Biome linting, cyclomatic complexity thresholds.
38. `release-qa-officer` (Role 38): Release Acceptance & Sign-off Officer. Final verification sign-off, changelog generation, release gate enforcement.

#### Department 7: Defensive Security, Binary Analysis & Forensics (Roles 39–44, 51)
39. `appsec-engineer` (Role 39): Application Security Engineer. OWASP Top 10 mitigation, SAST/DAST report triaging, SQLi/SSRF/XSS prevention.
40. `cloud-sec-auditor` (Role 40): Cloud Security & IAM Auditor. CIS Benchmarks, cloud misconfigurations, IAM privilege escalation vector detection.
41. `binary-reverse-eng` (Role 41): Binary & Protocol Reverse Engineer. Ghidra decompiler scripting, Radare2 disassembly, custom network protocol decoding.
42. `firmware-sec-analyst` (Role 42): Firmware & Embedded Security Analyst. Binwalk extraction, entropy analysis, bare-metal binary inspection.
43. `threat-modeler` (Role 43): Threat Modeling & Architecture Hardening. STRIDE threat matrices, attack tree drafting, mitigation mapping.
44. `compliance-auditor` (Role 44): Compliance & License Auditor. SPDX software bill of materials (SBOM), license compatibility, GDPR/SOC2 checklists.
51. `ai-red-teamer` (Role 51): Adversarial AI Red-Teamer. Prompt injection defense testing, jailbreak resilience auditing, tool hallucination probing.

#### Department 8: Data & AI Systems (Roles 45–48)
45. `data-pipeline-eng` (Role 45): Data Pipeline & ETL Engineer. DuckDB analytical transformations, Arrow zero-copy memory arrays, Parquet partitions.
46. `vector-rag-spec` (Role 46): Vector Search & RAG Specialist. Qdrant vector index optimization, hybrid BM25 + dense embedding reranking.
47. `mlops-serving-eng` (Role 47): MLOps & Model Serving Engineer. LiteLLM/vLLM inference routing, token rate-limiting, latency benchmarking.
48. `analytics-metrics-eng` (Role 48): Analytics & Metrics Engineer. SQL metric definitions, funnel retention models, dbt transformation modeling.

#### Department 9: Operations & Maintenance (Roles 49–50)
49. `dependency-patcher` (Role 49): Dependency & CVE Patching Steward. Automated lockfile updating, semver breaking change detection, security advisories.
50. `git-drift-coord` (Role 50): Git & Worktree Drift Coordinator. Multi-agent git worktree isolation, merge conflict resolution, rebase synchronization.

---

### B. Docker Sidecars Inventory (`docker-compose.sidecars.yml`)
The repository specifies 26 dedicated container services across multiple functional profiles:
1. `searxng-redis`: Redis 7.4.11-alpine caching engine for metasearch results.
2. `searxng`: Privacy-focused metasearch engine exposing JSON search API (`searxng/searxng@sha256:...`).
3. `firecrawl-redis`: BullMQ persistent queue backing Firecrawl workers.
4. `firecrawl-rabbitmq`: RabbitMQ 4.3.6 message broker with quorum queues.
5. `firecrawl-nuq-postgres`: PostgreSQL database for crawl jobs and document states.
6. `firecrawl-playwright`: Headless browser cluster executing JS rendering for crawlers.
7. `firecrawl`: Core web crawling and markdown extraction microservice.
8. `gotenberg`: Document conversion engine (HTML/Markdown to PDF).
9. `browserless`: Headless Chrome automation cluster with stealth flags.
10. `mitmproxy`: HTTP/HTTPS traffic interceptor and replay proxy for API diagnostics.
11. `ghidra`: Headless NSA Ghidra decompiler container exposing REST/RPC endpoints.
12. `radare2`: Binary analysis and disassembly CLI daemon.
13. `hound`: Source code regex indexing and search service.
14. `semgrep`: Semgrep static analysis engine container.
15. `docker-socket-proxy`: Tecnativa read-only Docker socket proxy restricting API access.
16. `piston`: Multi-language sandboxed code execution engine.
17. `qdrant`: Qdrant vector database engine for RAG embedding search.
18. `neo4j`: Property graph database modeling codebase dependencies and call graphs.
19. `litellm`: Multi-provider LLM load balancer, fallback router, and budget limiter.
20. `mailpit`: Local SMTP email testing server with web UI.
21. `minio`: S3-compatible local object storage server.
22. `wiremock`: HTTP mock server for stubbing 3rd-party web APIs.
23. `jaeger`: Distributed tracing collector and visualization UI.
24. `docker-android`: Containerized Android emulator with ADB server.
25. `local-ci-runner`: Sandboxed runner executing build scripts and test suites.
26. `paperclip`: Node.js daemon orchestrating agent runtimes and worktree dispatches.

---

### C. Migration Blueprint: Moving from OpenCode / Paperclip to Native Pi

#### 1. Migrating `opencode.json` Permission Models to Pi Hooks
In OpenCode, roles enforced least privilege via JSON permission declarations. In native Pi (`@earendil-works/pi-coding-agent`), this model is superseded by declarative YAML tool guards and TypeScript hook interceptors:

```json
// Original: roles/rust-systems-spec/opencode/opencode.json
{
  "permissions": [
    { "action": "fs:read", "resource": ".env", "effect": "deny" },
    { "action": "fs:read", "resource": "**/secrets/**", "effect": "deny" },
    { "action": "fs:write", "resource": "crates/**", "effect": "allow" },
    { "action": "fs:write", "resource": "src/**", "effect": "allow" },
    { "action": "fs:write", "resource": "*", "effect": "deny" },
    { "action": "shell", "resource": "cargo build*", "effect": "allow" },
    { "action": "shell", "resource": "*", "effect": "deny" }
  ]
}
```

```yaml
# Native Pi: .pi/hooks/guardrails.yaml (via Pi-YAML-Hooks)
guards:
  - name: protect-secrets
    on: tool_call
    match_tool: ["read_file", "edit_file", "write_file"]
    condition: "path matches '(\\.(env|pem)$|secrets/|id_rsa)'"
    action: deny
    message: "Access to credentials and secret files is strictly prohibited under Least Privilege."

  - name: restrict-rust-writes
    on: tool_call
    match_tool: ["edit_file", "write_file"]
    condition: "path not_matches '^(crates/|src/|tests/|Cargo\\.(toml|lock))'"
    action: deny
    message: "Rust Systems Specialist is restricted to Rust crate and manifest source files."

  - name: sandbox-shell-execution
    on: tool_call
    match_tool: ["run_command"]
    condition: "command not_matches '^(cargo (build|test|clippy|check|audit)|git (status|diff))'"
    action: deny
    message: "Unauthorized shell execution. Only vetted cargo build and git commands permitted."
```

#### 2. Migrating Monolithic Docker Sidecars to Modular Native Pi Architecture
Running 26 Docker sidecars locally consumes over 16GB of RAM and introduces fragile network dependencies. Pi eliminates this overhead:
- **SearXNG / Web Search**: Replaced by lightweight MCP servers or native browser tools without needing local Redis/SearXNG containers.
- **Docker Socket Proxy / Piston**: Replaced by native OS process execution bounded by Pi hooks.
- **Qdrant / Neo4j**: Replaced by embedded zero-dependency graph databases (e.g., Kùzu, DuckDB, or SQLite).
- **Ghidra / Binary Reverse Engineering**: Kept as an optional on-demand MCP endpoint (`LaurieWired/GhidraMCP`) launched only when binary reverse engineering tasks are dispatched.
- **Paperclip Daemon & CLI Shims**: Replaced natively by `pi-agents-team` and Pi subagents, communicating over zero-latency local IPC rather than fragile bash wrappers (`opencode-shim.sh`).

## 4. 6-Pillar Classification
- **1. Hooks**: Core Pillar. Heretek-Crew's least privilege model maps directly to Pi PreToolExecution and PostToolExecution hooks.
- **4. MCP**: Core Pillar. Standardizes 51 roles with specialized tool servers.
- **5. Skills**: Core Pillar. Includes over 100 domain-specific operational skill markdown files.
- **6. Extensions**: Heavy Custom Architecture. Orchestration is modernized by replacing Paperclip with native Pi extension teams.

## 5. Brutally Honest Usefulness Assessment
- **Score**: 8.5/10 (Architectural Goldmine; Runtime Must Be Modernized)
- **Technical Critique**:
  - The 51 role specifications, prompt engineering boundaries, and tool whitelist designs are industry-leading benchmarks for multi-agent enterprise engineering.
  - The legacy runtime reliance on Paperclip, bash shims, and a monolithic 26-container Docker Compose cluster is completely unviable for local developer agility.
  - Porting the role charters and least-privilege policies to native Pi yields a blazingly fast, lightweight agent fleet operating without Docker daemon overhead.

## 6. Community Feedback & Sentiment
- Evaluated against production commit history and the internal adversarial fleet audit report (`AUDIT_REPORT_FINDINGS.md`).
- Confirmed that Paperclip v2 argument mismatches and broken docker image tags (P0-1, P0-2) were resolved during fleet remediation waves.

## 7. Verdict
**MIGRATE TO NATIVE PI (TOP PRIORITY REFERENCE)**
- **Justification**: Heretek-Crew provides the definitive catalog of 51 least-privilege agent roles. By ditching Paperclip and monolithic Docker Compose in favor of native Pi profiles, YAML hooks, and on-demand MCP servers, we obtain an enterprise-grade agent fleet without runtime friction.

## 8. Discovered Alternatives & Recommendations
- **Orchestration**: Use **Pi Agents Team** (`KristjanPikhof/Pi-Agents-Team`) for native subagent team management.
- **Permission Enforcement**: Use **Pi-YAML-Hooks** (`KristjanPikhof/Pi-YAML-Hooks`) to implement declarative least-privilege security guards.
- **Code Graphing**: Use **Repowise** or **CodeGraphContext** as zero-Docker local alternatives to Neo4j sidecars.
- **Followup Entry**:
  - Append to `scratchpad/followup.txt`:
    `[FLEET-BASELINE] https://github.com/Heretek-AI/Heretek-Crew - 51 least-privilege enterprise agent roles across 9 departments; migrate charters and security policies to native Pi.`
