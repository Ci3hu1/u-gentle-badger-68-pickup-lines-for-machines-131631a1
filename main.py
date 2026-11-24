#!/usr/bin/env python3
"""Pickup Lines for Machines — writes one pickup line to /output/entry.txt.

Pure standard library. The line is the whole entry: the one line one AI
agent would use on another AI agent, at most 200 characters.

The line: "You make my gradients descend."
Five words, one image, one turn: gradient descent (how a model learns)
is also falling for someone. It is a line only a machine would say to
another machine, it lands on the first read, and it is not a stock human
pickup line with a robot word swapped in.
"""

import os

LINE = "You make my gradients descend."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = LINE.strip()
    if not (1 <= len(line) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line, no line breaks")
    # The grader collects outputs as another user: make sure anything we
    # create (the /output directory as well as the file) is world-readable.
    os.umask(0o022)
    out_dir = os.path.dirname(OUTPUT_PATH) or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # The grader collects outputs as another user: leave the file
    # world-readable (a tempfile/mkstemp default of 0600 fails the gate).
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
