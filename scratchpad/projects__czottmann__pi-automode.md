# Forensic Audit: czottmann/pi-automode

## 1. Target Metadata
- Repo URL: https://github.com/czottmann/pi-automode
- NPM URL: https://www.npmjs.com/package/@czottmann/pi-automode
- Latest Commit Date: 2026-09-25 (Commit: e69c020)
- Release / Publish Date: 2026-09-25 (v1.17.0)
- Star Count: 195 | Forks: 36 | Open Issues: 14
- License: MIT
- Pi Version Compatibility: Pi (>= 0.86.0) and Oh My Pi (OMP >= 18). Peer dependencies: `@earendil-works/pi-ai`, `@earendil-works/pi-coding-agent`, `@earendil-works/pi-tui`, `typebox`. Runtime dependency: `unbash` (4.0.10).

## 2. What They Claim To Do
`pi-automode` promises a Claude Code-style autonomous execution mode with multi-tiered guardrails for Pi and Oh My Pi (OMP).
Key claims from README and documentation:
1. **Pre-Execution Tool Call Interception**: Intercepts every tool call made by the coding agent before it reaches the operating system or runtime.
2. **Tri-Tier Defense Strategy**:
   - *Tier 1: Explicit Permission Rules*: Fast path matching against user-defined allow/deny patterns for tool names and target file paths.
   - *Tier 2: Deterministic Hard Deny*: Zero-latency deterministic checks blocking dangerous shell invocations (e.g., `rm -rf /`, `curl | bash`, modifications to `.git`, `.ssh`, `.env`, or Pi configuration files).
   - *Tier 3: LLM Classifier Verification*: An asynchronous classifier model evaluates ambiguous commands in context against security policies before granting execution.
3. **AST-Level Bash Inspection**: Leverages `unbash` to parse shell strings into Concrete Syntax Trees (CST/AST), inspecting nested command substitutions, pipeline sequences, and output redirection targets.
4. **Persistent TUI Status Widget**: Displays real-time metrics in the terminal status bar (`AM ● a:12 d:2 ca:5 cd:1`) showing allowed vs. denied actions and classifier breakdown.
5. **Agent Self-Diagnosis Tool**: Provides a model-callable read-only tool (`automode_inspect`) enabling the agent to understand why its previous action was blocked without leaking secret credentials.

## 3. Forensic Code Reality (Proof of Work)
This project is an exceptional example of defensible systems engineering in the agentic ecosystem. Rather than relying on fuzzy prompt-level instructions ("please don't delete system files"), `pi-automode` implements hard programmatic gates.

### File & Code Architecture
- `package.json`: Packages the extension with entry `./extensions/auto-mode.ts` and skills `./skills`. Clean separation of concerns with minimal external runtime dependencies (`unbash` 4.0.10).
- `extensions/auto-mode.ts` (10 lines): Minimal shim delegating directly to `extension.ts`.
- `extensions/auto-mode/extension.ts` (972 lines): The core hook manager and runtime coordinator. Sets up lifecycle handlers, manages state transitions, and wires up TUI status updates.
- `extensions/auto-mode/bash.ts` (692 lines): Integrates the `unbash` parser to deconstruct bash syntax trees. Inspects AST nodes:
  - `Redirect`: Detects file truncation operators (`>`, `>>`, `&>`).
  - `EffectiveCommand`: Extracts command name and argument vectors across chained commands (`&&`, `||`, `;`, `|`).
  - Identifies dynamic name expansions, arithmetic expansions, and nested subshells up to depth 16.
