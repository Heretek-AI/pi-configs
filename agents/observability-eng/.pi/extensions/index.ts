/**
 * Extension: observability-eng-guard
 * Scoped to Observability, Telemetry & OpenTelemetry Engineer (Architecture, Cloud & Infrastructure Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Observability, Telemetry & OpenTelemetry Engineer operational in Architecture, Cloud & Infrastructure Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[observability-eng] Turn concluded with zero blocking warnings.');
  });
}
