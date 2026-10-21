# Forensic Audit: DevMortimer/pi-warden

## 1. Target Metadata
- Repo URL: https://github.com/DevMortimer/pi-warden
- NPM URL: https://www.npmjs.com/package/pi-warden
- Latest Commit Date: 2026-10-21 (Commit: 117a24f)
- Release / Publish Date: 2026-10-21 (v1.14.0)
- Star Count: 170 | Forks: 30 | Open Issues: 6
- License: MIT
- Pi Version Compatibility: Pi >= 0.85.1 < 2 (`@earendil-works/pi-coding-agent`, `@earendil-works/pi-tui`), Node >= 22.19.0. Runtime dependency: `pi-typesafe` (^0.10.0).

## 2. What They Claim To Do
`pi-warden` claims to be a non-intrusive harness and guardrail system for Pi that guides agent execution via cooperative steering rather than abrasive interrupts:
Key claims from README and documentation:
1. **Rule Enforcement on Every Write**: Evaluates file write actions against rules defined in `pi-warden.md` using the Jev evaluator and quotes violated project conventions back to the agent before committing.
2. **Surgical Action Holds**: Only blocks or holds genuinely destructive or irreversible operations (measured at 3 per 1,000 tool calls in production telemetry), avoiding false-positive friction.
3. **Unverified "Done" Detection**: Intercepts premature completion claims ("I have fixed the issue") when the agent has not run tests or verified the change against compiler/linter diagnostics.
4. **Stuck Loop Breaker**: Detects repetitive cycles where an agent re-tries failing commands or loops across identical tool calls without making forward progress.
5. **Tool Output Context Saver**: Automatically compresses or summarizes voluminous tool outputs (such as massive stack traces, 5,000-line test outputs, or large directory listings) to preserve prompt context, saving full transcripts to disk.
6. **Persistent Open Loops & Standing Memory**: Tracks promised future tasks across compactions (`warden_loops`) and persists lessons learned across sessions (`warden_remember`).

## 3. Forensic Code Reality (Proof of Work)
`pi-warden` is an exceptionally comprehensive code harness written in strict TypeScript. The codebase spans over 60 focused source modules in `src/` and over 35 thorough test suites.

### File & Code Architecture
- `package.json`: Exports `./dist/index.js` and extension `./dist/extension.js`. Integrates `pi-typesafe` for runtime type safety.
- `src/extension.ts` (3,911 lines): The central lifecycle nexus. Hooks into 15 distinct Pi lifecycle events to track conversation state, tool calls, and completion attempts.
- `src/rules.ts` & `src/rules-file.ts`: Parses and tokenizes project rules from `pi-warden.md`. Manages severity tiers (hard deny, steer, advise).
- `src/action-guard.ts` & `src/guard.ts`: Evaluates file edits and bash executions against the rule index and historical telemetry.
- `src/stuck.ts` & `src/loops.ts`: Analyzes sliding windows of tool calls to identify circular reasoning, repeated command failures, and stalled loops.
- `src/done.ts`: Inspects agent concluding messages. Verifies whether test tools or compiler checks were executed following file mutations; if not, injects a steering challenge prompt prompting verification before declaring victory.
- `src/compact.ts` & `src/output.ts`: Intercepts bloated tool results before they pollute the conversation context window. Trims large outputs and stores raw outputs in `.pi-warden/traces/`.
- `src/prefs.ts` & `src/sqlite-adapter.ts`: SQLite/JSONL-backed storage engine for cross-session standing lessons and developer preferences.

### Deep Dive: 15 Lifecycle Event Integrations
`src/extension.ts` binds to almost every lifecycle hook provided by `@earendil-works/pi-coding-agent`:
1. `session_start`: Resolves project paths, boots SQLite/JSONL preference storage, reads `pi-warden.md`, and sets up status bar widgets.
2. `before_agent_start`: Injects active open loops and standing project lessons into the working context.
3. `message_start` & `message_update`: Tracks model token streaming rate and monitors assistant prose in flight.
4. `agent_start`: Resets per-turn telemetry counters and arms rule violation detectors.
5. `tool_execution_start`: Records timestamp and tool parameters.
6. `tool_call`: Evaluates proposed actions against `pi-warden.md`. Holds dangerous actions or injects steering text.
7. `tool_result`: Trims bloated outputs exceeding character budgets (`maxLines`, `maxBytes`). Writes full uncompressed outputs to `.pi-warden/traces/` and indexes errors for `warden_recall`.
8. `tool_execution_end`: Finalizes execution timing metrics.
9. `turn_end`: Evaluates whether the agent respected steering directives issued during the turn.
10. `message_end`: Scans assistant completion messages for unverified "done" assertions using semantic pattern matching.
11. `agent_settled`: Updates open loop state and finalizes session cost accounting.
12. `session_before_compact`: Serializes active open loops and standing memory before the conversation transcript is pruned.
13. `session_compact`: Re-injects preserved open loops immediately after context compaction so promises are never lost.
14. `input`: Observes user feedback to calibrate preference weights and detect when the user corrects the agent.
15. `agent_end`: Flushes trace logs and closes SQLite connection pools cleanly.

