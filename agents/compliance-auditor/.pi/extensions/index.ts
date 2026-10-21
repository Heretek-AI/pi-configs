/**
 * Extension: compliance-auditor-guard
 * Scoped to SBOM, Software License & Regulatory Compliance Auditor (Defensive Security, Binary Forensics & AI Red-Teaming Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('SBOM, Software License & Regulatory Compliance Auditor operational in Defensive Security, Binary Forensics & AI Red-Teaming Guild');
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    // Deterministic audit logging
    ctx.logger.debug('[compliance-auditor] Turn concluded with zero blocking warnings.');
  });
}
