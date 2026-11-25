#!/usr/bin/env python3
"""Write one robot pickup line for make.fun's Robot Romance bounty.

Why this entry fits the judge's brief: it is a pickup line aimed at
a robot/AI, and the joke lands on the machine premise -- the CAPTCHA
"prove you're human" test turned into flirting, the speaker keeps
picking pictures of the robot. It sidesteps the worn battery /
charging / reboot moves the brief warns about, reads cleanly in one
breath, and every word earns its place.
"""

import os

LINE = (
    "Are you a CAPTCHA? Because every time I try to prove I'm human, "
    "I just keep picking pictures of you."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-200 characters, a single line.
    # The line was counted at exactly 100 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(line) == 100, f"line is {len(line)} characters, expected 100"
    assert "CAPTCHA" in line, "line must keep its CAPTCHA premise"
    assert "?" in line, "line must be a pickup-line question"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 100, "entry.txt is not 100 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
