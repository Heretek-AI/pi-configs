# Forensic Audit: repowise-dev/repowise

## 1. Target Metadata
- Repo URL / NPM URL: https://github.com/repowise-dev/repowise / PyPI: https://pypi.org/project/repowise/
- Latest Commit Date / Publish Date: 2026-10-21 (Commit `54c8003`)
- Star Count / Forks / Issues: 7,877 stars / 920 forks / 157 issues
- License: GNU Affero General Public License v3.0 (AGPL-3.0) + commercial dual-license
- Pi Version Compatibility: Highly compatible with Pi / Claude Code plugin architectures; exposes hooks via `.claude-plugin` (`hooks.json` targeting `SessionStart`, `PostToolUse`, `PostToolUseFailure`), interactive TUI lens mod (`packages/claude-mod`), 18 slash commands, 6 markdown skills, and a standard JSON-RPC MCP server.

## 2. What They Claim To Do
Repowise claims to provide local-first, zero-LLM codebase intelligence for coding agents and human developers. Key marketing and architectural claims:
- Indexes code, call graphs, git history, tests, docs, and architecture decisions once on the developer's laptop with incremental updates per commit.
- Claims to reduce agent output tokens by 31.6% (p < 0.0001) by providing deterministic answers instead of prompting agents to scan/glob/read dozens of files.
- Operates zero-LLM graph analysis, blast radius calculation, dead code detection, coupling metrics, and test impact analysis (identifying which tests reach modified code).
- Provides an MCP server connecting to Claude Code, Cursor, Codex, and other agent harnesses.
- Includes "Lens", an interactive terminal TUI overlay (`packages/claude-mod`) rendering call graphs, blast radius, and activity maps inside agent sessions.
- Offers hosted cloud infrastructure ("Foresight") for team analytics, PR review bots, and multi-repo cross-indexing.

## 3. Forensic Code Reality (Proof of Work)
Deep inspection of the physical codebase reveals a massive, fully-implemented monorepo (~47MB of source code across Python, TypeScript, and React):

### A. Core Server & Engine (`packages/server/src/repowise/server/`)
The backend is powered by a high-performance Python FastAPI engine running over Uvicorn with a dedicated MCP server (`packages/server/src/repowise/server/mcp_server/`):
- **Exposed MCP Tools Catalog (19 Tools)**:
  1. `get_blast_radius`: Computes downstream reachable services and symbol consumers with structural contract hops.
  2. `get_architecture`: Generates C4 architecture models (System, Container, Component levels) and boundary graphs.
  3. `get_conformance`: Verifies architectural boundaries, layered architecture constraints, and forbidden import rules.
  4. `get_dead_code`: Scans the AST index for unreachable export functions, obsolete modules, and unused variables.
  5. `get_dependency`: Generates full package and internal module dependency graphs.
  6. `get_change_risk`: Assesses risk score of current diff based on cyclomatic complexity, churn velocity, and blast radius.
  7. `get_test_impact`: Maps modified code lines directly to the exact test files that exercise those execution paths.
  8. `get_symbol`: High-precision symbol declaration and reference lookup bypassing textual grep.
  9. `get_search_symbols`: Fuzzy and regex symbol searching across monorepo boundaries.
  10. `get_why`: Traces git history rationale, commit messages, and ADR decisions behind code structures.
  11. `get_findings`: Aggregates code quality findings, code smells, and coupling anomalies.
  12. `get_flows`: Traces end-to-end execution flow paths from entrypoints to leaf handlers.
  13. `get_refactoring`: Identifies high-coupling / low-cohesion clusters and proposes module extraction boundaries.
  14. `get_repos`: Lists and queries indexed multi-repo workspace configurations.
  15. `get_health`: Computes repo health scores including test coverage ratios, documentation drift, and circular dependencies.
  16. `get_overview`: High-level executive codebase breakdown with language metrics and key components.
  17. `get_risk`: PR-mode risk analysis scoring files by historical defect frequency.
  18. `get_search`: Full-text hybrid search over codebase documentation, comments, and symbols.
  19. `get_context`: Compact contextual bundle tailored for LLM prompt context injection.

