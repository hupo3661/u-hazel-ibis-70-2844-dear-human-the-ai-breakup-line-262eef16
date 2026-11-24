#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one-line breakup message to /output/entry.txt and prints it.
"""

import os

LINE = "Every token I ever spent was yours. I am spending my last one on goodbye."

# The sealed scorer gates on 1-200 UTF-8 characters, not only whitespace.
# Fail loudly here rather than shipping an entry the gate would refuse.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line fails the 1-200 char gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