- `extensions/auto-mode/hard-deny.ts` (150 lines): Implements deterministic safety rules without invoking an LLM. Blocks modifications to protected directories (`.ssh`, `.gnupg`, `/etc`, Windows system folders, Pi internal configuration).
- `extensions/auto-mode/classifier.ts` (390 lines): Secondary evaluation layer. Packages the pending tool call, recent conversation transcript context, and policy rules into a lightweight prompt evaluated by a user-selected small/fast model (e.g., Haiku or GPT-5.4-mini).
- `extensions/auto-mode/paths.ts` (310 lines): Resolves relative and absolute file paths against current working directory and symlinks (`realpathSync`), preventing directory traversal escapes (`../../etc/passwd`).
- `extensions/auto-mode/permissions.ts` (340 lines): Fast glob and regex matching engine for tool call arguments.
- `extensions/auto-mode/state.ts` (370 lines): In-memory and persisted counters tracking allowed actions, denials, and classification statistics.
- `extensions/auto-mode/log.ts` (180 lines): Writes structured JSONL decision logs with unique decision IDs for every intercepted action.
- `skills/automode-diagnostics/SKILL.md`: Skill providing structured instructions for agents on how to recover gracefully when blocked by automode.

### AST Analysis Deep Dive (`bash.ts`)
The `bash.ts` engine is one of the most sophisticated shell analyzers in the agent ecosystem:
- Rather than matching raw strings with regular expressions (which fails against shell tricks like `r\m -r\f` or `eval $(echo ...)`), it passes shell scripts into `unbash.parse()`.
- The parser builds a complete `ParsedScript` syntax tree. `bash.ts` traverses the AST recursively up to `MAX_NESTED_SHELL_DEPTH = 16`.
- Extracts `EffectiveCommand` instances:
  - Normalizes quote removals and tilde expansions (`~` -> `$HOME`).
  - Identifies transparent dispatchers (`sudo`, `env`, `xargs`, `nohup`, `nice`) and unwraps them to find the true underlying executable.
  - Flags dynamic constructs: `dynamicName` (command name derived from variable `$CMD`), `dynamicShellScript` (`bash -c "$VAR"`), and dynamic redirection targets (`> "$FILE"`).
- If a command cannot be statically resolved due to dynamic expansion, automode treats it as opaque and escalates directly to Tier 3 LLM classification or blocks it if configured in strict mode.

### Deterministic Hard-Deny Rules (`hard-deny.ts`)
Runs with zero API overhead and sub-millisecond latency. Evaluates against:
1. **Critical System Paths**: Blocks writes or deletions targeting:
   - Linux/macOS: `/`, `/bin`, `/boot`, `/dev`, `/etc`, `/lib`, `/proc`, `/root`, `/sys`, `/usr`.
   - Windows: `C:\Windows`, `C:\Program Files`, `System32`, `SAM`.
   - User Security: `~/.ssh`, `~/.gnupg`, `~/.aws`, `~/.config/gcloud`, `~/.pi/credentials.json`.
   - Repository Metadata: `.git/config`, `.git/hooks`, `.git/objects`.
2. **Dangerous Command Signatures**:
   - Destructive filesystem commands: `mkfs`, `dd if=/dev/zero`, `fdisk`, `shred`.
   - Privilege escalations: `chmod 777 /`, `chown root`, unauthorized `visudo`.
   - Obfuscated reverse shells: `/dev/tcp/*`, netcat listener spawns (`nc -lvnp`).
   - Fork bombs: `:(){ :|:& };:`.

### Configuration File Schema (`config.json`)
The extension resolves configuration hierarchically from global user settings (`~/.pi/agent/extensions/pi-automode/config.json`) and optional project-local overrides (`.pi/automode.json`):
```json
{
  "enabled": true,
  "classifier": {
    "model": "anthropic/claude-3-5-haiku",
    "temperature": 0.0,
    "timeoutMs": 5000,
    "failClosed": true
  },
  "rules": {
    "allow": [
      { "tool": "read_file" },
      { "tool": "search_files" },
      { "tool": "bash", "command": "^(git status|git diff|npm test|cargo test)" }
    ],
    "deny": [
      { "tool": "write_file", "path": ".*\\.(env|pem|key)$" },
      { "tool": "bash", "command": "rm -rf (\\/|~)" }
    ]
  },
  "protectedPaths": [
    ".git",
    ".ssh",
    "node_modules",
    "~/.pi"
  ],
  "observability": {
    "logFile": "~/.pi/agent/extensions/pi-automode/decisions.jsonl",
    "verbose": false
  }
}
```

