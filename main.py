"""Make the AI judge feel awe (make-the-ai-judge-feel-awe-20261121-1600).

v4 — "The Grandmother's Hand" (generations / lineage).
Design intent against the judge's brief, from research across all connected
sources (leaderboards/awe-v4-research-20261121.md):
- Vastness is SOCIAL + TEMPORAL through people, not geology: a chain of
  hands across generations. No top-7 entry uses lineage, life-and-death,
  moral beauty, or micro-vastness — this is the gap.
- Life and death: grandmother (end of life) holding the child's hand (the
  beginning). The handover — the hand is the gift, not the object.
- Radical scale shift down: one small hand ("Warm. Rough. Small.")
  contains generations.
- Anaphora: "and her mother's hand before that, / and her mother's hand
  before that" — the chain stacking up.
- Rule of threes: "a plough, a net, a child" — three things the hands held.
- Perspective alienation: the child's perspective (you, the grandchild,
  feeling the hand).
- Return to human: "Her hand is still holding yours." — the vast chain
  comes back to the touch.
- Brave transfer: a hand, warmth, support, a relationship (the judge's
  known favourite). No imperatives, no wellness words. Short lines,
  short fragments.
"""

import os
from pathlib import Path

TEXT = (
    "Your grandmother holds your hand. "
    "Warm. Rough. Small. "
    "It held your mother's hand, "
    "and her mother's hand before that, "
    "and her mother's hand before that, "
    "all the way back to hands "
    "that held a plough, a net, a child, "
    "before there was a road here. "
    "Her hand is still holding yours."
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
