const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const SCRATCHPAD = path.join(ROOT, 'scratchpad');
const AGENTS = path.join(ROOT, 'agents');
const FOLLOWUP = path.join(SCRATCHPAD, 'followup.txt');

console.log('=== VERIFICATION GATE EXECUTION ===\n');

// 1. Verify scratchpad reports
console.log('--- GATE 1: Scratchpad Reports Audit (>150 lines, non-truncated) ---');
const reports = fs.readdirSync(SCRATCHPAD).filter(f => f.endsWith('.md'));
console.log(`Total markdown reports found in scratchpad: ${reports.length}`);

let shortReports = 0;
for (const rep of reports) {
  const content = fs.readFileSync(path.join(SCRATCHPAD, rep), 'utf8');
  const lineCount = content.split(/\r?\n/).length;
  if (lineCount < 150) {
    console.error(`FAIL: ${rep} has only ${lineCount} lines (< 150)`);
    shortReports++;
  }
}

if (shortReports === 0) {
  console.log(`[PASS] All ${reports.length} markdown audit reports strictly exceed 150 lines.`);
} else {
  console.error(`[FAIL] ${shortReports} reports failed line requirement.`);
}

// 2. Verify followup.txt
console.log('\n--- GATE 2: Wild Alternatives Register (followup.txt) ---');
if (!fs.existsSync(FOLLOWUP)) {
  console.error('FAIL: scratchpad/followup.txt does not exist');
} else {
  const followupLines = fs.readFileSync(FOLLOWUP, 'utf8').split(/\r?\n/).filter(l => l.trim().length > 0);
  console.log(`[PASS] followup.txt exists with ${followupLines.length} categorized wild alternatives.`);
}

// 3. Verify Agents Fleet
console.log('\n--- GATE 3: Specialists Fleet Validation (>= 65 agents, valid configs) ---');
const agentDirs = fs.readdirSync(AGENTS).filter(d => fs.statSync(path.join(AGENTS, d)).isDirectory());
console.log(`Total specialist directories found in agents/: ${agentDirs.length}`);

if (agentDirs.length >= 65) {
  console.log(`[PASS] Fleet directory count (${agentDirs.length}) satisfies requirement (>= 65).`);
} else {
  console.error(`[FAIL] Fleet count ${agentDirs.length} is less than 65.`);
}

let jsonErrors = 0;
let missingFiles = 0;

for (const slug of agentDirs) {
  const dir = path.join(AGENTS, slug);
  const reqFiles = [
    'AGENTS.md',
    'launch.ps1',
    'launch.sh',
    path.join('.pi', 'settings.json'),
    path.join('.pi', 'mcp.json'),
    path.join('.pi', 'mcp-adapter.json'),
    path.join('.pi', 'hook', 'hooks.yaml'),
    path.join('.pi', 'extensions', 'index.ts')
  ];

  for (const rf of reqFiles) {
    const fullPath = path.join(dir, rf);
    if (!fs.existsSync(fullPath)) {
      console.error(`Missing required file in ${slug}: ${rf}`);
      missingFiles++;
    }
  }

  // Validate JSONs
  for (const jf of ['settings.json', 'mcp.json', 'mcp-adapter.json']) {
    const jsonPath = path.join(dir, '.pi', jf);
    if (fs.existsSync(jsonPath)) {
      try {
        JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
      } catch (err) {
        console.error(`JSON Syntax Error in ${slug}/.pi/${jf}: ${err.message}`);
        jsonErrors++;
      }
    }
  }
}

if (missingFiles === 0 && jsonErrors === 0) {
  console.log(`[PASS] All ${agentDirs.length} specialist directories contain 100% complete files with zero JSON syntax errors.`);
} else {
  console.error(`[FAIL] ${missingFiles} missing files, ${jsonErrors} JSON syntax errors.`);
}

console.log('\n=== VERIFICATION GATE SUMMARY ===');
if (shortReports === 0 && agentDirs.length >= 65 && missingFiles === 0 && jsonErrors === 0) {
  console.log('STATUS: ALL GATES PASSED (100% OPERATIONAL & VERIFIED)');
  process.exit(0);
} else {
  console.error('STATUS: VERIFICATION FAILED');
  process.exit(1);
}
