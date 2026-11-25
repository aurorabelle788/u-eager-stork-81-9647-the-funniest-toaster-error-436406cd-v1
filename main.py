"""The Funniest Toaster Error Message.

Writes one line -- the funniest error message a kitchen toaster would
show its owner -- to /output/entry.txt. Deterministic, stdlib only,
no network, no randomness, no files read outside the repo.

The joke: the toaster is not broken, burnt, or jammed. It is simply
confronted with a bagel -- an object it was never briefed on -- and
is too embarrassed to admit it. Deadpan, apologetic, one voice, and
deliberately nowhere near the burnt-toast / crumb / "pop up" pun
territory the obvious entries live in.
"""

import os

LINE = "ERROR: I have no idea what a bagel is and I am too afraid to ask."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
