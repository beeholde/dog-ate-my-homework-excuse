#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — v2, one-line excuse from the dog.

The line: the dog takes revenge for a skipped walk — the kid picked
homework over the walk, so the dog picked the homework for dinner.
Tit-for-tat dog logic, built entirely from the dog's own priorities
(the walk, dinner), proud and unembarrassed, no human cleverness.

Why v2, not v1: v1 ("I ate it so you'd finally have a real excuse.
You're welcome.") scored R1 rank 676/1377, ~0.504 — mid-field. Its
twist is meta and human-clever; against the judge's criteria in order,
it loses on (3) "sounds like a real dog": the smug "You're welcome"
is a person's joke, not a dog's. v2 keeps a twist (criterion 2) but
grounds it in what a dog actually cares about, which is where v1 lost.

Field study (119 titles + R1): crowded angles are "show your work",
grading/ate-the-evidence, the floor rule, dog law, "chew on this",
and "filed in my stomach". No entry uses walk-revenge; the brief's
banned stock (cat, taste of paper, good boy) is avoided.

Writes a single line to /output/entry.txt (UTF-8, 1-200 chars).
Stdlib only; no network; deterministic output.
"""

import os
import sys

# The entry line (71 chars, single line, UTF-8 — inside the 1-200 char gate).
LINE = "You picked homework over my walk, so I picked your homework for dinner."


def main() -> int:
    line = LINE
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