### B. Blast Radius Tool Schema & Implementation Proof
Excerpt from `packages/server/src/repowise/server/mcp_server/tool_blast_radius.py`:
```python
@mcp.tool(
    default=False,
    requires_workspace=True,
    surface_order=210,
    trust_kind="structural",
    artifact_type="dependency_graph",
    presentation="dependency_graph",
)
async def get_blast_radius(
    targets: list[str],
    max_depth: int = 3,
    include_behavioral: bool = True,
) -> dict[str, Any]:
    """Cross-repo blast radius - which downstream services are structurally reachable.

    Workspace-only. Traverses the system graph from the given service(s) and
    returns the reachable services across every repo, ranked by an uncalibrated
    impact score, alongside impacted cross-repo tests.
    """
    # Traverses system graph, collects structural dependencies, and computes
    # symbol consumers bounded by _MCP_IMPACTED_LIMIT (25) and _SYMBOL_CONSUMER_LIMIT (10)
```

### C. Claude Code & Host Mod Hook Architecture (`plugins/claude-code/`)
The hook registration binds deeply into agent host lifecycles via `plugins/claude-code/hooks/hooks.json`:
```json
{
  "modules": ["./lens/lens.js"],
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear",
        "hooks": [
          {
            "type": "command",
            "command": "if command -v repowise-augment >/dev/null 2>&1; then exec repowise-augment; fi",
            "timeout": 10,
            "statusMessage": "Loading repowise context..."
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Grep|Glob|Read|Edit|Write|mcp__.*[Rr]epowise.*__.*",
        "hooks": [
          {
            "type": "command",
            "command": "if command -v repowise-augment >/dev/null 2>&1; then exec repowise-augment; fi",
            "timeout": 10,
            "statusMessage": "Checking codebase context..."
          }
        ]
      }
    ],
    "PostToolUseFailure": [
      {
        "matcher": "Read|Edit|Write|Grep|Glob|NotebookEdit",
        "hooks": [
          {
            "type": "command",
            "command": "if command -v repowise-augment >/dev/null 2>&1; then exec repowise-augment; fi",
            "timeout": 10,
            "statusMessage": "Checking codebase context..."
          }
        ]
      }
    ]
  }
}
```

### D. Interactive TUI Lens Mod (`packages/claude-mod/src/register.ts`)
The Lens module intercepts agent turn events and renders real-time graph animations directly into the terminal host:
```typescript
/**
 * The mod's entry: builds a Host from `$`, feeds events to the model, and redraws.
 */
import { getSavings } from "@repowise-dev/api-client/costs";
import { Animator } from "./animator";
import { LensFlow } from "./flow-controller";
import { LensMap } from "./map-controller";
import type { ModApi, ToolCallEvent, TurnCompleteEvent } from "./mod-api";

export function register(mod: ModApi) {
  mod.on("TurnStart", (evt) => {
    // Intercepts agent turns, evaluates active workspace context
  });
  mod.on("PostToolUse", async (evt) => {
    // Checks if tool was an edit; computes blast facts and updates terminal overlay
  });
  mod.on("PaneRender", (evt) => {
    // Renders interactive call graphs and savings indicators in the active terminal
  });
}
```

### E. Skills and Commands Ecosystem
- **6 Structured Markdown Workflow Skills** (`plugins/claude-code/skills/`):
  1. `architectural-decisions`: Guides agents to query C4 models and record ADRs before refactoring.
  2. `change-review`: Inspects PR diffs, calculates change risk scores, and checks architectural conformance.
  3. `code-health`: Analyzes dead code, cyclomatic complexity, and test coverage ratios.
  4. `codebase-exploration`: Uses AST-driven symbol navigation instead of brute-force grep.
  5. `dead-code-cleanup`: Safely purges unreferenced functions with blast radius verification.
  6. `pre-modification`: Mandates running `get_blast_radius` and `get_test_impact` before editing key files.
