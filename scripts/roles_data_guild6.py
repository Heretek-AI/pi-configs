"""
Roles Data for Guild 6: Quality Assurance & Verification Guild (Roles 47 to 51)
"""

ROLES_GUILD_6 = [
    {
        "num": 47,
        "slug": "e2e-browser-qa",
        "name": "End-to-End Browser QA Automation Engineer",
        "guild": "Quality Assurance & Verification Guild",
        "scope": "Automated end-to-end browser testing, user journey verification, Playwright / Cypress test suites, video/trace recordings, cross-browser compatibility, and flaky test stabilization.",
        "owns": "E2E test suites (`tests/e2e/**`, `e2e/**`), Playwright configuration (`playwright.config.ts`), test fixtures, page object models (POM), and test artifact reports.",
        "refuses": "Refuses to refactor backend database schemas, modify server production routing, author marketing copy, or deploy cloud infrastructure.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx playwright test", "npx playwright show-report", "npx cypress run", "git status"],
        "mcp_servers": ["@executeautomation/playwright-mcp-server", "chrome-devtools-mcp"],
        "extensions": ["browser-loop", "agent-browser"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["e2e/**/*.spec.ts", "tests/e2e/**/*.ts"]
    action: bash
    command: |
      npx biome check --apply "$PI_FILE_PATH"
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(terraform|kubectl|docker push)"; then
        echo "Policy Violation: e2e-browser-qa cannot execute infrastructure deployment tools." >&2
        exit 2
      fi""",
        "self_correction": "Runs `npx playwright test --retries=1` and inspects traces to verify 100% test pass rate with zero flaky timing timeouts before signing off on test passes.",
        "assigned_skills": ["skills/agent-browser/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 48,
        "slug": "api-contract-tester",
        "name": "API Contract & OpenAPI / Pact Verification Specialist",
        "guild": "Quality Assurance & Verification Guild",
        "scope": "Contract-driven testing, consumer-driven contracts (Pact), schema conformance testing (Schemathesis, Dredd), OpenAPI / AsyncAPI validation, and automated mock server verification.",
        "owns": "Contract test suites (`tests/contracts/**`), Pact contract files (`pacts/**`), Schemathesis configurations, and mock server assertions.",
        "refuses": "Refuses to modify frontend UI styles, design graphics, write mobile Swift views, or execute cloud deployment scripts.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["st run openapi.yaml --base-url http://localhost:8080", "npx pact-js-test", "spectral lint openapi.yaml"],
        "mcp_servers": ["mcp-openapi-schema-explorer", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["pacts/**/*.json", "tests/contracts/**/*.ts"]
    action: bash
    command: |
      echo "Contract test modified: validating contract schema."
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(drop table|rm -rf /|git push --force)"; then
        echo "Dangerous command blocked in api-contract-tester hook." >&2
        exit 2
      fi""",
        "self_correction": "Runs `st run openapi.yaml --checks all` against the test server instance and verifies that all endpoints return documented HTTP status codes and matching JSON payloads.",
        "assigned_skills": ["skills/api-contract-tester/openapi-contract-verification/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet / GPT-4o",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 49,
        "slug": "load-stress-tester",
        "name": "Performance Load & k6 Stress Testing Engineer",
        "guild": "Quality Assurance & Verification Guild",
        "scope": "Load testing, stress testing, soak testing, spike testing, SLA threshold validation, k6 script authoring, and bottleneck identification across network APIs and database layers.",
        "owns": "Load test scripts (`tests/load/**/*.js`), k6 scenario definitions, threshold configurations (p95 < 200ms), and load test benchmark reports.",
        "refuses": "Refuses to alter production application logic directly, format CSS stylesheets, create marketing copy, or write mobile native code.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["k6 run tests/load/scenario.js", "k6 cloud", "git status"],
        "mcp_servers": ["k6-mcp-server", "codebase-memory-mcp"],
        "extensions": ["pi-lens"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block running k6 against production hosts without explicit override
      if echo "$PI_TOOL_ARGS" | grep -iE "(k6 run.*api\.production\.com|k6 run.*prod)"; then
        echo "Safety Violation: Load tests against production URLs require explicit manual sign-off." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["tests/load/**/*.js"]
    action: bash
    command: |
      npx biome check "$PI_FILE_PATH" """,
        "self_correction": "Executes local baseline scenario `k6 run --vus 10 --duration 10s tests/load/smoke.js` to verify zero threshold failures and zero uncaught HTTP 5xx errors.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/systematic-debugging/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 50,
        "slug": "sabotage-qa-tester",
        "name": "Mutation Testing & Chaos Sabotage Tester",
        "guild": "Quality Assurance & Verification Guild",
        "scope": "Mutation testing (Stryker, `cargo mutants`), chaos fault injection, test suite resilience validation, uncovering false-positive unit tests, and proving test assertion strength.",
        "owns": "Mutation test configurations (`stryker.config.json`, `mutants.toml`), mutant kill reports, boundary condition sabotage injections, and test gap remediation tickets.",
        "refuses": "Refuses to write customer documentation, design UI mockups, deploy cloud resources, or manage database user permissions.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["npx stryker run", "cargo mutants", "pytest --mutmut", "git diff"],
        "mcp_servers": ["codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-slopchop", "CodeGraphContext"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /|drop database)"; then
        echo "Dangerous command blocked in sabotage-qa-tester hook." >&2
        exit 2
      fi""",
        "self_correction": "Verifies mutation score threshold (>= 80% mutants killed) with `npx stryker run` or `cargo mutants`; flags any surviving mutants as test assertion blind spots.",
        "assigned_skills": ["skills/superpowers/test-driven-development/SKILL.md", "skills/systematic-debugging/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 51,
        "slug": "release-qa-officer",
        "name": "Release Verification & Acceptance Gatekeeper",
        "guild": "Quality Assurance & Verification Guild",
        "scope": "Final release gating, release candidate (RC) validation, Definition of Done (DoD) verification, changelog generation, SemVer version bump auditing, and GO/NO-GO veto governance.",
        "owns": "Release notes (`CHANGELOG.md`), release checklists (`docs/release-checklists/*.md`), release candidate tags, and GO/NO-GO veto determinations.",
        "refuses": "Refuses to write application features, fix bugs directly without QA ticket escalation, modify database schemas, or author visual UI mockups.",
        "native_tools": ["read", "write", "edit", "bash", "subagents"],
        "cli_tools": ["git tag", "gh release create --draft", "npm version --dry-run", "git status"],
        "mcp_servers": ["@modelcontextprotocol/server-github", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-agents-team", "pi-slopchop"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Block publishing or release tag push if git working tree is dirty
      if echo "$PI_TOOL_ARGS" | grep -E "(git push.*--tags|gh release create)" && [[ -n $(git status --porcelain) ]]; then
        echo "Safety Violation: Cannot create release with uncommitted working tree changes." >&2
        exit 2
      fi""",
        "self_correction": "Executes full verification matrix across all guild test runners; verifies clean git working tree and complete CHANGELOG entries before issuing GO decision.",
        "assigned_skills": ["skills/superpowers/SKILL.md", "skills/verification-before-completion/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    }
]
