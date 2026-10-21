---
name: gamedev-skills__awesome-gamedev-agent-skills
description: Specialized capabilities and operational workflow for Game Systems & Gameplay Programmer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: gamedev-skills__awesome-gamedev-agent-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `game-systems-dev` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   godot --headless --check-only
   ```
2. Execute core operations adhering to Gameplay scripts (`scripts/gameplay/**`, `src/game/**`), character controller logic, state transition graphs, weapon/combat calculation formulas, and gameplay unit tests..
3. Run self-correction verification:
   ```bash
   Executes headless gameplay validation (`godot --headless --script test/run_gameplay_tests.gd` or `cargo test --lib game`) to ensure zero regression in state transitions.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with game-systems-dev boundaries.
- Exit code 0 required on all diagnostic commands.
