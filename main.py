#!/usr/bin/env python3
"""The joke about the demo.

A one-line joke about working beside AI coding agents, for a room
watching a demo. Pure standard library; no network. Writes the joke
to /output/entry.txt (128 characters).
"""

import os

JOKE = (
    "In the live demo, my coding agent fixed the bug, broke the build, "
    "and left an apology in the commit message longer than the fix."
)


def main():
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise SystemExit("entry text must be 1-280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        raise SystemExit("entry.txt content mismatch after write")


if __name__ == "__main__":
    main()
