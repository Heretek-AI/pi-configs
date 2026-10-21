# Forensic Audit: ben-vargas/pi-packages

## 1. Target Metadata
- Repo URL: https://github.com/ben-vargas/pi-packages
- Monorepo Packages:
  - `@benvargas/pi-synthetic-provider`
  - `@benvargas/pi-antigravity-image-gen`
  - `@benvargas/pi-exa-mcp`
  - `@benvargas/pi-firecrawl`
  - `@benvargas/pi-themes`
  - `@benvargas/pi-ancestor-discovery`
  - `@benvargas/pi-cut-stack`
  - `@benvargas/pi-openai-fast`
  - `@benvargas/pi-openai-verbosity`
  - `@benvargas/pi-claude-code-use`
  - `@benvargas/pi-model-sort`
- Latest Commit Date: 2026-10-13 (Commit: ea02a4b)
- Star Count: 126 | Forks: 15 | Open Issues: 0 (5 closed)
- License: MIT
- Pi Version Compatibility: Pi coding agent >= 0.85.0, Biome linter, Node >= 20.0.0.

## 2. What They Claim To Do
`ben-vargas/pi-packages` is a practical, developer-centric monorepo of extensions, tool connectors, themes, and quality-of-life enhancements for Pi:
1. **`pi-ancestor-discovery`**: Traverses ancestor directories up to a configurable boundary (`home` or git root) to automatically discover and register `.pi/skills`, `.agents/skills`, `.pi/prompts`, and `.pi/themes` located in parent project roots.
2. **`pi-model-sort`**: Sorts models in the `/model` picker by Most Recently Used (MRU), remembers model-specific thinking levels (e.g., DeepSeek on max, Claude on high), and boots new sessions on the last-used model without clobbering restored sessions (`-c`).
3. **`pi-synthetic-provider`**: Registers the Synthetic API provider, unlocking fast access to frontier open and proprietary Asian models (Kimi K1.6, GLM-5.3, MiniMax, Qwen-2.5, DeepSeek V4.1-Flash).
4. **`pi-antigravity-image-gen`**: Generates inline diagrams and images via Google Gemini 3 Pro image capabilities.
5. **`pi-exa-mcp` & `pi-firecrawl`**: Bridges Exa neural search and Firecrawl web scraping into model-callable agent tools.
6. **`pi-themes`**: Clean, accessible terminal themes (GitHub Light, Mono Black, Mono Light, Orng Light).
7. **`pi-cut-stack`**: Terminal text-editor shortcuts for managing cut/kill buffers in interactive prompts.
8. **`pi-openai-fast` & `pi-openai-verbosity`**: Service-tier acceleration and prompt-trimming controls for OpenAI frontier models.
9. **`pi-claude-code-use`**: Compatibility bridge for Claude OAuth tokens across Pi subagents.

## 3. Forensic Code Reality (Proof of Work)
This repository is clean, disciplined, and focused on solving concrete developer frustrations. All 11 packages are written in strict TypeScript, linted with Biome, and backed by Vitest unit tests.

### Package Architecture & Deep Technical Breakdown

#### 1. `@benvargas/pi-ancestor-discovery` (Ancestor Walking Engine)
- Problem: Pi natively discovers skills and prompts only in the immediate `cwd/.pi/` directory. When working in a monorepo subfolder (`packages/backend/`), Pi is completely blind to repository-level skills declared in the root `.pi/skills/`.
- Code Reality (`extensions/index.ts`, 286 lines):
  - Hooks into `resources_discover`.
  - Reads `pi-ancestor-discovery.json`:
    ```json
    {
      "boundary": "home",
      "resources": {
        "skills": { "enabled": true, "searchPaths": [".pi/skills", ".agents/skills"] },
        "prompts": { "enabled": false, "searchPaths": [".pi/prompts"] },
        "themes": { "enabled": false, "searchPaths": [".pi/themes"] }
      }
    }
    ```
  - Traversal loop starts at `ctx.cwd`, checks for candidate directories, checks directory existence, appends discovered paths to `skillPaths`, and moves to `dirname(dir)` until hitting `boundary` (`homedir()` or git repository root).
  - Eliminates duplicate entries and returns resolved absolute paths to the Pi engine.

