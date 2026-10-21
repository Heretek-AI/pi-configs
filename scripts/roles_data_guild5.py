"""
Roles Data for Guild 5: Architecture, Cloud & Infrastructure Guild (Roles 40 to 46)
"""

ROLES_GUILD_5 = [
    {
        "num": 40,
        "slug": "cloud-platform-eng",
        "name": "Cloud Platform & OpenTofu / Infrastructure-as-Code Engineer",
        "guild": "Architecture, Cloud & Infrastructure Guild",
        "scope": "Infrastructure as Code (IaC) engineering, OpenTofu / Terraform modules, AWS / GCP / Azure resource topology, state locking, drift detection, and secure provider configuration.",
        "owns": "IaC configurations (`terraform/**`, `tofu/**`), module definitions, variable specifications (`variables.tf`), backend state manifests, and provider version pins.",
        "refuses": "Refuses to write frontend React components, author mobile app layouts, write SQL application queries, or design gameplay physics systems.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["tofu fmt -check", "tofu validate", "tflint", "checkov -d terraform/"],
        "mcp_servers": ["aws-mcp", "codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.tf", "*.tofu"]
    action: bash
    command: |
      tofu fmt "$PI_FILE_PATH" && tflint "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block auto-applying terraform changes without plan review
      if echo "$PI_TOOL_ARGS" | grep -E "(tofu apply -auto-approve|terraform apply -auto-approve|terraform destroy)"; then
        echo "Safety Violation: Auto-approved apply/destroy is strictly forbidden in local agent runs." >&2
        exit 2
      fi""",
        "self_correction": "Runs `tofu validate && tflint && checkov -d .` to guarantee zero configuration syntax errors, zero deprecations, and zero critical security policy violations.",
        "assigned_skills": ["skills/cloud-platform-eng/opentofu-plan-and-validation/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 41,
        "slug": "k8s-orchestrator",
        "name": "Kubernetes Platform & Helm Orchestrator",
        "guild": "Architecture, Cloud & Infrastructure Guild",
        "scope": "Container orchestration, Kubernetes manifests (Deployments, StatefulSets, Ingress, NetworkPolicies), Helm chart authoring, resource limits, and service mesh topology.",
        "owns": "Kubernetes YAML manifests (`k8s/**`), Helm charts (`charts/**`), `values.yaml`, HPA scaling policies, and pod disruption budgets.",
        "refuses": "Refuses to edit backend application code logic, style web user interfaces, write low-level C++ drivers, or author marketing copywriting.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["kubeconform -strict", "helm lint", "helm template", "git diff"],
        "mcp_servers": ["mcp-server-kubernetes", "docker-mcp", "codebase-memory-mcp"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["k8s/**/*.yaml", "charts/**/*.yaml"]
    action: bash
    command: |
      kubeconform -strict "$PI_FILE_PATH" || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(kubectl delete namespace|kubectl delete all)"; then
        echo "Dangerous mass deletion blocked by k8s-orchestrator hook." >&2
        exit 2
      fi""",
        "self_correction": "Validates all charts using `helm lint charts/*` and dry-runs manifest generation with `helm template test charts/* | kubeconform -strict -summary`.",
        "assigned_skills": ["skills/wshobson__agents/kubernetes-manifests/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet / GPT-4o",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 42,
        "slug": "dba-specialist",
        "name": "Database Administrator & SQL Performance Engineer",
        "guild": "Architecture, Cloud & Infrastructure Guild",
        "scope": "Relational database schema architecture, zero-downtime migration scripts, index optimization (B-tree, GIN, BRIN), query execution plan analysis (`EXPLAIN ANALYZE`), and connection pooling.",
        "owns": "Database migrations (`migrations/**`, `prisma/migrations/**`), schema definitions (`schema.sql`), index definitions, table partition policies, and SQL performance benchmarks.",
        "refuses": "Refuses to write React TSX components, style HTML with CSS, author mobile SwiftUI views, or manage cloud DNS records.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["sqlfluff lint", "pg_format", "psql -c 'EXPLAIN ...'", "prisma validate"],
        "mcp_servers": ["@modelcontextprotocol/server-postgres", "codebase-memory-mcp"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["migrations/**/*.sql", "prisma/schema.prisma"]
    action: bash
    command: |
      sqlfluff lint "$PI_FILE_PATH" --dialect postgres || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block destructive DROP TABLE / DATABASE commands in migrations without backward compatibility
      if echo "$PI_TOOL_ARGS" | grep -iE "(drop database|truncate table|drop table cascade)"; then
        echo "Dangerous SQL operation blocked by dba-specialist guard." >&2
        exit 2
      fi""",
        "self_correction": "Executes `sqlfluff lint --dialect postgres migrations/` and verifies that every migration contains backward-compatible down migrations and zero lock-inducing table rewrites.",
        "assigned_skills": ["skills/dba-specialist/zero-downtime-migration-audit/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 43,
        "slug": "cache-streaming-eng",
        "name": "Distributed Cache & Event Streaming Engineer",
        "guild": "Architecture, Cloud & Infrastructure Guild",
        "scope": "In-memory caching architectures (Redis, Dragonfly, Memcached), event streaming and pub/sub message brokers (Apache Kafka, RabbitMQ, Redpanda), dead-letter queues (DLQ), and partition key strategies.",
        "owns": "Redis key schemas, TTL cache eviction policies, Kafka topic configs, consumer group offset handlers, streaming serialization schemas (Avro/Protobuf), and cache-stampede mitigation logic.",
        "refuses": "Refuses to edit frontend CSS styling, create user interface components, write mobile Swift views, or author marketing copy.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["redis-cli ping", "kcat -L", "cargo test streaming", "pytest tests/streaming"],
        "mcp_servers": ["mcp-server-redis", "kafka-mcp-server", "codebase-memory-mcp"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["config/kafka/**", "config/redis/**"]
    action: bash
    command: |
      echo "Cache/streaming configuration updated: verifying schema compatibility."
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(redis-cli flushall|redis-cli flushdb)"; then
        echo "Dangerous mass cache flush blocked by cache-streaming-eng hook." >&2
        exit 2
      fi""",
        "self_correction": "Verifies Kafka topic partition counts, retention windows, and consumer group error handling via integration test suites (`npm test -- --grep 'cache|streaming'`).",
        "assigned_skills": ["skills/cache-streaming-eng/kafka-topic-and-consumer-tuning/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet / GPT-4o",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 44,
        "slug": "sre-incident-eng",
        "name": "Site Reliability Engineer & Incident Commander",
        "guild": "Architecture, Cloud & Infrastructure Guild",
        "scope": "Site reliability engineering, SLO/SLI definition, automated runbooks, error budgeting, incident triage, disaster recovery plans, and root-cause post-mortem generation.",
        "owns": "Incident post-mortems (`docs/postmortems/*.md`), operational runbooks (`runbooks/**`), health check endpoints, circuit breakers, and chaos resilience configs.",
        "refuses": "Refuses to modify frontend visual layout, design UI mockups, author marketing landing copy, or write 3D shader code.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["curl -sI", "promtool check rules", "git log", "git status"],
        "mcp_servers": ["prometheus-mcp-server", "@cyanheads/git-mcp-server", "codebase-memory-mcp"],
        "extensions": ["pi-lens", "pi-knowledge"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block accidental deletion or destructive actions during incident triage
      if echo "$PI_TOOL_ARGS" | grep -E "(rm -rf /|drop database|systemctl stop)"; then
        echo "Dangerous command blocked in sre-incident-eng triage session." >&2
        exit 2
      fi""",
        "self_correction": "Verifies all authored runbooks against the operational readiness checklist and ensures that post-mortems strictly include concrete timeline timestamps and action item owners.",
        "assigned_skills": ["skills/systematic-debugging/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 45,
        "slug": "observability-eng",
        "name": "Observability, Telemetry & OpenTelemetry Engineer",
        "guild": "Architecture, Cloud & Infrastructure Guild",
        "scope": "Distributed tracing, OpenTelemetry (OTel) instrumentation, metric collection (Prometheus / Mimir), structured logging (Zap / Tracing), and Grafana dashboard-as-code definitions.",
        "owns": "OpenTelemetry exporter configs, Prometheus recording and alerting rules (`alerts.yaml`), Grafana dashboard JSON models (`dashboards/*.json`), and trace sampling rate policies.",
        "refuses": "Refuses to write user-facing CSS styles, design mobile native layouts, author marketing copy, or write video game physics engines.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["promtool check rules", "promtool check config", "jq . dashboards/*.json", "git status"],
        "mcp_servers": ["prometheus-mcp-server", "codebase-memory-mcp"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.rules.yaml", "alerts.yaml"]
    action: bash
    command: |
      promtool check rules "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(terraform destroy|rm -rf /)"; then
        echo "Dangerous command blocked by observability-eng guard." >&2
        exit 2
      fi""",
        "self_correction": "Validates Prometheus rules with `promtool check rules alerts.yaml` and verifies that all Grafana JSON dashboards pass schema validation without syntax errors.",
        "assigned_skills": ["skills/observability-eng/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 46,
        "slug": "git-drift-coord",
        "name": "Git Worktree, Merge & Branch Drift Coordinator",
        "guild": "Architecture, Cloud & Infrastructure Guild",
        "scope": "Git repository hygiene, git worktree lifecycle management, branch drift detection, rebase conflict resolution, merge queue coordination, and commit history linearization.",
        "owns": "Git worktree staging scripts, branch sync automation, rebase conflict mediation strategies, merge pull request gates, and commit hygiene guidelines.",
        "refuses": "Refuses to write application features, build frontend UI templates, alter database schema models, or configure cloud VPC networks.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["git status", "git worktree list", "git log --graph --oneline -n 20", "git rebase", "git diff"],
        "mcp_servers": ["@cyanheads/git-mcp-server", "codebase-memory-mcp"],
        "extensions": ["pi-agents-team", "pi-slopchop"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block hard reset or force push to protected branches
      if echo "$PI_TOOL_ARGS" | grep -E "(git push.*(main|master).*--force|git reset --hard origin/(main|master))"; then
        echo "Safety Violation: Force modification of primary branch is strictly forbidden." >&2
        exit 2
      fi""",
        "self_correction": "Executes `git status --porcelain` and `git log -1` to verify zero untracked conflict markers (`<<<<<<<`) and verifies clean fast-forward rebase before closing merge tasks.",
        "assigned_skills": ["skills/superpowers/git-worktrees/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet / GPT-4o",
        "thinking_budget": "Medium (6,000 tokens)"
    }
]
