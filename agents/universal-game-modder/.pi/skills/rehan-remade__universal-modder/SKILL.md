---
name: rehan-remade__universal-modder
description: Specialized capabilities and operational workflow for Universal PC Game Modding & Injection Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: rehan-remade__universal-modder

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `universal-game-modder` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   python -m universal_modder.cli scan
   ```
2. Execute core operations adhering to Mod manifests, injection scripts (`mods/**`), BepInEx plugin DLLs, Harmony runtime patches, asset replacement bundles, and anti-cheat guardrails..
3. Run self-correction verification:
   ```bash
   Runs `python -m universal_modder.cli verify --staging` to verify mod loader presence, file staging paths, and anti-cheat whitelist clean status before completing run.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with universal-game-modder boundaries.
- Exit code 0 required on all diagnostic commands.
