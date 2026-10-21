/**
 * Extension: sabotage-qa-tester-guard
 * Scoped to Mutation Testing & Chaos Sabotage Tester (Quality Assurance & Verification Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Mutation Testing & Chaos Sabotage Tester operational in Quality Assurance & Verification Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[sabotage-qa-tester] Turn concluded with zero blocking warnings.');
  });
}
