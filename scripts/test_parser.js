const fs = require('fs');
const path = require('path');

const specContent = fs.readFileSync(path.join(__dirname, '../scratchpad/01_SPECIALIST_ROSTER_SPEC.md'), 'utf8');

function parseRoles(markdown) {
  // Regex to split on role headers
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
      assignedSkills: skillsMatch ? skillsMatch[1].trim().split('\n').map(s => s.replace(/^[-*]\s*/, '').trim()).filter(Boolean) : []
    });
  }

  return roles;
}

const parsed = parseRoles(specContent);
console.log(`Successfully parsed ${parsed.length} / 70 roles.`);
console.log('Sample parsed role 1:', JSON.stringify(parsed[0], null, 2));
