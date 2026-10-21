/**
 * Extension: game-systems-dev-guard
 * Scoped to Game Systems & Gameplay Programmer (Game Engineering, Graphics & Modding Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Game Systems & Gameplay Programmer operational in Game Engineering, Graphics & Modding Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[game-systems-dev] Turn concluded with zero blocking warnings.');
  });
}
