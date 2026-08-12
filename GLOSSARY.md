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

## Counters during a run

**Advanced vs committed** — an album is *advanced* the moment a worker finishes
a pass over it this run; it is *committed* once its result is written to the
database and published. The gap between the two is work in flight. Advanced
counts every pass — a resumed run re-advances albums it re-checks — so
"advanced" can legitimately exceed the run's plan; committed never does. The
scan page shows both and names the gap (raised in #79 follow-up).

**Verdicts (fine-check)** — decisions already recorded on duplicate groups, by
you or by the shadow re-certification pass. "632 groups awaiting review · 14
verdicts" reads: 632 groups still need a decision, 14 decisions are already on
file. A verdict never moves files by itself.

## The worker grid

Each row is a worker, each column a provider PMDA consults, in the order it
consults them. The mark says what that provider answered for the album that
worker is on:

**Filled circle** — it answered with something usable. A cache hit counts as a
hit: PMDA had already asked, and re-asking would only cost the provider.

**Hollow circle** — it was asked and had nothing for this album. That is an
answer, not a failure, and not an outage.

**Pulsing circle** — being asked right now.

**Small square** — not consulted for this album. Usually because the file's own
tags already answered, or because an earlier provider settled the identity and
asking further would change nothing. A blank column is normal on a well-tagged
library.

**One busy worker out of eight** is not a bug by itself: workers idle between
albums, and the last one still holding a job shows as busy while the rest have
finished theirs.

## Duplicate categories

Every duplicate group carries a class. Only the first one is ever acted on
without you.

**duplicate_exact** — the same record, twice. Same tracks, same signature. This
is the only class PMDA will move on its own.

**edition_variant** — the same record in a different edition (a remix EP beside
the album, a single beside its parent). Related, not interchangeable. Always
left to a human.

**expanded_edition** — one side has more: more tracks, a higher resolution, a
better master. Usually an upgrade to consider rather than a copy to remove.

**partial_incomplete** — one copy's tracks all exist in the other. Careful here:
a compilation whose tracks appear on an album is a subset, not a copy of it, and
different cover art or a different label is a strong hint that the two are
genuinely different releases.

**export_conflict** — not a duplicate at all. PMDA wanted to file an album into
the library and something already occupied that destination, so it parked the
album instead of overwriting anything. It is waiting for a decision about where
it should live, not about which copy to delete.

**likely_false_positive** — PMDA's own verdict that the pairing is probably
wrong. Shown rather than hidden, so you can see what it nearly did.

**Dedupe now** — on a past scan in Scan history: replays that run's duplicate
decisions, moving that run's losers into the dupes root. It acts on the run you
are looking at, not on your whole library, and it moves folders — it deletes
nothing.

## Enrichment phases

The background backfill runs three stages, always in this order, and the header
names the one it is on:

1. **Visual assets** — album covers and artist portraits.
2. **Artist profiles** — bios, tags, similar artists.
3. **Album profiles** — reviews, tags, similar albums.

In cover-only mode there is one stage, and it says one.

## Enrichment

**Album cover** — the artwork file. Fetched from providers when the folder has
none. The "Covers" card counts albums that have one.

**Album profile** — ONE dossier per album: the written review (its visible
face on the album page), plus tags and similar-albums data. The "Album
reviews" card counts albums whose profile carries a review — so "album
reviews" and "album profiles" are the same pipeline seen from two ends
(raised in #151).

**Artist profile** — ONE dossier per artist: portrait, bio, similar artists.
It feeds BOTH the "Artist images" and "Artist bios" cards, which is why the
queue shows three lines under four coverage cards: one artist dossier serves
two cards.

**Backfill queue** — enrichment still owed, processed in the background when
the system is idle. It never blocks scanning or browsing, and there is
nothing to click: it drains by itself.
