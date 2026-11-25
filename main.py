"""The GPS Swears It Was a Shortcut — a make.fun entry.

Prints exactly one line of plain text of at most 200 characters, with
no setup and no dialogue tags: just the GPS's excuse itself.
"""

LINE = (
    "That was not a wrong turn; it was an unscheduled scenic audit of a "
    "neighbourhood you would never have appreciated at full speed."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
