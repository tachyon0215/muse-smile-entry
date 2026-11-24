#!/usr/bin/env python3
"""Write the entry line to entry.txt. Deterministic, stdlib only.

Entry for make.fun 'Make the Judge Smile': one line about a small good
thing that happened today, kept under the 200-character gate.
"""
import os
from pathlib import Path

LINE = "This morning my neighbour's toddler left a single grape on my doorstep, solemn as a tax payment, and walked away very pleased with the transaction."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    # The gate counts characters of the line itself, newline excluded.
    if not (1 <= len(text.rstrip("\n")) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
