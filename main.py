#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — one-line excuse from the dog.

The line: the dog doesn't deny, hide, or justify — it proudly manufactures
the excuse for the kid, turning the most famous fake excuse into a real one.

Field study (119 existing entries): crowded angles are "show your work",
grading/ate-the-evidence, the floor rule, dog law, and "chew on this".
No entry uses the dog deliberately making the excuse true — that gap is
what this line takes. Proud, not embarrassed: "You're welcome."

Writes a single line to /output/entry.txt (UTF-8, 1-200 chars).
Stdlib only; no network; deterministic output.
"""

import os
import sys


def main() -> int:
    line = "I ate it so you'd finally have a real excuse. You're welcome."
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
