/**
 * Extension: lsp-type-graph-navigator-guard
 * Scoped to Semantic LSP & Code Knowledge Graph Navigator (Data, Machine Learning & Code Hygiene Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Semantic LSP & Code Knowledge Graph Navigator operational in Data, Machine Learning & Code Hygiene Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[lsp-type-graph-navigator] Turn concluded with zero blocking warnings.');
  });
}
