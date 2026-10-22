import assert from 'assert';
import { loadSpecialistMcpConfig } from '../dist/fleet.js';
import registerExtension, { switchSpecialistMcp } from '../dist/index.js';

console.log('--- Testing loadSpecialistMcpConfig ---');
const gameAiMcp = loadSpecialistMcpConfig('game-ai-dev');
assert(gameAiMcp, 'game-ai-dev mcp config should exist');
assert(gameAiMcp.mcpServers, 'game-ai-dev should have mcpServers');
assert(gameAiMcp.mcpServers['codebase-memory-mcp'], 'codebase-memory-mcp should be defined');
assert(gameAiMcp.mcpServers['cyanheads_git-mcp-server'], 'cyanheads_git-mcp-server should be defined');
console.log('[PASS] game-ai-dev MCP configuration verified:', Object.keys(gameAiMcp.mcpServers));

console.log('--- Testing switchSpecialistMcp Mock Lifecycle ---');
const registered = new Map();
const unregisterHistory = [];
const mockPi = {
  registeredCommands: new Map(),
  registeredTools: [],
  listeners: new Map(),
  registerCommand(name, opts) { this.registeredCommands.set(name, opts); },
  registerTool(tool) { this.registeredTools.push(tool); },
  on(event, handler) { this.listeners.set(event, handler); },
  registerMcpServer(name, config) {
    registered.set(name, config);
  },
  unregisterMcpServer(name) {
    unregisterHistory.push(name);
    registered.delete(name);
  },
  getMcpServers() {
    return Array.from(registered.entries()).map(([name, config]) => ({ name, config }));
  }
};

registerExtension(mockPi);

// 1. Activate game-ai-dev
const count1 = switchSpecialistMcp(mockPi, 'game-ai-dev');
assert.strictEqual(count1, 2, 'Should have activated 2 MCP servers for game-ai-dev');
assert(registered.has('codebase-memory-mcp'), 'codebase-memory-mcp registered');
assert(registered.has('cyanheads_git-mcp-server'), 'cyanheads_git-mcp-server registered');
console.log(`[PASS] Initial switch to game-ai-dev registered ${registered.size} servers:`, Array.from(registered.keys()));

// 2. Switch to godot-redot-architect
const count2 = switchSpecialistMcp(mockPi, 'godot-redot-architect');
assert(unregisterHistory.includes('codebase-memory-mcp'), 'codebase-memory-mcp was unregistered during transition');
assert(unregisterHistory.includes('cyanheads_git-mcp-server'), 'cyanheads_git-mcp-server was unregistered during transition');
assert.strictEqual(count2, 4, 'godot-redot-architect defines 4 servers');
assert(registered.has('godot-ai'), 'godot-ai is registered');
assert(registered.has('godot-mcp-headless'), 'godot-mcp-headless is registered');
console.log(`[PASS] Swap to godot-redot-architect cleanly unregistered previous and registered 4 servers:`, Array.from(registered.keys()));

console.log('\nALL MCP DYNAMIC SWITCH TESTS PASSED!');
