"""Have You Tried Turning It Off (tech support line).

Writes one funny line a hopeless tech support agent says to a desperate
customer to /output/entry.txt: the router is in the attic, the attic is
locked, and the key is inside the attic. Pure Python 3.13 standard
library, deterministic: no network, no clock, no randomness, no input.
Two runs write byte-identical output.
"""

import os
import sys

LINE = "Ma'am, I can fix your Wi-Fi, but the router is in the attic, the attic is locked, and the key is -- and I cannot stress this enough -- inside the attic."

# Bounty gate: the entry must be one line of 1-199 UTF-8 characters.
MIN_CHARS = 1
MAX_CHARS = 199


def main() -> None:
    if not MIN_CHARS <= len(LINE) <= MAX_CHARS:
        print(
            f"invalid entry: {len(LINE)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} range",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in LINE or "\r" in LINE:
        print("invalid entry: must be a single line", file=sys.stderr)
        sys.exit(1)
    if LINE != LINE.strip():
        print(
            "invalid entry: must not start or end with whitespace",
            file=sys.stderr,
        )
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