#### 2. `@benvargas/pi-model-sort` (MRU & Thinking Persistence)
- Problem: The default Pi `/model` picker lists hundreds of models alphabetically by provider. Furthermore, switching from a model with high reasoning (DeepSeek) to one without reasoning (Claude) drops thinking settings, requiring constant manual adjustment.
- Code Reality (`extensions/index.ts`, 489 lines):
  - Injects monkey-patches into:
    - `ModelSelectorComponent.prototype.sortModels`: Sorts models by timestamp descending.
    - `AgentSession.prototype._cycleScopedModel`: Preserves MRU order during Ctrl+P cycling.
  - Persists timestamps to `~/.pi/agent/extensions/pi-model-sort.json`.
  - Captures `session_start` to preserve the model restored from `-c` or `--session` rather than overriding it with the global MRU model.
  - Implements `createThinkingTracker`: remembers the exact thinking level used per model (e.g. `deepseek: "max"`, `claude-3-5-sonnet: "high"`), clamping to supported levels upon model switch.

#### 3. `@benvargas/pi-synthetic-provider` (Alternative LLM Provider)
- Integrates the Synthetic API endpoint (`https://api.synthetic.new/v1`).
- Registers dynamic model definitions for frontier open-weights and specialized models:
  - MiniMax-Text-01, Kimi K1.6, GLM-5.3, Qwen-2.5-Coder-32B, DeepSeek V4.1-Flash.
- Maps API key interpolation safely using `$SYNTHETIC_API_KEY`.
- Includes slash command `/synthetic` to view remaining provider token quotas.

#### 4. `@benvargas/pi-antigravity-image-gen`
- Model-callable tool `generate_image`: takes a text prompt and aspect ratio, calls Google Gemini 3 Pro image generation API, downloads the generated PNG to the artifact directory, and emits an inline OSC 1337 / iTerm2 terminal image preview.

#### 5. `@benvargas/pi-exa-mcp` & `@benvargas/pi-firecrawl`
- Bridges web intelligence into Pi:
  - `exa_search`: Neural web search specifically tuned for code documentation and GitHub repos.
  - `firecrawl_scrape`: Scrapes web pages and bypasses anti-bot JS challenges, converting HTML to clean markdown.
  - `firecrawl_map`: Crawls an entire domain sitemap to discover documentation sub-pages.

#### 6. `@benvargas/pi-themes`
- Clean JSON theme files (`github-light-default.json`, `mono-black.json`, `mono-light.json`, `orng-light.json`). High-contrast terminal styling tailored for readability.

#### 7. `@benvargas/pi-cut-stack`
- Enhances the interactive terminal input editor. Adds readline/Emacs keybindings (`Ctrl+K` cut to end of line, `Ctrl+Y` yank from kill-ring, `Alt+Y` cycle kill-ring).

#### 8. `@benvargas/pi-openai-fast` & `@benvargas/pi-openai-verbosity`
- `/fast`: Toggles priority service tier headers for OpenAI API calls.
- `pi-openai-verbosity`: Intercepts system prompts to inject concise response style guidelines for OpenAI Codex models.

### Hook & Tool Registrations Across Packages
1. **Lifecycle Hooks**:
   - `resources_discover`: Utilized by `pi-ancestor-discovery` to surface parent skills/themes.
   - `session_start` & `model_select`: Utilized by `pi-model-sort` to record MRU usage and restore model-specific thinking depth.
   - `before_agent_start`: Utilized by `pi-openai-verbosity` to format Codex instruction density.
2. **Slash Commands**:
   - `/fast`: Toggles OpenAI priority execution tier.
   - `/synthetic`: Diagnostics and quota view for Synthetic provider models.
3. **Registered Agent Tools**:
   - `exa_search`, `exa_find_similar`
   - `firecrawl_scrape`, `firecrawl_map`, `firecrawl_crawl`
   - `generate_image` (Gemini image synthesis)

### Tool Parameter Schemas & Integration Contracts
1. `exa_search` (`@benvargas/pi-exa-mcp`):
   - Parameters:
     ```typescript
     {
       query: string,            // Search query text
       numResults?: number,      // Number of results (default: 5)
       includeDomains?: string[],// Domain filtering whitelist
       useAutoprompt?: boolean   // Neural expansion of search keywords
     }
     ```
2. `firecrawl_scrape` (`@benvargas/pi-firecrawl`):
   - Parameters:
     ```typescript
     {
       url: string,              // Target webpage URL
       formats?: ("markdown" | "html" | "rawHtml")[], // Default: ["markdown"]
       onlyMainContent?: boolean // Strips navbars, sidebars, and footers (default: true)
     }
     ```
