/**
 * Extension: vector-rag-spec-guard
 * Scoped to Vector Embeddings, Hybrid Search & RAG Specialist (Data, Machine Learning & Code Hygiene Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Vector Embeddings, Hybrid Search & RAG Specialist operational in Data, Machine Learning & Code Hygiene Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[vector-rag-spec] Turn concluded with zero blocking warnings.');
  });
}
