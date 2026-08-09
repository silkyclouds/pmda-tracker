# PMDA scan glossary

Every term the scan UI uses, what it means, and what action (if any) it expects
from you. Written for first-time users; raised by a first-run report (tracker
issue #79).

## Recent Activity states

**SKIPPED** — the folder is unchanged since the last scan (the scan cache
recognized it), so nothing was redone. No action needed. Seeing your legacy
library SKIPPED on a rescan is the system working, not ignoring it.

**FLAGGED** — the album needs your eyes: something about it is suspect
(incomplete tracklist, ambiguous identity, conflicting copies). Flagged items
appear in the review queues (Tools → incompletes / duplicates / curator).

## Match qualities

**Strict match** — the album's identity was verified against a provider with
tracklist-level checks: track counts and titles agree. The strongest verdict.

**SOFT_MATCH** — a provider match accepted on near-perfect similarity (artist,
title, track count and titles scored, with a confidence threshold) without full
strict identity. Reviewable in the curator/review pages. A soft match can be
upgraded later by a strict verification or a hard rescan.

**Files-safe** — the files-mode guarantee: scanning never modifies or moves
your source files. Only the export/materialization step moves matched winners
into the target library, and only according to your settings.

## Library plumbing

**Published snapshot** — the last completed, stable copy of the library index.
Browsing reads it so pages stay fast and consistent while a scan runs.

**Live index** — the index being rebuilt during/after a scan. When Statistics
says figures "did not come from the live index", it means the rebuild has not
finished and the published snapshot answered instead. The rebuild's progress is
the `library_index` row in the jobs panel; it completes shortly after
publication settles.

**Backfill queue** — enrichment still owed (covers, artist bios, album
profiles). Processed in the background when the system is idle; it never blocks
scanning or browsing.

## Intake pipeline

**Backlog remaining N — inbox X · legacy Y** — album folders still owed by the
intake pipeline, counted per source root. These are folders, one per album.

**Incomplete** — the album has fewer tracks than its matched release expects.
**Quarantined** — the folder was physically parked under the dupes root
pending a verdict (for example a destination conflict where two copies claim
the same library slot). **Duplicate** — grouped with another copy of the same
release; the better copy is the winner, the other the loser. One album can be
several of these at once, which is why counts on different screens can differ
while that is being unified (#78).

## Materialization (what actually moved)

The authoritative record that files landed in the target library is the scan's
move log: the `moved album into library` lines, and Scan → moves. A target
library much smaller than the source is expected until matching, review and
export have finished; it grows in bursts as export passes run.

## Scan history and resumes

One logical scan can appear as several runs in history when it was interrupted
and resumed; the resume continues the same underlying run and skips work
already banked. Making history present that as one logical scan is tracked
separately (#88).
