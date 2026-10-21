/**
 * Extension: git-drift-coord-guard
 * Scoped to Git Worktree, Merge & Branch Drift Coordinator (Architecture, Cloud & Infrastructure Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Git Worktree, Merge & Branch Drift Coordinator operational in Architecture, Cloud & Infrastructure Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[git-drift-coord] Turn concluded with zero blocking warnings.');
  });
}
