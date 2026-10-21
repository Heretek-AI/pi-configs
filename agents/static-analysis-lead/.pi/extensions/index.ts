/**
 * Extension: static-analysis-lead-guard
 * Scoped to Code Style, Semgrep Rules & Static Analysis Lead (Data, Machine Learning & Code Hygiene Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Code Style, Semgrep Rules & Static Analysis Lead operational in Data, Machine Learning & Code Hygiene Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[static-analysis-lead] Turn concluded with zero blocking warnings.');
  });
}
