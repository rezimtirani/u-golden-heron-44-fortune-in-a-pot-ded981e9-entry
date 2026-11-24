#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant.

The fortune is a single line of at most 120 characters, written to
``$MAKEFUN_OUTPUT_DIR/entry.txt``. It is written for the plant on the
windowsill itself: sunshine spilling across the sill, and a keeper
proud enough to brag about it to every guest who walks in.
"""

import os
import sys


FORTUNE = (
    "Soon the sun will spill across your windowsill, and your keeper "
    "will brag about you to every guest who walks in."
)


def validate_fortune(text: str) -> str:
    """Return the fortune stripped, or raise if it breaks the gate."""
    clean = text.strip()
    if not clean:
        raise ValueError("fortune must not be only white space")
    if len(clean) > 120:
        raise ValueError(
            f"fortune is {len(clean)} characters, must be at most 120")
    if "\n" in clean:
        raise ValueError("fortune must be a single line")
    return clean


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    try:
        text = validate_fortune(FORTUNE)
    except ValueError as err:
        print(err, file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
