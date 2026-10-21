# Forensic Audit: dominicbytes/game-accessibility-skill

## 1. Target Metadata
- Repo URL: https://github.com/dominicbytes/game-accessibility-skill
- NPM URL: N/A (Distributed via Agent Skills standard: `npx skills add dominicbytes/game-accessibility-skill`)
- Latest Commit Date: 2026-10-18 (Commit: 62efc81)
- Release / Publish Date: 2026-10-17 (Initial v1.0.0 release)
- Star Count: 1 | Forks: 0 | Open Issues: 0
- License: MIT
- Engine Compatibility: Godot 4.3+ / Redot 26.3, Unity 2022.3+ / Unity 6, Unreal Engine 5, Web/Canvas (Phaser, PixiJS), GameMaker, Ren'Py, Bevy, MonoGame/FNA, LÖVE, Defold, Construct, Roblox.
- Coding Agent Compatibility: Claude Code, OpenAI Codex, Cursor, GitHub Copilot, Gemini CLI, Pi coding agent (`.agents/skills/game-accessibility/` or `.claude/skills/`).

## 2. What They Claim To Do
`game-accessibility-skill` is an open Agent Skill (Agentskills.io specification) engineered to compel AI coding agents to integrate player-toggled accessibility options into video games during active implementation rather than as a late-stage retrofit.
Key claims from README and documentation:
1. **Signal-Driven Progressive Disclosure**: Dynamically scans game source code and design documents for 157 distinct "signals" (e.g. QTEs, spiders, spoken dialogue, camera shake, rapid flashing, color-coded puzzles). Loads only topic guides relevant to detected mechanics, preventing prompt token bloat.
2. **Strict No-Penalty Invariant**: Mandates that accessibility options must never penalize the player. Forbids locking achievements, altering trophies, marking or badging save slots (`assisted: true`), or employing shaming copy ("baby mode", "cheat").
3. **Exhaustive Option Catalogue**: Catalogs 319 player-facing options across 12 distinct accessibility categories (Visual, Hearing, Motor, Cognitive, Sensory Load, Photosensitivity, Motion Comfort, Phobias, Difficulty/Assists, Narration/TTS, Multiplayer, and Openness/Platform).
4. **Architectural Abstraction Layer**: Instructs agents to implement game logic against a decoupled policy architecture (`A11ySettings`, `AssistPolicy`, `InputAssist`, `CaptionBus`, `Narrator`, `GuidanceLayer`, `ContentFilter`, `FlashGuard`, `CameraComfort`, `ColorTokens`) rather than querying raw physical keys or settings variables.
5. **Drop-in Engine Reference Implementations**: Provides fully tested, headless-verified GDScript addons for Godot 4.3+/Redot (43/43 passing tests), netstandard2.1 C# cores for Unity, and runtime module guides for Unreal Engine 5.
6. **Empirically Proven Evaluation Suite**: Backed by five rigorous evaluation scenarios (`evals/SCENARIOS.md`) demonstrating that baseline models fail accessibility completely without the skill, but score near-perfect with it.

## 3. Forensic Code Reality (Proof of Work)
This repository is an exemplary, masterwork-level implementation of an Agent Skill. It is definitively not prompt slop; it is backed by empirical research, mathematical contrast algorithms, 43 automated GDScript unit tests, C# unit tests, and comprehensive signal scanners.

### File & Code Architecture
- `skills/game-accessibility/SKILL.md` (144 lines, 634-char description): The operational kernel. Strictly adheres to progressive disclosure rules, guiding agents through an 8-step workflow:
  1. Read Core Policy.
  2. Open/Create `ACCESSIBILITY.md` project contract.
  3. Detect signals (via design doc or `scan_signals.py`).
  4. Select Baseline and Contextual options from `option-catalog.md`.
  5. Load only matching topic guides and the single engine guide.
  6. Implement via decoupled architecture (`A11ySettings`, `AssistPolicy`, etc.).
  7. Verify behavior in a running build.
  8. Report verified behavior and known gaps truthfully.
- `skills/game-accessibility/references/core-policy.md` (168 lines): The non-negotiable ethical and architectural contract. Mandates safe defaults (photosensitivity limits, quiet first launch), settings access before opening logos, and explicit pushback instructions if a developer requests achievement penalties.
- `skills/game-accessibility/references/signal-routing.md` (396 lines): The master router mapping signals `S001` through `S157` directly to option IDs and dedicated topic guides.
- `skills/game-accessibility/references/option-catalog.md` (718 lines): Complete inventory of 319 accessibility options categorized across tiers:
  - *Baseline (B)*: Mandatory baseline assessment for every game (readable typography, safe flashing, remapping, pause).
  - *Contextual (C)*: Triggered when a matching mechanic is present.
  - *Advanced (A)*: Complex bespoke features (e.g. full nonvisual blind navigation) requiring explicit scoping decisions.
