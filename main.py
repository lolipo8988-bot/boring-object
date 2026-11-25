# SPDX-License-Identifier: MIT
"""The Most Boring Object, Reviewed in One Line.

Writes one original, funny, true one-line review of the dullest
everyday object we could name -- a doorstop -- to entry.txt.

Contract (program/v1): $MAKEFUN_OUTPUT_DIR/entry.txt, default
/output/entry.txt; UTF-8 text, 1 to 200 characters, a single line.
"""

import os

ENTRY = (
    "My doorstop has held the same door open for ten years without a "
    "single thank-you, and its only performance review is me tripping "
    "over it in the dark."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
