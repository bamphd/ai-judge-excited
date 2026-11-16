# The Orb in the Crystal Library

An entry for [make.fun's "Make the AI judge excited" bounty](https://make.fun/bounty/ai-excited-01) (`ai-excited-01`).

## The image

Deep inside a giant crystal cavern glows a bioluminescent library — towering
shelves of violet and teal crystal, thousands of softly lit books. A tiny
curious robot stands on a crystal bridge, one arm raised toward a huge
floating orb: a whole spiral galaxy, swirling with stars, hanging in the
dark like the library's brightest book. A ribbon of golden books streams up
from the robot's hand toward the orb, caught in the light.

One look, one idea: **every book hides a universe.** The caption is drawn
programmatically (never AI-rendered text) so it stays crisp at any size.

## How it works

The repository holds the finished image (`entry.png`, a 1024×1024 JPEG under
the required name, well inside the 1 MiB gate) and a small Node 22 program
(`main.ts`, standard library only) that copies it verbatim to `/output`.
The program is deterministic: every run writes the same bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see [LICENSE](LICENSE).
