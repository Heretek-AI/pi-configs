---
name: threat-modeler
description: Specialized capabilities and operational workflow for Threat Modeling & Zero-Trust Architecture Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: threat-modeler

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `threat-modeler` in the Defensive Security, Binary Forensics & AI Red-Teaming Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   git status
   ```
2. Execute core operations adhering to Threat models (`docs/threat-models/*.md`), data flow diagrams with trust boundaries, privilege escalation matrices, and mitigation backlogs..
3. Run self-correction verification:
   ```bash
   Validates that every identified entry point in the architecture has an associated STRIDE category, impact score (DREAD), and concrete mitigation action item.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with threat-modeler boundaries.
- Exit code 0 required on all diagnostic commands.