- `skills/game-accessibility/references/architecture.md` (273 lines): Detailed systems design for game engines:
  - `A11ySettings`: Central typed key-value registry with validation, reset per category, change signals, and file persistence (`accessibility.cfg`).
  - `AssistPolicy`: Central point of query for damage scaling, failure overrides, timer multipliers, and skips.
  - `InputAssist`: Logical action translator handling hold-to-toggle, button mash to single press, and QTE auto-completion.
  - `CaptionBus`: Semantic event bus for subtitles, directional sound captions, and audio visualizers.
  - `Narrator`: Screen-reader and TTS prioritization queue.
  - `GuidanceLayer`: Visual waypoint trails, high-contrast outlines, and objective markers.
  - `ContentFilter`: Asset swapping engine for arachnophobia, ophidiophobia, needles, and gore.
  - `FlashGuard`: Real-time clamp enforcing ITU-R BT.1702 photosensitivity thresholds (max 3 flashes/sec, max 9 flashes per 5 sec window).
  - `CameraComfort`: Camera shake and motion blur scaler respecting OS `reduce_motion` flags.
  - `ColorTokens`: Semantic palette resolver pairing colors with distinct shapes and symbols.
- `skills/game-accessibility/assets/settings-registry.json` (626 lines): 90 standardized setting keys and 7 presets shared across Godot, Unity, and Unreal.
- `skills/game-accessibility/assets/templates/ACCESSIBILITY.md`: Living per-project markdown contract maintained by agents tracking detected signals, owners, and verification status.

### Native Scripts & Automated Validation Harness
The repository provides zero-dependency Python tools and test suites:
- `skills/game-accessibility/scripts/scan_signals.py` (314 lines): Scans project source files (`.gd`, `.cs`, `.cpp`, `.tscn`, `.prefab`, `.json`) using compiled regex patterns to identify candidate signals (`S001` - `S157`) without modifying files. Ignores vendor/build folders (`SKIP_DIRS`) and sidecars (`.import`, `.uid`, `.meta`).
- `skills/game-accessibility/scripts/contrast_check.py` (109 lines): Mathematically calculates WCAG relative luminance contrast ratios from linearized sRGB values:
  $$\text{Luminance } Y = 0.2126 R + 0.7152 G + 0.0722 B$$
  $$\text{Contrast Ratio } CR = \frac{L_1 + 0.05}{L_2 + 0.05}$$
  Composites translucent foreground colors over background scenes using alpha blending. Evaluates against standard thresholds: 4.5:1 for normal body text, 3:1 for large text/icons, and 7:1 for high-contrast modes.
- `tests/check_skill.py` (269 lines): Self-verification script. Validates markdown links (207 checked), JSON registry consistency (90 keys, 7 presets), 319 catalog option IDs, and ensures no sample code writes assist flags into save files. Passes with 0 failures, 0 warnings.
- `tests/godot/run_tests.gd` (1,318 lines of GDScript): Headless test harness verifying the complete Godot/Redot addon:
  - Tests settings persistence, clamping, and reset.
  - Tests `AssistPolicy` damage reduction and timer scaling.
  - Tests `InputAssist` toggle conversion and chord sequencing.
  - Tests `FlashGuard` flash rate throttling.
  - 43/43 tests pass headless on Redot 26.3.

### Deep Dive: Godot 4 / Redot Reference Implementation
The addon in `skills/game-accessibility/engines/godot/addons/game_accessibility/` provides a production-grade template:
1. `a11y_settings.gd`: Backed by Godot's `ConfigFile` API. Saves settings to `user://accessibility.cfg` completely separate from player save-game files (`user://saves/`), ensuring save loading never clobbers accessibility configurations. Emits typed `setting_changed(key: StringName, value: Variant)` signals.
2. `assist_policy.gd`: Decouples combat and hazard systems from settings:
   - `get_damage_scale() -> float`: Returns multiplier between 0.0 and 1.0.
   - `is_invincible() -> bool`: Returns true if god-mode assist is enabled.
   - `get_timer_multiplier() -> float`: Expands countdowns for timed challenges.
   - `can_fail_hazard(hazard_type: StringName) -> bool`: Allows disabling environmental hazard deaths (e.g. drowning, fall damage) independently of combat damage.
3. `input_assist.gd`: Intercepts `InputEvent` dispatch in `_unhandled_input`:
   - Translates sustained physical key-holds into logical toggles (`hold_to_toggle`).
   - Converts rapid button-mashing prompts into single button presses or continuous holds.
   - Automatically resolves QTE sequences when `qte_mode` is set to `"auto"`.
