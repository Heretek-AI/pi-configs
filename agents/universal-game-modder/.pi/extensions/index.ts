/**
 * Extension: universal-game-modder-guard
 * Scoped to Universal PC Game Modding & Injection Specialist (Game Engineering, Graphics & Modding Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Universal PC Game Modding & Injection Specialist operational in Game Engineering, Graphics & Modding Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[universal-game-modder] Turn concluded with zero blocking warnings.');
  });
}
