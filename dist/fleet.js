import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
export function getAgentsDirectory() {
    // Check if agents/ is adjacent to dist/ (installed package root) or in parent dir
    const candidate1 = path.resolve(__dirname, '../agents');
    if (fs.existsSync(candidate1))
        return candidate1;
    const candidate2 = path.resolve(__dirname, '../../agents');
    if (fs.existsSync(candidate2))
        return candidate2;
    return candidate1;
}
export function listSpecialists() {
    const agentsDir = getAgentsDirectory();
    if (!fs.existsSync(agentsDir))
        return [];
    return fs.readdirSync(agentsDir).filter((name) => {
        const full = path.join(agentsDir, name);
        return fs.statSync(full).isDirectory() && fs.existsSync(path.join(full, 'AGENTS.md'));
    });
}
export function loadSpecialistCharter(slug) {
    const agentsDir = getAgentsDirectory();
    const filePath = path.join(agentsDir, slug, 'AGENTS.md');
    if (fs.existsSync(filePath)) {
        return fs.readFileSync(filePath, 'utf8');
    }
    return null;
}
export function loadSpecialistSettings(slug) {
    const agentsDir = getAgentsDirectory();
    const filePath = path.join(agentsDir, slug, '.pi', 'settings.json');
    if (fs.existsSync(filePath)) {
        try {
            return JSON.parse(fs.readFileSync(filePath, 'utf8'));
        }
        catch {
            return null;
        }
    }
    return null;
}
export function loadSpecialistMcpConfig(slug) {
    const agentsDir = getAgentsDirectory();
    const filePath = path.join(agentsDir, slug, '.pi', 'mcp.json');
    if (fs.existsSync(filePath)) {
        try {
            return JSON.parse(fs.readFileSync(filePath, 'utf8'));
        }
        catch {
            return null;
        }
    }
    return null;
}
//# sourceMappingURL=fleet.js.map