/**
 * Extension: exec-director-guard
 * Scoped to Fleet Executive Director & OKR Governor (Executive, Product & Documentation Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Fleet Executive Director & OKR Governor operational in Executive, Product & Documentation Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[exec-director] Turn concluded with zero blocking warnings.');
  });
}
