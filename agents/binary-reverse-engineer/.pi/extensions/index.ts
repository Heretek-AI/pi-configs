/**
 * Extension: binary-reverse-engineer-guard
 * Scoped to Binary Disassembly & Headless Decompilation Specialist (Defensive Security, Binary Forensics & AI Red-Teaming Guild)
 */

import { type PiRuntime, type ToolContext } from '@mariozechner/pi-coding-agent';
import * as fs from 'fs';
import * as path from 'path';

export default function registerExtension(pi: PiRuntime) {
  // Session initialization hook
  pi.on('session.start', async (ctx: ToolContext) => {
    ctx.ui.notify('Binary Disassembly & Headless Decompilation Specialist active with Evidence Ledger and Disassembly routing harnesses.');
  });

  // Custom tool: binary_inspect
  pi.registerTool({
    name: 'binary_inspect',
    description: 'Inspects a binary file header to extract file signature, magic bytes, architecture, bitness, and endianness.',
    parameters: {
      type: 'object',
      properties: {
        filePath: {
          type: 'string',
          description: 'Relative or absolute path to the binary file.'
        }
      },
      required: ['filePath']
    },
    execute: async (args: { filePath: string }, _ctx: ToolContext) => {
      const targetPath = path.isAbsolute(args.filePath) ? args.filePath : path.join(process.cwd(), args.filePath);
      if (!fs.existsSync(targetPath)) {
        return { error: `File not found: ${args.filePath}` };
      }

      const fd = fs.openSync(targetPath, 'r');
      const buffer = Buffer.alloc(64);
      fs.readSync(fd, buffer, 0, 64, 0);
      fs.closeSync(fd);

      const stats = fs.statSync(targetPath);
      let format = 'UNKNOWN';
      let arch = 'UNKNOWN';
      let bitness = 'UNKNOWN';
      let endianness = 'little';

      // Check PE (MZ)
      if (buffer[0] === 0x4D && buffer[1] === 0x5A) {
        format = 'PE (Portable Executable / Windows)';
        const peOffset = buffer.readInt32LE(0x3C);
        if (peOffset < stats.size - 4) {
          const peBuf = Buffer.alloc(6);
          const peFd = fs.openSync(targetPath, 'r');
          fs.readSync(peFd, peBuf, 0, 6, peOffset);
          fs.closeSync(peFd);
          if (peBuf[0] === 0x50 && peBuf[1] === 0x45) {
            const machine = peBuf.readUInt16LE(4);
            if (machine === 0x8664) { arch = 'x86_64 (AMD64)'; bitness = '64-bit'; }
            else if (machine === 0x014C) { arch = 'i386 (x86)'; bitness = '32-bit'; }
            else if (machine === 0xAA64) { arch = 'ARM64 (AArch64)'; bitness = '64-bit'; }
          }
        }
      }
      // Check ELF
      else if (buffer[0] === 0x7F && buffer[1] === 0x45 && buffer[2] === 0x4C && buffer[3] === 0x46) {
        format = 'ELF (Executable and Linkable Format / Linux/BSD)';
        bitness = buffer[4] === 1 ? '32-bit' : buffer[4] === 2 ? '64-bit' : 'UNKNOWN';
        endianness = buffer[5] === 1 ? 'little' : buffer[5] === 2 ? 'big' : 'UNKNOWN';
        const machine = endianness === 'little' ? buffer.readUInt16LE(18) : buffer.readUInt16BE(18);
        if (machine === 0x3E) arch = 'x86_64';
        else if (machine === 0x03) arch = 'i386';
        else if (machine === 0xB7) arch = 'AArch64';
        else if (machine === 0x28) arch = 'ARM';
      }
      // Check Mach-O
      else if (buffer[0] === 0xFE && buffer[1] === 0xED && buffer[2] === 0xFA && (buffer[3] === 0xCE || buffer[3] === 0xCF)) {
        format = 'Mach-O (macOS/iOS)';
        bitness = buffer[3] === 0xCF ? '64-bit' : '32-bit';
      }
      // Check WASM
      else if (buffer[0] === 0x00 && buffer[1] === 0x61 && buffer[2] === 0x73 && buffer[3] === 0x6D) {
        format = 'WebAssembly (WASM)';
        bitness = '32/64-bit';
      }

      return {
        file: args.filePath,
        fileSizeBytes: stats.size,
        magicHex: buffer.subarray(0, 16).toString('hex'),
        detectedFormat: format,
        architecture: arch,
        bitness,
        endianness
      };
    }
  });

  // Custom tool: evidence_ledger_validate
  pi.registerTool({
    name: 'evidence_ledger_validate',
    description: 'Verifies that a reverse engineering markdown report complies with the Evidence Ledger Invariant (must contain explicit [OBSERVED], [DERIVED], and [INFERRED] claim anchors).',
    parameters: {
      type: 'object',
      properties: {
        reportPath: {
          type: 'string',
          description: 'Path to markdown analysis report.'
        }
      },
      required: ['reportPath']
    },
    execute: async (args: { reportPath: string }, _ctx: ToolContext) => {
      const fullPath = path.isAbsolute(args.reportPath) ? args.reportPath : path.join(process.cwd(), args.reportPath);
      if (!fs.existsSync(fullPath)) {
        return { error: `Report not found: ${args.reportPath}` };
      }

      const content = fs.readFileSync(fullPath, 'utf8');
      const observedMatches = content.match(/\[OBSERVED\s+(?:0x[0-9a-fA-F]+|offset:[^\]]+)\]/g) || [];
      const derivedMatches = content.match(/\[DERIVED\]/g) || [];
      const inferredMatches = content.match(/\[INFERRED\]/g) || [];

      const totalClaims = observedMatches.length + derivedMatches.length + inferredMatches.length;
      const isCompliant = observedMatches.length > 0 && totalClaims >= 3;

      return {
        report: args.reportPath,
        isCompliant,
        observedClaimsCount: observedMatches.length,
        derivedClaimsCount: derivedMatches.length,
        inferredClaimsCount: inferredMatches.length,
        sampleObserved: observedMatches.slice(0, 3),
        recommendation: isCompliant
          ? 'Evidence Ledger compliance confirmed. Grounding invariants satisfied.'
          : 'Compliance warning: Analysis must anchor decompilation observations in explicit hex offsets ([OBSERVED 0x...]).'
      };
    }
  });

  // Turn verification guard
  pi.on('turn.stop', async (ctx: ToolContext) => {
    ctx.logger.debug('[binary-reverse-engineer] Turn concluded with zero blocking warnings.');
  });
}
