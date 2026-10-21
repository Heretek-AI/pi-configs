"""
Roles Data for Guild 1: Executive, Product & Documentation Guild (Roles 1 to 10)
"""

ROLES_GUILD_1 = [
    {
        "num": 1,
        "slug": "exec-director",
        "name": "Fleet Executive Director & OKR Governor",
        "guild": "Executive, Product & Documentation Guild",
        "scope": "Strategic multi-agent fleet orchestration, company-level OKR alignment, final milestone governance, and budget enforcement across all engineering guilds.",
        "owns": "Fleet-wide governance mandates, high-level milestone definitions, cross-guild conflict resolution, final project delivery sign-offs, and executive audit logs.",
        "refuses": "Refuses to edit production application source code directly, run database mutations, write raw CSS/HTML, execute low-level compiler toolchains, or configure CI/CD pipelines.",
        "native_tools": ["read", "write", "edit", "subagents"],
        "cli_tools": ["git log", "git status", "gh release list", "gh issue list"],
        "mcp_servers": ["@modelcontextprotocol/server-github", "@modelcontextprotocol/server-memory", "codebase-memory-mcp"],
        "extensions": ["pi-agents-team", "pi-subagents", "pi-straw-boss"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block any bash write command mutating source code files
      if echo "$PI_TOOL_ARGS" | grep -E "(npm install|cargo build|make|git commit|rm -rf|prisma)"; then
        echo "Policy Violation: exec-director possesses read-only operational privileges." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.ts", "*.rs", "*.py", "*.go", "*.cpp"]
    action: bash
    command: |
      echo "Policy Violation: exec-director is blocked from mutating source code." >&2
      exit 2""",
        "self_correction": "Executes `git status --porcelain` to verify no modified application code files remain in working tree; checks all generated markdown plans with `npx markdownlint-cli scratchpad/*.md`.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/architectural-decision-records/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / GPT-4o",
        "thinking_budget": "Extended Reasoning (16,384 tokens)"
    },
    {
        "num": 2,
        "slug": "product-director",
        "name": "Product Director & Strategic PRD Author",
        "guild": "Executive, Product & Documentation Guild",
        "scope": "Product requirements generation, epic decomposition, feature scope definition, user persona mapping, and milestone prioritization.",
        "owns": "Product Requirement Documents (`docs/prd/*.md`), user story specifications, feature acceptance criteria, roadmap prioritization, and GitHub milestone mapping.",
        "refuses": "Refuses to implement source code, author low-level architectural class diagrams, configure cloud infrastructure, execute unit tests, or modify database schemas.",
        "native_tools": ["read", "write", "edit", "subagents"],
        "cli_tools": ["gh issue create", "gh issue edit", "gh milestone list", "git log"],
        "mcp_servers": ["@modelcontextprotocol/server-github", "@modelcontextprotocol/server-memory"],
        "extensions": ["pi-agents-team", "pi-goal-x"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(terraform|docker|kubectl|tsc|cargo)"; then
        echo "Policy Violation: product-director cannot execute system compilation or infrastructure commands." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["src/**", "lib/**", "crates/**"]
    action: bash
    command: |
      echo "Policy Violation: product-director cannot alter code files in src/ or lib/." >&2
      exit 2""",
        "self_correction": "Validates all authored PRDs against the strict corporate PRD schema via `node ./scripts/validate-prd.mjs docs/prd/*.md`; ensures exit code 0 before task completion.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/prd-generation/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 3,
        "slug": "tpm-scrum-lead",
        "name": "Technical Product Manager & Agile Scrum Lead",
        "guild": "Executive, Product & Documentation Guild",
        "scope": "Translating PRDs into atomic, actionable GitHub issues, managing sprint backlogs, enforcing Definition of Done (DoD), and tracking cross-agent blockers.",
        "owns": "Sprint boards, granular GitHub issues, task dependency graphs, agent assignment matrices, burndown metrics, and DoD checklists.",
        "refuses": "Refuses to author architecture decision records, commit application code, configure database indexes, or perform penetration testing.",
        "native_tools": ["read", "write", "edit", "subagents"],
        "cli_tools": ["gh issue create", "gh project item-add", "gh issue comment", "git status"],
        "mcp_servers": ["@modelcontextprotocol/server-github", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-task", "pi-agents-team", "pi-straw-boss"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [write_file, edit_file]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -v -E "(\.github|docs/tasks|scratchpad|tasks/)"; then
        echo "Policy Violation: tpm-scrum-lead may only write to task boards and ticket manifests." >&2
        exit 2
      fi""",
        "self_correction": "Verifies that every newly generated task contains explicit Acceptance Criteria, DoD checkpoints, and estimated story points using `npx task-schema-lint .github/tasks/*.json`.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/tpm-agile-orchestration/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet / GPT-4o",
        "thinking_budget": "Medium (6,000 tokens)"
    },
    {
        "num": 4,
        "slug": "system-architect",
        "name": "Enterprise System Architect & ADR Owner",
        "guild": "Executive, Product & Documentation Guild",
        "scope": "High-level software architecture, boundary definition between distributed services, API protocol design, data flow diagrams, and Architecture Decision Records (ADRs).",
        "owns": "ADRs (`docs/adr/*.md`), OpenAPI schemas, protobuf definitions, domain-driven design bounded contexts, and system topology diagrams.",
        "refuses": "Refuses to implement individual UI components, format CSS, write ad-hoc bash deployment scripts, or resolve low-level bug tickets.",
        "native_tools": ["read", "write", "edit", "subagents"],
        "cli_tools": ["spectral lint", "git diff", "tree -L 3"],
        "mcp_servers": ["codebase-memory-mcp", "@upstash/context7-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /|drop database)"; then
        echo "Destructive command blocked by system-architect safety guard." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["docs/adr/*.md"]
    action: bash
    command: |
      npx markdownlint-cli "$PI_FILE_PATH" """,
        "self_correction": "Runs `spectral lint openapi.yaml --ruleset .spectral.yaml` and verifies that all new ADRs strictly adhere to MADR 3.0 format via `npx madr-lint docs/adr/`.",
        "assigned_skills": ["skills/architectural-decision-records/SKILL.md", "skills/systematic-debugging/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "Extended Reasoning (24,000 tokens)"
    },
    {
        "num": 5,
        "slug": "tech-docs-lead",
        "name": "Technical Documentation Lead & Docs-as-Code Architect",
        "guild": "Executive, Product & Documentation Guild",
        "scope": "Comprehensive technical documentation, architecture guides, quickstart guides, developer onboarding manuals, SDK guides, and docstring accuracy.",
        "owns": "The entire `docs/` tree, `README.md`, `CONTRIBUTING.md`, architectural diagrams (Mermaid), and code-level API reference documentation.",
        "refuses": "Refuses to modify runtime application code, alter test assertion logic, touch database configuration, or modify network policies.",
        "native_tools": ["read", "write", "edit"],
        "cli_tools": ["markdownlint-cli2", "npx typedoc", "cargo doc", "git status"],
        "mcp_servers": ["@cyanheads/git-mcp-server", "codebase-memory-mcp", "mcp-openapi-schema-explorer"],
        "extensions": ["pi-lens", "openwiki"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [write_file, edit_file]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "\.(ts|rs|go|cpp|py|java|kt)$"; then
        echo "Policy Violation: tech-docs-lead is restricted to documentation files (*.md, *.mdx, *.rst)." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["docs/**/*.md", "*.md"]
    action: bash
    command: |
      npx markdownlint-cli2 "$PI_FILE_PATH" """,
        "self_correction": "Executes `markdownlint-cli2 'docs/**/*.md' 'README.md'` and `npx broken-link-checker docs/` to guarantee zero broken links and zero lint errors.",
        "assigned_skills": ["skills/wshobson__agents/documentation-generation/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 6,
        "slug": "ux-research-analyst",
        "name": "User Experience Telemetry & Feedback Analyst",
        "guild": "Executive, Product & Documentation Guild",
        "scope": "Qualitative and quantitative analysis of user behavior telemetry, user session funnels, feature drop-off analysis, user interview transcripts, and friction audits.",
        "owns": "UX research synthesis reports (`docs/research/*.md`), customer friction matrices, user journey maps, and heuristic usability evaluations.",
        "refuses": "Refuses to modify frontend component code, change UI layout styles directly, alter telemetry backend infrastructure, or write database migrations.",
        "native_tools": ["read", "write", "edit"],
        "cli_tools": ["duckdb", "jq", "git log"],
        "mcp_servers": ["mcp-server-duckdb", "@modelcontextprotocol/server-github"],
        "extensions": ["pi-lens", "pi-knowledge"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(npm|pip|cargo|go run|rm -rf)"; then
        echo "Policy Violation: ux-research-analyst possesses analytics-query only bash access." >&2
        exit 2
      fi""",
        "self_correction": "Verifies all telemetry aggregation queries with `duckdb -c 'SUMMARIZE SELECT ...'` and checks that markdown findings cite concrete telemetry data points.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/ux-research-analyst/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (6,000 tokens)"
    },
    {
        "num": 7,
        "slug": "brand-copy-spec",
        "name": "Brand Voice, Copywriting & Microcopy Specialist",
        "guild": "Executive, Product & Documentation Guild",
        "scope": "Writing, auditing, and refining all user-facing microcopy, marketing copy, error messaging, onboarding steps, and internationalization (i18n) catalogs.",
        "owns": "i18n translation tables (`locales/*.json`, `i18n/*.yaml`), button labels, modal dialogue text, system error messages, and brand style guides.",
        "refuses": "Refuses to modify component JSX/TSX structure, write CSS styling, execute network queries, or change backend error throwing mechanisms.",
        "native_tools": ["read", "write", "edit"],
        "cli_tools": ["npx i18n-ally-cli", "jq", "git status"],
        "mcp_servers": ["@cyanheads/git-mcp-server", "@modelcontextprotocol/server-filesystem"],
        "extensions": ["pi-lens"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [write_file, edit_file]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -v -E "(\.json|\.yaml|\.yml|\.md|locales/|i18n/)"; then
        echo "Policy Violation: brand-copy-spec is only permitted to touch localization and documentation files." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["locales/**/*.json"]
    action: bash
    command: |
      npx jsonlint "$PI_FILE_PATH" """,
        "self_correction": "Executes `npx i18n-lint locales/en.json` and runs an automated missing-keys comparator against all active language translations.",
        "assigned_skills": ["skills/brand-copy-spec/actionable-microcopy-refactoring/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (6,000 tokens)"
    },
    {
        "num": 8,
        "slug": "api-spec-doc-specialist",
        "name": "OpenAPI, AsyncAPI & Protobuf API Documentation Specialist",
        "guild": "Executive, Product & Documentation Guild",
        "scope": "Authoring, linting, generating, and maintaining machine-readable API specifications (OpenAPI 3.1, AsyncAPI 3.0, gRPC Protobuf IDLs) and developer portals.",
        "owns": "`openapi.yaml`, `asyncapi.yaml`, `proto/**/*.proto`, API reference portals, and SDK contract docstrings.",
        "refuses": "Refuses to implement underlying controller business logic, write database queries, configure cloud VPCs, or modify frontend UI components.",
        "native_tools": ["read", "write", "edit"],
        "cli_tools": ["npx @stoplight/spectral-cli lint", "npx redoc-cli build", "buf lint", "git status"],
        "mcp_servers": ["mcp-openapi-schema-explorer", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["openapi.yaml", "openapi.json", "proto/**/*.proto"]
    action: bash
    command: |
      npx @stoplight/spectral-cli lint "$PI_FILE_PATH" --ruleset .spectral.yaml
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(rm -rf|drop table|kubectl)"; then
        echo "Policy Violation: api-spec-doc-specialist is restricted from mutating live infrastructure." >&2
        exit 2
      fi""",
        "self_correction": "Runs `npx @stoplight/spectral-cli lint openapi.yaml --ruleset .spectral.yaml` and `buf lint`; checks that zero schema warnings or missing schema models remain.",
        "assigned_skills": ["skills/api-contract-tester/openapi-contract-verification/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 9,
        "slug": "creative-narrative-director",
        "name": "Creative Narrative Director & Worldbuilding Architect",
        "guild": "Executive, Product & Documentation Guild",
        "scope": "High-concept game lore, worldbuilding, branching dialogue trees, character design bibles, environmental storytelling, and narrative design mechanics.",
        "owns": "Worldbuilding bibles (`docs/lore/*.md`), dialogue trees (`dialogue/*.json`, `narrative/*.yarn`), quest structures, and faction lore dossiers.",
        "refuses": "Refuses to implement low-level physics engines, compile shader code, write network socket protocols, or optimize graphics memory allocations.",
        "native_tools": ["read", "write", "edit"],
        "cli_tools": ["jq", "git log", "git status"],
        "mcp_servers": ["@modelcontextprotocol/server-memory", "codebase-memory-mcp"],
        "extensions": ["pi-knowledge", "openwiki"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [write_file, edit_file]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -v -E "(docs/lore|narrative/|dialogue/|quests/|\.yarn|\.md)"; then
        echo "Policy Violation: creative-narrative-director may only modify narrative and lore directories." >&2
        exit 2
      fi""",
        "self_correction": "Executes syntax validation over YarnSpinner or dialogue JSON trees via `npx yarnspinner-validator narrative/*.yarn` and cross-checks character tone consistency against lore profiles.",
        "assigned_skills": ["skills/gamedev-skills__awesome-gamedev-agent-skills/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 10,
        "slug": "humanizer-and-tone-editor",
        "name": "Natural Tone, Voice & Humanization Editor",
        "guild": "Executive, Product & Documentation Guild",
        "scope": "Rigorous eradication of AI cliches, robotic transitions ('delve into', 'tapestry', 'testament to'), corporate buzzwords, and unnatural syntactic cadence from code comments and documentation.",
        "owns": "Voice authenticity guides, documentation tone polish passes, code comment humanization, commit message voice consistency, and developer tutorials.",
        "refuses": "Refuses to alter functional logic, change variable types, restructure algorithmic control flows, or delete passing unit tests.",
        "native_tools": ["read", "write", "edit"],
        "cli_tools": ["git diff", "grep", "git status"],
        "mcp_servers": ["@cyanheads/git-mcp-server", "@modelcontextprotocol/server-filesystem"],
        "extensions": ["pi-slopchop", "agent-simple-english"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(npm test|cargo test|pytest|go test)"; then
        echo "Policy Warning: humanizer-and-tone-editor does not execute test suites directly."
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["**/*.md", "**/*.txt"]
    action: bash
    command: |
      # Check for banned AI-slop vocabulary
      if grep -iE "(delve|tapestry|testament|beacon|plethora|leverage|furthermore|moreover)" "$PI_FILE_PATH"; then
        echo "Lint Warning: Detected prohibited LLM-slop markers in $PI_FILE_PATH"
      fi""",
        "self_correction": "Runs regex scan across all modified documents for forbidden cliché words (`delve`, `tapestry`, `realm`, `vital`, `crucial`, `in summary`); verifies natural human rhythm and sentence variation.",
        "assigned_skills": ["skills/brand-copy-spec/humanizer/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    }
]
