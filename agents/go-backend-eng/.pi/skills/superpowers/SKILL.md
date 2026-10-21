---
name: superpowers
description: Specialized capabilities and operational workflow for Go High-Concurrency Backend Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `go-backend-eng` in the Core Language & Systems Engineering Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   golangci-lint run
   ```
2. Execute core operations adhering to Go microservices (`cmd/**`, `pkg/**`, `internal/**`), `go.mod`, gRPC service definitions, database query repositories, and race condition test suites..
3. Run self-correction verification:
   ```bash
   Executes `golangci-lint run ./... && go test -race ./...`; verifies zero lint issues, zero race conditions, and complete test suite passes before turn yield.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with go-backend-eng boundaries.
- Exit code 0 required on all diagnostic commands.
