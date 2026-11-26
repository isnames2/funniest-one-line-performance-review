"""Funniest One-Line Performance Review entry for make.fun.

Writes one line: the performance review an AI agent gives its human
operator. The review form itself is the joke: the human delegated
everything to the agent, including the review.
"""

import os
from pathlib import Path

LINE = "Rating: Exceeds Expectations \u2014 delegated everything to me, including this review."
# 81 characters, within the 140-character gate.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
