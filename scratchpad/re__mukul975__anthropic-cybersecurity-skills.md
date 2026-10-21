# Forensic Audit: mukul975/anthropic-cybersecurity-skills

## 1. Target Metadata
- **Repo URL / Upstream:** https://github.com/mukul975/anthropic-cybersecurity-skills (often styled as `Anthropic-Cybersecurity-Skills`)
- **Local Review Path:** `C:\Users\derek\Desktop\Projects\pi-configs\review\reverse-engineering\anthropic-cybersecurity-skills`
- **Latest Commit Date / Release:** Mon Aug 31 04:32:42 2026 +0000 (Commit `54a7988`, active maintenance in October 2026)
- **Star Count / Forks / Issues:** 34,812 GitHub Stars / 4,228 Forks / 63 Open Issues
- **License:** Apache License 2.0 (Apache-2.0)
- **Standard & Format:** `agentskills.io` specification (Structured YAML frontmatter + Markdown procedural workflows + Python agent runners)

---

## 2. What They Claim To Do
`anthropic-cybersecurity-skills` advertises itself as *"the largest open-source cybersecurity skills library for AI agents"*. It promises to transform general-purpose LLM coding agents (Claude Code, Pi, OpenAI Codex, GitHub Copilot, Cursor, Hermes Agent) into specialized senior cybersecurity analysts, penetration testers, DFIR incident responders, and reverse engineers.

Primary claims and advertised features:
1. **818 Production-Grade Cybersecurity Skills:** Spanning **34 distinct security domains**, from cloud posture management and SOC tier-3 playbooks to binary exploitation and firmware decompilation.
2. **Six-Framework Multi-Mapping:** Maps skills across six primary industry frameworks:
   - **MITRE ATT&CK v19.1:** 805 skills mapped to 290 distinct enterprise/mobile/ICS techniques.
   - **NIST CSF 2.0:** 804 skills mapped to 106 subcategories.
   - **MITRE D3FEND:** 139 defensive countermeasure mappings.
   - **NIST AI RMF:** 97 artificial intelligence risk management mappings.
   - **MITRE F3 (Fight Fraud Framework v1.1):** 94 cyber-fraud monetization and positioning mappings.
   - **MITRE ATLAS:** 93 adversarial machine learning threat mappings.
3. **AI-Native Decision Playbooks:** Claims to bridge the 4.8 million unfilled cybersecurity workforce gap by replacing static cheatsheets with structured agent decision trees: prerequisite verification, step-by-step execution, and concrete output validation.
4. **Universal Agent Compatibility:** Compatible with 26+ agent runtimes via standard skill discovery (`npx skills add mukul975/Anthropic-Cybersecurity-Skills` or git clone).

---

