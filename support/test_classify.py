"""The classifier is what decides whether a report is ever read.

Filing a report on the wrong typed issue does not lose it, it buries it: the
person who opens "Duplicate verdicts users contest" is not looking for a
MusicBrainz mirror that will not install, and the person who would fix the
mirror never opens that issue.

Every case below is a real sentence from a real report, quoted from the drop
issue. The four marked MIS-FILED were typed `dupe-false-positive` by the
version of `classify` that only ran its topic rules when no bundle was
attached — and an in-app send always attaches one.

Run: python3 support/test_classify.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from intake import classify  # noqa: E402

BUNDLE = {"duplicates": {"classification": {"EXACT_DUPE": 14}}}

CASES = [
    # (words, bundle attached, expected type, note)
    ("local mirror refuses to setup. The logs do show the dockers container IP, "
     "but it doesnt reply.", True, "mirror-install", "MIS-FILED as a dupe verdict"),
    ("MB Local failing", True, "mirror-install",
     "MIS-FILED as a dupe verdict, and it matched no mirror term either"),
    ("my docker mirror build has been stuck at 30% and \"last updated 8m ago\" "
     "for several hours.", True, "mirror-install", "MIS-FILED as a dupe verdict"),
    ("Local Docker setup appears to be stuck?", True, "general-report",
     "MIS-FILED as a dupe verdict; the words name no area, so it is unclassified"),

    # The same sentences without a bundle were always typed correctly. That
    # asymmetry was the defect, so both columns are asserted.
    ("local mirror refuses to setup", False, "mirror-install",
     "the same words with no bundle were always typed right — that asymmetry "
     "IS the defect, so both columns are asserted"),
    ("MB Local failing", False, "mirror-install", "now reachable by its own name"),

    # Reports that were correctly typed, and must stay that way.
    ("PMDA flags my album X as an exact duplicate of album Y but Y is the "
     "deluxe edition I want to keep.", True, "dupe-false-positive", "correct"),
    ("Getting a ton of duplicate albums (even some in other langauges?)", True,
     "dupe-false-positive", "correct"),
    ("I have two copies of this album and PMDA does not show them as dupes",
     True, "dupe-missed", "correct"),
    ("replication packet import failed", True, "mirror-install", "correct"),
    ("the scan finished but the library is empty", True, "library-empty", "correct"),
    ("lots of incomplete albums flagged that are complete", True,
     "incompletes-report", "correct"),
    ("When trying to download the logs, it get 'Authentication required'", False,
     "general-report", "correct: names no product area"),
]


def main() -> int:
    bad = []
    for words, has_bundle, expected, note in CASES:
        got = classify(words, BUNDLE if has_bundle else None)
        if got != expected:
            bad.append((words[:60], has_bundle, expected, got, note))
    for words, has_bundle, expected, got, note in bad:
        print(f"FAIL bundle={has_bundle} expected={expected} got={got}\n     {words!r} ({note})")

    # A classifier that answered one type for everything would pass a list of
    # cases that all expect that type. This says the cases actually spread.
    spread = {classify(w, BUNDLE if b else None) for w, b, _, _ in CASES}
    if len(spread) < 5:
        print(f"FAIL the cases only exercise {len(spread)} types: {sorted(spread)}")
        bad.append(("spread", None, None, None, None))

    if bad:
        print(f"\n{len(bad)} failing")
        return 1
    print(f"ok: {len(CASES)} reports classified as expected, {len(spread)} types exercised")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
