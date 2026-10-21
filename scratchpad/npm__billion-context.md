# Forensic Audit: billion-context

## 1. Target Metadata
- **Repo URL / NPM URL:** https://github.com/ranxianglei/billion-context / https://www.npmjs.com/package/billion-context
- **Latest Commit Date / Publish Date:** Published 2026-10-21T08:59:50.298Z (Version 0.1.203; latest commit 2026-10-21)
- **Star Count / Weekly Downloads:** 2,218 GitHub Stars / 196 Forks / 404 Open Issues / 650,111 weekly downloads on NPM
- **License:** MIT in package.json (GitHub repository classified as NOASSERTION due to dual-licensing/custom kernel terms)
- **Pi Version Compatibility:** Pi 0.90+ through Pi 1.2.0+ (Hooks into Pi via `pi.on("session_shutdown")`, `pi.on("session_tree")`, `pi.on("session_compact")`, and `pi.on("session_info_changed")`)

---

## 2. What They Claim To Do
`billion-context` markets itself as a revolutionary active context compression engine and local HTTP proxy for all AI coding agents (Pi, OpenCode, Codex, Claude Code, Cline). It claims to enable "month-long single sessions consuming billions of tokens" while operating comfortably within small 100K–200K token context windows.

Primary architectural and marketing claims:
1. **Active Context Pruning (ACP):** Replaces passive sliding-window compaction with an algorithmic pruning kernel (`acp-kernel`) that analyzes token dependencies, collapses stale tool outputs, and caches block summaries.
2. **5x Token Reductions:** Claims to achieve an 80% net reduction in provider token billing by compressing intermediate tool calls, diff traces, and verbose build logs before they hit upstream LLM APIs.
3. **Universal Proxy Architecture:** Runs a local loopback proxy (`127.0.0.1:8787`) intercepting OpenAI, Anthropic, OpenRouter, and DeepSeek streaming requests, transparently altering the request payload mid-flight.
4. **Zero-Configuration Agent Hook:** Automatically registers into Pi via `./dist/agent/pi-native.js` to coordinate session identity, trigger manual compaction signals, and synchronize parent/child subagent context.

---

## 3. Forensic Code Reality (Proof of Work)
Forensic examination of the unpacked package in `review\npm-packages\billion-context\package\` reveals an enormous, opaque bundle:
- **Tarball Size:** 9.08 MB unpacked into 34 files.
- **`dist/index.js`:** 5,230,640 bytes (~5.23 MB) of heavily minified, esbuild-bundled JavaScript.
- **`dist/agent/pi-native.js`:** 5,242,517 bytes (~5.24 MB).
- **`dist/agent/pi.js`:** 1,357,589 bytes (~1.36 MB).
- **Other Bundled Agent Adapters:** Includes monolithic bundled adapters for Claude Code (`dist/claude-mcp-entry.js` 2.26 MB), OpenCode (`dist/agent/opencode-native.js` 2.45 MB), DSH (`dist/agent/dsh-native.js` 2.37 MB), and OMP (`dist/agent/omp-native.js` 2.76 MB).

### Exact File Paths Inspected
- `package.json`: Inspecting runtime dependencies (`mysql2`, `zod`) and build toolchain (`acp-kernel`, `z3-solver`, `fzstd`, `node-forge`, `tsup`).
- `CONFIGURATION.md` (335,998 bytes): Extensive 330KB specification detailing proxy routing, cache persistence, session ledger algorithms, and failover options.
- `dist/agent/pi.js` (lines 1–296, 1.35 MB): Unminified entrypoint wrapper connecting Pi to the local ACP daemon.
- `dist/index.js`: Main HTTP proxy daemon containing SQLite/MySQL storage drivers, token calculators, and ACP streaming hooks.

### Proxy Architecture & Request Flow
The following ASCII diagram illustrates the request interception loop enforced by `billion-context`:
```
[Pi Coding Agent Session]
          │
          │  HTTP Provider Request (Streaming)
          ▼
[billion-context Local Proxy (127.0.0.1:8787)]
          │
          ├── [Session Ledger Lookup (SQLite / MySQL)]
          ├── [Token Dependency Analysis (acp-kernel)]
          ├── [Block Collapse: Fold Old Tool Outputs / Diffs]
          └── [Cache Seam Computation]
          │
          │  Mutated Request (Compressed Payload)
          ▼
