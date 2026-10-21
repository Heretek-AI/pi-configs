# Forensic Audit: edgehero/pi-dispatch

## 1. Target Metadata
- Repo URL: https://github.com/edgehero/pi-dispatch
- NPM URL: https://www.npmjs.com/package/@edgehero/pi-dispatch-admin
- Latest Commit Date: 2026-10-21 (Commit: 473410b)
- Release / Publish Date: 2026-10-21 (v4.3.1)
- Star Count: 185 | Forks: 9 | Open Issues: 13
- License: MIT
- Pi Version Compatibility: Pi >= 1.2.0 (`@earendil-works/pi-coding-agent`, `@earendil-works/pi-ai`, `@earendil-works/pi-tui` pinned at 1.2.0 in overrides), Node >= 22.19.0.

## 2. What They Claim To Do
`pi-dispatch` claims to turn Pi into a robust, self-hosted, continuous autonomous coding service:
Key claims from README and documentation:
1. **Containerized Sandbox Isolation**: Every agent task executes inside an ephemeral Docker or Podman container with dropped Linux capabilities, non-root user, and read-only system mounts.
2. **Pre-Spend Financial Hard Caps**: Computes potential cost before dispatching any model API call; halts jobs before they exceed per-job, daily, weekly, monthly, or project-scoped dollar limits.
3. **Multi-Platform Event Triggers**: Listens for webhooks and events from GitHub, GitLab, Forgejo, and Azure DevOps (e.g., label an issue `ai` or comment `@pi` on a PR). Also supports cron schedules and CLI triggers.
4. **Project Budgets & Resource Sizing**: Multi-tenant resource allocation per project (CPU, memory, concurrent worker slots) to prevent starvation.
5. **Interactive Operator Console & Pi Extension**: Ships `@edgehero/pi-dispatch-admin` as a native Pi extension with `/dispatch` interactive TUI panel, HTML web console (`pi-dispatch-console`), and 20+ administrative tools.
6. **Zero Self-Merge Policy**: Guaranteed guardrail that the agent can open pull requests but never merge them.

## 3. Forensic Code Reality (Proof of Work)
This repository is an enterprise-grade autonomous agent operations platform. It contains a complete multi-tier architecture spanning container runtimes, job queues, webhook receivers, and an expansive Pi extension operator console.

### File & Code Architecture
- Monorepo workspace containing 4 primary subsystems:
  - `image/runner`: Dockerfile and container bootstrap scripts. Configures headless Chromium, Playwright, git, and locked-down Linux user accounts.
  - `worker`: Background daemon consuming job queues from Redis/filesystem, spawning isolated containers via Docker Engine or Podman socket API, streaming logs, and enforcing hard timeout and CPU/RAM ceilings.
  - `receiver`: HTTP webhook service parsing push, issue, and PR payloads from GitHub, GitLab, Forgejo, and Azure DevOps, verifying HMAC signatures, and enqueuing jobs.
  - `admin`: The Pi extension and web dashboard (`@edgehero/pi-dispatch-admin`).
- `admin/package.json`: Exposes binary `pi-dispatch-console` and Pi extension `./dist/index.mjs` with bundled skills.
- `admin/src/index.ts` (1,863 lines): The master extension wiring. Registers `/dispatch` command, model-callable operator tools, and security hooks.
- `admin/src/dashboard.ts` (305 KB TypeScript): Massive TUI terminal dashboard providing real-time ASCII/Unicode meters, job graphs, trigger editors, and financial dial gauges.
- `admin/src/read-model.mjs` (378 KB JavaScript): High-throughput query engine reading job histories, logs, metrics, and spend records from the underlying queue database.
- `admin/src/costs.mjs` (51 KB): Pricing calculator and pre-spend token valuation engine for OpenAI, Anthropic, Google, and local models.
- `admin/src/audited-write.mjs` & `dialog-gate.mjs`: Safety guard ensuring that if an agent tries to modify dispatch configuration files via tools, human confirmation is required.
- `admin/skills/operate-pi-dispatch/SKILL.md` (31 KB): Complete operator instructions for Pi agents managing the fleet.

### Container Security & Sandbox Hardening
The container execution model in `worker` and `image/runner` implements defense-in-depth:
- Runs strictly as unprivileged user (`node:node`, UID 1000).
- Drops all Linux kernel capabilities: `--cap-drop=ALL`.
- Sets `--security-opt=no-new-privileges:true` to block setuid binaries.
- Mounts the project root filesystem as read-only (`--read-only`), providing tmpfs overlays only for `/tmp` and build cache directories.
- CPU and memory ceilings enforced by cgroups (`--cpus=2 --memory=4g`).
- Network egress can be optionally sandboxed or restricted to approved package registries and model provider API endpoints.
- Ephemeral lifecycle: the container is destroyed and wiped immediately upon task completion, leaving zero persistent artifacts outside of the git commits explicitly pushed to a feature branch.

