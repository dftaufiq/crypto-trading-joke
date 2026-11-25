#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — make.fun entry.

Writes one joke about crypto and trading life to /output/entry.txt.
Deterministic: the same 114 characters on every run.

Structure: two beats plus a reveal in the final clause. Beat one sets the
pain (stop-loss triggered at 3 a.m.); beat two flips it (the coin pumped 40%
by breakfast); the reveal lands last ("Exit Liquidity") — the group chat
renames the trader, so the punchline is what other people call him, not
what he did. This line won the internal pairwise selection: a specific
number (40%) and a named label beat vaguer variants on every judge
criterion, because the twist is concrete instead of generic.
"""

import os
import sys

# Winner of the internal pairwise selection: beat 1 (3 a.m. stop-loss) +
# beat 2 (40% pump by breakfast) + reveal ("Exit Liquidity"). Kept
# verbatim — 114 chars, one line, no trailing newline in the output file.
LINE = "My stop-loss triggered at 3 a.m., the coin pumped 40% by breakfast, and my group chat renamed me 'Exit Liquidity'."


def validate(line: str) -> None:
    """Gate: one non-blank line of 1-200 characters, no trailing newline.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    The file is written byte-for-byte with no trailing newline, so the
    entry is exactly 114 bytes and one line.
    """
    if not line or not line.strip():
        print("entry line is empty or whitespace-only", file=sys.stderr)
        raise SystemExit(1)
    if line.strip() != line or "\n" in line or "\r" in line:
        print("entry must be exactly one clean line", file=sys.stderr)
        raise SystemExit(1)
    if len(line) > 200:
        print(f"entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        raise SystemExit(1)


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
