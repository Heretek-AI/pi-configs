---
name: superpowers
description: Specialized capabilities and operational workflow for Java / Kotlin Enterprise Platform Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: superpowers

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `java-kotlin-eng` in the Core Language & Systems Engineering Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   ./gradlew test
   ```
2. Execute core operations adhering to JVM source files (`src/main/java`, `src/main/kotlin`), `build.gradle.kts` / `pom.xml`, Spring configuration properties, JPA entity models, and JUnit test suites..
3. Run self-correction verification:
   ```bash
   Executes `./gradlew check test` and verifies that all unit and integration tests pass and test coverage criteria are satisfied.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with java-kotlin-eng boundaries.
- Exit code 0 required on all diagnostic commands.