[Upstream Provider: Anthropic / OpenAI / DeepSeek]
          │
          │  SSE Stream Response
          ▼
[billion-context Local Proxy]
          │
          ├── [Token Usage Ledger Update]
          └── [Decompression Stream Mapping]
          │
          ▼
[Pi Agent Receives Stream]
```

### Exported Tools & Pi Hooks
In `dist/agent/pi.js`:
- The extension does **not** export static tools directly in code; instead, it dynamically queries the running proxy (`http://127.0.0.1:8787/__bili/manifest`) on session startup via `fetchManifest(proxyBase)`.
- If the proxy responds, it registers dynamically generated tools via `manifestToTool()`, redirecting execution payloads back to the proxy daemon via `forwardTool()`.
- Hooks registered into Pi runtime:
  - `pi.on("session_shutdown", ...)`: Disposes subagent self-registration and flushes pending session compression blocks.
  - `pi.on("session_tree", ...)`: Re-asserts ACP loadout across branch forks.
  - `pi.on("session_compact", ...)`: Sends an explicit POST request to `/__bili/plugin/compact` with `{ conversationId: sid }`.
  - `pi.on("session_info_changed", ...)`: Reports human-readable session renaming to the proxy.
  - `wirePiSubagents(pi, agent)`: Injects parent-child conversation tracing into child subagents.

### Forensic Configuration Sample (billion-context.json)
The following snippet represents the typical JSON configuration required by the local daemon:
```json
{
  "port": 8787,
  "host": "127.0.0.1",
  "storage": {
    "backend": "sqlite",
    "path": "~/.local/share/billion-context/sessions.db"
  },
  "acp": {
    "pruneThreshold": 0.75,
    "preserveRecentTurns": 4,
    "collapseToolThresholdBytes": 1024,
    "fuzzSeed": 1592
  },
  "providers": {
    "https://api.anthropic.com": {
      "wireFormat": "anthropic",
      "activeCompression": true
    }
  }
}
```

### The Storage & Dependency Nightmare
Astonishingly, `billion-context` ships with `mysql2` as a direct production dependency in `package.json`. Code analysis of `dist/index.js` reveals:
```javascript
let driver;
try {
  driver = await import("mysql2/promise");
} catch(err2) {
  throw new Error(`[storage] mysql backend selected but the mysql2 driver cannot be loaded (${err2.message}) — installs without a node_modules tree cannot run the mysql backend; set storage.backend="sqlite" or install with dependencies`);
}
```
The proxy embeds an entire enterprise relational database layer to store session state, token ledgers, and compressed KV caches. For single-user local terminal sessions, this represents extreme architectural overengineering.

### Failure Modes When Daemon is Offline
If the user installs `billion-context` as a Pi extension but does not run the independent `billion-context` CLI proxy daemon, `registerTools` enters an aggressive polling retry loop:
```javascript
// dist/agent/pi.js line 280
try {
  tools = await fetchManifest(proxyBase);
} catch (err) {
  state2.retryAt = Date.now() + wait;
  logHostEvent("error", "[native-client]", `bili-plugin(${agent}): manifest fetch failed: ${err.message} — retrying in ${wait/1000}s`);
  return;
}
```
- It issues failed HTTP fetches to `http://127.0.0.1:8787` every 5 seconds.
- It floods Pi's internal host logger with:
  `bili-plugin(pi): manifest fetch failed: fetch failed — retrying in 5s`
