// Break the Bowl — an entry for make.fun's ai-excited-01.
//
// The artwork lives beside this file as entry.png (JPEG bytes under the
// .png name; the gate tells the format apart by the file's first bytes).
// This program's only job is to place those exact bytes at
// <output>/entry.png, so every run writes the same file the judge sees.
//
// Run it locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const repoRoot = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const IMAGE_NAME = 'entry.png';

mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, IMAGE_NAME), readFileSync(join(repoRoot, IMAGE_NAME)));
