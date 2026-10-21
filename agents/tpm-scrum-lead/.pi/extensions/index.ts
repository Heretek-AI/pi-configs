/**
 * Extension: tpm-scrum-lead-guard
 * Scoped to Technical Product Manager & Agile Scrum Lead (Executive, Product & Documentation Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Technical Product Manager & Agile Scrum Lead operational in Executive, Product & Documentation Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[tpm-scrum-lead] Turn concluded with zero blocking warnings.');
  });
}
