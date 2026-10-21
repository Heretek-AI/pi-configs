---
name: thedivergentai__game-dev-agentic-skills
description: Specialized capabilities and operational workflow for Godot 4 / Redot Engine Architecture Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: thedivergentai__game-dev-agentic-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `godot-redot-architect` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   godot --headless --validate-scripts
   ```
2. Execute core operations adhering to `project.godot`, scene files (`scenes/**/*.tscn`), custom GDExtensions, autoload singleton configurations, and engine export automation scripts..
3. Run self-correction verification:
   ```bash
   Executes `godot --headless --script test/runner.gd` to confirm scene instantiation, resource load times, and script static type integrity without engine runtime warnings.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with godot-redot-architect boundaries.
- Exit code 0 required on all diagnostic commands.
