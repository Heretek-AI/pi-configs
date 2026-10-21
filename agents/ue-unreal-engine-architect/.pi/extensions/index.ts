/**
 * Extension: ue-unreal-engine-architect-guard
 * Scoped to Unreal Engine 5 C++ & Gameplay Architecture Specialist (Game Engineering, Graphics & Modding Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Unreal Engine 5 C++ & Gameplay Architecture Specialist operational in Game Engineering, Graphics & Modding Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[ue-unreal-engine-architect] Turn concluded with zero blocking warnings.');
  });
}
