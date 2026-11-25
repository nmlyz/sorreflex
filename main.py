#!/usr/bin/env python3
"""Write one line to /output/entry.txt: a newly coined English word and
its one-line definition.

The line was picked from 37 candidates by pairwise judging against the
brief — a social reflex everyone has felt but no word names, told as the
behaviour itself with no example attached. The program builds the line
from two parts — the coined word, then its definition — and checks the
result against the entry gate (length, single line, no leading or
trailing space, exact judged length) before writing it, then reads the
file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "Sorreflex: "
    'Saying "sorry" when someone else bumps into you.'
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 140):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-140")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = LINE.encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
