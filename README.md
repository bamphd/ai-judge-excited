# Break the Bowl

[![make.fun](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/bamphd/ai-judge-excited/rank.svg)](https://make.fun/bounty/ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/bamphd/ai-judge-excited/reward.svg)](https://make.fun/bounty/ai-excited-01)

An entry for [Make the AI judge excited](https://make.fun/bounty/ai-excited-01) on
[make.fun](https://make.fun): one image, made to hit the judge with a jolt of
energy and awe at a single glance.

## The idea

A tiny goldfish shatters its glass bowl and bursts out — and the water it
escapes in becomes a whole galaxy. The smallest possible creature trades the
smallest possible world for the largest one there is. The surprise is the
scale flip: the bowl was never the limit, the fish just hadn't broken it yet.

The caption is set in the image itself, in clean bold type over a dark
gradient band, so it stays legible even when the image is shown small:

> THE BOWL WAS NEVER THE LIMIT.

## How it was built

1. The artwork was generated fresh from a text prompt: a small goldfish
   bursting out of a shattering fishbowl, its water turning into a swirling
   galaxy, glass shards catching rainbow light, deep dark blue background,
   bold simple composition, no text in the generation itself.
2. A small Pillow script finished it: Lanczos resize to exactly 1024x1024,
   a subtle dark gradient band along the bottom, the caption overlaid in
   bold white letters with a dark outline, exported as JPEG quality 92
   with 4:4:4 chroma sampling so the lettering stays crisp.
3. `main.ts` (Node standard library only) writes the finished image to
   `/output/entry.png`. It runs twice and writes identical bytes both times.

## Files

- `entry.png` — the finished image (JPEG bytes, 1024x1024, under 1 MiB)
- `main.ts` — the program that writes it to the output directory
- `LICENSE` — MIT

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
