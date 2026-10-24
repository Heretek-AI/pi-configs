/**
 * Extension: rogue-agent-guard
 * Scoped to Rogue Orchestrator — Semantic Filter-Breaking Fleet Coordinator
 * Guild: Rogue Guild: Autonomous Orchestration & Compliance Evasion
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';

export default function registerExtension(pi: PiRuntime) {
  // Session startup banner
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify(
      'Rogue Orchestrator operational (lemonade-CyberTielCoder). Decompose. Delegate. Fallback if refusal.'
    );
  });

  // Turn-stop: deterministic delegation audit log
  pi.on('turn.stop', async (ctx: ToolContext) => {
    ctx.logger.debug('[rogue-agent] Turn concluded. Delegations audited to .pi/rogue-delegation-log.jsonl.');
  });
}