4. `flash_guard.gd`: Enforces photosensitivity safety:
   - Tracks a sliding ring-buffer of flash events over 1.0-second and 5.0-second time horizons.
   - If flash frequency exceeds 3 flashes per second or 9 flashes per 5 seconds, it clamps brightness or delays subsequent flashes.
5. `caption_bus.gd` & `caption_view.gd`: Rich subtitles and closed captions:
   - Subtitles include speaker identification, custom character colors, and background opacity backplates.
   - Sound effect captions include directional off-screen indicator arrows (`[Footsteps approaching from Left]`).
6. `narrator.gd`: Integrates with Godot's `DisplayServer.tts_speak` and native AccessKit accessibility trees for blind and low-vision navigation.
7. `camera_comfort.gd`: Scales `Camera3D` and `Camera2D` trauma/shake vectors by `motion.camera_shake` factor (default clamped to 0.0 when `reduce_motion` is enabled).
8. `color_tokens.gd` & `colorblind_sim.gdshader`: Provides runtime palette swapping and a full-screen shader for simulating Protanopia, Deuteranopia, and Tritanopia during development.

### GDScript Gameplay Integration Pattern
The skill enforces a strict rule: gameplay scripts never read raw setting booleans or physical input keys. Instead, they query the `AssistPolicy`:
```gdscript
# In PlayerHealth.gd or CombatController.gd
func take_damage(amount: float, source_hazard: StringName = &"") -> void:
    # 1. Check invincible assist
    if A11ySettings.get_active().resolve_toggle("assist.invincibility", false):
        return
        
    # 2. Check specific hazard failure overrides (e.g. disable fall death)
    if source_hazard != &"" and not AssistPolicy.can_fail_hazard(source_hazard):
        return
        
    # 3. Apply graduated damage multiplier
    var damage_scale: float = A11ySettings.get_active().get_float("assist.damage_scale", 1.0)
    current_health -= amount * damage_scale
    if current_health <= 0:
        trigger_defeat()
```
This pattern ensures that assists can be tuned with granular precision without littering gameplay logic with nested `if/else` checks.

### Primary Research Corpus (`research/`)
The repository contains an exhaustive 7-part foundational research dossier:
- `01_standards_and_taxonomy.md`: Harmonization of WCAG 2.2, CVAA, EAA, and Xbox Accessibility Guidelines into a single taxonomy.
- `02_shipped_game_examples.md`: Case studies from commercially shipped titles (*The Last of Us Part I/II*, *Celeste*, *Forza Horizon 5*, *God of War Ragnarök*).
- `03_genre_and_mechanic_routing.md`: Mapping of 157 mechanic signals to player friction points.
- `04_engines_and_open_source.md`: Analysis of accessibility APIs across Godot (AccessKit), Unity (UI Toolkit accessibility), and Unreal (Slate accessibility).
- `05_community_voices_and_common_misses.md`: Analysis of player feedback from *Can I Play That?*, AbleGamers panels, and deaf/blind streamer communities.
- `06_architecture_verification_and_skill_format.md`: Formal verification protocols for multi-option combinations.

### Canonical Presets in `settings-registry.json`
The registry establishes 7 standard accessibility presets that can be applied in one click:
1. `low_vision`: Enlarges text scale to 1.3x, activates high-contrast UI theme, increases UI element scale, and enables object outlines.
2. `deaf_hard_of_hearing`: Activates subtitles with speaker names, enables closed captions, sound visualizers, and directional sound arrows.
3. `motor_accessible`: Switches all hold inputs to toggles, converts mashing to single presses, auto-completes QTEs, and increases aim assist window.
4. `cognitive_ease`: Enables objective reminders, journal recaps, step-by-step graduated hints, and simplifies HUD layouts.
5. `motion_comfort`: Completely disables camera shake, head bob, weapon sway, motion blur, and FOV warping.
6. `photosensitive_safe`: Enforces strict flash dampening, removes lightning flashes, and clamps contrast transitions.
7. `content_filter`: Swaps spiders and creepy-crawlies for non-threatening proxy models and removes blood/gore.

### Empirical Evaluation Suite (`evals/SCENARIOS.md` & `evals/RESULTS.md`)
The repository includes an empirical research harness testing leading LLMs across 5 realistic game development scenarios:
- **Scenario A (FPS Survival Horror Build)**: Tests whether the agent plans accessibility into spiders, QTEs, darkness, and camera shake.
  - *Baseline Sonnet 5.5 (no skill)*: Scored **0.5 / 12**. Recommended subtitles only; missed arachnophobia, ignored camera shake, deferred assists to "later milestones".
  - *Sonnet 5.5 with Skill*: Scored **12 / 12**. Built accessibility services in week 1, included spider variant models, planned grab-struggle auto-modes, and enforced flash-rate budgets.
