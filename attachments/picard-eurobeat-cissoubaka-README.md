# Picard run on the Eurobeat compilations — reference log for issue #34

Shared by **cissoubaka**, who ran MusicBrainz Picard over the same Super Eurobeat
collection PMDA fails to match (folders named `SEB vol 01` instead of
*Super Eurobeat Vol. 1*, with unreliable tags). This is the only third-party
trace we have of what a mature matcher does with these exact files, so it is
kept here as evidence while #34 is implemented.

File: `picard-eurobeat-cissoubaka-redacted.log.gz` (12 MB compressed,
59 MB raw, 98k lines, Picard debug level).

## Redaction

Published only after redaction — 2833 replacements, verified zero remaining:

- `client=<key>` AcoustID API keys (2611 occurrences) → `client=<redacted>`
- Windows/macOS/Linux user paths → `C:\Users\<user>`, `/Users/<user>`, `/home/<user>`

## What the log shows

| Signal | Count |
|---|---|
| AcoustID lookups | 14,373 |
| Fingerprint activity lines | 7,831 |
| Requests to api.acoustid.org | 5,901 |
| Cover Art Archive requests | 2,826 + 1,124 archive.org |
| MusicBrainz `/ws/2/` calls | 231 |
| Errors | 811 |

Errors break down as 418 network failures, 228 Cover Art Archive JSON errors and
165 cover download failures, over 228 distinct albums — dominated by **HTTP 500
from the Cover Art Archive CDN** (393 of the errors), plus 15×404 and 10×503.

## Why it matters for #34

1. **Picard leans on fingerprinting, not on names.** 14,373 AcoustID lookups
   against 231 MusicBrainz text queries: when the folder name lies, the audio is
   what resolves the release. That is exactly the escalation #34 proposes, and
   this log is the empirical argument for making it automatic rather than manual.
2. **Fingerprinting is chatty.** ~14k lookups for one compilation set: whatever
   PMDA does here needs rate-limit discipline and caching, or it becomes the next
   timeout source (see the MusicBrainz queue work in #7).
3. **Cover art is a separate, unreliable dependency.** Nearly half the errors are
   the CAA CDN returning 500. Cover OCR (rung 3 of the ladder) must treat a
   missing cover as a normal outcome, never as a failure that stops the chain.

## How to read it

```bash
gunzip -c picard-eurobeat-cissoubaka-redacted.log.gz | grep '^E:'          # errors only
gunzip -c picard-eurobeat-cissoubaka-redacted.log.gz | grep -i acoustid    # fingerprint path
```
