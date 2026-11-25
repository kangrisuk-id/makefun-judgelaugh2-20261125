#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI Judge Laugh" bounty.

Writes one funny line about office life to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).

The line was picked by a local tournament: 44 candidates scored
against the judge's five published criteria, in the brief's order,
then an 8-seed knockout. See candidates.md for the full record.
"""

import os

LINE = (
    "The fire drill was the only meeting this quarter that started "
    "on time, ended early, and had a clear action item: leave."
)


def validated_line() -> str:
    """Return the entry line after checking it against the gate.

    The gate takes UTF-8 text of 1 to 200 characters, not only white
    space; the brief takes one line, so a newline is a failure too.
    """
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and "\n" not in LINE
    return LINE


def main() -> None:
    line = validated_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {path}: {len(line)} chars")


if __name__ == "__main__":
    main()
