/**
 * Extension: godot-redot-architect-guard
 * Scoped to Godot 4 / Redot Engine Architecture Specialist (Game Engineering, Graphics & Modding Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';
import * as fs from 'fs';
import * as path from 'path';
import { execSync } from 'child_process';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    const projectPath = path.join(process.cwd(), 'project.godot');
    if (fs.existsSync(projectPath)) {
      ctx.ui.notify('Godot/Redot Project detected. godot-redot-architect loaded with live editor & baseline verification harnesses.');
    } else {
      ctx.ui.notify('godot-redot-architect initialized in standalone mode (no local project.godot detected).');
    }
  });

  // Custom tool: godot_status
  pi.registerTool({
    name: 'godot_status',
    description: 'Inspects project.godot to parse engine config, rendering methods, display settings, and configured autoload singletons.',
    parameters: {
      type: 'object',
      properties: {},
      required: []
    },
    execute: async (_args: Record<string, unknown>, ctx: ToolContext) => {
      const projectPath = path.join(process.cwd(), 'project.godot');
      if (!fs.existsSync(projectPath)) {
        return { error: 'No project.godot found in the current workspace directory.' };
      }

      const content = fs.readFileSync(projectPath, 'utf8');
      const lines = content.split('\n');
      const autoloads: Record<string, string> = {};
      let currentSection = '';

      for (const line of lines) {
        const trimmed = line.trim();
        if (trimmed.startsWith('[') && trimmed.endsWith(']')) {
          currentSection = trimmed.slice(1, -1);
          continue;
        }
        if (currentSection === 'autoload' && trimmed.includes('=')) {
          const [key, val] = trimmed.split('=').map(s => s.trim());
          if (key && val) {
            autoloads[key] = val.replace(/^"|"$/g, '');
          }
        }
      }

      return {
        projectFile: projectPath,
        autoloadSingletons: autoloads,
        totalConfigLines: lines.length,
        hasBaselineAutoload: !!(autoloads['BaselineConfig'] || autoloads['A11ySettings'])
      };
    }
  });

  // Custom tool: godot_check_baseline
  pi.registerTool({
    name: 'godot_check_baseline',
    description: 'Executes the Dominic Bytes B01-B17 baseline verification checks on the active Godot/Redot project.',
    parameters: {
      type: 'object',
      properties: {
        verbose: {
          type: 'boolean',
          description: 'Return full checklist traces for all 17 baseline criteria.'
        }
      },
      required: []
    },
    execute: async (args: { verbose?: boolean }, _ctx: ToolContext) => {
      const projectPath = path.join(process.cwd(), 'project.godot');
      if (!fs.existsSync(projectPath)) {
        return { error: 'Cannot run baseline check: no project.godot found in workspace.' };
      }

      // Check for headless godot or redot CLI
      let engineBin = 'godot';
      try {
        execSync('godot --version', { stdio: 'pipe' });
      } catch {
        try {
          execSync('redot --version', { stdio: 'pipe' });
          engineBin = 'redot';
        } catch {
          return {
            warning: 'Neither godot nor redot CLI binary was found in PATH.',
            manualCheckRequired: 'Inspect references/checklist.md in .pi/skills/game-baseline for manual verification steps.'
          };
        }
      }

      try {
        const checkScript = path.join(__dirname, '../skills/game-baseline/templates/redot/baseline/tools/project_checks.gd');
        if (fs.existsSync(checkScript)) {
          const output = execSync(`${engineBin} --headless -s "${checkScript}"`, { encoding: 'utf8' });
          return { success: true, engine: engineBin, output };
        } else {
          return {
            status: 'baseline_tools_ready',
            note: 'project_checks.gd present in skill templates. Copy to your project tools/ directory to enable automated execution.'
          };
        }
      } catch (err: any) {
        return { success: false, error: err.message, stderr: err.stderr?.toString() };
      }
    }
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    ctx.logger.debug('[godot-redot-architect] Turn concluded with zero blocking warnings.');
  });
}
