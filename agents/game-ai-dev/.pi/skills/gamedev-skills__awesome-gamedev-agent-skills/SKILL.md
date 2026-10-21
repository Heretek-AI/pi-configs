---
name: gamedev-skills__awesome-gamedev-agent-skills
description: Specialized capabilities and operational workflow for Game AI & Autonomous Decision Systems Programmer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: gamedev-skills__awesome-gamedev-agent-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `game-ai-dev` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   godot --headless --script test/ai/test_navmesh.gd
   ```
2. Execute core operations adhering to AI actor controllers (`ai/**`, `scripts/ai/**`), behavior tree definition files, perception stimulus handlers, blackboard memory stores, and AI simulation regression tests..
3. Run self-correction verification:
   ```bash
   Executes headless simulation loop validating pathfinding convergence across 1,000 randomized start/target coordinates with zero deadlocks or oscillation traps.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with game-ai-dev boundaries.
- Exit code 0 required on all diagnostic commands.