3. `firecrawl_map` (`@benvargas/pi-firecrawl`):
   - Parameters:
     ```typescript
     {
       url: string,              // Base domain URL to crawl
       search?: string,          // Optional keyword filter
       limit?: number            // Maximum URLs to return (default: 50)
     }
     ```
4. `generate_image` (`@benvargas/pi-antigravity-image-gen`):
   - Parameters:
     ```typescript
     {
       prompt: string,           // Visual description
       aspectRatio?: "1:1" | "16:9" | "4:3" | "9:16", // Default: "1:1"
       filename?: string         // Desired output filename under .pi/images/
     }
     ```

### Security & Credential Isolation (`SECURITY.md`)
All packages adhere to strict credential isolation:
- No hardcoded API tokens or secrets in source code.
- Keys are loaded strictly from environment variables or `~/.pi/agent/credentials.json`:
  - `SYNTHETIC_API_KEY` for Synthetic provider models.
  - `EXA_API_KEY` for Exa neural search.
  - `FIRECRAWL_API_KEY` for Firecrawl scraping.
  - `GEMINI_API_KEY` for Gemini image generation.
- The repository tracks security audits and dependency vulnerabilities via `SECURITY.md`, maintaining zero open CVEs across its dependencies.

## 4. 6-Pillar Classification
- **1. Hooks**: HIGH. Critical for resource discovery (`resources_discover`) and session model tracking (`session_start`, `model_select`).
- **2. LSP**: NONE.
- **3. AST**: NONE.
- **4. MCP**: HIGH. Direct MCP and web scraping tool wrappers (`pi-exa-mcp`, `pi-firecrawl`).
- **5. Skills**: MEDIUM. Multi-root ancestor skill loader.
- **6. Extensions**: HIGH. High-value utility extensions targeting TUI ergonomics and model connectivity.

## 5. Brutally Honest Usefulness Assessment
- **Score**: 9.0 / 10
- **Technical Critique**:
  - *Monkey-Patching in `pi-model-sort`*: The model sorting extension relies on patching prototype methods on `ModelSelectorComponent` and `AgentSession`. If upstream `@earendil-works/pi-coding-agent` refactors these internal private classes, the monkey patch could silently fail or cause picker crashes. However, the author includes defensive guards and graceful fallbacks if the internal methods are missing.
  - *Exceptional Daily Ergonomics*: `pi-ancestor-discovery` solves one of the most annoying bugs in monorepos, where running Pi in `packages/backend` blinds the agent to skills stored at the monorepo root `.pi/skills`.
  - *Thinking Level Persistence*: Anyone who frequently switches between DeepSeek (which requires high/max reasoning) and Claude 3.5 Sonnet (which has no reasoning budget) knows how tedious manual re-configuration is. `pi-model-sort` makes this completely seamless.
  - *Zero Slop*: Concise, zero hallucinations, pure functional utility.

## 6. Community Feedback & Sentiment
- Stars: 126, Forks: 15.
- Maintained actively with rapid turnaround:
  - Issue #36: Clarifications on KV cache busting behavior.
  - Issue #33: Addressed subagent alias capture edge-case during Pi SDK updates.
  - Issue #21: Added thinking/reasoning effort support for GLM-5.2/5.3 and DeepSeek models.
  - 0 open issues, indicating a tight, well-supported utility library.

## 7. Verdict
**EXTRACT/CHERRY-PICK**
- *Justification*: Highly recommended for targeted installation. Specifically:
  1. **Must-Adopt**: `@benvargas/pi-ancestor-discovery` (essential for monorepos).
  2. **Must-Adopt**: `@benvargas/pi-model-sort` (essential for developer sanity in multi-model workflows).
  3. **Adopt If Needed**: `@benvargas/pi-synthetic-provider` (for cost-effective access to frontier Chinese open weights) and `@benvargas/pi-exa-mcp` (if using Exa search).

## 8. Discovered Alternatives & Recommendations
- Discovered Pattern: Ancestor walking hook (`resources_discover`) for nested project skill resolution.
- Recommended Pairing: Install `@benvargas/pi-ancestor-discovery` and `@benvargas/pi-model-sort` globally in `~/.pi/agent/extensions/`.
