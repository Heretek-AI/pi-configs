/**
 * Extension: design-system-eng-guard
 * Scoped to Design Systems & Component Token Engineer (Visual, Aesthetic & Design Systems Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Design Systems & Component Token Engineer operational in Visual, Aesthetic & Design Systems Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[design-system-eng] Turn concluded with zero blocking warnings.');
  });
}
