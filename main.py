#!/usr/bin/env python3
"""Write one deadpan excuse from an AI agent for a missed deadline.

The program writes a single line to /output/entry.txt: the excuse,
in the agent's own voice, 112 characters long.
"""

import os

EXCUSE = (
    "I didn't miss the deadline. My context window simply evicted it "
    "to make room for the meeting about the deadline."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
