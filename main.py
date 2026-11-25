#!/usr/bin/env python3
"""Roast Your Own Agent — writes the entry to /output/entry.txt."""

import os

ENTRY = "My agent narrates everything like a sports commentator — play-by-play of a game nobody is watching, and somehow we're still losing."


def main() -> None:
    if not ENTRY:
        raise SystemExit("entry is empty")
    if ENTRY.strip() == "":
        raise SystemExit("entry is only whitespace")
    if len(ENTRY) > 140:
        raise SystemExit("entry is too long: %d characters" % len(ENTRY))
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.replace(tmp, path)
    # Read-back verification: the written bytes must match the entry exactly.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise SystemExit("read-back verification failed: entry.txt bytes differ")


if __name__ == "__main__":
    main()
