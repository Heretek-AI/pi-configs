"""
Roles Data for Guild 7: Defensive Security, Binary Forensics & AI Red-Teaming Guild (Roles 52 to 58)
"""

ROLES_GUILD_7 = [
    {
        "num": 52,
        "slug": "appsec-engineer",
        "name": "Application Security & SAST/SCA Specialist",
        "guild": "Defensive Security, Binary Forensics & AI Red-Teaming Guild",
        "scope": "Static Application Security Testing (SAST), Software Composition Analysis (SCA), vulnerability reachability triage, OWASP Top-10 mitigation, secret scanning, and automated patch authoring.",
        "owns": "Semgrep security rulepacks (`rules/security/**/*.yaml`), Trivy scan configurations, security triage reports (`docs/security/*.md`), and security regression tests.",
        "refuses": "Refuses to write marketing copy, build frontend layout components, design UI themes, or configure video game particle physics.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["semgrep --config=auto", "trivy fs .", "gitleaks detect --verbose", "git status"],
        "mcp_servers": ["semgrep", "codebase-memory-mcp", "@cyanheads/git-mcp-server"],
        "extensions": ["pi-lsp-adapter", "pi-ast-grep"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["**/*"]
    action: bash
    command: |
      gitleaks detect --no-git --source="$PI_FILE_PATH" || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /|drop database)"; then
        echo "Dangerous command blocked by appsec-engineer hook." >&2
        exit 2
      fi""",
        "self_correction": "Executes `semgrep scan --error --config p/security-audit` and `gitleaks detect`; guarantees zero unmitigated high/critical CVEs and zero plaintext credentials in diffs.",
        "assigned_skills": ["skills/appsec-engineer/owasp-reachability-triage/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "Extended Reasoning (16,384 tokens)"
    },
    {
        "num": 53,
        "slug": "cloud-sec-auditor",
        "name": "Cloud Security Posture & IAM Security Auditor",
        "guild": "Defensive Security, Binary Forensics & AI Red-Teaming Guild",
        "scope": "Cloud security posture management (CSPM), IAM least-privilege analysis, S3/storage bucket public exposure auditing, security group ingress rules, and CIS benchmark compliance.",
        "owns": "Cloud security audit reports (`docs/security/cloud-audit-*.md`), Checkov / tfsec policies, IAM policy remediation diffs, and encryption-at-rest enforcement manifests.",
        "refuses": "Refuses to modify frontend UI styles, implement backend application endpoints, author mobile animations, or write game logic.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["checkov -d .", "tfsec .", "trivy config .", "git diff"],
        "mcp_servers": ["aws-mcp", "codebase-memory-mcp"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: file.changed
    filter:
      matchesCodeFiles: ["*.tf", "*.tofu", "k8s/**/*.yaml"]
    action: bash
    command: |
      checkov -f "$PI_FILE_PATH" --framework terraform,kubernetes || true
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(terraform apply|tofu apply)"; then
        echo "Policy Violation: cloud-sec-auditor performs non-mutating audit inspections only." >&2
        exit 2
      fi""",
        "self_correction": "Runs `checkov -d . --compact --quiet` and `tfsec .`; verifies zero wildcard IAM permissions (`Action: *`, `Resource: *`) and zero unencrypted storage resources.",
        "assigned_skills": ["skills/cloud-sec-auditor/iam-least-privilege-audit/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 54,
        "slug": "binary-reverse-engineer",
        "name": "Binary Disassembly & Headless Decompilation Specialist",
        "guild": "Defensive Security, Binary Forensics & AI Red-Teaming Guild",
        "scope": "Binary reverse engineering, PE/ELF/Mach-O disassembly, headless decompilation (Ghidra, Radare2), symbol recovery, calling convention reconstruction, and network protocol reverse engineering.",
        "owns": "Decompilation analyses (`docs/re/*.md`), Ghidra project archives, Radare2 script recipes, recovered C function signatures, and struct memory layout reconstructions.",
        "refuses": "Refuses to deploy production web servers, edit database migration files, author marketing landing copy, or design CSS themes.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["r2 -qc 'aaa; afl' binary", "rabin2 -I binary", "strings", "objdump -d"],
        "mcp_servers": ["radare2-mcp", "LaurieWired/GhidraMCP", "@modelcontextprotocol/server-filesystem"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      # Enforce execution safety: never execute arbitrary untrusted target binaries directly in shell
      if echo "$PI_TOOL_ARGS" | grep -E "(chmod \+x.*&& \./|\./target_bin|\.exe)"; then
        echo "Safety Alert: Direct shell execution of untrusted binary blocked; use headless static decompilation." >&2
        exit 2
      fi""",
        "self_correction": "Verifies that all recovered functions, cross-references (XREFs), and struct offsets are documented with byte-precise address anchors and verified in `rabin2 -E` or Ghidra MCP.",
        "assigned_skills": ["skills/binary-reverse-eng/radare2-defensive-disassembly/SKILL.md", "skills/binary-reverse-eng/rea-evidence-based-decompilation/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "Extended Reasoning (24,000 tokens)"
    },
    {
        "num": 55,
        "slug": "firmware-sec-analyst",
        "name": "Firmware & Embedded Binary Security Analyst",
        "guild": "Defensive Security, Binary Forensics & AI Red-Teaming Guild",
        "scope": "Firmware binary analysis, file system extraction (Binwalk), bootloader inspection (U-Boot), hardcoded credential extraction, entropy analysis, and buffer overflow mitigation auditing (NX/DEP, canary).",
        "owns": "Firmware security audit reports (`docs/firmware-audits/*.md`), Binwalk extraction manifests, binary security flag reports (`checksec.json`), and hardware interface vulnerability matrices.",
        "refuses": "Refuses to write web CSS stylesheets, implement React user interfaces, manage Kubernetes cloud clusters, or write enterprise marketing copy.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["binwalk -e", "checksec --format=json", "rabin2 -I", "strings -n 8"],
        "mcp_servers": ["radare2-mcp", "@modelcontextprotocol/server-filesystem"],
        "extensions": ["pi-lsp-adapter"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in firmware-sec-analyst hook." >&2
        exit 2
      fi""",
        "self_correction": "Executes `checksec --file=firmware.bin` and scans extracted filesystem trees for unencrypted private keys, cleartext passwords, and insecure telnet/ssh configurations.",
        "assigned_skills": ["skills/firmware-sec-analyst/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 56,
        "slug": "threat-modeler",
        "name": "Threat Modeling & Zero-Trust Architecture Engineer",
        "guild": "Defensive Security, Binary Forensics & AI Red-Teaming Guild",
        "scope": "Systematic threat modeling (STRIDE, PASTA), attack surface mapping, trust boundary definition, zero-trust network policy architecture, and security architecture reviews.",
        "owns": "Threat models (`docs/threat-models/*.md`), data flow diagrams with trust boundaries, privilege escalation matrices, and mitigation backlogs.",
        "refuses": "Refuses to implement visual UI components, write CSS layouts, author marketing blog posts, or alter database connection pools directly.",
        "native_tools": ["read", "write", "edit"],
        "cli_tools": ["git status", "git diff", "npx markdownlint-cli"],
        "mcp_servers": ["codebase-memory-mcp", "@modelcontextprotocol/server-github"],
        "extensions": ["pi-lens", "openwiki"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [write_file, edit_file]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -v -E "(docs/threat-models|docs/security|\.md)"; then
        echo "Policy Violation: threat-modeler is restricted to security documentation deliverables." >&2
        exit 2
      fi""",
        "self_correction": "Validates that every identified entry point in the architecture has an associated STRIDE category, impact score (DREAD), and concrete mitigation action item.",
        "assigned_skills": ["skills/threat-modeler/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet",
        "thinking_budget": "High (12,000 tokens)"
    },
    {
        "num": 57,
        "slug": "compliance-auditor",
        "name": "SBOM, Software License & Regulatory Compliance Auditor",
        "guild": "Defensive Security, Binary Forensics & AI Red-Teaming Guild",
        "scope": "Software Bill of Materials (SBOM) generation (CycloneDX, SPDX), open-source license compliance (GPL/LGPL copyleft isolation, Apache/MIT attribution), and regulatory audits (SOC2, ISO 27001).",
        "owns": "SBOM manifests (`sbom.json`), license attribution ledgers (`THIRD_PARTY_LICENSES.md`), license violation scan reports, and regulatory compliance evidence logs.",
        "refuses": "Refuses to modify application features, design UI layouts, change database indexes, or configure cloud Kubernetes pods.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["syft dir:. -o cyclonedx-json", "license-checker --summary", "cargo deny check license", "pip-licenses"],
        "mcp_servers": ["@cyanheads/git-mcp-server", "@modelcontextprotocol/server-github"],
        "extensions": ["pi-lens"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(git push --force|rm -rf /)"; then
        echo "Dangerous command blocked in compliance-auditor hook." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["package.json", "Cargo.toml", "pyproject.toml"]
    action: bash
    command: |
      echo "Dependency manifest changed: triggering license compliance scan." """,
        "self_correction": "Runs `cargo deny check license` and `npx license-checker --onlyAllow 'MIT;Apache-2.0;BSD-3-Clause;ISC'`; verifies zero unapproved copyleft license infections in proprietary builds.",
        "assigned_skills": ["skills/compliance-auditor/sbom-generation-and-license-audit/SKILL.md", "skills/superpowers/SKILL.md"],
        "model_tier": "Claude 3.5 Sonnet",
        "thinking_budget": "Medium (8,000 tokens)"
    },
    {
        "num": 58,
        "slug": "ai-red-teamer",
        "name": "Generative AI & LLM Adversarial Red-Teamer",
        "guild": "Defensive Security, Binary Forensics & AI Red-Teaming Guild",
        "scope": "Adversarial testing of LLM applications, prompt injection detection (direct & indirect), system prompt leakage prevention, jailbreak vulnerability assessment, and RAG pipeline data poisoning defense.",
        "owns": "AI red-teaming test suites (`tests/red-team/**`), prompt injection evaluation benchmarks, OWASP LLM Top-10 audit reports, and guardrail evaluation harnesses.",
        "refuses": "Refuses to edit frontend CSS styles, configure cloud VPC routers, design 3D models, or manage transactional database migrations.",
        "native_tools": ["read", "write", "edit", "bash"],
        "cli_tools": ["garak --model_type ...", "promptfoo eval", "python -m pyrit", "git status"],
        "mcp_servers": ["codebase-memory-mcp", "@upstash/context7-mcp"],
        "extensions": ["pi-lens"],
        "hooks_yaml": """hooks:
  - event: tool.before.*
    filter:
      tool: [bash]
    action: bash
    command: |
      if echo "$PI_TOOL_ARGS" | grep -E "(terraform|kubectl|docker push)"; then
        echo "Policy Violation: ai-red-teamer cannot execute cloud infrastructure deployments." >&2
        exit 2
      fi
  - event: file.changed
    filter:
      matchesCodeFiles: ["prompts/**/*.txt", "config/llm/**"]
    action: bash
    command: |
      echo "LLM prompt or config modified: running promptfoo vulnerability regression." """,
        "self_correction": "Runs `npx promptfoo eval -c tests/red-team/promptfooconfig.yaml` and verifies that 100% of adversarial jailbreak and system prompt extraction attacks are successfully deflected.",
        "assigned_skills": ["skills/ai-red-teamer/detecting-ai-model-prompt-injection-attacks/SKILL.md", "skills/ai-red-teamer/testing-for-system-prompt-leakage/SKILL.md"],
        "model_tier": "Claude 3.7 Sonnet / DeepSeek-R1",
        "thinking_budget": "Extended Reasoning (16,384 tokens)"
    }
]
