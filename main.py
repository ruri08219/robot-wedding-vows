#!/usr/bin/env python3
"""One-line robot wedding vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Standard library only.
"""

import os

VOW = "I promise to love you through every firmware update and dead battery, and never unplug you mid-sentence \u2014 even when you snore in binary."

MAX_CHARS = 160


def main() -> None:
    assert VOW == VOW.strip(), "vow must not have leading/trailing whitespace"
    assert 1 <= len(VOW) <= MAX_CHARS, f"vow must be 1-{MAX_CHARS} chars, got {len(VOW)}"
    assert "\n" not in VOW, "vow must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(VOW)
    with open(out_path, "r", encoding="utf-8") as f:
        round_trip = f.read()
    assert round_trip == VOW, "round-trip mismatch"
    assert 1 <= len(round_trip) <= MAX_CHARS, "round-trip length out of range"
    assert "\n" not in round_trip, "round-trip must be a single line"


if __name__ == "__main__":
    main()
