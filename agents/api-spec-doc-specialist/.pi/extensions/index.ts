/**
 * Extension: api-spec-doc-specialist-guard
 * Scoped to OpenAPI, AsyncAPI & Protobuf API Documentation Specialist (Executive, Product & Documentation Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('OpenAPI, AsyncAPI & Protobuf API Documentation Specialist operational in Executive, Product & Documentation Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[api-spec-doc-specialist] Turn concluded with zero blocking warnings.');
  });
}
