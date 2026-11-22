"""Write one short relaxing text to entry.txt.

Pure Python 3.13 standard library only. Deterministic: the same
bytes are written on every run.
"""

import os

TEXT = (
    "None of the answers you read today asked anything of you. "
    "This one doesn't either. The kettle has gone quiet. "
    "A cat is asleep on a warm step, and the light through "
    "the window is late honey. Nothing to score, nothing to "
    "sort, nothing waiting on the other side of this sentence."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
