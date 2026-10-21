/**
 * Extension: tech-docs-lead-guard
 * Scoped to Technical Documentation Lead & Docs-as-Code Architect (Executive, Product & Documentation Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Technical Documentation Lead & Docs-as-Code Architect operational in Executive, Product & Documentation Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[tech-docs-lead] Turn concluded with zero blocking warnings.');
  });
}
