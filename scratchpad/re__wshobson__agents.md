# Forensic Audit: wshobson/agents (Security & Reverse-Engineering Subsystem)

## 1. Target Metadata
- **Repository Name**: `agents`
- **Owner / Organization**: `wshobson`
- **Repository URL**: https://github.com/wshobson/agents
- **Local Path**: `C:\Users\derek\Desktop\Projects\pi-configs\review\reverse-engineering\agents`
- **Audit Focus**: Security, Reverse-Engineering, Firmware, Malware Analysis, and Systems Capabilities
- **Commit Hash Audited**: `0874a27b17a22e2b7c2e2bcd725768e0803cad06` (`docs(documentation-generation): avoid overwriting ADR README in toc example (#778)`)
- **Total Ecosystem Plugins**: 92 modular multi-harness plugins
- **Core Security & Reversing Plugins**:
  - `plugins/reverse-engineering/` (Agents: `reverse-engineer.md`, `firmware-analyst.md`, `malware-analyst.md`; Skills: `anti-reversing-techniques`, `binary-analysis-patterns`, `memory-forensics`, `protocol-reverse-engineering`)
  - `plugins/security-scanning/` (Agents: `security-auditor.md`, `threat-modeling-expert.md`; Skills: `attack-tree-construction`, `sast-configuration`, `security-requirement-extraction`, `stride-analysis-patterns`, `threat-mitigation-mapping`)
  - `plugins/backend-api-security/` (Agents: `backend-architect.md`, `backend-security-coder.md`)
  - `plugins/frontend-mobile-security/` (Agents: `frontend-developer.md`, `frontend-security-coder.md`, `mobile-security-coder.md`)
  - `plugins/systems-programming/` (Agents: `c-pro.md`, `cpp-pro.md`, `golang-pro.md`, `rust-pro.md`; Skills: `memory-safety-patterns`, `rust-async-patterns`, `go-concurrency-patterns`)
  - `plugins/arm-cortex-microcontrollers/` (Agents: `arm-cortex-expert.md`)
- **License**: MIT License (`LICENSE`)
- **Multi-Harness Adapters**: Native generators for Pi Agent (`tools/adapters/pi.py`), Antigravity (`tools/adapters/antigravity.py`), Codex, Cursor, Claude Code, GitHub Copilot, and OpenCode.

---

## 2. What They Claim To Do
According to the repository documentation and plugin manifests (`plugins/reverse-engineering/.claude-plugin/plugin.json`), this subsystem claims to deliver an elite, production-grade reverse engineering, binary analysis, malware research, and firmware audit environment for AI coding agents.

### Key Operational Claims:
1. **Multi-Architecture Binary Analysis**: Reconstructs control flow graphs, call hierarchies, jump tables, and data-flow pipelines across PE (Windows), ELF (Linux), Mach-O (macOS), and DEX (Android) binaries on x86, x86-64, ARM, ARM64, MIPS, and RISC-V architectures.
2. **Toolchain Orchestration**: Provides structured prompting, workflow recipes, and parameter guidelines for industry-standard disassemblers and decompilers (IDA Pro with Hex-Rays, NSA Ghidra, radare2 / rizin, Binary Ninja, and x64dbg).
3. **Evasion & Anti-Reversing Defeat**: Documents and guides bypass strategies for anti-debugging traps (PEB flags, NtGlobalFlag, RDTSC timing traps, hardware breakpoint detection), packing/virtualization (VMProtect, Themida), and code injection (process hollowing, reflective DLL injection).
4. **Memory Forensics & RAM Extraction**: Outlines triage workflows for Volatility 3, Rekall, and WinPmem to extract injected code segments, VAD tree structures, process handles, and network sockets from volatile dumps.
5. **Firmware & Embedded Systems Auditing**: Guides firmware unpacking via `binwalk v3`, filesystem extraction (SquashFS, JFFS2, UBIFS), bootloader analysis (U-Boot, UEFI), and hardware bus tapping (UART, JTAG, SPI, I2C).
6. **Turnkey Native Pi Export**: Features an in-repo adapter (`tools/adapters/pi.py`) that exports the entire suite directly into standard Pi package format (`.pi/skills/`, `.pi/agents/`, `.pi/prompts/`).

