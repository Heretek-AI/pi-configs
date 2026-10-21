---
name: api-contract-tester/openapi-contract-verification
description: Specialized capabilities and operational workflow for API Contract & OpenAPI / Pact Verification Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: api-contract-tester/openapi-contract-verification

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `api-contract-tester` in the Quality Assurance & Verification Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   st run openapi.yaml --base-url http://localhost:8080
   ```
2. Execute core operations adhering to Contract test suites (`tests/contracts/**`), Pact contract files (`pacts/**`), Schemathesis configurations, and mock server assertions..
3. Run self-correction verification:
   ```bash
   Runs `st run openapi.yaml --checks all` against the test server instance and verifies that all endpoints return documented HTTP status codes and matching JSON payloads.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with api-contract-tester boundaries.
- Exit code 0 required on all diagnostic commands.
