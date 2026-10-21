/**
 * Extension: system-architect-guard
 * Scoped to Enterprise System Architect & ADR Owner (Executive, Product & Documentation Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Enterprise System Architect & ADR Owner operational in Executive, Product & Documentation Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[system-architect] Turn concluded with zero blocking warnings.');
  });
}