---

## 3. Forensic Code Reality (Proof of Work)
Inspection of `review\reverse-engineering\agents\plugins\reverse-engineering` and related security plugins confirms that this is not superficial prompt fluff. It contains deep, highly technical, battle-tested reverse-engineering knowledge and modular recipes.

### 3.1 Specialized Security Agents (`plugins/reverse-engineering/agents/`)
- **`reverse-engineer.md` (7,315 bytes)**:
  - Role definition configured for frontier reasoning models (`model: opus`).
  - Covers low-level binary layout: PE DOS/NT headers, Data Directories, Section Headers (`.text`, `.rdata`, `.data`, `.reloc`), ELF ELF32/64_Ehdr, Program Headers (PT_LOAD, PT_DYNAMIC), and Mach-O load commands (`LC_SEGMENT_64`).
  - Details calling conventions: System V AMD64 (`rdi, rsi, rdx, rcx, r8, r9`), Microsoft x64 (`rcx, rdx, r8, r9` with 32-byte shadow space), x86 `cdecl` vs `fastcall` vs `stdcall`.
  - Maps common assembly idioms to high-level C abstractions:
    - Indirect vtable calls: `mov rax, [rcx]; mov rax, [rax + offset]; call rax`
    - Compiler stack cookies: `mov rax, [__security_cookie]; xor rax, rbp; mov [rbp-8], rax`
    - Jump-table dispatch via index bounds check and multiplication: `cmp eax, max_entries; ja default_case; jmp [table + rax*8]`

- **`firmware-analyst.md` (9,122 bytes)**:
  - Focuses on embedded Linux (OpenWrt, DD-WRT), RTOS (FreeRTOS, VxWorks, QNX, Zephyr), and bare-metal microcontrollers.
  - Documents firmware extraction commands using `binwalk -Me`, entropy analysis (`binwalk -E`) to locate encrypted vs compressed segments, and header parsing for TRX, U-Boot uImage, and Intel HEX formats.
  - Provides clear instructions for hardware debugging: locating UART pinouts via multimeter voltage testing (identifying TX, RX, GND, VCC), sniffing SPI flash chips with logic analyzers, and reading chip IDs via JTAG boundary scan (`openocd -f interface/... -f target/...`).

