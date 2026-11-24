"""The Funniest Out-of-Office: write one funny out-of-office line.

The program writes a single line to /output/entry.txt. The line is the
whole entry: it must read like an out-of-office reply a real person
would actually set, and its joke has to land in that one line.
"""

import os

LINE = (
    "I'm out of office until Monday. In my absence, please direct all "
    "emails to my replacement: me, but on a beach, ignoring you."
)


def main() -> None:
    # The gate only accepts 1-140 characters of non-blank text on one line,
    # so refuse to write anything that would fail it instead of guessing.
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 140:
        raise ValueError(
            f"entry line must be one line of 1-140 characters, got {len(LINE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