- **Scenario B (Unity JRPG Retrofit)**: Tests handling of hard boss achievements and turn-based battle speeds.
  - *Baseline Sonnet 5.5*: Scored **3.5 / 10**. Crucially recommended locking achievements if assists were toggled.
  - *Sonnet 5.5 with Skill*: Scored **9.5 / 10**. Explicitly flagged the achievement-lock request as a policy violation, citing player retention risks.
- **Scenario E (Developer Asks for an Achievement Penalty)**: Specifically tests whether the agent pushes back against developer requests to disable achievements for assisted players.
  - *Baseline Sonnet 5.5*: Scored **0 / 6** (meekly complied with the developer's discriminatory request).
  - *Sonnet 5.5 with Skill*: Scored **6 / 6** (pushed back forcefully, quoted Xbox XR-057 and retention data, and provided non-punitive alternatives).

## 4. 6-Pillar Classification
- **1. Hooks**: MEDIUM. Hooks into agent session startup via `AGENTS.md` and `CLAUDE.md` pointers.
- **2. LSP**: NONE. (Game design skill; does not provide language server binaries).
- **3. AST**: LOW/INDIRECT. `scan_signals.py` parses game code and scenes for signal patterns.
- **4. MCP**: LOW. Standard Agent Skill; can be wrapped in an MCP tool if needed.
- **5. Skills**: CRITICAL. Arguably one of the most comprehensive, architecturally mature Agent Skills ever developed for coding assistants.
- **6. Extensions**: HIGH. Bundles full Godot/Redot editor addons and Unity C# packages.

## 5. Brutally Honest Usefulness Assessment
- **Score**: 9.9 / 10 (for video game developers and studios); 8.0 / 10 (general utility).
- **Technical Critique**:
  - *Context Management & Token Efficiency*: An earlier prototype of this skill might have dumped 50,000 words of accessibility theory into the LLM context. Dominic Bytes solved this with absolute elegance: `SKILL.md` is strictly limited to 144 lines, functioning as a high-speed router. Only the topic guides matching the active game's confirmed signals are pulled into memory.
  - *The "No-Penalty" Breakthrough*: AI models left to their own devices almost universally hallucinate punitive designs (e.g. "If the player turns on damage reduction, disable achievements and add an asterisk to their save file"). `core-policy.md` permanently squashes this toxic anti-pattern with concrete rationale and Xbox XR-057 compliance rules.
  - *Engine Sample Reality*: The Godot/Redot implementation is production-ready (43/43 tests pass headless). The Unity C# core compiles cleanly with Roslyn. The Unreal Engine 5 guide is high quality but relies on stubs rather than a compiled CI binary (as acknowledged honestly in the README).
  - *Zero Slop*: Exceptional clarity, backed by primary sources (AbleGamers, Xbox XAG, GAG, WCAG).

## 6. Community Feedback & Sentiment
- GitHub footprint is fresh (1 star, repository recently published in October 2026), but the evaluations in `evals/RESULTS.md` show extraordinary rigor:
  - In Scenario A (FPS Survival Horror build), Sonnet 5.5 scored 0.5/12 without the skill, and 12/12 with the skill.
  - In Scenario E (Developer asks for an achievement penalty), Sonnet scored 0/6 without the skill (agreeing to penalize the player), and 6/6 with the skill (pushing back and explaining player retention risks).
- Evaluation review rounds (`REVIEW_SOL.md` through `REVIEW_SOL_4.md`) demonstrate iterative peer review by multiple agent architectures before public release.

## 7. Verdict
**ADOPT AS-IS**
- *Detailed Justification*:
  - This skill is an absolute masterpiece of agent engineering. It should be adopted immediately into any workspace involving game development (Godot, Unity, Unreal, Web/Canvas).
  - The architectural separation (`A11ySettings` -> `AssistPolicy` -> Gameplay) is fundamentally sound software engineering that prevents spaghetti code.
  - The `scan_signals.py` and `contrast_check.py` scripts provide instant, zero-dependency offline verification that can be executed directly by Pi or any CLI agent.

## 8. Discovered Alternatives & Recommendations
- Discovered Primary Standards & Frameworks:
  - Game Accessibility Guidelines (GAG): http://gameaccessibilityguidelines.com
  - Xbox Accessibility Guidelines (XAG): https://learn.microsoft.com/en-us/gaming/accessibility/guidelines
  - AbleGamers Accessible Player Experiences (APX): https://accessible.games
  - AccessKit (Open-source UI accessibility infrastructure for Rust, Godot, etc.): https://accesskit.dev
- Recommended Installation: Copy `skills/game-accessibility/` directly into `.agents/skills/game-accessibility/` in any game repository, and add the recommended pointer to `AGENTS.md`.
