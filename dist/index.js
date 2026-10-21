import { spawn } from 'child_process';
import * as path from 'path';
import * as fs from 'fs';
import { fileURLToPath } from 'url';
import { getAgentsDirectory, listSpecialists, loadSpecialistCharter, loadSpecialistSettings } from './fleet.js';
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
export { getAgentsDirectory, listSpecialists, loadSpecialistCharter, loadSpecialistSettings };
export default function registerExtension(pi) {
    // 1. Session start notification
    pi.on('session.start', async (ctx) => {
        const specialists = listSpecialists();
        ctx.ui.notify(`[pi-configs] Heretek Specialist Fleet v1.0.0 active (${specialists.length} specialists ready). Use /fleet to view roster or /specialist <slug> to switch charters.`);
    });
    // 2. Command: /fleet
    pi.registerCommand({
        name: 'fleet',
        description: 'Display all 70 autonomous specialists in the Heretek Pi Fleet',
        handler: async (args, ctx) => {
            const specialists = listSpecialists();
            if (specialists.length === 0) {
                ctx.ui.error('No specialists discovered in agents directory.');
                return;
            }
            const query = args ? args.trim().toLowerCase() : '';
            const matched = query ? specialists.filter(s => s.toLowerCase().includes(query)) : specialists;
            let output = `=== HERETEK SPECIALIST FLEET (${matched.length} / ${specialists.length} Available) ===\n\n`;
            for (const slug of matched) {
                const settings = loadSpecialistSettings(slug);
                const displayName = settings && typeof settings['displayName'] === 'string' ? settings['displayName'] : slug;
                const guild = settings && typeof settings['guild'] === 'string' ? settings['guild'] : 'Specialist';
                output += `• ${slug.padEnd(35)} [${guild}] - ${displayName}\n`;
            }
            output += `\nTo activate a specialist: /specialist <slug>`;
            ctx.ui.writeBox(output);
        }
    });
    // 3. Command: /specialist <slug>
    pi.registerCommand({
        name: 'specialist',
        description: 'Switch active session system prompt and boundary to a chosen specialist',
        handler: async (args, ctx) => {
            const slug = args ? args.trim() : '';
            if (!slug) {
                ctx.ui.error('Usage: /specialist <slug>. Run /fleet to see available specialists.');
                return;
            }
            const charter = loadSpecialistCharter(slug);
            if (!charter) {
                ctx.ui.error(`Specialist '${slug}' not found. Run /fleet to list valid slugs.`);
                return;
            }
            const settings = loadSpecialistSettings(slug);
            const displayName = settings && typeof settings['displayName'] === 'string' ? settings['displayName'] : slug;
            if (ctx.session && typeof ctx.session.setSystemPrompt === 'function') {
                ctx.session.setSystemPrompt(charter);
            }
            ctx.ui.notify(`Specialist Activated: ${displayName} (${slug})`);
            ctx.ui.writeBox(`Specialist Charter Mounted: ${displayName} [${slug}]\nAll domain boundaries, anti-slop directives, and self-correction protocols are now active.`);
        }
    });
    // 4. Tool: dispatch_specialist
    pi.registerTool({
        name: 'dispatch_specialist',
        description: 'Delegates a bounded task to one of the 70 narrow specialists with isolated execution and returns the result.',
        parameters: {
            type: 'object',
            properties: {
                specialistSlug: {
                    type: 'string',
                    description: 'The slug of the specialist to execute (e.g. "gui-visual-critic", "ast-structural-refactorer", "godot-redot-architect")'
                },
                taskPrompt: {
                    type: 'string',
                    description: 'The explicit, self-contained task description for the specialist'
                },
                workingDirectory: {
                    type: 'string',
                    description: 'Optional target working directory for the specialist process'
                }
            },
            required: ['specialistSlug', 'taskPrompt']
        },
        handler: async ({ specialistSlug, taskPrompt, workingDirectory }, ctx) => {
            const agentsDir = getAgentsDirectory();
            const agentDir = path.join(agentsDir, specialistSlug);
            if (!fs.existsSync(agentDir)) {
                return {
                    status: 'error',
                    error: `Specialist '${specialistSlug}' does not exist in agents directory.`
                };
            }
            const cwd = workingDirectory && fs.existsSync(workingDirectory) ? workingDirectory : process.cwd();
            ctx.logger.info(`Dispatching specialist '${specialistSlug}' in ${cwd}`);
            const isWindows = process.platform === 'win32';
            const launcher = isWindows ? path.join(agentDir, 'launch.ps1') : path.join(agentDir, 'launch.sh');
            if (!fs.existsSync(launcher)) {
                return {
                    status: 'error',
                    error: `Launcher script not found at ${launcher}`
                };
            }
            return new Promise((resolve) => {
                let child;
                if (isWindows) {
                    child = spawn('powershell.exe', ['-ExecutionPolicy', 'Bypass', '-File', launcher, '-p', taskPrompt], {
                        cwd,
                        env: { ...process.env, PI_SKIP_VERSION_CHECK: '1' }
                    });
                }
                else {
                    child = spawn('bash', [launcher, '-p', taskPrompt], {
                        cwd,
                        env: { ...process.env, PI_SKIP_VERSION_CHECK: '1' }
                    });
                }
                let stdout = '';
                let stderr = '';
                child.stdout?.on('data', (d) => { stdout += d.toString(); });
                child.stderr?.on('data', (d) => { stderr += d.toString(); });
                child.on('close', (code) => {
                    if (code === 0) {
                        resolve({
                            status: 'success',
                            specialist: specialistSlug,
                            exitCode: code,
                            output: stdout.slice(-8192) // bounded output buffer
                        });
                    }
                    else {
                        resolve({
                            status: 'failed',
                            specialist: specialistSlug,
                            exitCode: code,
                            error: stderr.slice(-4096) || stdout.slice(-4096)
                        });
                    }
                });
                child.on('error', (err) => {
                    resolve({
                        status: 'error',
                        specialist: specialistSlug,
                        error: err.message
                    });
                });
            });
        }
    });
}
//# sourceMappingURL=index.js.map