### Pre-Spend Dollar Limits & Financial Circuit Breakers
Unlike reactive token meters that notify the user after an expensive run has already finished, `pi-dispatch` implements proactive pre-spend valuation in `costs.mjs`:
- Evaluates pending prompt token counts against current provider price tables (Anthropic Claude 3.7 Sonnet, OpenAI GPT-5.4, Google Gemini 2.5 Pro).
- Checks cumulative spend across multiple rolling time windows:
  - Per-Job Cap: Halts execution before a single run can exceed its allocated limit (e.g. $2.00).
  - Daily Window: Rolling 24-hour deployment ceiling.
  - Weekly Window: 7-day spend budget.
  - Monthly Window: Calendar month total ceiling.
  - Project/Repo Scoped Limit: Specific cap for high-traffic repositories.
- If a proposed model call risks exceeding any of these windows, the job is refused before container spawn or paused mid-run with status `HELD_OVER_BUDGET`.

### Webhook Event Translation (`receiver/`)
The `receiver` workspace acts as an intelligent API gateway:
- Verifies HMAC webhook signatures using repository secrets.
- Filters events based on user permissions: only users with `write` or `admin` access to the repository can trigger agent runs via issue labels or PR comments.
- Translates forge-specific event payloads into a uniform `JobTrigger` envelope:
  - GitHub: Issue opened/labeled (`ai`), PR opened, PR review comment (`@pi`).
  - GitLab: Merge request notes, issue events.
  - Forgejo / Gitea: Self-hosted git forge webhooks.
  - Azure DevOps: Pull request threads and work item updates.

### Configuration File Formats
`pi-dispatch` utilizes structured JSON files located in the deployment folder:
1. `triggers.json`:
   ```json
   {
     "triggers": [
       {
         "id": "nightly-cleanup",
         "type": "cron",
         "schedule": "0 2 * * *",
         "repo": "owner/repo",
         "branch": "main",
         "flow": "triage-backlog",
         "run": {
           "models": ["anthropic/claude-3-7-sonnet"],
           "dollarCap": 1.50,
           "turnLimit": 20
         }
       },
       {
         "id": "github-pr-review",
         "type": "forge",
         "provider": "github",
         "events": ["pull_request_comment"],
         "matchPattern": "@pi fix.*",
         "run": { "dollarCap": 0.75 }
       }
     ]
   }
   ```
2. `scoped-limits.json`:
   ```json
   {
     "deployment": {
       "dailyDollarCap": 50.00,
       "weeklyDollarCap": 250.00,
       "monthlyDollarCap": 800.00
     },
     "projects": {
       "frontend": { "dailyDollarCap": 15.00, "floor": 5.00 },
       "backend": { "dailyDollarCap": 30.00, "floor": 10.00 }
     }
   }
   ```
3. `pause-windows.json`:
   ```json
   {
     "windows": [
       {
         "name": "Weekend Moratorium",
         "cronStart": "0 18 * * 5",
         "cronEnd": "0 8 * * 1",
         "reason": "Freeze autonomous deployments over the weekend"
       }
     ]
   }
   ```

### Web Console & Insights Architecture (`pi-dispatch-console`)
Beyond the terminal TUI, `@edgehero/pi-dispatch-admin` ships a built-in HTTP server (`bin/pi-dispatch-console`):
- `insights-html.mjs` (128 KB): Generates interactive charts visualizing historical spend trends, dollar consumption per flow/trigger/model/repo, and host hardware saturation.
- `graph-html.mjs` (102 KB): Generates an interactive visual DAG (Directed Acyclic Graph) showing trigger-to-flow relationships and chained downstream executions.
- `dispatch-chat.mjs`: Lightweight web chat interface enabling developers to interact with the dispatch queue directly from a browser.

### Hook & Tool Registrations
1. **Lifecycle Hooks**:
   - `pi.on("tool_call", (event, ctx) => guard(event, ctx))`: Intercepts file writes targeting dispatch configuration (`triggers.json`, `limits.json`) to enforce human confirmation gates.
   - `pi.on("resources_discover", ...)`: Discovers operator skills dynamically.
2. **Slash Commands**:
   - `/dispatch`: Launches the full interactive TUI admin dashboard, setup wizard, or diagnostic panel.