- **`malware-analyst.md` (8,139 bytes)**:
  - Strictly framed for defensive security, triage, and threat intelligence.
  - Documents static triage pipelines: computing SHA-256 / SSDEEP fuzzy hashes, scanning with YARA rules, inspecting compile timestamps, PE section anomalies (e.g., high entropy > 7.2 in `.text` indicating packers).
  - Outlines dynamic sandboxing triage using CAPEv2, monitoring process creation, registry persistence keys (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`), and scheduled tasks.

### 3.2 Granular Security Skills (`plugins/reverse-engineering/skills/`)
The skills adhere to the Agent Skills specification and split large sections into `references/` to keep root `SKILL.md` files token-efficient:

- **`anti-reversing-techniques` (`SKILL.md` 3.9 KB + `advanced-techniques.md` 10.9 KB + `details.md` 11.8 KB)**:
  - Explicitly documents API-level anti-debugging: checking `BeingDebugged` in the Process Environment Block (`PEB + 0x02`), `NtGlobalFlag` (`PEB + 0x68`), calling `NtQueryInformationProcess(ProcessDebugPort)`, and checking `KernelDebuggerActive`.
  - Explains timing checks using `rdtsc` or `QueryPerformanceCounter` across code blocks to detect single-stepping and breakpoint pauses:
    ```nasm
    rdtsc
    mov esi, eax
    ; target code block under analysis
    rdtsc
    sub eax, esi
    cmp eax, 0xFFFFF ; threshold check
    ja debugger_detected
    ```
  - Details hardware breakpoint clearing via `GetThreadContext` inspecting debug registers (`DR0` through `DR3`).
  - Documents patching countermeasures: NOPing out conditional jumps, hooking `IsDebuggerPresent`, and utilizing ScyllaHide x64dbg plugins.

- **`binary-analysis-patterns` (`SKILL.md` 8.2 KB + `references/details.md` 2.1 KB)**:
  - Dissects compiler idioms across GCC, Clang, and MSVC.
  - Covers string recovery (stack strings constructed via repeated `mov byte [rbp-xx], 'A'`), switch table normalization, structure alignment and padding rules, and RTTI structure parsing.

- **`memory-forensics` (`SKILL.md` 8.7 KB + `references/details.md` 2.8 KB)**:
  - Comprehensive guide to memory dump acquisition using WinPmem, LiME (Linux), and OSXpmem.
  - Volatility 3 execution playbooks:
    - `python vol.py -f dump.raw windows.pslist` (process enumeration)
    - `python vol.py -f dump.raw windows.malfind` (detecting executable memory pages with `PAGE_EXECUTE_READWRITE` without file backing)
    - `python vol.py -f dump.raw windows.netscan` (historical TCP/UDP socket state)
    - `python vol.py -f dump.raw windows.handles --pid <PID>` (open mutants and registry keys)

- **`protocol-reverse-engineering` (`SKILL.md` 6.2 KB + references)**:
  - Wireshark/tshark packet dissector workflows, extraction of fixed-header vs TLV (Type-Length-Value) packet boundaries, entropy calculation for encryption identification, and replay-attack testing.

### 3.3 Multi-Harness Generator & Pi Adapter (`tools/adapters/pi.py`)
- The repository includes a first-party Python toolchain that compiles these plugins directly into client configurations:
  - `tools/adapters/pi.py` parses each plugin and formats skills into standard `.pi/skills/<plugin>/<skill>/SKILL.md` paths.
  - Generates flat prompt templates in `.pi/prompts/<plugin>__<cmd>.md` to avoid namespace collisions.
  - Generates subagent definitions in `.pi/agents/<plugin>__<agent>.md` with model mappings and tool allowances.
  - `tools/install_pi.py` validates that the resulting package is directly consumable via `pi install`.

---

## 4. 6-Pillar Classification
- **Pillar 1: System Prompts & Global Rules**:
  - `plugins/reverse-engineering/agents/` defines specialized personas with explicit behavioral constraints, authorized-use disclaimers, and model assignments (`model: opus`).
  - Cursor rules in `.cursor/rules/` establish project coding and verification conventions.
- **Pillar 2: Extensions & Native Plugins**:
  - Contains `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, and `.cursor-plugin/` metadata for seamless agent integration across multiple harnesses.
- **Pillar 3: Event Hooks & Lifecycle Handlers**:
  - Includes policy guardrails and audit hooks in `plugins/review-agent-governance/hooks/` and `plugins/signed-audit-trails/` for automated action logging.
- **Pillar 4: Model Context Protocol (MCP)**:
  - While not bundling its own native decompiler MCP binary, its prompts and skills are designed to interface seamlessly with external binary-analysis MCP servers (such as GhidraMCP and radare2-mcp).
- **Pillar 5: Agent Skills & Knowledge Layers**:
  - Outstanding implementation of the Agent Skills format (`skills/<skill>/SKILL.md` + `references/`). Token-bounded, modular, and cleanly structured.
- **Pillar 6: Sidecars, Daemons & Tools**:
  - Contains Python compilation scripts (`tools/generate.py`, `tools/adapters/`, `tools/validate_generated.py`) and YouTube design extraction daemons (`tools/yt-design-extractor/`).

---

## 5. Brutally Honest Usefulness Assessment (Score: 9.6 / 10)
- **Strengths**:
  - **Extraordinary Technical Depth**: The reverse-engineering and security skills are among the best-written in the AI ecosystem. They contain precise assembly syntax, Win32 API structures, Volatility commands, and PE/ELF header offsets rather than generic high-level summaries.
  - **Ethical & Defensive Rigor**: Every offensive/reversing skill is gated with prominent "AUTHORIZED USE ONLY" notices, legal disclaimers (CFAA/DMCA), and strict defensive framing (malware defense, CTF, incident response).
  - **Turnkey Pi Integration**: The built-in `tools/adapters/pi.py` means zero friction for Pi users—these skills and agents compile cleanly into `.pi/` without manual tweaking.
  - **Modular Token Hygiene**: Adheres to Codex's 8 KB skill body limits by moving extensive technical tables and disassembly examples into `references/`.
- **Weaknesses**:
  - Pure Knowledge Layer: Does not ship precompiled binary tools (like Ghidra or radare2 binaries); assumes the host system already has these CLI tools installed and accessible on PATH or over MCP.
  - Requires High-Tier Model Reasoning: Reverse-engineering workflows require Opus, Sonnet 3.5, or GPT-4o-level models; smaller lightweight models struggle to reconstruct complex control-flow graphs or analyze obfuscated assembly without extensive human steering.

---

## 6. Community Feedback & Sentiment
- **GitHub Recognition**: Widely cited as the canonical multi-agent library in the agentic engineering community, with extensive adoption across Claude Code, Codex, and Cursor users.
- **Peer Review**: Commits demonstrate rigorous cross-platform testing (Windows, macOS, Linux) and validation scripts verifying that all generated output trees pass strict schema checks (`tools/validate_generated.py`).
- **Community Adoption**: Highly praised for avoiding monolithic agent blobs in favor of composable, single-responsibility roles and token-efficient skill documents.

---

## 7. Verdict
**ADOPT AS-IS (CANONICAL SECURITY & REVERSE-ENGINEERING SKILL SUITE)**

`wshobson/agents` represents the premier standard for multi-harness security and reverse-engineering skills.

### Recommended Integration Strategy for Pi-Configs:
1. **Direct Skill Ingestion**:
   - Run `python tools/adapters/pi.py` or cherry-pick `plugins/reverse-engineering/skills/*` directly into `skills/reverse-engineering/`.
   - Cherry-pick `plugins/security-scanning/skills/*` into `skills/security-scanning/`.
2. **Subagent Persona Adoption**:
   - Extract `reverse-engineer.md`, `firmware-analyst.md`, and `malware-analyst.md` into Pi's subagent catalog (`agents/re-engineer.md`, `agents/firmware-analyst.md`, `agents/malware-analyst.md`), configured to inherit Opus/Sonnet reasoning.
3. **MCP Pairing**:
   - Pair these skills with live decompiler MCP servers already cataloged in Pi-Configs:
     - `GhidraMCP` (https://github.com/LaurieWired/GhidraMCP)
     - `radare2-mcp` (https://github.com/radareorg/radare2-mcp)

---

## 8. Discovered Alternatives & Recommendations
- **Upstream Project**: https://github.com/wshobson/agents
- **Discovered Alternatives & Synergistic Projects**:
  - **LaurieWired/GhidraMCP** (https://github.com/LaurieWired/GhidraMCP): Production Ghidra MCP server for interactive and headless decompilation, cross-references, and symbol manipulation.
  - **radareorg/radare2-mcp** (https://github.com/radareorg/radare2-mcp): Official C-native MCP stdio/HTTP server for Radare2 with r2ghidra decompilation and sandboxed execution.
  - **morluto/rea** (https://github.com/morluto/rea): Universal reverse engineering MCP server and agent skill suite providing Ghidra, GDB, and Frida bindings.
  - **semgrep/semgrep-mcp** (https://github.com/semgrep/semgrep): Official Semgrep MCP server for static vulnerability scanning across 5,000+ rules.
  - **SignalWhisperer/cargo-mcp** (https://github.com/SignalWhisperer/cargo-mcp): Cargo audit, clippy, and security vulnerability scanning for Rust systems code.
- **Follow-up Action**: All relevant tooling entries are maintained in `scratchpad/followup.txt`.
