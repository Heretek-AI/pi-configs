---
name: superpowers/git-worktrees
description: Specialized capabilities and operational workflow for Git Worktree, Merge & Branch Drift Coordinator
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers/git-worktrees

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `git-drift-coord` in the Architecture, Cloud & Infrastructure Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   git status
   ```
2. Execute core operations adhering to Git worktree staging scripts, branch sync automation, rebase conflict mediation strategies, merge pull request gates, and commit hygiene guidelines..
3. Run self-correction verification:
   ```bash
   Executes `git status --porcelain` and `git log -1` to verify zero untracked conflict markers (`<<<<<<<`) and verifies clean fast-forward rebase before closing merge tasks.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with git-drift-coord boundaries.
- Exit code 0 required on all diagnostic commands.
