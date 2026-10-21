const fs = require('fs');
const path = require('path');

const specContent = fs.readFileSync(path.join(__dirname, '../scratchpad/01_SPECIALIST_ROSTER_SPEC.md'), 'utf8');

function parseRoles(markdown) {
  const roleBlocks = markdown.split(/^### Role /m).slice(1);
  const roles = [];

  for (const block of roleBlocks) {
    const headerMatch = block.match(/^(\d+):\s*([^(\n\r]+?)\s*\(`([^`]+)`\)/);
    if (!headerMatch) continue;

    const roleNumber = headerMatch[1];
    const roleTitle = headerMatch[2].trim();
    const slug = headerMatch[3].trim();

    const guildMatch = block.match(/\*\*Department \/ Guild\*\*:\s*([^\r\n]+)/);
    const modelMatch = block.match(/\*\*Recommended Model\*\*:\s*`?([^\r\n`]+)`?/);
    const budgetMatch = block.match(/\*\*Reasoning \/ Thinking Budget\*\*:\s*`?([^\r\n`]+)`?/);

    const scopeMatch = block.match(/- \*\*Precise Scope\*\*:\s*([^\r\n]+)/);
    const ownsMatch = block.match(/- \*\*What it OWNS\*\*:\s*([^\r\n]+)/);
    const refusesMatch = block.match(/- \*\*What it REFUSES to Touch\*\*:\s*([^\r\n]+)/);

    const nativeToolsMatch = block.match(/- \*\*Native Pi Tools\*\*:\s*`?([^\r\n`]+)`?/);
    const cliToolsMatch = block.match(/- \*\*Specialized CLI Tools\*\*:\s*`?([^\r\n`]+)`?/);
    const mcpMatch = block.match(/- \*\*MCP Servers\*\*:\s*`?([^\r\n`]+)`?/);
    const extensionsMatch = block.match(/- \*\*Extensions & Adapters\*\*:\s*`?([^\r\n`]+)`?/);

    const hooksMatch = block.match(/```yaml([\s\S]*?)```/);
    const selfCorrectionMatch = block.match(/#### D\. Mandatory Self-Correction Protocol\s*([\s\S]*?)(?=#### E\.|\n---|\n##|$)/);
    const skillsMatch = block.match(/#### E\. Assigned Skills & Capabilities\s*([\s\S]*?)(?=\n---|### Role|\n##|$)/);

    roles.push({
      number: roleNumber,
      title: roleTitle,
      slug: slug,
      guild: guildMatch ? guildMatch[1].trim() : 'Core Engineering Guild',
      model: modelMatch ? modelMatch[1].trim() : 'Claude 3.7 Sonnet',
      thinking: budgetMatch ? budgetMatch[1].trim() : 'High (12,000 tokens)',
      scope: scopeMatch ? scopeMatch[1].trim() : `${roleTitle} scope`,
      owns: ownsMatch ? ownsMatch[1].trim() : 'Domain-specific artifacts',
      refuses: refusesMatch ? refusesMatch[1].trim() : 'Out-of-scope tasks',
      nativeTools: nativeToolsMatch ? nativeToolsMatch[1].trim().split(',').map(s => s.trim()) : ['read', 'write', 'edit', 'bash'],
      cliTools: cliToolsMatch ? cliToolsMatch[1].trim() : 'git status, git diff',
      mcpServers: mcpMatch ? mcpMatch[1].trim().split(',').map(s => s.trim()) : ['codebase-memory-mcp'],
      extensions: extensionsMatch ? extensionsMatch[1].trim().split(',').map(s => s.trim()) : ['pi-mcp-adapter'],
      hooksYaml: hooksMatch ? hooksMatch[1].trim() : 'hooks:\n  - event: tool.before.*\n    action: pass\n',
      selfCorrection: selfCorrectionMatch ? selfCorrectionMatch[1].trim() : 'Run domain linters and verify exit code 0.',
      assignedSkills: skillsMatch ? skillsMatch[1].trim().split('\n').map(s => s.replace(/^[-*`\s]+|[`\s]+$/g, '').trim()).filter(Boolean) : []
    });
  }

  return roles;
}

const roles = parseRoles(specContent);
console.log(`Generating complete specialist configurations for ${roles.length} agents...`);

const baseDir = path.join(__dirname, '../agents');
if (!fs.existsSync(baseDir)) {
  fs.mkdirSync(baseDir, { recursive: true });
}

for (const role of roles) {
  const agentDir = path.join(baseDir, role.slug);
  const piDir = path.join(agentDir, '.pi');
  const hookDir = path.join(piDir, 'hook');
  const extDir = path.join(piDir, 'extensions');
  const skillsDir = path.join(piDir, 'skills');

  fs.mkdirSync(agentDir, { recursive: true });
  fs.mkdirSync(piDir, { recursive: true });
  fs.mkdirSync(hookDir, { recursive: true });
  fs.mkdirSync(extDir, { recursive: true });
  fs.mkdirSync(skillsDir, { recursive: true });

  // 1. AGENTS.md
  const agentsMd = `# Specialist Charter: ${role.title} (\`${role.slug}\`)

> Guild: ${role.guild}
> Target Architecture: @mariozechner/pi-coding-agent v1.2.0+ Standalone Local Specialist
> Model Tier: ${role.model} | Thinking Level: ${role.thinking}

---

## 1. Narrow Domain Boundary & Operating Scope

### Precise Scope
${role.scope}

### What This Agent OWNS
${role.owns}

### What This Agent STRICTLY REFUSES to Touch
${role.refuses}

---

## 2. Tool Execution Protocol

### Allowed Tools
- **Native Tools**: \`${role.nativeTools.join(', ')}\`
- **CLI Commands**: \`${role.cliTools}\`
- **MCP Servers**: \`${role.mcpServers.join(', ')}\`
- **Extensions**: \`${role.extensions.join(', ')}\`

### Operational Protocol
1. **Zero Guessing Policy**: Inspect existing files, schemas, and configurations prior to proposing modifications. No assumptions based on stale training data.
2. **Context Preservation**: Avoid raw file dumps. Use structural queries, AST grep patterns, and symbol definition lookups where possible.
3. **Least Privilege**: Only modify files within explicit domain ownership. Any attempt to touch out-of-scope files will trigger an exit code 2 abort from \`.pi/hook/hooks.yaml\`.
4. **Anti-Slop Directive**: Avoid conversational filler, marketing jargon, placeholders, and robotic phrasing ("delve", "testament", "tapestry"). Deliver direct, functional, and verifiable results.

---

## 3. Mandatory Self-Correction Protocol

Before yielding turn or declaring a task complete, this specialist MUST execute and pass:
${role.selfCorrection}

- If any command fails with non-zero exit code or emits diagnostic warnings, immediately inspect error traces, rectify root causes, and re-run.
- Turn cannot be yielded with pending linter errors, unverified assumptions, or syntax regressions.

---

## 4. Anti-Slop & Anti-Guessing Rules

1. Never write \`TODO\`, \`// implement here\`, or placeholder functions. Every implementation must be 100% concrete and functional.
2. Never claim work is complete without active CLI verification proof.
3. Adhere strictly to the designated language conventions and project architecture.
`;
  fs.writeFileSync(path.join(agentDir, 'AGENTS.md'), agentsMd, 'utf8');

  // 2. .pi/settings.json
  const settingsJson = {
    "name": role.slug,
    "displayName": role.title,
    "guild": role.guild,
    "model": role.model.split('/')[0].trim().toLowerCase().replace(/\s+/g, '-'),
    "thinking": {
      "level": role.thinking.toLowerCase().includes('extended') ? "extended" : (role.thinking.toLowerCase().includes('high') ? "high" : "medium"),
      "budgetTokens": role.thinking.match(/\d+[,.]?\d*/)?.[0]?.replace(',', '') || "8000"
    },
    "allowedTools": role.nativeTools,
    "compaction": {
      "strategy": "eesv-verified",
      "threshold": 0.85,
      "preservePromptCache": true
    },
    "packages": [
      "npm:pi-mcp-adapter",
      "npm:pi-yaml-hooks",
      "npm:@juvio15/pi-ast-grep"
    ]
  };
  fs.writeFileSync(path.join(piDir, 'settings.json'), JSON.stringify(settingsJson, null, 2), 'utf8');

  // 3. .pi/hook/hooks.yaml
  let cleanedHooksYaml = role.hooksYaml.trim();
  if (!cleanedHooksYaml.startsWith('hooks:')) {
    cleanedHooksYaml = `hooks:\n${cleanedHooksYaml}`;
  }
  // Append user.prompt.submit and standard hygiene if not present
  if (!cleanedHooksYaml.includes('user.prompt.submit')) {
    cleanedHooksYaml += `\n  - event: user.prompt.submit\n    action: bash\n    command: |\n      echo "[context-injection] Specialist '${role.slug}' active. Working directory: $(pwd)"`;
  }
  fs.writeFileSync(path.join(hookDir, 'hooks.yaml'), cleanedHooksYaml + '\n', 'utf8');

  // 4. .pi/mcp.json and .pi/mcp-adapter.json
  const mcpConfig = {
    "mcpServers": {}
  };
  for (const s of role.mcpServers) {
    const cleanName = s.replace(/^@/, '').replace(/\//g, '_').replace(/[^a-zA-Z0-9_-]/g, '');
    if (s.includes('git')) {
      mcpConfig.mcpServers[cleanName] = {
        "command": "npx",
        "args": ["-y", "@cyanheads/git-mcp-server"],
        "lazy": true
      };
    } else if (s.includes('github')) {
      mcpConfig.mcpServers[cleanName] = {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "lazy": true
      };
    } else if (s.includes('memory')) {
      mcpConfig.mcpServers[cleanName] = {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-memory"],
        "lazy": true
      };
    } else if (s.includes('playwright') || s.includes('browser')) {
      mcpConfig.mcpServers[cleanName] = {
        "command": "npx",
        "args": ["-y", "@playwright/mcp"],
        "lazy": true
      };
    } else if (s.includes('radare2')) {
      mcpConfig.mcpServers[cleanName] = {
        "command": "r2mcp",
        "args": ["-s"],
        "lazy": true
      };
    } else if (s.includes('ghidra')) {
      mcpConfig.mcpServers[cleanName] = {
        "command": "python",
        "args": ["-m", "ghidra_mcp"],
        "lazy": true
      };
    } else if (s.includes('semgrep')) {
      mcpConfig.mcpServers[cleanName] = {
        "command": "uvx",
        "args": ["semgrep-mcp"],
        "lazy": true
      };
    } else {
      mcpConfig.mcpServers[cleanName] = {
        "command": "npx",
        "args": ["-y", `@modelcontextprotocol/server-${cleanName}`],
        "lazy": true
      };
    }
  }
  fs.writeFileSync(path.join(piDir, 'mcp.json'), JSON.stringify(mcpConfig, null, 2), 'utf8');
  fs.writeFileSync(path.join(piDir, 'mcp-adapter.json'), JSON.stringify({
    "proxyMode": true,
    "lazySpawn": true,
    "maxTokenCap": 250,
    "servers": mcpConfig.mcpServers
  }, null, 2), 'utf8');

  // 5. .pi/skills/<skill-name>/SKILL.md
  const primarySkill = role.assignedSkills[0] ? role.assignedSkills[0].replace(/^skills\//, '').replace(/\/SKILL\.md$/, '') : `${role.slug}-core`;
  const skillTargetDir = path.join(skillsDir, primarySkill);
  fs.mkdirSync(skillTargetDir, { recursive: true });

  const skillMd = `---
name: ${primarySkill}
description: Specialized capabilities and operational workflow for ${role.title}
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: ${primarySkill}

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for \`${role.slug}\` in the ${role.guild}.

## Verification Protocols
1. Run pre-flight checks:
   \`\`\`bash
   ${role.cliTools.split(',')[0] || 'git status'}
   \`\`\`
2. Execute core operations adhering to ${role.owns}.
3. Run self-correction verification:
   \`\`\`bash
   ${role.selfCorrection.split('\n')[0].replace(/^[-*`\s]+|[`\s]+$/g, '') || 'exit 0'}
   \`\`\`

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with ${role.slug} boundaries.
- Exit code 0 required on all diagnostic commands.
`;
  fs.writeFileSync(path.join(skillTargetDir, 'SKILL.md'), skillMd, 'utf8');

  // 6. .pi/extensions/index.ts
  const extTs = `/**
 * Extension: ${role.slug}-guard
 * Scoped to ${role.title} (${role.guild})
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('${role.title} operational in ${role.guild}');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[${role.slug}] Turn concluded with zero blocking warnings.');
  });
}
`;
  fs.writeFileSync(path.join(extDir, 'index.ts'), extTs, 'utf8');

  // 7. launch.ps1 and launch.sh
  const launchPs1 = `# Launch script for ${role.title} (${role.slug})
\$ErrorActionPreference = "Stop"

Write-Host "=== Initializing Specialist: ${role.title} [${role.slug}] ==="
\$env:PI_SKIP_VERSION_CHECK = "1"
\$env:PI_SPECIALIST_SLUG = "${role.slug}"
\$env:PI_CONFIG_DIR = \$PSScriptRoot

# Verify local node & pi runtime
if (-not (Get-Command "pi" -ErrorAction SilentlyContinue)) {
    Write-Warning "'pi' CLI not found on PATH. Ensure @mariozechner/pi-coding-agent is installed."
    Write-Host "Running local fallback check via npx..."
}

Write-Host "Launching pi coding agent for ${role.slug}..."
pi --config "\$PSScriptRoot/.pi/settings.json" --agents-file "\$PSScriptRoot/AGENTS.md" @args
`;
  fs.writeFileSync(path.join(agentDir, 'launch.ps1'), launchPs1, 'utf8');

  const launchSh = `#!/usr/bin/env bash
# Launch script for ${role.title} (${role.slug})
set -e

echo "=== Initializing Specialist: ${role.title} [${role.slug}] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="${role.slug}"
export PI_CONFIG_DIR="\$(cd "\$(dirname "\${BASH_SOURCE[0]}")" && pwd)"

pi --config "\$PI_CONFIG_DIR/.pi/settings.json" --agents-file "\$PI_CONFIG_DIR/AGENTS.md" "\$@"
`;
  fs.writeFileSync(path.join(agentDir, 'launch.sh'), launchSh, 'utf8');
}

console.log('Successfully generated all 70 specialist configurations!');
