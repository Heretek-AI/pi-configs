---
name: appsec-engineer/owasp-reachability-triage
description: Specialized capabilities and operational workflow for Application Security & SAST/SCA Specialist
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: appsec-engineer/owasp-reachability-triage

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `appsec-engineer` in the Defensive Security, Binary Forensics & AI Red-Teaming Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   semgrep --config=auto
   ```
2. Execute core operations adhering to Semgrep security rulepacks (`rules/security/**/*.yaml`), Trivy scan configurations, security triage reports (`docs/security/*.md`), and security regression tests..
3. Run self-correction verification:
   ```bash
   Executes `semgrep scan --error --config p/security-audit` and `gitleaks detect`; guarantees zero unmitigated high/critical CVEs and zero plaintext credentials in diffs.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with appsec-engineer boundaries.
- Exit code 0 required on all diagnostic commands.