## 3. Forensic Code Reality (Proof of Work)
Physical forensic inspection of `review\reverse-engineering\anthropic-cybersecurity-skills\` confirms an enormous, highly structured knowledge repository:
- **Total Indexed Skills:** Exactly **818 skills** verified in `index.json` (version `1.1.0`).
- **Physical Directory Tree:** 818 individual directories under `skills/`, each containing `SKILL.md`, `LICENSE`, and in most cases a `scripts/agent.py` and `references/` directory.
- **Repository Tooling:** 11 custom Python management and verification scripts in `tools/`.
- **Top-Level Governance & Coverage:** Includes `ATTACK_COVERAGE.md` (MITRE ATT&CK mapping), `SCOPE.md` (contribution boundaries), `CITATION.cff`, and `.claude-plugin/plugin.json`.

### The 34 Security Domains Distribution
The complete skill portfolio is distributed across 34 operational specializations:
| Domain Category | Skill Count | Core Representative Playbooks |
|---|---|---|
| Cloud Security | 66 | AWS/Azure/GCP IAM hardening, CSPM triage, CloudTrail log analysis |
| SOC Operations | 63 | Tier-1 to Tier-3 triage, alert correlation, escalation runbooks |
| Threat Hunting | 58 | Hypothesis-driven hunts, LOLBAS detection, fleet EVTX analysis |
| Threat Intelligence | 52 | STIX/TAXII pipelines, OpenCTI integration, threat actor profiling |
| Web Application Security | 46 | OWASP Top 10, blind SQLi exploitation, SSRF, Deserialization |
| Network Security | 43 | Snort/Suricata rule tuning, PCAP stream carving, Zeek analytics |
| Digital Forensics (DFIR) | 41 | Volatility3 memory dumps, Hayabusa EVTX timeline, KAPE triage |
| Identity & Access Management | 40 | Entra ID / BloodHound, Kerberoasting, Golden Ticket attacks |
| Malware Analysis | 39 | Static triage, Ghidra decompilation, Cuckoo sandbox evasion |
| Red Teaming | 35 | Active Directory Certificate Services (ADCS), C2 infrastructure |
| Container & K8s Security | 33 | Kubernetes RBAC misconfigurations, container escape, Falco rules |
| OT / ICS Security | 29 | Modbus/DNP3 anomaly detection, SCADA network segmentation |
| API Security | 28 | GraphQL introspection attacks, REST authorization bypass |
| Incident Response | 26 | Ransomware containment, live artifact preservation, IR tabletop |
| Vulnerability Management | 25 | CVSS v4 scoring, Nessus/Qualys scan ingestion, prioritization |
| Penetration Testing | 23 | Internal infrastructure assessment, privilege escalation |
| DevSecOps & Supply Chain | 26 | SBOM generation, Trivy container scanning, Sigstore signing |
| AI Security & LLM Defenses | 14 | Prompt injection defense, PyRIT red-teaming, MCP tool poisoning |
| Hardware & Firmware | 10 | CHIPSEC UEFI firmware audit, binwalk image extraction |
| Cryptography & Blockchain | 18 | Post-quantum crypto transitions, EVM smart contract reentrancy |

### The "Anthropic" Branding Reality & Provenance
A critical forensic distinction must be established:
- **Not Official Anthropic Software:** Despite the prominent repository name `Anthropic-Cybersecurity-Skills` and the official-looking banner, this repository is **completely independent and not affiliated with Anthropic PBC**.
- **Community Disclaimer:** The README explicitly contains the disclaimer: `> ⚠️ Community Project — This is an independent, community-created project. Not affiliated with Anthropic PBC.`
- **Author & Commercial Funnel:** Created by Mukul Mahipal (SRH Berlin). The repository serves as an educational showcase and marketing top-of-funnel for `casky.ai` (an agentic security playground and commercial cohort launch offering "50 Casky Tokens" for survey participation).

### Reverse Engineering & Binary Analysis Deep Dive
Physical examination of the reverse engineering and binary analysis skill cluster reveals solid, practical technical playbooks:

#### 1. Binary Exploitation (`skills/performing-binary-exploitation-analysis/`)
- `SKILL.md` (460 lines): Guides agents through memory corruption assessment on Linux ELF binaries.
- Covers binary mitigation inspection: NX/DEP, ASLR, Stack Canaries, PIE, and RELRO.
- `scripts/agent.py`: Executable helper script wrapping `checksec`, `ROPgadget`, and `pwntools`:
  ```python
  # scripts/agent.py excerpt
  try:
      from pwn import ELF, ROP
      HAS_PWNTOOLS = True
  except ImportError:
      HAS_PWNTOOLS = False

  def run_checksec(binary_path):
      """Analyzes ELF security mitigations."""
  ```

#### 2. Headless Ghidra & Radare2 Decompilation (`skills/reverse-engineering-malware-with-ghidra/`)
- `SKILL.md` (298 lines): Directs the agent to orchestrate NSA Ghidra's Headless Analyzer (`analyzeHeadless`) to decompile suspicious functions, analyze cross-references, extract cryptographic constants, and uncover C2 communication loops:
  ```bash
  # Headless Ghidra batch decompilation command pattern enforced by skill
  analyzeHeadless /tmp/ghidra_project proj -import suspicious.exe \
    -postScript DecompileAllFunctions.py /tmp/output/ \
    -deleteProject -noanalysis
  ```
- `scripts/agent.py`: Bridges Ghidra batch analysis and `r2pipe` (Radare2 Python bridge) to extract entropy curves, imports, exports, and function hashes.

#### 3. Firmware Extraction & IoT Analysis (`skills/performing-firmware-extraction-with-binwalk/`)
- `SKILL.md` (295 lines): Step-by-step firmware dissection using `binwalk -Me`, entropy profiling, squashfs extraction, and kernel symbol recovery.

#### 4. Specialized Binary Architectures
- `reverse-engineering-rust-malware`: Reversing non-null-terminated fat-pointer strings, generic monomorphization duplicates, and Result/Option unwrap chains.
- `reverse-engineering-dotnet-malware-with-dnspy`: Decompiling CIL bytecode and reversing .NET ConfuserEx / reactor obfuscation.
- `reverse-engineering-android-malware-with-jadx`: Smali and Dalvik bytecode analysis.
- `analyzing-bootkit-and-rootkit-samples`: Low-level UEFI firmware module inspection and MBR/VBR boot sector disassembly.

### Collision Detection & Quality Engineering in `tools/`
The repository authors have built commendable automated linting and quality control infrastructure:
- `tools/detect-collisions.py`: Computes semantic and keyword overlap between skills to prevent "skill collisions" where agent routers cannot distinguish between competing triggers:
  ```python
  # detect-collisions.py excerpt
  def score_pair(desc_a: str, desc_b: str) -> float:
      tokens_a = set(re.findall(r"\b\w{3,}\b", desc_a.lower()))
      tokens_b = set(re.findall(r"\b\w{3,}\b", desc_b.lower()))
      intersection = tokens_a & tokens_b
      return len(intersection) / min(len(tokens_a), len(tokens_b))
  ```
- `tools/lint-descriptions.py`: Enforces strict routing guidelines: descriptions must contain explicit activation criteria and negative trigger conditions ("when NOT to fire").
- `tools/validate-agentskills.py`: Strict schema validator enforcing `tools/agentskills-skill.schema.json` and directory name consistency.

---

## 4. 6-Pillar Classification
1. **Hooks:** NO (Contains no Pi lifecycle hooks or event listeners).
2. **LSP:** NO (Contains no Language Server Protocol servers).
3. **AST:** NO (Contains no AST parsing logic).
4. **MCP:** NO (Contains no native Model Context Protocol servers; skills recommend MCP servers like GhidraMCP externally).
5. **Skills:** YES (Primary pillar - A massive library of 818 standalone agent skills).
6. **Extensions:** NO (Does not export Pi extension commands or TUI widgets).

---

## 5. Brutally Honest Usefulness Assessment
- **Score:** 8.2 / 10 (High Domain Quality, Extreme Context Window Risk)
- **Technical Critique:**
  - *Content Depth & Authenticity:* High. Unlike low-effort prompt dumps, the individual `SKILL.md` files are exceptionally well-researched. They provide real command-line flags, exact tool paths, verified MITRE ATT&CK v19.1 technique IDs, and genuine forensic heuristics.
  - *The Monolithic Context Storm Hazard:* **Severe Danger.** Blindly installing all 818 skills into an agent's global profile (`~/.pi/skills`) will inject **over 120,000 tokens of frontmatter descriptions** into the discovery index. In Pi or Claude Code, this either crashes the runtime or consumes 60%–90% of the entire context window before the first user message is processed!
  - *Toolchain Dependency Gap:* The skills assume underlying security tools are already compiled and present in the host system PATH (`ghidra`, `volatility3`, `binwalk`, `pwntools`, `checksec`, `hayabusa`, `radare2`). On standard developer machines (especially Windows without WSL), invoking these skills without prerequisite binaries leads to immediate shell execution failures.
  - *Brand Ambiguity:* Using "Anthropic" in the title is misleading and borders on brand appropriation, although the author includes a clear disclaimer in the body.

---

## 6. Community Feedback & Sentiment
Extremely popular across the cybersecurity and AI research community:
- **34,812 GitHub Stars** and 4,228 Forks establish it as one of the most starred security prompt repositories in the world.
- 63 open issues; recent issues demonstrate active, collaborative refinement:
  - Issue #161 (open): Resolving missing `os` imports in Python agent scripts.
  - Issue #159 (open): Canonicalizing subdomain aliases across 45 skills.
  - Issues #157 / #158: Adding negative triggers and explicit keywords to zero-trust and endpoint security descriptions to improve agent routing precision.

---

## 7. Verdict
**CHERRY-PICK SPECIFIC SECURITY DOMAINS (NEVER INSTALL ALL)**

### Detailed Justification
`anthropic-cybersecurity-skills` is a treasure trove of structured offensive, defensive, and reverse-engineering tradecraft. However, due to its sheer scale (818 skills), it **must never be installed globally as an uncurated monolith**.

Recommended Adoption Strategy for `pi-configs`:
1. **Strict Rejection of Bulk Install:** Block any automated script from adding all 818 skills to Pi's global skill index to prevent immediate context exhaustion and router degradation.
2. **Curated Security Subsets:** Extract and cherry-pick specialized subsets into modular packs:
   - `pi-configs/skills/reverse-engineering`: `reverse-engineering-malware-with-ghidra`, `reverse-engineering-rust-malware`, `performing-binary-exploitation-analysis`, `performing-firmware-extraction-with-binwalk`.
   - `pi-configs/skills/dfir`: `conducting-memory-forensics-with-volatility`, `generating-forensic-timelines-with-hayabusa`.
   - `pi-configs/skills/appsec`: `analyzing-ethereum-smart-contract-vulnerabilities`, `performing-threat-modeling-with-owasp-threat-dragon`.
3. **Pair with Native MCP Tooling:** Pair these procedural text skills with active MCP execution backends such as `LaurieWired/GhidraMCP` or `radareorg/radare2-mcp` so the agent can actually execute the disassembly and decompilation commands interactively.

---

## 8. Discovered Alternatives & Recommendations
- **Alternative:** `LaurieWired/GhidraMCP` (https://github.com/LaurieWired/GhidraMCP) — Live Ghidra headless/GUI MCP server for interactive binary decompilation.
- **Alternative:** `radareorg/radare2-mcp` (https://github.com/radareorg/radare2-mcp) — C-native Model Context Protocol server for Radare2 and r2ghidra.
- **Alternative:** `morluto/rea` (https://github.com/morluto/rea) — Universal reverse-engineering agent skills and binary analysis suite.
- **Alternative:** `semgrep/semgrep` (https://github.com/semgrep/semgrep) — Official static analysis vulnerability auditing MCP server.
- Recommendation: Register `mukul975/anthropic-cybersecurity-skills` in `scratchpad/followup.txt` as a selective, cherry-pick-only knowledge reference.