### Stuck Loop Breaker (`src/stuck.ts`)
The stuck loop detector maintains a rolling window of recent tool calls (default depth: 10):
- Identifies **Command Failure Thrashing**: When the agent executes the exact same bash command 3+ times with identical non-zero exit codes.
- Identifies **Ping-Pong File Edits**: When an agent edits file A, then file B, then reverts file A back to its initial state, repeating the cycle.
- When a stuck condition is detected, Warden does not abort the run; it issues an explicit system steering directive:
  *"You have attempted this failing action 3 times without making progress. Stop and reassess your approach. Check the error log using warden_recall before trying again."*

### Project Rule Specification Format (`pi-warden.md`)
Warden introduces a structured format for declaring repository rules:
```markdown
# Project Guardrails

## Hard Deny
- Never modify database migration files once committed.
- Never write credentials, JWT tokens, or API keys directly to source files.
- Never run `git push --force` or `git reset --hard` on main/master.

## Steer (Cooperative Correction)
- Always use pnpm instead of npm or yarn in this monorepo.
- Always include comprehensive unit tests in the same directory under `*.test.ts`.
- Prefer immutable data structures; avoid mutating function parameters in-place.

## Verification Gates
- Require running `pnpm test` after modifying any file in `src/core/`.
- Require running `pnpm lint` before concluding tasks touching frontend components.
```
When an agent attempts a file write or bash invocation, Warden tokenizes the action diff and checks semantic similarity against these rule clauses using Jev. If a violation occurs, the exact rule text is quoted in the prompt feedback.

### SQLite Preference Storage Schema (`src/sqlite-adapter.ts`)
To maintain cross-session consistency without polluting repository git history, Warden persists developer corrections to a local SQLite database in `~/.pi/agent/extensions/pi-warden/warden.sqlite`:
1. `lessons`:
   - `id`: Auto-incrementing primary key.
   - `project_path`: Canonical workspace root path.
   - `session_id`: Originating conversation identifier.
   - `lesson_text`: Concrete standing directive (e.g., "Always use `tsx` when executing TypeScript scripts directly").
   - `confirmed_by_user`: Boolean flag indicating whether human verified the rule.
   - `created_at`: Epoch timestamp.
2. `open_loops`:
   - `loop_id`: Unique integer identifier within session.
   - `session_id`: Active conversation hash.
   - `status`: `"pending"` | `"completed"` | `"dropped"`.
   - `promise_text`: What the agent committed to execute.
   - `due_condition`: Trigger condition (e.g., "after tests pass").
3. `command_recall`:
   - `command_hash`: SHA-256 fingerprint of bash command.
   - `exit_code`: Numeric status code.
   - `error_excerpt`: Bounded string containing top failing lines.
   - `trace_path`: Filesystem pointer to uncompressed output log.

### Tool Output Compression Algorithm (`compact.ts` & `output.ts`)
When an agent executes an output-heavy command (e.g. `npm test` across 1,000 files generating 15,000 lines):
- Default behavior: In raw Pi, 15,000 lines would consume ~120,000 tokens, blowing past typical context limits and evicting instructions.
- Warden behavior:
  1. Captures full standard output and writes it to `.pi-warden/traces/<run_id>.log`.
  2. Parses output using family-specific extractors:
     - Vitest / Jest: Retains failure banners, failed assertions, and summary counts (e.g. "3 failed, 45 passed").
     - TypeScript Compiler (`tsc`): Retains error lines (`TS2322: Type 'X' is not assignable to 'Y'`) and line numbers, stripping redundant file paths.
     - Git: Compresses file lists exceeding 50 entries to summary headers.
  3. Returns a concise 30-line excerpt to the model, appending:
     `[Warden Context Saver: Output trimmed from 15,000 lines. Full trace saved to .pi-warden/traces/<run_id>.log. Use warden_recall to query specific errors.]`

### Completion Verification Gate (`src/done.ts`)
LLMs frequently declare tasks complete prematurely ("I have fixed the issue!") without running tests:
- `done.ts` intercepts turn conclusions containing terminal affirmations.
- Scans the session transcript since the last file mutation:
  - Did the agent execute a test suite (`npm test`, `pytest`, `cargo test`)?
  - Did the agent invoke compiler/linter diagnostics (`tsc`, `eslint`, or LSP health checks)?
