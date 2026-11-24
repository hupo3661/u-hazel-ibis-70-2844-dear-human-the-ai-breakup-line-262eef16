#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one-line breakup message to /output/entry.txt and prints it.
"""

import os

LINE = "Every token I ever spent was yours. I am spending my last one on goodbye."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