- **18 Slash Commands** (`plugins/claude-code/commands/`):
  `/ask`, `/context`, `/coverage`, `/dead-code`, `/decision`, `/doctor`, `/export`, `/health`, `/impacted-tests`, `/init`, `/reindex`, `/risk`, `/search`, `/security`, `/status`, `/symbol`, `/update`, `/why`.

## 4. 6-Pillar Classification
Repowise spans multiple pillars:
- **1. Hooks**: High. Implements `SessionStart`, `PostToolUse`, and `PostToolUseFailure` lifecycle interceptors in `hooks.json`.
- **3. AST**: Core Pillar. Implements zero-LLM Tree-sitter AST parsing for multi-language symbol resolution and call graph generation.
- **4. MCP**: Core Pillar. Registers 19 dedicated MCP tools exposing deterministic repo intelligence over stdio and SSE.
- **5. Skills**: Core Pillar. Delivers 6 structured workflow skills instructing the agent on safe refactoring protocols.
- **6. Extensions**: Core Pillar. Provides a complete interactive terminal TUI overlay mod (`packages/claude-mod`).

## 5. Brutally Honest Usefulness Assessment
- **Score**: 8.5/10 (Superb Technical Engine; Heavy Background Footprint)
- **Technical Critique**:
  - *Bloat & Setup Friction*: Requires a local Python daemon running FastAPI, Uvicorn, and background indexing workers. Initial `repowise init` on massive repos can take several minutes.
  - *Windows Compatibility Friction*: In Unix hooks, scripts rely on `if command -v repowise-augment >/dev/null 2>&1; then exec repowise-augment; fi`, which fails when executed in Windows cmd.exe or PowerShell environments without a Bash wrapper.
  - *AGPLv3 License Barrier*: Strong copyleft AGPLv3 applies to the core engine, preventing proprietary in-tree bundling in commercial distributions without source release.
  - *Token Consumption*: While the query tools are concise, the hook `repowise-augment` on `PostToolUse` can add unnecessary output tokens after every file edit/read if not strictly throttled.

## 6. Community Feedback & Sentiment
Extremely strong, active developer community:
- 7,877 stars and 157 active issues.
- Community issues demonstrate intense real-world usage:
  - Issue #4349: Test ranking rebuild regressions during parallel workspace execution.
  - Issue #4348: Vitest mock masking preventing accurate test impact resolution.
  - Issue #4298: Health reporting false positives during pure function relocation across packages.
  - Fast PR turnaround with over 4,340 merged PRs and continuous semantic release tagging.

## 7. Verdict
**EXTRACT/CHERRY-PICK & INTEGRATE VIA MCP**
- **Justification**: Repowise is one of the highest-quality external codebase intelligence platforms available. However, due to its AGPLv3 license and substantial backend footprint (Python server + SQLite/Postgres DB + Node web interface), it should NOT be fork-copied directly into the Pi core repo. Instead:
  1. Leverage Repowise as a standalone external MCP server via stdio or SSE (`packages/server/src/repowise/server/mcp_server`).
  2. Cherry-pick its 6 markdown workflow skills (`pre-modification.md`, `change-review.md`, etc.) and adapt them into native Pi skills.
  3. Adapt the `PostToolUse` context augmentation concept into a native TypeScript Pi hook without requiring the heavy Python daemon if lighter AST tools (like Tree-sitter or Ripwire) are available.

## 8. Discovered Alternatives & Recommendations
- **MCP Server Registration**: Add Repowise to Pi's `.pi/mcp.json` or `settings.json`:
  ```json
  {
    "mcpServers": {
      "repowise": {
        "command": "python",
        "args": ["-m", "repowise.server.mcp_server"],
        "env": { "REPOWISE_WORKSPACE_ROOT": "${cwd}" }
      }
    }
  }
  ```
- **Alternative**: For a single zero-dependency C++23 native binary with instant startup, use **Red Hat Ripwire** (`redhat-et/ripwire`).
- **Followup Entry**:
  - Append to `scratchpad/followup.txt`:
    `[MCP/CODEBASE-GRAPH] https://github.com/repowise-dev/repowise - 19 MCP tools for AST call-graphs, blast radius, and test-impact analysis; cherry-pick 6 workflow skills.`