3. **Model-Facing Operator Tools (29 tools registered in `admin/src/index.ts`)**:
   - `dispatch_status`: Health and queue state overview.
   - `dispatch_runs`: Query historical and live job runs with status filters (`pending`, `running`, `completed`, `held`, `failed`).
   - `dispatch_costs`: Retrieve real-time financial expenditure vs. configured limits across daily/weekly/monthly windows.
   - `dispatch_pause` / `dispatch_resume`: Emergency pause switches for all or specific triggers.
   - `dispatch_run`: Enqueue a manual job run on a designated repository/branch with custom prompt parameters.
   - `dispatch_capacity`: Inspect container slot availability and host CPU/RAM pressure.
   - `dispatch_triggers`: List configured event and cron triggers.
   - `dispatch_trigger_add` / `dispatch_trigger_edit` / `dispatch_trigger_delete`: CRUD operations on automated triggers.
   - `dispatch_limits` / `dispatch_limit_add` / `dispatch_limit_edit` / `dispatch_limit_delete`: Manage dollar spend caps per repo, project, or deployment.
   - `dispatch_projects` / `dispatch_project_add` / `dispatch_project_edit` / `dispatch_project_delete`: Project-level budget grouping.
   - `dispatch_pauses` / `dispatch_pause_add` / `dispatch_pause_delete`: Scheduled quiet hours (e.g., weekend moratoriums).
   - `dispatch_allocations` / `dispatch_priorities_set` / `dispatch_envelope_set`: Portfolio dynamic budget allocation.

## 4. 6-Pillar Classification
- **1. Hooks**: HIGH. Uses `tool_call` hooks to protect administrative configuration files from unauthorized model manipulation.
- **2. LSP**: NONE.
- **3. AST**: NONE.
- **4. MCP**: MEDIUM. Provides model-facing tool interfaces that can bridge to MCP or native Pi tools.
- **5. Skills**: HIGH. Ships `operate-pi-dispatch` skill (31 KB) guiding the LLM on managing autonomous fleet operations.
- **6. Extensions**: CRITICAL. Massive TUI dashboard and system administration suite embedded as a Pi extension.

## 5. Brutally Honest Usefulness Assessment
- **Score**: 9.0 / 10 (for autonomous server/CI operations); 3.0 / 10 (for local interactive terminal coding).
- **Technical Critique**:
  - *Operational Burden*: Running `pi-dispatch` requires a running server infrastructure (Docker or Podman, Node 22 runtime, Redis or persistent volume storage, and webhook ingresses). This is not a lightweight local plugin; it is a full-blown continuous delivery platform.
  - *Weight of Admin Package*: The `admin/` bundle is substantial (>1.5 MB of TypeScript and UI logic), reflecting its feature-rich terminal dashboard. For users who only want simple cron execution, this can feel heavy.
  - *Hard Spend Prevention*: The pre-spend calculation is one of the most valuable features in the entire AI agent ecosystem, effectively preventing runaway loops from racking up thousands of dollars on cloud API bills.
  - *Container Cold Starts*: Spinning up a fresh Docker container with Playwright and browser dependencies adds a 3-8 second cold-start latency to every job invocation compared to running directly on the host.

## 6. Community Feedback & Sentiment
- Stars: 185, Forks: 9. Highly regarded by DevOps engineers and teams running headless agent fleets.
- Active development and issue tracking:
  - Issue #725: Edge case race condition in OpenShell lane copy-mode steering assertion.
  - Issue #717: Model roles and canary testing for newly proposed foundation models.
  - Issue #716: Automatic model failover on provider rate-limiting (429) or quota depletion.
  - Issues #710, #711: Console UI enhancements, form validation, and mobile accessibility.
- Strong reputation for reliability, safety, and strict permission bounding.

## 7. Verdict
**ADOPT AS-IS** (for server and automated background agent workflows).
- *Justification*: `pi-dispatch` solves the single biggest hazard of autonomous agents: unconstrained spend and unsandboxed execution. It is the premier open-source orchestrator for running Pi unattended on GitHub/GitLab repositories. The `@edgehero/pi-dispatch-admin` extension provides a peerless dashboard for monitoring agent health and enforcing spend caps.

## 8. Discovered Alternatives & Recommendations
- Recommended companion: Podman (https://podman.io) for daemonless rootless container execution of autonomous agent jobs.
- Discovered Pattern: Pre-spend budget validation in `admin/src/costs.mjs` — calculating pricing ceilings before issuing LLM API calls.
