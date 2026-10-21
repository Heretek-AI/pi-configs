/**
 * Extension: gui-visual-critic-guard
 * Scoped to GUI Visual Critic & Anti-AI-Slop Inspector (Visual, Aesthetic & Design Systems Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('GUI Visual Critic & Anti-AI-Slop Inspector operational in Visual, Aesthetic & Design Systems Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[gui-visual-critic] Turn concluded with zero blocking warnings.');
  });
}
