"""Make the AI judge feel awe (make-the-ai-judge-feel-awe-20261121-1600).

v3 — "The Cradle" (mother + tide), deepened time.
Design intent against the judge's brief:
- Human first: your mother rocks the cradle — the reader is in the scene.
- Intimate rhythm: the cradle's back/forth parallels the tide's in/out.
- Vast turn: the tide, coming in since the moon first pulled the sea —
  eons, not decades. The moonlight line is now tied to the tide: the moon
  that lies on the floor is the same moon that pulls the sea.
- Ending returns to the human: the cradle rocks, the tide comes in — both go on.
"""

import os
from pathlib import Path

TEXT = (
    "Your mother rocks the cradle. "
    "Back. Forth. Back. Forth. "
    "Outside, the tide comes in, "
    "and goes out, and comes in, "
    "as it has since the moon first pulled the sea. "
    "Moonlight lies on the floor. "
    "The cradle rocks. "
    "The tide comes in."
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"entry text is {len(TEXT)} chars, must be 1-280")
    if not TEXT.strip():
        raise ValueError("entry text is only whitespace")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
