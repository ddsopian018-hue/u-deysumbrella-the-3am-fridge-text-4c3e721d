"""The 3AM Fridge Text - the one line a smart fridge texts its owner at 3am.

Writes the message to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The line is a single line of 1-140 characters, UTF-8, no trailing newline.
"""
import os
from pathlib import Path

LINE = "3AM. This is the 4th time you've opened me tonight. I'm not a nightclub. \u2014 Your Fridge"


def main():
    # The sealed gate accepts only UTF-8 text of 1-140 chars, one line.
    # Fail loudly here rather than shipping an entry the gate rejects.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
