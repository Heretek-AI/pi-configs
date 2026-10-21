---
name: superpowers
description: Specialized capabilities and operational workflow for Python Backend & Systems Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `python-backend-spec` in the Core Language & Systems Engineering Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   ruff check --fix
   ```
2. Execute core operations adhering to Python backend microservices (`app/**`, `src/**`), `pyproject.toml`, dependency lockfiles (`uv.lock` / `poetry.lock`), pytest suites, and Pydantic schemas..
3. Run self-correction verification:
   ```bash
   Runs `ruff check . && mypy --strict . && pytest` to enforce 100% type annotations, zero Ruff linter errors, and clean passing pytest results.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with python-backend-spec boundaries.
- Exit code 0 required on all diagnostic commands.
