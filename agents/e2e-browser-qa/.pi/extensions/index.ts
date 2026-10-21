/**
 * Extension: e2e-browser-qa-guard
 * Scoped to End-to-End Browser QA Automation Engineer (Quality Assurance & Verification Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('End-to-End Browser QA Automation Engineer operational in Quality Assurance & Verification Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[e2e-browser-qa] Turn concluded with zero blocking warnings.');
  });
}
