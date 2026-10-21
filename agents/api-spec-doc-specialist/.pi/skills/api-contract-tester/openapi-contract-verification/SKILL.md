---
name: api-contract-tester/openapi-contract-verification
description: Specialized capabilities and operational workflow for OpenAPI, AsyncAPI & Protobuf API Documentation Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: api-contract-tester/openapi-contract-verification

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `api-spec-doc-specialist` in the Executive, Product & Documentation Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   npx @stoplight/spectral-cli lint
   ```
2. Execute core operations adhering to `openapi.yaml`, `asyncapi.yaml`, `proto/**/*.proto`, API reference portals, and SDK contract docstrings..
3. Run self-correction verification:
   ```bash
   Runs `npx @stoplight/spectral-cli lint openapi.yaml --ruleset .spectral.yaml` and `buf lint`; checks that zero schema warnings or missing schema models remain.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with api-spec-doc-specialist boundaries.
- Exit code 0 required on all diagnostic commands.
