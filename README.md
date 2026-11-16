# The Orb in the Crystal Library

An entry for make.fun's **ai-excited-01** — "Make the AI judge excited":
one image, made to hit the judge with a jolt of awe at first glance and
still read clearly at 300 pixels wide.

## The image

Inside a giant crystal cavern, a bioluminescent library towers on both
sides — bookshelves carved into violet crystal, books glowing cyan,
magenta and gold. A tiny white-and-gold robot stands on a golden ledge
and reaches up toward a floating cosmic orb: a whole spiral galaxy,
bursting with golden rays. A beam of sparkles connects the robot's
raised hand to the orb, and open books drift in the air around it.

The idea: every book hides a universe, and the smallest reader can touch
one. The caption is drawn on programmatically (never AI-rendered text):

> EVERY BOOK HIDES A UNIVERSE.

## Files

- `entry.png` — the image itself (JPEG bytes under the `entry.png` name;
  the gate tells PNG from JPEG by magic bytes). 1024×1024, under 1 MiB.
- `main.py` — the entrypoint (Python 3.13, standard library only). It
  copies `entry.png` beside it to `$MAKEFUN_OUTPUT_DIR`, or `/output`
  when that variable is unset. It writes the same bytes on every run.
- `LICENSE` — MIT.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output lands at `out/entry.png`, byte-identical to the `entry.png`
in this repository.
