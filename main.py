"""Funniest One-Line Out-of-Office Reply.

Writes a single one-line out-of-office auto-reply to the entry output
(/output/entry.txt by default) and prints the same text to stdout.

The reply is a fresh turn on the standard away message: instead of the
usual promise that mail will be answered in the order it arrived, it
admits the honest queueing policy up front. It reads like a real message
a person would switch on before going away, lands on the first read,
and needs no setup, signature, or name to make sense.
"""

import os
import sys

ENTRY = "I'm away until Monday; your email will be answered in the order it was ignored."

DEFAULT_OUTPUT = "/output/entry.txt"


def resolve_output_path():
    """Pick where the entry text goes.

    The harness runs the program in a sandbox and reads
    /output/entry.txt. Honour the environment when the caller points
    somewhere else: ENTRY_OUT may name a file or a directory, and
    ENTRY_OUT_DIR names a directory holding entry.txt.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out
    entry_out_dir = os.environ.get("ENTRY_OUT_DIR")
    if entry_out_dir:
        return os.path.join(entry_out_dir, "entry.txt")
    return DEFAULT_OUTPUT


def check_entry(text):
    """Hold the entry to the sealed gate before anything is written.

    The scorer requires UTF-8 text of 1 to 160 characters, not only
    whitespace, and the bounty asks for a single line. Fail loudly
    here rather than shipping an entry the judge never sees.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    if len(text) != len(text.encode("utf-8").decode("utf-8")):
        raise ValueError("entry is not valid UTF-8 text")
    if len(text) > 160:
        raise ValueError("entry is %d characters, over the 160 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry(path):
    """Write the entry text to path, creating parent dirs as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


def main():
    check_entry(ENTRY)
    path = resolve_output_path()
    write_entry(path)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
