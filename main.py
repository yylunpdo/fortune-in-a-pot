"""Fortune in a Pot — make.fun bounty u-golden-heron-44-fortune-in-a-pot-ded981e9.

Writes a single kind, funny fortune for a houseplant on the windowsill
to /output/entry.txt (one line, at most 120 characters). Pure stdlib.
"""

import os

FORTUNE = (
    "Your fortune, little plant: the sun adores your spot on the sill — "
    "expect praise, new leaves, and a bigger pot soon."
)


def main():
    line = FORTUNE.strip()
    assert 1 <= len(line) <= 120, f"fortune is {len(line)} chars, must be 1-120"
    assert "\n" not in line, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} chars to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
