---
name: simvyn
description: Specialized capabilities and operational workflow for iOS Swift / SwiftUI Native Mobile Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: simvyn

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `ios-mobile-spec` in the Core Language & Systems Engineering Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   xcodebuild test
   ```
2. Execute core operations adhering to Swift source files (`*.swift`), Xcode projects (`.xcodeproj`, `.xcworkspace`), `Package.swift`, Info.plist, SwiftUI views, and UI test targets..
3. Run self-correction verification:
   ```bash
   Runs `swift test` or `xcodebuild -scheme App -destination 'platform=iOS Simulator,name=iPhone 16' test` and verifies 0 build errors and 0 concurrency warnings under Swift 6 strict mode.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with ios-mobile-spec boundaries.
- Exit code 0 required on all diagnostic commands.