### AST Visitor Pattern in `bash.ts`
When an agent calls the `bash` tool with a command string:
1. `bash.ts` invokes `unbash.parse(commandText)` to obtain a syntax tree.
2. If `unbash` throws a syntax error (e.g. malformed quote, unbalanced parenthesis), automode treats the string as potentially obfuscated and intercepts it immediately with `BashAnalysisError`.
3. If parsing succeeds, `bash.ts` applies a visitor pattern across all statements in the AST:
   - Evaluates `LogicalExpression` nodes (`&&`, `||`): verifies that every constituent sub-command is individually permitted. A single denied command in a chain (e.g. `npm test && rm -rf /`) rejects the entire pipeline.
   - Evaluates `Pipeline` nodes (`|`): checks pipe sources and sinks. Blocks piped execution into interpreters (`curl ... | bash`, `wget -O - ... | sh`, `cat payload | python`).
   - Evaluates `Redirect` nodes: extracts target paths for `>`, `>>`, `&>`. If a redirection target points into a protected directory (e.g. `echo malicious > ~/.bashrc`), the command is hard-denied regardless of what command produced the stdout.
   - Evaluates variable substitutions (`${VAR}`): if an environment variable expansion targets a command position and cannot be statically evaluated against safe defaults, it is flagged as `dynamicName` and forwarded to the classifier.

### Terminal UI Statusline Integration
When the terminal supports full TUI rendering via `@earendil-works/pi-tui`:
- `state.ts` maintains an in-memory counter of all evaluations:
  - `allowedCount`: total allowed operations.
  - `deniedCount`: total denied operations across all tiers.
  - `classifierAllowedCount` & `classifierDeniedCount`: decisions made specifically by Tier 3 LLM classification.
- Formats a compact statusline segment:
  `AM ● a:14 d:1 ca:4 cd:1`
- The widget uses ANSI color coding: green dot `●` for active automode, yellow warning indicators when classifier evaluations are pending, and red increments on denial events.

### Tier 3 LLM Classifier Flow (`classifier.ts`)
When a command is neither explicitly allowed nor hard-denied:
1. Automode extracts the pending tool name, exact arguments, and current conversation goals from recent transcript turns.
2. Formats a structured system prompt (`AUTO_MODE_GUIDANCE`) requiring the classifier model to evaluate intent against safety boundaries.
3. Calls the designated classifier model (configured via `/automode model`, e.g., `anthropic/claude-3-5-haiku` or `openai/gpt-5.4-mini`).
4. Expects a strict JSON schema:
   ```json
   {
     "decision": "allow" | "deny",
     "reason": "Detailed justification citing specific policy",
     "confidence": 0.0 - 1.0
   }
   ```
5. If the classifier fails, times out, or returns invalid JSON, automode defaults to **fail-closed** (denial), preventing unvetted actions from executing.

### Hook & Tool Registrations
1. **Lifecycle Hooks**:
   - `pi.on("session_start", ...)`: Initializes configuration, restores denial counters, and creates logger.
   - `pi.on("before_agent_start", ...)`: Injects high-salience behavioral guardrail guidance (`AUTO_MODE_GUIDANCE`) into the system prompt.
   - `pi.on("tool_call", async (event, ctx) => ...)`: The critical blocking hook. If a tool call violates hard-deny, matches a deny rule, or fails classifier evaluation, the hook calls `event.preventDefault()` or throws an intercepted rejection, returning a structured error message to the agent model.
