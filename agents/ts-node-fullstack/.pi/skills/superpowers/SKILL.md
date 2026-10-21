---
name: superpowers
description: Specialized capabilities and operational workflow for TypeScript / Node.js Fullstack Systems Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `ts-node-fullstack` in the Core Language & Systems Engineering Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx tsc --noEmit
   ```
2. Execute core operations adhering to Fullstack TS codebases (`src/**/*.ts`, `src/**/*.tsx`), package dependencies, API route handlers, React Server Components, server actions, and type definitions..
3. Run self-correction verification:
   ```bash
   Executes `npx tsc --noEmit && npx vitest run` and verifies 100% type soundness and zero failing unit tests before declaring turn complete.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with ts-node-fullstack boundaries.
- Exit code 0 required on all diagnostic commands.
