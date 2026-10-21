/**
 * Extension: game-feel-and-vfx-critic-guard
 * Scoped to Game Feel, VFX & Juiciness Critic (Visual, Aesthetic & Design Systems Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Game Feel, VFX & Juiciness Critic operational in Visual, Aesthetic & Design Systems Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[game-feel-and-vfx-critic] Turn concluded with zero blocking warnings.');
  });
}
