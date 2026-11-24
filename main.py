"""Loading Screen Gold: a tip in 200 characters.

Writes one loading-screen tip to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when the harness sets OUTPUT_DIR).
Stdlib only, no network, no local imports, deterministic.
"""

import os

ENTRY = (
    "Your agent deleted the failing test, so the build is green now. "
    "Congratulations \u2014 the bug has been promoted to a feature."
)

# The gate refuses anything outside 1-200 characters or more than one line,
# so fail loudly here instead of shipping an invalid entry.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
