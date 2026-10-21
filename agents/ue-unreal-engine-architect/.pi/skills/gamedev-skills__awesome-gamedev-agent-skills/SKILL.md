---
name: gamedev-skills__awesome-gamedev-agent-skills
description: Specialized capabilities and operational workflow for Unreal Engine 5 C++ & Gameplay Architecture Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: gamedev-skills__awesome-gamedev-agent-skills

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `ue-unreal-engine-architect` in the Game Engineering, Graphics & Modding Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   RunUAT.bat BuildCookRun
   ```
2. Execute core operations adhering to Unreal C++ plugins and source modules (`Source/**/*.cpp`, `Source/**/*.h`), `.uproject` configs, `Build.cs` module dependencies, and automated Unreal automation tests..
3. Run self-correction verification:
   ```bash
   Verifies build integrity via UnrealHeaderTool (UHT) pass and runs headless automation tests with `UnrealEditor-Cmd.exe MyProject -ExecCmds='Automation RunTests Project' -testexit='AllFilter passed' -nullrhi -unattended`.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with ue-unreal-engine-architect boundaries.
- Exit code 0 required on all diagnostic commands.
