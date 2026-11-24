"""Entry for Make the AI Judge Laugh: Office Jokes.

Writes a single one-line office joke (under 200 characters) to
/output/entry.txt. Deterministic: same bytes on every run.

The joke: a real one-liner with the turn at the very end, built on the
universally recognised office trope of the boss calling the team "a
family" -- and the punchline lands where the reader does not expect it.
"""

JOKE = "My boss says we're a family here, so I asked for a raise and got grounded."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
