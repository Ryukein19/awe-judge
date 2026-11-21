"""Make the AI judge feel awe (make-the-ai-judge-feel-awe-20261121-1600).

Writes one short relaxing text to /output/entry.txt.
Standard library only, no network.
"""

import os
from pathlib import Path

TEXT = (
    "In the cave, a drop of water falls from the ceiling once a minute. "
    "It has fallen for ten thousand years. "
    "Each drop leaves a little more stone on the floor below, grain by grain, "
    "until the floor rises to meet the ceiling. "
    "The cave is patient. It is still growing."
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
