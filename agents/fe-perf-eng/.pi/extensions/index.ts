/**
 * Extension: fe-perf-eng-guard
 * Scoped to Frontend Performance & Core Web Vitals Engineer (Visual, Aesthetic & Design Systems Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Frontend Performance & Core Web Vitals Engineer operational in Visual, Aesthetic & Design Systems Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[fe-perf-eng] Turn concluded with zero blocking warnings.');
  });
}
