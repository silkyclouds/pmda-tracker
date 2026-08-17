# PMDA — issue tracker

Public bug tracker and feature backlog for **PMDA**, a self-hosted tool for auditing and maintaining messy music libraries.

This repository holds **no source code** — only issues. The code lives in a private repository; access is granted individually. Everything else about the project happens here in the open: what is broken, what is planned, and where each report stands.

<!-- dashboard:start -->
## Where things stand

A report is **resolved** only when the person who filed it confirms the fix — shipped
code waits in orange until its reporter says so. These charts count reports only;
improvements we opened ourselves are tallied separately so they cannot flatter the number.

<img src="charts/progress.svg" width="100%" alt="Progress"/>

<img src="charts/status.svg" width="100%" alt="All reports by status"/>

<img src="charts/severity.svg" width="100%" alt="Open bugs by severity"/>

<img src="charts/areas.svg" width="100%" alt="Open work by area"/>

**Shortcuts** — [ready to test](https://github.com/silkyclouds/pmda-tracker/issues?q=is%3Aissue+is%3Aopen+label%3Aneeds-testing) · [not started](https://github.com/silkyclouds/pmda-tracker/issues?q=is%3Aissue+is%3Aopen+-label%3Aneeds-testing+-label%3Aneeds-info) · [confirmed fixed](https://github.com/silkyclouds/pmda-tracker/issues?q=is%3Aissue+is%3Aclosed)

<!-- dashboard:end -->

<!-- issue-table:start -->
## Every report, one table per area

_163 fixed · 21 open — regenerated automatically. FIXED names the version that shipped it; IN BETA means the fix is on `:beta` awaiting its reporter; BACKLOG is not started._

<details open>
<summary><b>UI / UX</b> — 34 report(s), 4 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#180](https://github.com/silkyclouds/pmda-tracker/issues/180) | Incompletes page reports zero flagged albums: one binary cell makes the whole response unseri… | ovizii | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v429 | Awaiting reporter confirmation |
| [#162](https://github.com/silkyclouds/pmda-tracker/issues/162) | The Users page belongs under Settings | meaning_1 | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v420 | Awaiting reporter confirmation |
| [#160](https://github.com/silkyclouds/pmda-tracker/issues/160) | Your circle and Users and shares overlap: keep one listening-activity page | meaning_1 | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v420 | Awaiting reporter confirmation |
| [#86](https://github.com/silkyclouds/pmda-tracker/issues/86) | Onboarding should scan first, then let the user choose the scope | arty_ai | <img src="charts/badges/badge-backlog.svg" alt="BACKLOG" height="18"/> | — | — |
| [#165](https://github.com/silkyclouds/pmda-tracker/issues/165) | Library header counts disagree with Statistics, and the size on disk looks wrong | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v416 | Shipped & closed — reopen welcome |
| [#164](https://github.com/silkyclouds/pmda-tracker/issues/164) | The startup splash quote is not italic like every other standfirst | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v412 | Shipped & closed — reopen welcome |
| [#161](https://github.com/silkyclouds/pmda-tracker/issues/161) | Tools page is mostly redundant with pages that already exist | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v412 | Shipped & closed — reopen welcome |
| [#158](https://github.com/silkyclouds/pmda-tracker/issues/158) | Requests page: albums already in the library are not clickable | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v412 | Shipped & closed — reopen welcome |
| [#157](https://github.com/silkyclouds/pmda-tracker/issues/157) | Identify step headline hijacked by per-artist index refreshes (0 of 0 folders, then 1 of 2) | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v401 | Shipped & closed — reopen welcome |
| [#156](https://github.com/silkyclouds/pmda-tracker/issues/156) | Light theme: hovered rows in quick-search suggestions turn white and become invisible | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v400 | Shipped & closed — reopen welcome |
| [#154](https://github.com/silkyclouds/pmda-tracker/issues/154) | Every duplicates number must name its scope (sidebar 0 vs fine-check 632 vs top bar 631) | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#150](https://github.com/silkyclouds/pmda-tracker/issues/150) | Edition review modal: a single glued to its parent album offers only KEEP/DELETE — no way to … | Hodel1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v399 | Shipped & closed — reopen welcome |
| [#149](https://github.com/silkyclouds/pmda-tracker/issues/149) | Workers panel: provider states and icon grid need a legend, and busy/idle accounting disagree… | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v391 | Shipped & closed — reopen welcome |
| [#148](https://github.com/silkyclouds/pmda-tracker/issues/148) | Broken-album review showed a 'Run AI shadow' button with no explanation (removed) | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#146](https://github.com/silkyclouds/pmda-tracker/issues/146) | Scan card step count grows mid-run: 'Step 4 of 4' becomes 'of 5' when enrichment starts | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v389 | Shipped & closed — reopen welcome |
| [#92](https://github.com/silkyclouds/pmda-tracker/issues/92) | Library export label is truncated, and its relationship to the Export stage is unclear | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v392 | Shipped & closed — reopen welcome |
| [#89](https://github.com/silkyclouds/pmda-tracker/issues/89) | Nothing says which features stay inert until the first scan finalizes | edith1775 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#88](https://github.com/silkyclouds/pmda-tracker/issues/88) | Scan History: a resumed scan looks like a string of short failed runs | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v391 | Shipped & closed — reopen welcome |
| [#84](https://github.com/silkyclouds/pmda-tracker/issues/84) | Heart and Like do the same thing: pick one, or make the rating model explicit | bitsofbitsofbits | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | 1.0.5 | Shipped & closed — reopen welcome |
| [#79](https://github.com/silkyclouds/pmda-tracker/issues/79) | Scan vocabulary is undocumented: SKIPPED, FLAGGED, SOFT_MATCH, Files-safe, live index, backlog | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#77](https://github.com/silkyclouds/pmda-tracker/issues/77) | Artwork cache: missing .webp raises a traceback mid-scan | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v399 | Shipped & closed — reopen welcome |
| [#48](https://github.com/silkyclouds/pmda-tracker/issues/48) | Search results: play a track directly from the results page | cissoubaka | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v398 | Shipped & closed — reopen welcome |
| [#45](https://github.com/silkyclouds/pmda-tracker/issues/45) | Statistics: library size on disk and total playtime (years/months/days/hours) | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v398 | Shipped & closed — reopen welcome |
| [#41](https://github.com/silkyclouds/pmda-tracker/issues/41) | No version number anywhere in the product — testers cannot tell which build they are on | cissoubaka, foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v345 | Shipped & closed — reopen welcome |
| [#39](https://github.com/silkyclouds/pmda-tracker/issues/39) | Concerts: process newly added artists/genres against providers immediately | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#37](https://github.com/silkyclouds/pmda-tracker/issues/37) | Liked page caps at 96 songs while all likes are stored | foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#29](https://github.com/silkyclouds/pmda-tracker/issues/29) | After an update the library reads 0 artists / 0 albums with no explanation | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#22](https://github.com/silkyclouds/pmda-tracker/issues/22) | PMDA advertises "no AI" but shows AI prompts and an AI health row | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v391 | Shipped & closed — reopen welcome |
| [#17](https://github.com/silkyclouds/pmda-tracker/issues/17) | Backend logs are unreadable in light mode | lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#16](https://github.com/silkyclouds/pmda-tracker/issues/16) | Not enough padding between the Library heading and THE COLLECTION line | lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#14](https://github.com/silkyclouds/pmda-tracker/issues/14) | A popup flashes on screen for a split second when PMDA loads | lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#13](https://github.com/silkyclouds/pmda-tracker/issues/13) | Player bar covers the bottom of Search results and Tools | lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#11](https://github.com/silkyclouds/pmda-tracker/issues/11) | Right half of the tile size slider on the Artists page does nothing | lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v345 | Shipped & closed — reopen welcome |
| [#9](https://github.com/silkyclouds/pmda-tracker/issues/9) | Opening History before any scan has run shows a 404 page | lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v345 | Shipped & closed — reopen welcome |

</details>

<details>
<summary><b>Scanner & pipeline</b> — 43 report(s), 0 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#181](https://github.com/silkyclouds/pmda-tracker/issues/181) | A scan's tuple can be written into broken_albums with its columns shifted | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#175](https://github.com/silkyclouds/pmda-tracker/issues/175) | Library index rebuild restarts from zero on every interruption, and re-reads folders that nev… | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#145](https://github.com/silkyclouds/pmda-tracker/issues/145) | Finalize export pace is bounded by per-album bookkeeping, not I/O | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v401 | Shipped & closed — reopen welcome |
| [#137](https://github.com/silkyclouds/pmda-tracker/issues/137) | A scan in its preparation phases reports zero progress on every surface, and reads as hung | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v387 | Shipped & closed — reopen welcome |
| [#136](https://github.com/silkyclouds/pmda-tracker/issues/136) | Startup resume has been silently dead: reconciliation clears the exact status the picker requ… | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v387 | Shipped & closed — reopen welcome |
| [#105](https://github.com/silkyclouds/pmda-tracker/issues/105) | A full scan silently resumes a partial plan and reports it as the total | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v333 | Shipped & closed — reopen welcome |
| [#98](https://github.com/silkyclouds/pmda-tracker/issues/98) | SQLite 'database is locked' raises a traceback mid-scan instead of retrying | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#97](https://github.com/silkyclouds/pmda-tracker/issues/97) | Full scan segfaults on a large library, four seconds into filesystem discovery | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v350 | Shipped & closed — reopen welcome |
| [#96](https://github.com/silkyclouds/pmda-tracker/issues/96) | Stale pipeline job is flagged but never cleared: library_index stuck for 8.8 hours | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v339 | Shipped & closed — reopen welcome |
| [#95](https://github.com/silkyclouds/pmda-tracker/issues/95) | Scan emits no heartbeat during filesystem discovery, so a healthy scan looks stalled | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v335 | Shipped & closed — reopen welcome |
| [#82](https://github.com/silkyclouds/pmda-tracker/issues/82) | [scanner] One pacer for MusicBrainz, not two | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#81](https://github.com/silkyclouds/pmda-tracker/issues/81) | [scanner] Only look up a table of contents when the folder came off a disc | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#78](https://github.com/silkyclouds/pmda-tracker/issues/78) | Incomplete albums: the scan count and the review queue disagree | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v391 | Shipped & closed — reopen welcome |
| [#76](https://github.com/silkyclouds/pmda-tracker/issues/76) | [scanner] Wire every improvement into the live pipeline | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#75](https://github.com/silkyclouds/pmda-tracker/issues/75) | [scanner] Install the MusicBrainz call discipline on every call site | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#73](https://github.com/silkyclouds/pmda-tracker/issues/73) | [scanner] Key classical identity on the performance, not the work | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#72](https://github.com/silkyclouds/pmda-tracker/issues/72) | [scanner] Batch the Postgres writes instead of one round trip per row | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#71](https://github.com/silkyclouds/pmda-tracker/issues/71) | [scanner] Narrow the provider query rather than widening the results | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#69](https://github.com/silkyclouds/pmda-tracker/issues/69) | [scanner] Wire AcoustID escalation into the scan pipeline | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#68](https://github.com/silkyclouds/pmda-tracker/issues/68) | [scanner] Optimal track alignment instead of greedy pairing | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#67](https://github.com/silkyclouds/pmda-tracker/issues/67) | [scanner] Various Artists inferred at a dominance threshold | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#66](https://github.com/silkyclouds/pmda-tracker/issues/66) | [scanner] Album identity derived from content, not from the path | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#65](https://github.com/silkyclouds/pmda-tracker/issues/65) | [scanner] Per-folder manifest hash for incremental scans | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#64](https://github.com/silkyclouds/pmda-tracker/issues/64) | [scanner] Tag-based grouping cross-checked against folder grouping | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#63](https://github.com/silkyclouds/pmda-tracker/issues/63) | [scanner] Album-aware keeper cascade for duplicates | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#62](https://github.com/silkyclouds/pmda-tracker/issues/62) | [scanner] Call discipline for the public MusicBrainz web service | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#61](https://github.com/silkyclouds/pmda-tracker/issues/61) | [scanner] Fuzzy MusicBrainz TOC lookup identifies the exact release | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#60](https://github.com/silkyclouds/pmda-tracker/issues/60) | [scanner] AcoustID escalation with album-level consensus | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#59](https://github.com/silkyclouds/pmda-tracker/issues/59) | [scanner] Rip evidence from cue sheets and EAC/XLD logs | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#58](https://github.com/silkyclouds/pmda-tracker/issues/58) | [scanner] Three provider outcomes, circuit breaker and token bucket | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#57](https://github.com/silkyclouds/pmda-tracker/issues/57) | [scanner] Match distance with per-penalty veto and runner-up margin | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#56](https://github.com/silkyclouds/pmda-tracker/issues/56) | [scanner] Audio identity: stream hash and duration vector | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#55](https://github.com/silkyclouds/pmda-tracker/issues/55) | [scanner] Classical completeness judged by work structure, not file count | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#54](https://github.com/silkyclouds/pmda-tracker/issues/54) | [scanner] Detect albums truncated at the tail | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#52](https://github.com/silkyclouds/pmda-tracker/issues/52) | [scanner] Scan worker width raised to match provider-first | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#51](https://github.com/silkyclouds/pmda-tracker/issues/51) | [scanner] MusicBrainz quarantine per release group | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#50](https://github.com/silkyclouds/pmda-tracker/issues/50) | [scanner] Watchdog for zombie scan jobs | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#49](https://github.com/silkyclouds/pmda-tracker/issues/49) | [scanner] Post-scan export no longer re-runs discovery | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#47](https://github.com/silkyclouds/pmda-tracker/issues/47) | Scan roots: three competing sources of truth, and Settings changes can be silently ignored | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v391 | Shipped & closed — reopen welcome |
| [#32](https://github.com/silkyclouds/pmda-tracker/issues/32) | Identify with providers first, MusicBrainz asynchronously after | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v301 | Shipped & closed — reopen welcome |
| [#7](https://github.com/silkyclouds/pmda-tracker/issues/7) | Scanning is extremely slow — over a week for 100k tracks | lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#6](https://github.com/silkyclouds/pmda-tracker/issues/6) | FutureTimeout - Export failed | Hodel1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#1](https://github.com/silkyclouds/pmda-tracker/issues/1) | Stuck with error on first album | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |

</details>

<details open>
<summary><b>Duplicates</b> — 5 report(s), 1 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#174](https://github.com/silkyclouds/pmda-tracker/issues/174) | The duplicates page served 13 groups while the store held 6,805 | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | — | Awaiting reporter confirmation |
| [#104](https://github.com/silkyclouds/pmda-tracker/issues/104) | Duplicate keeper drops the copy that has cover art | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#103](https://github.com/silkyclouds/pmda-tracker/issues/103) | Export arbitration quarantines a split album's tail as a duplicate loser | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#15](https://github.com/silkyclouds/pmda-tracker/issues/15) | Duplicate detection calls different editions an exact duplicate | lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#12](https://github.com/silkyclouds/pmda-tracker/issues/12) | Sidebar reports duplicates found, but the Duplicates page is empty | edith1775, lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v418 | Shipped & closed — reopen welcome |

</details>

<details open>
<summary><b>Metadata & matching</b> — 16 report(s), 3 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#183](https://github.com/silkyclouds/pmda-tracker/issues/183) | Match vocabulary: edition / matched / tags-only, instead of hardmatched and softmatched | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v449 | Awaiting reporter confirmation |
| [#166](https://github.com/silkyclouds/pmda-tracker/issues/166) | The background match re-verification is invisible on the Enrichment page | meaning_1 | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v412 | Awaiting reporter confirmation |
| [#159](https://github.com/silkyclouds/pmda-tracker/issues/159) | Likes should drive the concert calendar automatically | meaning_1 | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v420 | Awaiting reporter confirmation |
| [#173](https://github.com/silkyclouds/pmda-tracker/issues/173) | A one-track folder could earn a permanent strict match on a similar title alone | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v415 | Shipped & closed — reopen welcome |
| [#172](https://github.com/silkyclouds/pmda-tracker/issues/172) | Track sizes and durations are overwritten with zero by a partial re-upsert, so size on disk a… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v414 | Shipped & closed — reopen welcome |
| [#144](https://github.com/silkyclouds/pmda-tracker/issues/144) | A persistent needs_ai_review quality flag on profiles, set at ingestion and queryable via MCP | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#143](https://github.com/silkyclouds/pmda-tracker/issues/143) | Artist bios assigned to the wrong entity when scraping resolves a homonym | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#142](https://github.com/silkyclouds/pmda-tracker/issues/142) | About 12,500 curator profile rows are empty placeholders that mask albums from missing-descri… | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#141](https://github.com/silkyclouds/pmda-tracker/issues/141) | Curator ingestion stores full tracklists, sometimes with lyrics, as the album description | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#138](https://github.com/silkyclouds/pmda-tracker/issues/138) | MusicBrainz provider shows error: release-group lookups 404 on the mirror for ids the public … | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#101](https://github.com/silkyclouds/pmda-tracker/issues/101) | No way to match an album by hand when automatic matching fails | bitsofbitsofbits | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v404 | Shipped & closed — reopen welcome |
| [#99](https://github.com/silkyclouds/pmda-tracker/issues/99) | Track titles that start with a number lose it: "100 Bad Days" becomes "Bad Days" | bitsofbitsofbits | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#90](https://github.com/silkyclouds/pmda-tracker/issues/90) | Albums silently un-match when MusicBrainz deletes the release they matched | iecj | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v404 | Shipped & closed — reopen welcome |
| [#34](https://github.com/silkyclouds/pmda-tracker/issues/34) | Unmatchable folder names (abbreviated compilations): automatic AcoustID / OCR escalation | cissoubaka | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v407 | Shipped & closed — reopen welcome |
| [#26](https://github.com/silkyclouds/pmda-tracker/issues/26) | Matching fails on a large share of the library | bitsofbitsofbits | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v302 | Shipped & closed — reopen welcome |
| [#10](https://github.com/silkyclouds/pmda-tracker/issues/10) | Artist names containing '&' are split, and the albums land on the wrong artist | lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |

</details>

<details>
<summary><b>Mobile apps</b> — 5 report(s), 0 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#94](https://github.com/silkyclouds/pmda-tracker/issues/94) | No documented route into the Android beta | foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#44](https://github.com/silkyclouds/pmda-tracker/issues/44) | Android app: Liked music list has no play or shuffle button | foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | 1.0.4 | Shipped & closed — reopen welcome |
| [#43](https://github.com/silkyclouds/pmda-tracker/issues/43) | Android app: no Download button on playlists | foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | 1.0.4 | Shipped & closed — reopen welcome |
| [#36](https://github.com/silkyclouds/pmda-tracker/issues/36) | Android app: proper offline support (cached lists, offline filtering) | foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | 1.0.5 | Shipped & closed — reopen welcome |
| [#35](https://github.com/silkyclouds/pmda-tracker/issues/35) | Mobile apps cannot log in when MFA is enabled | iecj | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | 1.0.4 | Shipped & closed — reopen welcome |

</details>

<details>
<summary><b>Player & playback</b> — 1 report(s), 0 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#83](https://github.com/silkyclouds/pmda-tracker/issues/83) | Web player stays at 0:00 on some albums while the mobile app plays them | bitsofbitsofbits | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v401 | Shipped & closed — reopen welcome |

</details>

<details>
<summary><b>Providers & integrations</b> — 4 report(s), 0 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#140](https://github.com/silkyclouds/pmda-tracker/issues/140) | Last.fm bios keep the Creative Commons boilerplate and arrive unformatted | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#139](https://github.com/silkyclouds/pmda-tracker/issues/139) | Discogs pressing notes are stored as the album review | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#19](https://github.com/silkyclouds/pmda-tracker/issues/19) | Incompletes page says acquisition is disabled although Lidarr is configured and on | foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#18](https://github.com/silkyclouds/pmda-tracker/issues/18) | Spotify setup shows a redirect URI that PMDA never actually sends | bitsofbitsofbits, foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |

</details>

<details>
<summary><b>Settings & onboarding</b> — 12 report(s), 0 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#163](https://github.com/silkyclouds/pmda-tracker/issues/163) | Removing a shared library needs a confirmation and must disappear immediately | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v412 | Shipped & closed — reopen welcome |
| [#102](https://github.com/silkyclouds/pmda-tracker/issues/102) | Setting up the AI integrations is enough friction that testers give up | bitsofbitsofbits | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#100](https://github.com/silkyclouds/pmda-tracker/issues/100) | Reset PMDA returns a 400 and does nothing | bitsofbitsofbits | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#91](https://github.com/silkyclouds/pmda-tracker/issues/91) | Database-only mode, with an opt-in write-through to files | iecj | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v408 | Shipped & closed — reopen welcome |
| [#85](https://github.com/silkyclouds/pmda-tracker/issues/85) | No dry-run mode: nothing lets a user see what PMDA would do before it does it | arty_ai | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#80](https://github.com/silkyclouds/pmda-tracker/issues/80) | Web searches during scan are not disclosed or configurable | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v391 | Shipped & closed — reopen welcome |
| [#74](https://github.com/silkyclouds/pmda-tracker/issues/74) | [scanner] Report which item the scan is on, not just how far along | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#53](https://github.com/silkyclouds/pmda-tracker/issues/53) | [scanner] Self-hosted error telemetry, strictly opt-in | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#46](https://github.com/silkyclouds/pmda-tracker/issues/46) | MCP: like artists, genres and labels through the PMDA MCP server | meaning_1 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v398 | Shipped & closed — reopen welcome |
| [#25](https://github.com/silkyclouds/pmda-tracker/issues/25) | Worker count and batch size display 0 while a manual override is still active | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#20](https://github.com/silkyclouds/pmda-tracker/issues/20) | Spotify Client ID has to be set as a Docker variable, but the docs point at the UI | bitsofbitsofbits, foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#8](https://github.com/silkyclouds/pmda-tracker/issues/8) | Onboarding asks only for the Last.fm API key, settings also asks for the secret | lewis91 | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |

</details>

<details open>
<summary><b>Deployment & docs</b> — 16 report(s), 2 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#179](https://github.com/silkyclouds/pmda-tracker/issues/179) | One-click MusicBrainz mirror: proven end to end, after two bugs that made it impossible | bitsofbitsofbits, iecj, mushm0uth | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v431 | Awaiting reporter confirmation |
| [#33](https://github.com/silkyclouds/pmda-tracker/issues/33) | Legacy cleanup campaign: dead modes, dead vars, dead log lines, monolith factoring, security … | — | <img src="charts/badges/badge-backlog.svg" alt="BACKLOG" height="18"/> | — | — |
| [#93](https://github.com/silkyclouds/pmda-tracker/issues/93) | Document whether PMDA and Jellyfin can share one music library | bitsofbitsofbits | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#87](https://github.com/silkyclouds/pmda-tracker/issues/87) | Cache layers are undocumented: which paths want NVMe, and how much each will consume | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#70](https://github.com/silkyclouds/pmda-tracker/issues/70) | [scanner] Test container disk leak filled the Docker pool | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#42](https://github.com/silkyclouds/pmda-tracker/issues/42) | Beta instructions point testers at :latest, but the fixes ship on :beta | foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#40](https://github.com/silkyclouds/pmda-tracker/issues/40) | Unraid reuses the cached image when switching to :beta — testers test the old build believing… | foggymtndrifter | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#38](https://github.com/silkyclouds/pmda-tracker/issues/38) | OOM crashes during first big scan (4G container limit) | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#28](https://github.com/silkyclouds/pmda-tracker/issues/28) | Lost web UI access after updating | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#27](https://github.com/silkyclouds/pmda-tracker/issues/27) | Ollama is not detected when it runs in the same Docker stack | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#24](https://github.com/silkyclouds/pmda-tracker/issues/24) | Container CPU limit ignored — PMDA sizes itself from the host's CPU count | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#23](https://github.com/silkyclouds/pmda-tracker/issues/23) | Repeated PostgreSQL error: relation "files_albums" does not exist | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#21](https://github.com/silkyclouds/pmda-tracker/issues/21) | Bootstrap is refused over Tailscale — 100.x addresses are treated as public | ovizii | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#5](https://github.com/silkyclouds/pmda-tracker/issues/5) | UnRAID 7.1.2 inability to create PMDA docker container from default settings related to confi… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#4](https://github.com/silkyclouds/pmda-tracker/issues/4) | KeyError 'Missing required configuration key' | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#2](https://github.com/silkyclouds/pmda-tracker/issues/2) | 'pull access denied for silkyclouds/pmda' through compose | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |

</details>

<details>
<summary><b>Sharing & social</b> — 1 report(s), 0 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#31](https://github.com/silkyclouds/pmda-tracker/issues/31) | Device-link check crashes: 'sqlite3.Row' object has no attribute 'get' | cissoubaka | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |

</details>

<details open>
<summary><b>Other</b> — 45 report(s), 10 open</summary>

| # | Issue | Reporter | Status | Fix | Validation |
|---|-------|----------|--------|-----|------------|
| [#182](https://github.com/silkyclouds/pmda-tracker/issues/182) | Setup => Metadata Sources => Serper gets re-activated with every container restart | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v474 | Awaiting reporter confirmation |
| [#178](https://github.com/silkyclouds/pmda-tracker/issues/178) | Question about the wording on the enrichment page | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v474 | Awaiting reporter confirmation |
| [#177](https://github.com/silkyclouds/pmda-tracker/issues/177) | PMDA moves winners into library root, then flags them as foreign entries | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v474 | Awaiting reporter confirmation |
| [#176](https://github.com/silkyclouds/pmda-tracker/issues/176) | Issue with a duplicate report reporting two different albums as duplicates | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v474 | Awaiting reporter confirmation |
| [#171](https://github.com/silkyclouds/pmda-tracker/issues/171) | Composition: add a sample-rate filter alongside the bitrate buckets | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v419 | Awaiting reporter confirmation |
| [#170](https://github.com/silkyclouds/pmda-tracker/issues/170) | Incompletes review: say what each button does, and show the album facts in the Detail modal | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v419 | Awaiting reporter confirmation |
| [#169](https://github.com/silkyclouds/pmda-tracker/issues/169) | Artist/album mismatch reviews offer no way to resolve them | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v420 | Awaiting reporter confirmation |
| [#168](https://github.com/silkyclouds/pmda-tracker/issues/168) | "Why flagged" shows one reason while the row shows another | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v421 | Awaiting reporter confirmation |
| [#167](https://github.com/silkyclouds/pmda-tracker/issues/167) | A review row links to an album page that answers "no longer in your library" | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | — | Awaiting reporter confirmation |
| [#134](https://github.com/silkyclouds/pmda-tracker/issues/134) | Resume granularity is per-artist, so a 9,382-album Various Artists bucket restarts from zero … | — | <img src="charts/badges/badge-beta.svg" alt="IN BETA" height="18"/> | v474 | Awaiting reporter confirmation |
| [#185](https://github.com/silkyclouds/pmda-tracker/issues/185) | Pages are computed in the background and served instantly from cache | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v473 | Shipped & closed — reopen welcome |
| [#155](https://github.com/silkyclouds/pmda-tracker/issues/155) | enhance the "composition" analysis | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v412 | Shipped & closed — reopen welcome |
| [#153](https://github.com/silkyclouds/pmda-tracker/issues/153) | Manually starting background enrichment process from tools menu leads to API Error: 409 CONFLICT | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#152](https://github.com/silkyclouds/pmda-tracker/issues/152) | How to handle "incompletes" without a pmda handbook? | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v410 | Shipped & closed — reopen welcome |
| [#151](https://github.com/silkyclouds/pmda-tracker/issues/151) | Enrichment vocabulary is undocumented | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#135](https://github.com/silkyclouds/pmda-tracker/issues/135) | MusicBrainz local still reports timeouts while the mirror answers the same query in 30 ms | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v387 | Shipped & closed — reopen welcome |
| [#133](https://github.com/silkyclouds/pmda-tracker/issues/133) | Segfault located: a werkzeug request thread dies in the auth guard, and runtime binding has n… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v367 | Shipped & closed — reopen welcome |
| [#132](https://github.com/silkyclouds/pmda-tracker/issues/132) | A resumed scan restores its plan, reports the plan size as albums scanned, and identifies zer… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v366 | Shipped & closed — reopen welcome |
| [#131](https://github.com/silkyclouds/pmda-tracker/issues/131) | Export moved the entire intake root (3.8 TB) into Music_matched as a single album on tag-trus… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v362 | Shipped & closed — reopen welcome |
| [#130](https://github.com/silkyclouds/pmda-tracker/issues/130) | Three runs claim status running at once, and resume ranks candidates by plan size instead of … | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v362 | Shipped & closed — reopen welcome |
| [#129](https://github.com/silkyclouds/pmda-tracker/issues/129) | Consider a review-gated tool to contribute releases PMDA finds elsewhere back to MusicBrainz | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#128](https://github.com/silkyclouds/pmda-tracker/issues/128) | The loose MusicBrainz search sends fielded syntax to dismax, which cannot parse it: 3 of 40 a… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v387 | Shipped & closed — reopen welcome |
| [#127](https://github.com/silkyclouds/pmda-tracker/issues/127) | Run duplicate detection after the MBID backfill, not during the scan | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v391 | Shipped & closed — reopen welcome |
| [#126](https://github.com/silkyclouds/pmda-tracker/issues/126) | Workers panel: show which providers answered for each in-flight album, as a grid | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v391 | Shipped & closed — reopen welcome |
| [#125](https://github.com/silkyclouds/pmda-tracker/issues/125) | The MusicBrainz row measures different things from the other providers under the same column … | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#124](https://github.com/silkyclouds/pmda-tracker/issues/124) | 98% of the MusicBrainz lookup cache is negative, written while MB was deferred or throttled, … | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#123](https://github.com/silkyclouds/pmda-tracker/issues/123) | Stopping during the walk loses all folder-probing progress, and the API still reports resume_… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v355 | Shipped & closed — reopen welcome |
| [#122](https://github.com/silkyclouds/pmda-tracker/issues/122) | Local MusicBrainz mirror is still paced at the public API's 1 req/s: 25 timeouts against 20 m… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v387 | Shipped & closed — reopen welcome |
| [#121](https://github.com/silkyclouds/pmda-tracker/issues/121) | No hard rescan: a bad match can be cached in a way nothing in the UI can clear | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v389 | Shipped & closed — reopen welcome |
| [#120](https://github.com/silkyclouds/pmda-tracker/issues/120) | Public share pages use a reduced player with no PMDA branding | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v400 | Shipped & closed — reopen welcome |
| [#119](https://github.com/silkyclouds/pmda-tracker/issues/119) | Request-available notifications are not clickable and do not open the album | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |
| [#118](https://github.com/silkyclouds/pmda-tracker/issues/118) | Check the MusicBrainz mirror's replication lag before a scan starts matching | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v353 | Shipped & closed — reopen welcome |
| [#117](https://github.com/silkyclouds/pmda-tracker/issues/117) | Stop snapshot can overwrite every artist name in the resume plan with "Unknown", collapsing t… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v352 | Shipped & closed — reopen welcome |
| [#116](https://github.com/silkyclouds/pmda-tracker/issues/116) | Stopping a scan waits for the current artist to finish — three days on a 9,819-album compilat… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v367 | Shipped & closed — reopen welcome |
| [#115](https://github.com/silkyclouds/pmda-tracker/issues/115) | Profile backfill dies on a 64 MB /dev/shm and reports it as "No space left on device" | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v387 | Shipped & closed — reopen welcome |
| [#114](https://github.com/silkyclouds/pmda-tracker/issues/114) | Album progress commits only when an artist completes, so an interrupted scan loses the entire… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v352 | Shipped & closed — reopen welcome |
| [#113](https://github.com/silkyclouds/pmda-tracker/issues/113) | Scan parallelism is keyed on artist, so a compilation-heavy intake runs 76% of the plan on a … | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v352 | Shipped & closed — reopen welcome |
| [#112](https://github.com/silkyclouds/pmda-tracker/issues/112) | Scan progress overstates itself when one artist dominates the plan: 12,792 of 12,950 shown ag… | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v352 | Shipped & closed — reopen welcome |
| [#111](https://github.com/silkyclouds/pmda-tracker/issues/111) | Three duplicate counts on screen at once, none of them labelled | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v391 | Shipped & closed — reopen welcome |
| [#110](https://github.com/silkyclouds/pmda-tracker/issues/110) | Duplicate engine evicts a library album on a generic title alone, bypassing the relationship … | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v367 | Shipped & closed — reopen welcome |
| [#109](https://github.com/silkyclouds/pmda-tracker/issues/109) | Artist MusicBrainz IDs are almost never stored (666 of 115,793) | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v388 | Shipped & closed — reopen welcome |
| [#108](https://github.com/silkyclouds/pmda-tracker/issues/108) | TheAudioDB is queried by name when the MusicBrainz ID is already known | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | — | Shipped & closed — reopen welcome |
| [#107](https://github.com/silkyclouds/pmda-tracker/issues/107) | Worker activity is never published, so a stuck worker is invisible | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v335 | Shipped & closed — reopen welcome |
| [#106](https://github.com/silkyclouds/pmda-tracker/issues/106) | Discovery emits no durable heartbeat: the scan job goes stale while the scan is healthy | — | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v335 | Shipped & closed — reopen welcome |
| [#30](https://github.com/silkyclouds/pmda-tracker/issues/30) | [BUG] numpy error | cissoubaka | <img src="charts/badges/badge-fixed.svg" alt="FIXED" height="18"/> | v396 | Shipped & closed — reopen welcome |

</details>

<!-- issue-table:end -->

## What PMDA is

PMDA is not a music player, and it is not meant to replace Plex, Plexamp, Navidrome, Jellyfin, beets, Picard, SongKong or Lidarr. The goal is more modest: help you inspect the library behind them.

It currently helps with:

- finding possible duplicate releases
- spotting incomplete albums
- surfacing missing or weak metadata
- showing missing covers
- scanning messy intake folders
- optionally preparing a cleaner destination library

The safest way to try it is read-only first — no deletes or file moves are required.

## Links

- Website and docs — https://pmda.muteq.eu/
- Docker image — https://hub.docker.com/r/meaning/pmda
- Discord — https://discord.gg/2jkwnNhHHR
- Subreddit — https://reddit.com/r/PMDA
- Also available on Unraid Community Applications

## Testing on Unraid — read this first

Switching a container to the `:beta` tag does **not** always pull the new image: Unraid may reuse the cached one, and its update checker can say "up to date" while a newer beta exists (#40). Before every test:

1. Edit the container, set the repository tag to `meaning/pmda:beta`, then use **Force Update** on the Docker page.
2. Open the web UI and check the **bottom of the expanded sidebar**: it shows the version actually running (`pmda v30x`). Every test protocol on this tracker names the version it needs — if the sidebar shows an older one, the image did not update.

## Reporting something

Open an issue here, or post on the Discord or the subreddit — reports from both are collected and filed here automatically, so nothing gets lost either way. If your report already exists, you will be pointed at the existing issue rather than getting a duplicate.

Useful things to include: what you expected, what happened, a screenshot, your PMDA version, and how your library is stored (folder structure, tag quality, compilation handling). Large or messy collections are the interesting cases — old rips, bad tags, multiple editions, bootlegs, live albums, classical, partial downloads.

## How issues are labelled

Every issue carries up to four labels, so the backlog stays readable:

| Axis | Labels |
| --- | --- |
| Type | `bug` · `enhancement` · `question` · `documentation` |
| Area | `area: scan` · `area: metadata` · `area: duplicates` · `area: player` · `area: mobile` · `area: sharing` · `area: settings` · `area: providers` · `area: deployment` · `area: ui` |
| Severity | `severity: blocker` · `severity: major` · `severity: minor` · `severity: cosmetic` |
| Source | `source: discord` · `source: reddit` · `source: both` |

Two more mark a state rather than a category: `needs-info` when a report is waiting on its author, and `fix-shipped` when a fix has been released and is awaiting confirmation. An issue is closed only once the person who reported it confirms it is actually fixed.

PMDA is still early. Bug reports, screenshots, logs, workflow feedback and criticism are all welcome — the point is to find out where it gets things wrong.
