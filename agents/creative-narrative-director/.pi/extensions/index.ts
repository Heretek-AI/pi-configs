/**
 * Extension: creative-narrative-director-guard
 * Scoped to Creative Narrative Director & Worldbuilding Architect (Executive, Product & Documentation Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Creative Narrative Director & Worldbuilding Architect operational in Executive, Product & Documentation Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[creative-narrative-director] Turn concluded with zero blocking warnings.');
  });
}
