#!/usr/bin/env python3
"""One-line joke for the demo room.

Composes a single joke about pairing with an AI coding agent during a
live demo, then saves it as plain text. Standard library only, and it
never touches the network.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")

PARTS = [
    "In the live demo, my coding agent ",
    "fixed the bug, broke the build, and ",
    "left an apology in the commit message ",
    "longer than the fix.",
]

TEXT = "".join(PARTS)


def check(text):
    if not text.strip():
        raise SystemExit("joke is blank")
    if text != text.strip() or "  " in text:
        raise SystemExit("joke has stray whitespace")
    if len(text) > 280:
        raise SystemExit("joke is too long: %d chars" % len(text))


def main():
    check(TEXT)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(TEXT, encoding="utf-8")
    if OUT.read_text(encoding="utf-8") != TEXT:
        raise SystemExit("saved joke differs from the text")


main()
