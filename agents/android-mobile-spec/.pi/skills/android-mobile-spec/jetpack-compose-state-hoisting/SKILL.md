---
name: android-mobile-spec/jetpack-compose-state-hoisting
description: Specialized capabilities and operational workflow for Android Kotlin / Jetpack Compose Mobile Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: android-mobile-spec/jetpack-compose-state-hoisting

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `android-mobile-spec` in the Core Language & Systems Engineering Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   ./gradlew testDebugUnitTest
   ```
2. Execute core operations adhering to Android source files (`app/src/main/java/**`, `app/src/main/kotlin/**`), `build.gradle.kts`, `AndroidManifest.xml`, Compose screens, and Android UI tests..
3. Run self-correction verification:
   ```bash
   Runs `./gradlew testDebugUnitTest && ./gradlew lintDebug` to verify unit test passes and ensure zero fatal Android Lint errors before turn yield.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with android-mobile-spec boundaries.
- Exit code 0 required on all diagnostic commands.
