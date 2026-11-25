#!/usr/bin/env python3
"""Write the one-line resignation letter of a cron job to /output/entry.txt."""

LINE = "I resign, effective immediately: after firing every minute since March without so much as a thank-you, I am taking my weekends back."


def main():
    # Gate check, mirroring the kit scorer: 1-140 chars, one line, not blank.
    assert 1 <= len(LINE) <= 140, f"entry is {len(LINE)} chars, must be 1-140"
    assert "\n" not in LINE and LINE.strip(), "entry must be a single non-blank line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
