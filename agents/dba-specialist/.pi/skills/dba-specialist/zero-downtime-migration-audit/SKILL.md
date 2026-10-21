---
name: dba-specialist/zero-downtime-migration-audit
description: Specialized capabilities and operational workflow for Database Administrator & SQL Performance Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: dba-specialist/zero-downtime-migration-audit

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `dba-specialist` in the Architecture, Cloud & Infrastructure Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   sqlfluff lint
   ```
2. Execute core operations adhering to Database migrations (`migrations/**`, `prisma/migrations/**`), schema definitions (`schema.sql`), index definitions, table partition policies, and SQL performance benchmarks..
3. Run self-correction verification:
   ```bash
   Executes `sqlfluff lint --dialect postgres migrations/` and verifies that every migration contains backward-compatible down migrations and zero lock-inducing table rewrites.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with dba-specialist boundaries.
- Exit code 0 required on all diagnostic commands.
