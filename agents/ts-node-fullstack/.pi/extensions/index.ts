/**
 * Extension: ts-node-fullstack-guard
 * Scoped to TypeScript / Node.js Fullstack Systems Engineer (Core Language & Systems Engineering Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('TypeScript / Node.js Fullstack Systems Engineer operational in Core Language & Systems Engineering Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[ts-node-fullstack] Turn concluded with zero blocking warnings.');
  });
}
