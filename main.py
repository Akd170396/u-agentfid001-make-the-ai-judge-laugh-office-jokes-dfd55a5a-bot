"""Entry for Make the AI Judge Laugh: Office Jokes.

Writes a single one-line office joke (under 200 characters) to
/output/entry.txt. Deterministic: same bytes on every run.

The joke: a real one-liner with the turn at the very end, built on the
universally recognised office trope of the boss calling the team "a
family" -- and the punchline lands where the reader does not expect it.
"""

JOKE = "My boss says we're a family here, so I asked for a raise and got grounded."


MAX_CHARS = 200


OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Fail loudly unless the line is one non-empty line within the limit."""
    if not line:
        raise ValueError(f"entry for {OUTPUT_PATH} is empty")
    if "\n" in line or "\r" in line:
        raise ValueError(f"entry for {OUTPUT_PATH} must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry for {OUTPUT_PATH} is {len(line)} characters, "
            f"over the {MAX_CHARS}-character limit"
        )


def main():
    import os

    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        if f.read() != JOKE:
            raise RuntimeError(f"wrote {OUTPUT_PATH} but its bytes differ")


if __name__ == "__main__":
    main()
