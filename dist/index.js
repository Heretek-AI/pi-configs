import { spawn } from 'child_process';
import * as path from 'path';
import * as fs from 'fs';
import { fileURLToPath } from 'url';
import { getAgentsDirectory, listSpecialists, loadSpecialistCharter, loadSpecialistSettings } from './fleet.js';
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
export { getAgentsDirectory, listSpecialists, loadSpecialistCharter, loadSpecialistSettings };
let activeSpecialist = null;
export default function registerExtension(pi) {
    // 1. Session start notification & footer status
    pi.on('session_start', async (_event, ctx) => {
        const specialists = listSpecialists();
        if (ctx.ui?.setStatus) {
            ctx.ui.setStatus('fleet', `Fleet: ${specialists.length} Specialists`);
        }
        if (ctx.ui?.notify) {
            ctx.ui.notify(`Heretek Specialist Fleet loaded (${specialists.length} specialists available). Run /fleet to browse or /specialist <slug> to activate.`, 'info');
        }
    });
    // 2. Dynamic specialist charter injection via before_agent_start lifecycle hook
    pi.on('before_agent_start', async (event) => {
        if (activeSpecialist && event.systemPromptOptions) {
            const current = event.systemPromptOptions.appendSystemPrompt || [];
            event.systemPromptOptions.appendSystemPrompt = [
                ...current,
                activeSpecialist.charter
            ];
        }
    });
    // 3. Command: /fleet
    pi.registerCommand('fleet', {
        description: 'Display and browse all 70 autonomous specialists in the Heretek Pi Fleet',
        handler: async (args, ctx) => {
            const specialists = listSpecialists();
            if (specialists.length === 0) {
                if (ctx.ui?.notify) {
                    ctx.ui.notify('No specialists discovered in agents directory.', 'error');
                }
                else {
                    console.error('No specialists discovered in agents directory.');
                }
                return;
            }
            const query = args ? args.trim().toLowerCase() : '';
            const matched = query ? specialists.filter(s => s.toLowerCase().includes(query)) : specialists;
            if (matched.length === 0) {
                if (ctx.ui?.notify) {
                    ctx.ui.notify(`No specialists matching "${query}". Run /fleet without arguments to see all.`, 'warning');
                }
                else {
                    console.warn(`No specialists matching "${query}".`);
                }
                return;
            }
            if (ctx.hasUI && ctx.ui?.select) {
                const items = matched.map(slug => {
                    const settings = loadSpecialistSettings(slug);
                    const displayName = settings && typeof settings['displayName'] === 'string' ? settings['displayName'] : slug;
                    const guild = settings && typeof settings['guild'] === 'string' ? settings['guild'] : 'Specialist';
                    return `${slug.padEnd(35)} [${guild}] - ${displayName}`;
                });
                const selected = await ctx.ui.select(`Heretek Fleet (${matched.length} Available)`, items);
                if (selected) {
                    const chosenSlug = selected.split(/\s+/)[0];
                    const charter = loadSpecialistCharter(chosenSlug);
                    if (charter) {
                        const settings = loadSpecialistSettings(chosenSlug);
                        const displayName = settings && typeof settings['displayName'] === 'string' ? settings['displayName'] : chosenSlug;
                        activeSpecialist = { slug: chosenSlug, displayName, charter };
                        if (ctx.ui?.setStatus) {
                            ctx.ui.setStatus('specialist', `Specialist: ${chosenSlug}`);
                        }
                        if (ctx.ui?.notify) {
                            ctx.ui.notify(`Specialist Activated: ${displayName} [${chosenSlug}]`, 'info');
                        }
                    }
                }
            }
            else {
                let output = `=== HERETEK SPECIALIST FLEET (${matched.length} / ${specialists.length} Available) ===\n\n`;
                for (const slug of matched) {
                    const settings = loadSpecialistSettings(slug);
                    const displayName = settings && typeof settings['displayName'] === 'string' ? settings['displayName'] : slug;
                    const guild = settings && typeof settings['guild'] === 'string' ? settings['guild'] : 'Specialist';
                    output += `• ${slug.padEnd(35)} [${guild}] - ${displayName}\n`;
                }
                output += `\nTo activate a specialist: /specialist <slug>`;
                console.log(output);
            }
        }
    });
    // 4. Command: /specialist <slug>
    pi.registerCommand('specialist', {
        description: 'Switch active session system prompt and boundary to a chosen specialist',
        handler: async (args, ctx) => {
            const slug = args ? args.trim() : '';
            if (!slug) {
                if (ctx.ui?.notify) {
                    ctx.ui.notify('Usage: /specialist <slug>. Run /fleet to see available specialists.', 'error');
                }
                else {
                    console.error('Usage: /specialist <slug>. Run /fleet to see available specialists.');
                }
                return;
            }
            const charter = loadSpecialistCharter(slug);
            if (!charter) {
                if (ctx.ui?.notify) {
                    ctx.ui.notify(`Specialist '${slug}' not found. Run /fleet to list valid slugs.`, 'error');
                }
                else {
                    console.error(`Specialist '${slug}' not found. Run /fleet to list valid slugs.`);
                }
                return;
            }
            const settings = loadSpecialistSettings(slug);
            const displayName = settings && typeof settings['displayName'] === 'string' ? settings['displayName'] : slug;
            activeSpecialist = { slug, displayName, charter };
            if (ctx.ui?.setStatus) {
                ctx.ui.setStatus('specialist', `Specialist: ${slug}`);
            }
            if (ctx.ui?.notify) {
                ctx.ui.notify(`Specialist Activated: ${displayName} [${slug}]`, 'info');
            }
        }
    });
    // 5. Tool: dispatch_specialist
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
        handler: dispatchHandler,
        execute: dispatchHandler
    });
}
async function dispatchHandler({ specialistSlug, taskPrompt, workingDirectory }, ctx) {
    const agentsDir = getAgentsDirectory();
    const agentDir = path.join(agentsDir, specialistSlug);
    if (!fs.existsSync(agentDir)) {
        return {
            status: 'error',
            error: `Specialist '${specialistSlug}' does not exist in agents directory.`
        };
    }
    const cwd = workingDirectory && fs.existsSync(workingDirectory) ? workingDirectory : process.cwd();
    const logger = ctx?.logger;
    if (logger?.info) {
        logger.info(`Dispatching specialist '${specialistSlug}' in ${cwd}`);
    }
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
//# sourceMappingURL=index.js.map