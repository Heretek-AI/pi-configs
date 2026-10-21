---
name: juvio15__pi-ast-grep
description: Specialized capabilities and operational workflow for Tree-sitter Structural Search & AST Refactoring Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: juvio15__pi-ast-grep

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `ast-structural-refactorer` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   ast-grep scan
   ```
2. Execute core operations adhering to `sgconfig.yml`, structural AST rewrite patterns (`rules/ast-grep/**`), dry-run preview verification manifests, and multi-file code structural migrations..
3. Run self-correction verification:
   ```bash
   Executes dry-run preview (`ast-grep run --pattern ... --rewrite ... --json`) and inspects diffs via `git diff` to ensure zero accidental semantic alterations before applying changes.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with ast-structural-refactorer boundaries.
- Exit code 0 required on all diagnostic commands.