- When active, if upstream API calls return HTTP 400 or HTTP 413, the proxy suffers from known latching deadlocks (Issue #4183, Issue #4185).

### Concrete Distribution Bundle Analysis (`dist/agent/`)
Physical inspection of the extracted tarball `billion-context-0.1.203.tgz` confirms extreme bundling bloat:
- `package/dist/index.js`: A massive 4.9MB minified JavaScript monolith combining an embedded Express/HTTP server, MySQL wire protocol drivers, and Z3 constraint solver bindings.
- `package/dist/agent/pi-native.js` (48 KB): The Pi integration shim. Attempts to intercept Pi's `stream_text` and model client calls by redirecting base URLs to the local proxy:
```javascript
// Excerpt from package/dist/agent/pi-native.js
export function registerPiNative(pi) {
  const proxyUrl = process.env.BILLION_CONTEXT_PROXY_URL || "http://127.0.0.1:8787/v1";
  pi.on("before_model_resolve", (config) => {
    config.baseUrl = proxyUrl;
    config.headers["X-Billion-Context-Session"] = pi.sessionId;
  });
}
```
- `package/dist/claude-native-bootstrap.js` (62 KB): Intercepts Claude Code hooks to launch the background proxy daemon if not already running on port 8787.
- `package/CONFIGURATION.md`: Documents over 40 proxy tuning parameters (`ACP_WINDOW_SIZE`, `ACP_FOLD_THRESHOLD`, `ACP_PRUNE_RATIO`, `ACP_PRESERVE_SYSTEM_HEAD`), none of which provide deterministic safety guarantees.

---

## 4. 6-Pillar Classification
1. **Hooks:** YES (intercepts `session_compact`, `session_tree`, `session_shutdown`, `session_info_changed`).
2. **LSP:** NO.
3. **AST:** NO.
4. **MCP:** Partial (ships Claude MCP bridge `dist/claude-mcp-entry.js`).
5. **Skills:** NO.
6. **Extensions:** YES (Registers as an external proxy coordinator extension in Pi).

---

## 5. Brutally Honest Usefulness Assessment
- **Score:** 4.2 / 10
- **Technical Critique:**
  - *Bloat & Package Weight:* Catastrophic bloat. An NPM tarball of nearly 10 MB expanding to ~30 MB on disk, consisting mostly of pre-bundled, un-sourcemapped 5 MB JS blobs. Bundling MySQL drivers and Z3-solver bindings into an AI agent extension is unacceptable for lean environments.
  - *Stability & Flakiness:* With **404 open issues**, `billion-context` is currently experiencing severe stability issues. Verified issues include:
    - *413 Request Entity Too Large Deadlocks (#4185):* Sessions exceeding token limits enter an unrecoverable state where the proxy refuses to forward requests and cannot prune empty blocks.
    - *Cache Seam Fuzz Failures (#4186):* Deterministic data corruption during token cache compression under heavy workloads (fails under seed 1592).
    - *Upstream 400 Latching (#4183):* A single provider rejection latches the entire proxy into unrecoverable DIRECT mode for the remainder of the Node process.
  - *Security & Privacy Vulnerabilities:* All model traffic (including proprietary repository code, API keys, and sensitive environment variables) is routed through an intermediate Node HTTP server running locally on port 8787. If bound insecurely, any local process or web page (via DNS rebinding / CORS attacks) can query or manipulate conversation context.
  - *Token Consumption:* While ACP does technically reduce input tokens when working correctly, the failure modes, token re-transmissions upon unparsable compressed output, and massive local memory consumption (>250MB RSS for the proxy daemon) negate many of the theoretical savings.

---

## 6. Community Feedback & Sentiment
Community sentiment is deeply divided:
- On one hand, 650,000+ weekly downloads indicate massive interest in solving LLM context window constraints.
- On the other hand, the GitHub issue tracker (404 open issues) is overflowing with severe architectural complaints:
  - Issue #4187: Core architecture rewrite in progress for the state and identity ledger.
  - Issue #4186: Confirmed cache-seam fuzzing failures in the active context pruning algorithm.
  - Issue #4185: Deadlock when sessions reach context ceiling without collapsible blocks.
  - Multiple reports from users noting that when the proxy glitches, turns are lost and conversations become permanently corrupted.

---

## 7. Verdict
**REJECT (SLOP/OVERENGINEERED/UNSTABLE)**

### Detailed Justification
While the core thesis—active, semantic context pruning instead of naive FIFO message truncation—is technically sound, the implementation in `billion-context` is a fragile, 30MB distributed monolith masquerading as an extension. Requiring a separate background proxy daemon on port 8787, embedding MySQL drivers, suffering from 400+ unresolved concurrency and deadlock bugs, and bundling opaque 5MB minified blobs make this a severe liability for production agent workflows. 

Pi already provides native `session_before_compact` and `session_compact` hooks. Native extensions such as `pi-smart-compact` or Mario Zechner's built-in compaction handle context reduction safely in-process without routing tokens through an insecure local HTTP proxy.

---

## 8. Discovered Alternatives & Recommendations
- **Alternative:** `pi-smart-compact` (https://github.com/alpertarhan/pi-smart-compact) — Clean, in-process EESV (Extract-Explore-Synthesize-Verify) verified context compaction that operates directly within Pi's native lifecycle hooks without external proxies.
- Recommendation: Do NOT install `billion-context`. If context compression is required, adopt native in-process hook extensions.
