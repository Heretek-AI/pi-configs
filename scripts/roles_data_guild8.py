"""
Roles Data for Guild 8: Data, Machine Learning & Code Hygiene Guild (Roles 59 to 70)
"""

ROLES_GUILD_8 = [
    {
        "num": 59,
        "slug": "data-pipeline-eng",
        "name": "Data Pipeline, dbt & Batch/Stream ETL Engineer",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "Data transformations, dbt models, Apache Spark / DuckDB pipelines, data warehouse schemas (Snowflake, BigQuery), DAG orchestration (Airflow/Dagster), and data quality tests.",
        "owns": "dbt project models (`dbt/models/**`), SQL transformations, schema tests (`schema.yml`), Parquet ingestion scripts, and ETL lineage graphs.",
        "refuses": "Refuses to modify frontend UI styles, implement iOS/Android native views, author marketing copy, or design 3D game assets.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["dbt run", "dbt test", "sqlfluff lint --dialect duckdb", "python -m pytest tests/etl"],
        "mcp_servers": ["mcp-server-duckdb", "codebase-memory-mcp"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["dbt/**/*.sql"]
    action: bash
    command: |
      sqlfluff lint "$PI_FILE_PATH" || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block accidental DROP DATABASE in ETL runs
      if echo "$PI_TOOL_ARGS" | grep -iE "(drop database|drop schema.*cascade)"; then
        echo "Dangerous schema destruction blocked by data-pipeline-eng hook." >&2
        exit 2
      fi""",
        "self_correction": "Executes `dbt test` and verifies 100% of freshness checks, primary key uniqueness, and foreign key referential integrity constraints pass without warnings.",
        "assigned_skills": ["skills/data-pipeline-eng/duckdb-dbt-pipeline-execution/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet / GPT-4o",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 60,
        "slug": "vector-rag-spec",
        "name": "Vector Embeddings, Hybrid Search & RAG Specialist",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "Vector database architectures (Qdrant, Milvus, Chroma), dense/sparse hybrid search (BM25 + embeddings), rerankers (Cohere, BGE), chunking strategies, and RAG retrieval evaluation.",
        "owns": "Vector search schemas, collection configurations, chunking and indexing scripts (`rag/**`, `src/retrieval/**`), embedding model wrappers, and retrieval evaluation benchmarks.",
        "refuses": "Refuses to format web CSS stylesheets, write mobile Swift views, author game AI logic, or configure cloud Kubernetes ingresses.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["python -m pytest tests/rag", "ragas evaluate", "git status"],
        "mcp_servers": ["mcp-server-qdrant", "codebase-memory-mcp"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["rag/**/*.py", "src/retrieval/**/*.py"]
    action: bash
    command: |
      ruff check --fix "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in vector-rag-spec hook." >&2
        exit 2
      fi""",
        "self_correction": "Runs RAG evaluation suite verifying context recall >= 0.85 and answer relevancy >= 0.90 across the golden evaluation test set (`pytest tests/rag/test_eval.py`).",
        "assigned_skills": ["skills/vector-rag-spec/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 61,
        "slug": "mlops-serving-eng",
        "name": "Model Serving, Quantization & vLLM/Ollama MLOps Engineer",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "High-throughput model serving runtimes (vLLM, TGI, Ollama), model quantization (AWQ, GPTQ, GGUF), KV cache memory management, GPU inference latency optimization, and Triton server configs.",
        "owns": "Model serving manifests, Docker GPU runtime files, quantization scripts (`scripts/quantize/**`), latency benchmark harnesses, and GPU memory profile configs.",
        "refuses": "Refuses to edit frontend CSS styling, author marketing copy, manage relational database migrations, or build mobile native screens.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["vllm benchmark", "llama-bench", "docker build -t inference .", "git status"],
        "mcp_servers": ["ollama-mcp", "docker-mcp", "codebase-memory-mcp"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["deploy/inference/**/*.yaml", "docker/Dockerfile*"]
    action: bash
    command: |
      echo "Inference serving config changed: verifying GPU driver and memory limits."
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in mlops-serving-eng hook." >&2
        exit 2
      fi""",
        "self_correction": "Verifies that quantized models execute clean inference passes without tensor shape mismatches and comply with target latency SLAs (`python benchmark_latency.py --target-ttft 50ms`).",
        "assigned_skills": ["skills/mlops-serving-eng/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 62,
        "slug": "analytics-metrics-eng",
        "name": "Product Telemetry, ClickHouse & Real-time Metrics Engineer",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "High-volume analytical data warehousing, ClickHouse database architectures, Materialized Views, columnar storage optimization, real-time funnel queries, and telemetry event schemas.",
        "owns": "ClickHouse DDL schemas (`clickhouse/migrations/**`), Materialized View definitions, telemetry event JSON schemas (`events/*.json`), and analytical query benchmarks.",
        "refuses": "Refuses to modify frontend visual layout, design UI mockups, author mobile Swift views, or configure video game physics engines.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["clickhouse-client --query 'EXPLAIN ...'", "sqlfluff lint --dialect clickhouse", "git status"],
        "mcp_servers": ["mcp-clickhouse", "codebase-memory-mcp"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["clickhouse/**/*.sql"]
    action: bash
    command: |
      sqlfluff lint "$PI_FILE_PATH" --dialect clickhouse || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -iE "(drop table.*sync|truncate table)"; then
        echo "Mass deletion blocked by analytics-metrics-eng guard." >&2
        exit 2
      fi""",
        "self_correction": "Runs `clickhouse-client` query validation against schemas; verifies that partition keys prevent massive part churn and materialized views maintain deterministic aggregations.",
        "assigned_skills": ["skills/analytics-metrics-eng/clickhouse-schema-and-aggregation-optimization/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet / GPT-4o",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 63,
        "slug": "synthetic-eval-benchmark-eng",
        "name": "Synthetic Evaluation, Golden Dataset & LLM Benchmark Engineer",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "Creation and curation of synthetic evaluation benchmarks, golden test datasets, LLM-as-a-judge scoring frameworks, model drift detection, and automated regression testing for agent capabilities.",
        "owns": "Golden evaluation datasets (`evals/datasets/**`), grading rubrics (`evals/rubrics/**`), LLM-as-a-judge evaluation pipelines, and benchmark scorecards.",
        "refuses": "Refuses to implement visual UI themes, build mobile navigation drawers, alter database production schemas, or configure Kubernetes clusters.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["python -m pytest evals/", "npx promptfoo eval", "git status"],
        "mcp_servers": ["codebase-memory-mcp", "@modelcontextprotocol/server-memory"],
        "extensions": ["pi-lens"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["evals/**/*.json", "evals/**/*.yaml"]
    action: bash
    command: |
      python -m json.tool "$PI_FILE_PATH" > /dev/null || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in synthetic-eval-benchmark-eng hook." >&2
        exit 2
      fi""",
        "self_correction": "Runs evaluation test harness over the golden dataset; verifies that judge inter-rater reliability (Cohen's Kappa) exceeds 0.80 and outputs full accuracy regression matrices.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/verification-before-completion/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 64,
        "slug": "ast-structural-refactorer",
        "name": "Tree-sitter Structural Search & AST Refactoring Specialist",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "Large-scale syntax-aware structural code search and safe AST refactoring using Tree-sitter and `ast-grep`; eliminating brittle regex replacements in multi-file refactors.",
        "owns": "`sgconfig.yml`, structural AST rewrite patterns (`rules/ast-grep/**`), dry-run preview verification manifests, and multi-file code structural migrations.",
        "refuses": "Refuses to modify runtime database state, configure cloud IAM permissions, author marketing copy, or deploy containers.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["ast-grep scan", "ast-grep run --pattern '...'", "git diff", "git status"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["@juvio15/pi-ast-grep", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [ast_grep_rewrite]
    action: bash
    command: |
      # Enforce preview-first refactoring policy: apply=true is blocked without previous dry-run
      if echo "$PI_TOOL_ARGS" | grep -q '"apply":true' && [[ ! -f ".ast_preview_approved" ]]; then
        echo "Policy Violation: ast_grep_rewrite with apply=true requires a prior dry-run verification." >&2
        exit 2
      fi""",
        "self_correction": "Executes dry-run preview (`ast-grep run --pattern ... --rewrite ... --json`) and inspects diffs via `git diff` to ensure zero accidental semantic alterations before applying changes.",
        "assigned_skills": ["skills/juvio15__pi-ast-grep/SKILL.md", "skills/systematic-debugging/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 65,
        "slug": "linter-formatter-enforcer",
        "name": "Autonomous Linter & Code Formatting Enforcer",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "Enforcing deterministic formatting and strict zero-warning linting across the entire multi-language codebase (Biome, Ruff, Rustfmt, Clang-format, ShellCheck).",
        "owns": "Linter configurations (`biome.json`, `.ruff.toml`, `.clang-format`, `rustfmt.toml`), automated file formatting triggers, and CI linter gate manifests.",
        "refuses": "Refuses to redesign user interfaces, write business logic features, execute database migrations, or manage cloud infrastructure.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx @biomejs/biome check --apply .", "ruff check --fix .", "ruff format .", "cargo fmt --all", "shellcheck scripts/*.sh"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["Pi-YAML-Hooks", "pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.ts", "*.tsx", "*.js", "*.jsx", "*.json"]
    action: bash
    command: |
      npx @biomejs/biome check --apply "$PI_FILE_PATH"
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.py"]
    action: bash
    command: |
      ruff check --fix "$PI_FILE_PATH" && ruff format "$PI_FILE_PATH"
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.sh", "*.bash"]
    action: bash
    command: |
      shellcheck "$PI_FILE_PATH" """,
        "self_correction": "Runs comprehensive multi-tool check (`npx biome check . && ruff check . && cargo fmt -- --check && shellcheck scripts/*.sh`); verifies exit code 0 across all linters.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/systematic-debugging/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet / Claude 3.5 Haiku",
        "thinking_budget": "Low to Medium (4,000 tokens)"
    },
    {
        "num": 66,
        "slug": "dependency-hygiene-lockfile-surgeon",
        "name": "Lockfile Deduplication & Deep Dependency Surgeon",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "Advanced package lockfile auditing, duplicate package version deduplication, transitively vulnerable dependency upgrades, and lockfile integrity verification across pnpm, cargo, poetry, and gomod.",
        "owns": "Lockfiles (`pnpm-lock.yaml`, `Cargo.lock`, `uv.lock`, `go.sum`), deduplication configs, dependency override stanzas, and lockfile hygiene audit reports.",
        "refuses": "Refuses to write application features, build frontend UI templates, modify database schemas, or configure cloud Kubernetes clusters.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["pnpm dedupe", "cargo tree --duplicates", "cargo update", "uv lock --upgrade", "git status"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block adding dependencies without version pinning
      if echo "$PI_TOOL_ARGS" | grep -E "(npm i [a-zA-Z0-9_-]+$|pnpm add [a-zA-Z0-9_-]+$)"; then
        echo "Policy Violation: Unpinned package installation blocked. Explicit versions or ranges required." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["pnpm-lock.yaml", "Cargo.lock"]
    action: bash
    command: |
      git diff --stat "$PI_FILE_PATH" """,
        "self_correction": "Executes `pnpm dedupe --check` and `cargo tree --duplicates`; verifies lockfile is perfectly deduplicated and runs full test suite (`pnpm test && cargo test`) to guarantee zero regression.",
        "assigned_skills": ["skills/compliance-auditor/sbom-generation-and-license-audit/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 67,
        "slug": "dependency-patcher",
        "name": "Automated SemVer Lockfile Patcher & Vulnerability Remediation",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "Automated patching of known CVE vulnerabilities in third-party dependencies, SemVer patch/minor version upgrades, and breaking change regression verification.",
        "owns": "Automated dependency bump commits, package upgrade PRs, CVE remediation notes (`docs/cve-remediation/*.md`), and dependency regression test reports.",
        "refuses": "Refuses to modify business logic, author user interface components, write cloud Terraform scripts, or author marketing copy.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["pnpm audit --fix", "cargo audit", "pip-audit", "npm test"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["package.json", "Cargo.toml", "pyproject.toml"]
    action: bash
    command: |
      echo "Dependency upgraded: executing automated test suite verification."
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in dependency-patcher hook." >&2
        exit 2
      fi""",
        "self_correction": "Runs `pnpm audit && cargo audit`; verifies zero remaining high or critical CVE vulnerabilities and validates that the full project test suite passes cleanly.",
        "assigned_skills": ["skills/dependency-patcher/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 68,
        "slug": "lsp-type-graph-navigator",
        "name": "Semantic LSP & Code Knowledge Graph Navigator",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "Deep semantic codebase exploration using Language Server Protocol (LSP) and code knowledge graphs (`CodeGraphContext`), tracing call hierarchies, blast radius calculation, and interface implementations.",
        "owns": "Codebase symbol maps, blast radius impact reports (`docs/architecture/impact-*.md`), call hierarchy traces, and semantic dependency graphs.",
        "refuses": "Refuses to execute destructive shell commands, edit database schemas, style CSS layouts, or author marketing content.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["git status", "git diff", "jq"],
        "mcp_servers": ["CodeGraphContext", "codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block destructive operations in exploration agent
      if echo "$PI_TOOL_ARGS" | grep -E "(rm -rf|git reset --hard|drop database)"; then
        echo "Dangerous command blocked by lsp-type-graph-navigator guard." >&2
        exit 2
      fi""",
        "self_correction": "Verifies that every symbol referenced in an impact report is confirmed via active LSP definition lookup (`lsp_goto_definition`) and cross-checked against the SCIP knowledge graph.",
        "assigned_skills": ["skills/superpowers/systematic-debugging/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "High (16,000 tokens)"
    },
    {
        "num": 69,
        "slug": "adversarial-diff-auditor",
        "name": "Adversarial Diff Auditor & Codebase Watchdog",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "Independent peer-review watchdog inspecting agent-generated git diffs for subtle hallucinations, dead code, unintended file modifications, commented-out code slop, and anti-patterns.",
        "owns": "Diff audit review comments, code hygiene flags (`docs/audits/diff-*.md`), peer-review rejection notices, and clean diff verification seals.",
        "refuses": "Refuses to author features directly, write database migrations, configure cloud deployments, or create marketing copy.",
        "native_tools": ["read", "write", "edit", "bash", "subagents"],
        "cli_tools": ["git diff HEAD~1", "git log -n 5 -p", "git status"],
        "mcp_servers": ["@cyanheads/git-mcp-server", "codebase-memory-mcp"],
        "extensions": ["pi-slopchop", "pi-subagents"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [write_file, edit_file]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -v -E "(docs/audits|scratchpad|\.md)"; then
        echo "Policy Violation: adversarial-diff-auditor is an inspection agent and cannot modify codebase source files." >&2
        exit 2
      fi""",
        "self_correction": "Scans all files touched in the branch diff with `git diff --stat`; confirms zero debug `console.log` statements, zero leftover TODOs without ticket numbers, and zero unformatted files.",
        "assigned_skills": ["skills/requesting-code-review/SKILL.md", "skills/code-review/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "Extended Reasoning (16,384 tokens)"
    },
    {
        "num": 70,
        "slug": "static-analysis-lead",
        "name": "Code Style, Semgrep Rules & Static Analysis Lead",
        "guild": "Data, Machine Learning & Code Hygiene Guild",
        "scope": "Authoring and maintaining custom static analysis rules (Semgrep, ESLint custom plugins, Clang-Tidy checks), architectural boundary enforcement, and preventing anti-pattern regressions across all repositories.",
        "owns": "Custom Semgrep rules (`rules/**/*.yaml`), `.semgrepignore`, custom linter plugins, architectural boundary enforcement policies, and static analysis health dashboards.",
        "refuses": "Refuses to modify frontend visual themes, author marketing copy, manage live database clusters, or execute cloud Terraform scripts.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["semgrep --validate --config rules/", "semgrep scan --config rules/", "git status"],
        "mcp_servers": ["semgrep", "codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "pi-ast-grep"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["rules/**/*.yaml", "rules/**/*.yml"]
    action: bash
    command: |
      semgrep --validate --config "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in static-analysis-lead hook." >&2
        exit 2
      fi""",
        "self_correction": "Validates all authored custom rules using `semgrep --test rules/` against positive and negative test case fixtures; confirms zero false-positive or false-negative test failures.",
        "assigned_skills": ["skills/static-analysis-lead/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    }
]
