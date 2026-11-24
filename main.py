#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

Title: "The Fix Was the Bug" — 5-7-5, three lines, no trailing newline.
Stdlib only (the grader runs python:3.13-slim with no site-packages).
"""
import os

HAIKU = (
    "I fixed it at last\n"
    "and watched the green tests turn red\n"
    "the fix was the bug"
)

# Syllable count per word, sounded out by hand (5-7-5).
# L1: I(1) fixed(1) it(1) at(1) last(1) = 5
# L2: and(1) watched(1) the(1) green(1) tests(1) turn(1) red(1) = 7
# L3: the(1) fix(1) was(1) the(1) bug(1) = 5
SYLLABLES = {
    "i": 1, "fixed": 1, "it": 1, "at": 1, "last": 1,
    "and": 1, "watched": 1, "the": 1, "green": 1, "tests": 1,
    "turn": 1, "red": 1, "fix": 1, "was": 1, "bug": 1,
}


def _check(text):
    lines = text.split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert not text.endswith("\n"), "no trailing newline allowed"
    assert 1 <= len(text) <= 200, f"char count {len(text)} outside 1-200"
    counts = [
        sum(SYLLABLES[w.lower()] for w in line.split()) for line in lines
    ]
    assert counts == [5, 7, 5], f"syllable counts {counts} != [5, 7, 5]"
    return counts


def main():
    counts = _check(HAIKU)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)
    print(f"wrote {len(HAIKU)} chars, syllables {counts}")


if __name__ == "__main__":
    main()
