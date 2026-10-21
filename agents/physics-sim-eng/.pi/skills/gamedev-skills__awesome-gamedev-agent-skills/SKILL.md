---
name: gamedev-skills__awesome-gamedev-agent-skills
description: Specialized capabilities and operational workflow for Physics Simulation & Collision Geometry Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: gamedev-skills__awesome-gamedev-agent-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `physics-sim-eng` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   cargo test physics
   ```
2. Execute core operations adhering to Physics simulation bindings (`physics/**`, `src/physics/**`), collision layer bitmasks, joint constraint setups, gravity and drag coefficients, and physics determinism tests..
3. Run self-correction verification:
   ```bash
   Runs determinism validation test verifying identical collision contact points and linear velocities across 10,000 simulated ticks with fixed delta timestamps.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with physics-sim-eng boundaries.
- Exit code 0 required on all diagnostic commands.