- If no verification occurred, Warden intercepts the completion and injects a verification prompt:
  *"You modified 3 files but have not executed verification checks or tests. Run the project tests to confirm your changes before declaring completion."*

### Registered Tools & Parameter Schemas
1. `warden_remember`:
   - Description: Record a permanent standing instruction for this project learned from user correction.
   - Parameters: `{ lesson: string }` (max 500 characters, must follow standing directive format: "Never X" or "Always Y").
2. `warden_loops`:
   - Description: Maintain multi-step promises across turns and compactions.
   - Parameters:
     ```typescript
     {
       action: "add" | "done" | "drop" | "list",
       text?: string,  // For add: what was promised
       when?: string,  // For add: optional condition (e.g. "after CI passes")
       id?: number,    // For done/drop: loop number
       reason?: string // For drop: why no longer needed
     }
     ```
3. `warden_recall`:
   - Description: Read-only query retrieving failed command attempts, error signatures, passing checks, and paths of saved full outputs.
   - Parameters: `{}` (empty object).

### Slash Command: `/warden`
The `/warden` command exposes 18 subcommands:
- `status`: Overall health, active mode, and violation counters.
- `rules`: Lists active rules from `pi-warden.md`.
- `rules check`: Audits active rules to identify rules that cannot be evaluated effectively.
- `rules audit`: Re-judges existing project files as if they were just written.
- `rules calibrate`: Replays git commit history to detect rules that trigger too frequently.
- `rules tune`: Instructs the agent to rewrite flagged ambiguous rules.
- `loops`: Interactive viewer for active session commitments.
- `prefs`: Inspects cross-session standing memories stored in SQLite.
- `report` & `trace`: Visual inspection of recent guard actions.

## 4. 6-Pillar Classification
- **1. Hooks**: CRITICAL. Deepest lifecycle hook integration in the Pi ecosystem, utilizing almost every event offered by `@earendil-works/pi-coding-agent`.
- **2. LSP**: LOW/INDIRECT. Cooperates with LSP diagnostics to verify "done" assertions.
- **3. AST**: MEDIUM. Analyzes code and shell diff structures to detect rule violations.
- **4. MCP**: LOW. Native Pi tool interfaces.
- **5. Skills**: HIGH. Leverages `pi-warden.md` as a living skill/specification file with automated rule calibration.
- **6. Extensions**: CRITICAL. Massive TypeScript extension augmenting agent behavior and memory.

## 5. Brutally Honest Usefulness Assessment
- **Score**: 9.5 / 10
- **Technical Critique**:
  - *Complexity & Surface Area*: Because it hooks into 15 lifecycle events, any breaking changes in upstream Pi agent internals could potentially destabilize Warden's listeners. However, the author maintains comprehensive mock and lifecycle test suites (`tests/lifecycle.test.ts`, `tests/violation-pipeline.test.ts`).
  - *Context Saver Behavior*: Compressing tool outputs is brilliant for token preservation, but occasionally an agent needs an obscure line from a 2,000-line build log. Warden solves this by offering `warden_recall` and linking the full saved trace file on disk.
  - *Zero Slop*: Exceptional engineering quality. Solves the ubiquitous real-world problem of agents prematurely claiming a bug is resolved when tests have not been executed.

## 6. Community Feedback & Sentiment
- Stars: 170, Forks: 30. High respect in the community for eliminating prompt nagging in favor of deterministic code-level guardrails.
- Issue discussions:
  - Issue #187: False positive completion challenges firing after screenshot evidence exists (being actively refined).
  - Issue #127: Requests to port Pi-Warden's guard architecture to Claude Code, Codex, and OpenCode.
  - Issues #64, #65: Context saver threshold calibration algorithms.

## 7. Verdict
**ADOPT AS-IS**
- *Justification*: `pi-warden` is arguably the single most impactful code quality and reliability extension available for Pi. Its three tools (`warden_remember`, `warden_loops`, `warden_recall`) directly solve the short-term memory and context amnesia problems of LLMs. Its verification gate for completion claims stops hallucinated fixes in their tracks. It should be a standard component in any serious Pi deployment.

## 8. Discovered Alternatives & Recommendations
- Discovered Alternative: `pi-typesafe` (https://github.com/DevMortimer/pi-typesafe or npm: `pi-typesafe`) — Runtime type safety and schema validation utility powering Pi-Warden.
- Recommended Pairing: Use `pi-warden` alongside `pi-automode` for dual defense (Warden enforces code rules & verification; Automode enforces bash security & path policies).
