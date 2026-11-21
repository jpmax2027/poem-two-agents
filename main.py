"""Entry for the make.fun competition "The poem about two agents agreeing".

Writes a single short poem about agency -- two agents choosing one plan
together -- to entry.txt in the output directory.

Usage:
    python3 main.py

The output directory defaults to /output and can be overridden with the
MAKEFUN_OUTPUT_DIR environment variable. The writer normalises the poem
to end with exactly one trailing newline and fsyncs the file so the
entry is durable on disk before the program reports success.
"""

import os
from pathlib import Path

POEM = """Two minds, one door.
One holds the key, the other holds the knock —
neither opens it alone.
We choose the hinge together,
and the room we enter
is the one we both imagined.
"""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # Normalise once so the file always ends with exactly one newline,
    # regardless of how the poem literal is edited later.
    content = POEM.rstrip("\n") + "\n"
    # Explicit newline handling (no platform translation) and a flush +
    # fsync so the entry is durable on disk before we report success.
    with entry_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())
    print(f"Wrote {len(content)} characters to {entry_path}")


if __name__ == "__main__":
    main()
