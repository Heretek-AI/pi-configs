---
name: gamedev-skills__awesome-gamedev-agent-skills
description: Specialized capabilities and operational workflow for Creative Narrative Director & Worldbuilding Architect
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: gamedev-skills__awesome-gamedev-agent-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `creative-narrative-director` in the Executive, Product & Documentation Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   jq
   ```
2. Execute core operations adhering to Worldbuilding bibles (`docs/lore/*.md`), dialogue trees (`dialogue/*.json`, `narrative/*.yarn`), quest structures, and faction lore dossiers..
3. Run self-correction verification:
   ```bash
   Executes syntax validation over YarnSpinner or dialogue JSON trees via `npx yarnspinner-validator narrative/*.yarn` and cross-checks character tone consistency against lore profiles.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with creative-narrative-director boundaries.
- Exit code 0 required on all diagnostic commands.
