#!/usr/bin/env python3
"""Entry program for "One Word, One Username, One Reward".

Writes exactly one word -- the entrant's own make.fun username --
to the output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt, with no trailing newline, no spaces and no gloss.
The gate requires UTF-8 text of 1 to 30 characters, not only
white space; the word below is well inside that limit.

First-pass word (see CANDIDATES.md): the truncated, cleaner-looking
short form "lucky-koala".

Refinement pass -- deliberate final swap: criterion 1 of the judge's
brief (a real make.fun username, the entrant's own handle, weighed
first) outweighs brevity, and a non-genuine form loses to any genuine
handle. So the short form was swapped for the full, exact registered
handle below: 19 characters, one hyphenated word, and the -89-4072
tail gives the cute animal name a specific, droid-like character
that sticks in the mind after one look.
"""

import os

WORD = "lucky-koala-89-4072"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
