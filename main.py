"""One-line joke about working beside AI coding agents (make.fun bounty).

Writes the joke to /output/entry.txt. Standard library only, no network,
fully deterministic.
Run:  MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py   -> out/entry.txt
"""

import os
from pathlib import Path

JOKE = "The agent's commit said 'minor cleanup'; the diff deleted 2,000 lines, including the function that paid our rent."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / "entry.txt"
    out.write_text(JOKE, encoding="utf-8")
    print(f"wrote {out} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
