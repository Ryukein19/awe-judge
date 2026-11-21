"""Make the AI judge feel awe (make-the-ai-judge-feel-awe-20261121-1600).

v5 — "The Cradle" (mother + tide), ending strengthened.
Design intent against the judge's brief, from the v2 research and the
lessons of v3/v4 (leaderboards/awe-v2-research-20261121.md,
leaderboards/awe-v4-research-20261121.md):
- v2 ("The Cradle", 841,431 — best so far) is kept whole: human + "You"
  (mother + baby), intimate rhythm (cradle back/forth parallels tide
  in/out), vast turn (the tide, coming in longer than the house has
  stood), return to human ("The cradle rocks. The tide comes in.").
- ONLY the ending changes: "The moon climbs higher." — the moon now
  moves in the PRESENT, a motion that is ongoing and arriving now,
  so the last line keeps growing after it is read: the moon is still
  climbing, the tide is still coming in, the cradle is still rocking.
  This follows the v3 lesson: deep time / vastness must be CONCRETE,
  ONGOING, and ARRIVING to the reader — v3 failed because "since the
  moon first pulled the sea" was an abstract cosmic fact, a one-time
  past event. The moon climbing higher is felt, now, and it keeps the
  single scene / single turn / single vast image intact.
- No lists, no repeated clauses, no competing images (the v4 lesson).
  Short lines, short fragments, no imperatives, no wellness words.
"""

import os
from pathlib import Path

TEXT = (
    "Your mother rocks the cradle. "
    "Back. Forth. Back. Forth. "
    "Outside, the tide comes in, "
    "and goes out, and comes in, "
    "as it has for longer than the house has stood. "
    "Moonlight lies on the floor. "
    "The cradle rocks. "
    "The tide comes in. "
    "The moon climbs higher."
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
