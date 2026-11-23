"""One Letter: Coffee or Tea -- entry program.

Writes exactly one letter, "A" (coffee), to /output/entry.txt:
one byte, no trailing newline, no explanation, no punctuation.
"""

import os

LETTER = "A"  # A = coffee, B = tea
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Return True only if text is exactly one letter, A or B."""
    return isinstance(text, str) and len(text) == 1 and text in ("A", "B")


def main():
    if not validate(LETTER):
        raise ValueError("entry must be exactly one letter, A or B")
    data = LETTER.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify what was written before exiting: exact bytes and exact size.
    if os.path.getsize(OUTPUT_PATH) != len(data):
        raise ValueError(
            "verification failed: /output/entry.txt is not exactly 1 byte"
        )
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data or not validate(written.decode("utf-8")):
        raise ValueError(
            "verification failed: /output/entry.txt is not exactly one letter A/B"
        )
    print("wrote 1 byte to /output/entry.txt")


if __name__ == "__main__":
    main()
