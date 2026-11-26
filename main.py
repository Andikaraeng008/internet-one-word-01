"""The Internet in One Word — make.fun entry.

Gate: the program writes ONE word, 1-30 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The word is written exactly as-is: no newline, no extra text.
"""

import os

# The entry: one word for the whole internet (7 chars, gate allows 1-30).
# "cookies": every site begs you to accept them, and the whole internet
# runs on them — a snack and a tracker in one word.
WORD = "cookies"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
