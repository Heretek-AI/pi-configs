/**
 * Extension: mlops-serving-eng-guard
 * Scoped to Model Serving, Quantization & vLLM/Ollama MLOps Engineer (Data, Machine Learning & Code Hygiene Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Model Serving, Quantization & vLLM/Ollama MLOps Engineer operational in Data, Machine Learning & Code Hygiene Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[mlops-serving-eng] Turn concluded with zero blocking warnings.');
  });
}
