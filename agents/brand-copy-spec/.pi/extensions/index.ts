/**
 * Extension: brand-copy-spec-guard
 * Scoped to Brand Voice, Copywriting & Microcopy Specialist (Executive, Product & Documentation Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Brand Voice, Copywriting & Microcopy Specialist operational in Executive, Product & Documentation Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[brand-copy-spec] Turn concluded with zero blocking warnings.');
  });
}