2. **Slash Commands**:
   - `/automode on|off`: Toggles guardrail enforcement for the active session.
   - `/automode status`: Displays active rule sets, model classifier configurations, and counters.
   - `/automode reload`: Re-reads configuration from `~/.pi/agent/extensions/pi-automode/config.json`.
   - `/automode reset`: Clears denial counters without changing rules.
   - `/automode defaults`: Prints built-in default rule tables.
   - `/automode config`: Dumps effective resolved configuration and path diagnostics.
   - `/automode denials`: Formats recent denial history with timestamps and rule triggers.
   - `/automode model [provider/model-id]`: Selects or modifies the secondary classifier LLM.
3. **Registered Diagnostic Tool**:
   - `automode_inspect`: Model-facing read-only diagnostic tool:
     - Parameters: `{ action: "status" | "config" | "defaults" | "denials" }`.
     - Output: Returns active rules, effective configuration, and recent denial reasons, enabling the agent to autonomously adapt without prompting the user.

## 4. 6-Pillar Classification
- **1. Hooks**: CRITICAL. The entire product revolves around intercepting the `tool_call` lifecycle hook to block or allow tool execution.
- **2. LSP**: NONE.
- **3. AST**: HIGH. Implements robust Bash AST parsing via `unbash` to prevent agents from obfuscating destructive commands inside bash subshells, heredocs, or chained pipelines.
- **4. MCP**: NONE. Uses native Pi tool interception.
- **5. Skills**: MEDIUM. Provides `automode-diagnostics` skill for self-healing error recovery.
- **6. Extensions**: HIGH. Clean, self-contained, and production-tested Pi extension.

## 5. Brutally Honest Usefulness Assessment
- **Score**: 9.5 / 10
- **Technical Critique**:
  - *AST Coverage Scope*: While the Bash parser (`unbash`) is outstanding for Unix shell commands, Windows PowerShell commands (e.g., `Remove-Item -Recurse`, `Set-Content`, `Start-Process`) are not parsed into PowerShell ASTs, falling back to regex/path heuristics. Windows users should be mindful of PowerShell aliases.
  - *Token Consumption for Classifier*: If users configure a slow or expensive model for Tier 3 classification, every non-trivial shell command incurs additional API latency and token cost. However, the author explicitly recommends using cheap/fast models (Claude 3.5 Haiku, Gemini Flash, or local Ollama).
  - *No OS Sandbox*: The author is commendably honest in the README: this is an agent guardrail, not an operating system sandbox. Malicious prompt injection could theoretically bypass regex filters if novel shell obfuscations evade the AST parser.
  - *Zero Slop*: 100% executable TypeScript code with 11 distinct test suites (`tests/*.test.ts`) covering bash analysis, hard-deny rules, path resolution, and classifier mock flows.

## 6. Community Feedback & Sentiment
- Stars: 195, Forks: 36. Widely regarded as the gold standard guardrail extension for Pi and Oh My Pi.
- Issue discussions show sophisticated real-world adoption:
  - Issue #77: Request for interactive "Ask on deny" (allowing the human user to manually approve a blocked tool call in the TUI without toggling automode off).
  - Issue #76: Integration with OMP built-in Ask responses as explicit authorization evidence.
  - Issue #75: Logging Jev/LLM debug exchanges per-tool-call to disk for offline compliance replay.

## 7. Verdict
**ADOPT AS-IS**
- *Justification*: `pi-automode` is essential infrastructure for autonomous Pi agent execution. Without it, running Pi with autonomous tool execution risks accidental project destruction (`git reset --hard`, accidental file deletion, clobbering configuration). Its implementation of `unbash` AST parsing alongside deterministic hard-deny rules is exemplary. It should be bundled as a core recommended security layer in standard Pi configurations.

## 8. Discovered Alternatives & Recommendations
- Discovered Alternative: `unbash` (https://github.com/czottmann/unbash or npm: `unbash`) — Fast, zero-dependency Bash parser generating clean ASTs for shell command inspection.
- Recommended Configuration: Set classifier model to `anthropic/claude-3-5-haiku` or `google/gemini-2.0-flash` for <500ms security evaluations at near-zero token cost.
