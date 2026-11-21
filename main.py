"""Make the AI judge feel awe (make-the-ai-judge-feel-awe-20261121-1600).

v6 — "The Whale" (a living vastness, seen from a cliff).
Design intent against the judge's brief, from the v2/v4 research and
the lessons of v3/v4/v5 (leaderboards/awe-v2-research-20261121.md,
leaderboards/awe-v4-research-20261121.md):
- A COMPLETELY DIFFERENT concept from v1-v5. No cave, no cradle/tide,
  no moon, no grandmother's hand. No top-7 image either: no starlight
  arriving, no ferry + turning earth, no potter's clay, no stone in a
  lake, no red float + marine snow, no peas + sky, no honey + mother
  humming.
- The whale is a LIVING vastness: it breathes, it surfaces, it goes
  on. "You" stand on a cliff at dusk and watch it — the reader is IN
  the scene, small on the cliff, while the whale moves below.
- The cliff vantage is the dwarfing device: you are small and still
  above, the whale is huge and moving below — the scale gap is felt
  in the body, not thought about.
- Intimate rhythm: the breath and the spout ("It breathes, once,
  slow. The spout rises, and falls.") — a slow, felt cadence.
- Vast turn: "It has crossed this sea a hundred times, and it will
  cross it a hundred more." — the crossings are CONCRETE, ONGOING,
  and ARRIVING: a hundred behind it, a hundred ahead of it, and the
  whale is crossing NOW. This follows the v3 lesson (deep time must
  be concrete/ongoing/arriving, never an abstract cosmic fact).
- Return to the human: "You are still standing there. The whale
  goes on." — the vastness comes back to you, standing on the cliff,
  and keeps going after the last line.
- ONE scene, ONE turn, ONE vast image. No lists, no repeated whole
  clauses, no dense competing images, no tacked-on extra sentences
  (the v4/v5 lessons). Short lines, short fragments, no imperatives,
  no wellness words.
"""

import os
from pathlib import Path

TEXT = (
    "You stand on the cliff at dusk. "
    "Below you, the sea is dark. "
    "A whale surfaces. "
    "It breathes, once, slow. "
    "The spout rises, and falls. "
    "It has crossed this sea a hundred times, "
    "and it will cross it a hundred more. "
    "You are still standing there. "
    "The whale goes on."
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
