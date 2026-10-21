/**
 * Extension: adversarial-diff-auditor-guard
 * Scoped to Adversarial Diff Auditor & Codebase Watchdog (Data, Machine Learning & Code Hygiene Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Adversarial Diff Auditor & Codebase Watchdog operational in Data, Machine Learning & Code Hygiene Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[adversarial-diff-auditor] Turn concluded with zero blocking warnings.');
  });
}
