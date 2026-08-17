#!/usr/bin/env python3
"""Support intake bot for the PMDA tracker.

Users drop diagnostic bundles (the Duplicates page's "Export for support"
JSON) as comments on the pinned drop issue. This script, run on a schedule by
GitHub Actions with the repository's own token:

1. reads new comments on the drop issue since the last processed id;
2. downloads any attached .json bundle and computes a digest (version, pair
   counts by class, incompletes counts);
3. classifies the report into a TYPE from the bundle and the user's words;
4. files the example as a comment on the one aggregation issue for that type
   (creating it on first sight, labeled `user-report` + `report-type`), and
   updates the counter block in that issue's body;
5. acknowledges under the user's comment with a link to where it was filed.

One issue per problem type, a counter per issue, every example preserved --
knowledge accumulates instead of scattering across tickets.

State lives in support/state.json, committed back by the workflow.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request

REPO = os.getenv("GITHUB_REPOSITORY", "silkyclouds/pmda-tracker")
TOKEN = os.getenv("GITHUB_TOKEN", "")
DROP_ISSUE = int(os.getenv("SUPPORT_DROP_ISSUE", "187"))
STATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")
API = "https://api.github.com"

MAX_BUNDLE_BYTES = 30 * 1024 * 1024

TYPES = {
    "dupe-false-positive": "Duplicate verdicts users contest (false positives)",
    "dupe-missed": "Duplicates users expected but PMDA did not report",
    "incompletes-report": "Incompletes detection reports",
    "mirror-install": "MusicBrainz mirror setup failures",
    "general-report": "General user reports (unclassified)",
}


def _api(path: str, method: str = "GET", body: dict | None = None):
    req = urllib.request.Request(
        API + path,
        method=method,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "pmda-support-intake",
        },
        data=json.dumps(body).encode() if body is not None else None,
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode() or "null")


def _download(url: str) -> bytes | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "pmda-support-intake"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read(MAX_BUNDLE_BYTES + 1)
            if len(data) > MAX_BUNDLE_BYTES:
                return None
            return data
    except Exception:
        return None


def load_state() -> dict:
    try:
        with open(STATE_PATH, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"last_comment_id": 0, "type_issues": {}}


def save_state(state: dict) -> None:
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, sort_keys=True)
        f.write("\n")


def classify(text: str, bundle: dict | None) -> str:
    t = (text or "").lower()
    if bundle is None:
        if re.search(r"mirror|musicbrainz[- ]docker|replication", t):
            return "mirror-install"
        if re.search(r"incomplete|missing track", t):
            return "incompletes-report"
        if re.search(r"dup|copy|copies", t):
            return "dupe-missed" if re.search(r"miss|not show|no dupes|nothing|zero", t) else "dupe-false-positive"
        return "general-report"
    if re.search(r"incomplete|missing track", t) and not re.search(r"dup", t):
        return "incompletes-report"
    if re.search(r"false|nonsense|wrong|not (a )?dup|shouldn.t|mis-?identif", t):
        return "dupe-false-positive"
    if re.search(r"miss(ed|ing)|expected|should (be|show)|does ?n.t (show|find)|zero dup", t):
        return "dupe-missed"
    return "dupe-false-positive" if bundle else "general-report"


def bundle_digest(bundle: dict) -> str:
    dup = bundle.get("duplicates") or {}
    cls = dup.get("classification") or {}
    total = sum(int(v or 0) for v in cls.values())
    actionable = int(cls.get("EXACT_DUPE") or 0) + int(cls.get("INCOMPLETE_COPY") or 0)
    inc = bundle.get("incompletes")
    inc_count = len(inc) if isinstance(inc, list) else "n/a"
    top = ", ".join(f"{k}: {v}" for k, v in sorted(cls.items(), key=lambda x: -int(x[1] or 0))[:5])
    return (
        f"PMDA version: `{bundle.get('pmda_version') or 'unknown'}` | pairs analyzed: {total} | "
        f"actionable: {actionable} | incompletes rows: {inc_count}\n"
        f"Top classes: {top or 'none'}"
    )


def counter_block(count: int, versions: list[str]) -> str:
    versions_txt = ", ".join(sorted(set(v for v in versions if v))) or "unknown"
    return (
        "<!-- support-bot:stats -->\n"
        f"**Examples collected: {count}** | PMDA versions seen: {versions_txt}\n"
        "<!-- /support-bot:stats -->"
    )


def ensure_type_issue(state: dict, type_slug: str) -> int:
    known = state.setdefault("type_issues", {})
    if type_slug in known:
        return int(known[type_slug])
    created = _api(
        f"/repos/{REPO}/issues",
        method="POST",
        body={
            "title": TYPES.get(type_slug, type_slug),
            "labels": ["user-report", "report-type"],
            "body": (
                f"Aggregation issue for user reports of type `{type_slug}`. The intake bot files each "
                f"new example from the drop zone (#{DROP_ISSUE}) as a comment here and keeps the "
                "counter below current. Human analysis happens in the comments; when a fix ships, "
                "note the version here so later examples can be judged against it.\n\n"
                + counter_block(0, [])
            ),
        },
    )
    known[type_slug] = int(created["number"])
    return known[type_slug]


def update_counter(issue_number: int, version: str) -> None:
    issue = _api(f"/repos/{REPO}/issues/{issue_number}")
    body = issue.get("body") or ""
    m = re.search(r"<!-- support-bot:stats -->\n\*\*Examples collected: (\d+)\*\* \| PMDA versions seen: ([^\n]*)\n<!-- /support-bot:stats -->", body)
    count, versions = 0, []
    if m:
        count = int(m.group(1))
        versions = [v.strip().strip("`") for v in m.group(2).split(",") if v.strip() and v.strip() != "unknown"]
    versions.append(version or "")
    new_block = counter_block(count + 1, versions)
    if m:
        body = body[: m.start()] + new_block + body[m.end():]
    else:
        body = body.rstrip() + "\n\n" + new_block
    _api(f"/repos/{REPO}/issues/{issue_number}", method="PATCH", body={"body": body})


def main() -> int:
    if not TOKEN:
        print("no GITHUB_TOKEN", file=sys.stderr)
        return 1
    state = load_state()
    last_id = int(state.get("last_comment_id") or 0)
    comments = _api(f"/repos/{REPO}/issues/{DROP_ISSUE}/comments?per_page=100&sort=created&direction=asc")
    new_last = last_id
    processed = 0
    for comment in comments or []:
        cid = int(comment.get("id") or 0)
        if cid <= last_id:
            continue
        user = (comment.get("user") or {}).get("login") or "unknown"
        if user.endswith("[bot]"):
            new_last = max(new_last, cid)
            continue
        text = comment.get("body") or ""
        if "filed this report into" in text:
            new_last = max(new_last, cid)
            continue
        bundle = None
        for url in re.findall(r"https://github\.com/user-attachments/files/\S+?\.json", text):
            data = _download(url)
            if data:
                try:
                    candidate = json.loads(data.decode("utf-8", errors="replace"))
                    if isinstance(candidate, dict) and "pmda" in str(candidate.get("kind", "")):
                        bundle = candidate
                        break
                except Exception:
                    continue
        type_slug = classify(text, bundle)
        issue_number = ensure_type_issue(state, type_slug)
        digest = bundle_digest(bundle) if bundle else "No bundle attached (text-only report)."
        quoted = "\n".join("> " + line for line in text.strip().splitlines()[:20])
        _api(
            f"/repos/{REPO}/issues/{issue_number}/comments",
            method="POST",
            body={
                "body": (
                    f"New example from @{user} in the drop zone "
                    f"([original comment]({comment.get('html_url')})).\n\n{quoted}\n\n{digest}"
                )
            },
        )
        update_counter(issue_number, str((bundle or {}).get("pmda_version") or ""))
        _api(
            f"/repos/{REPO}/issues/{DROP_ISSUE}/comments",
            method="POST",
            body={
                "body": (
                    f"@{user} thanks -- the bot filed this report into #{issue_number} "
                    f"(`{type_slug}`). Follow the analysis there."
                )
            },
        )
        processed += 1
        new_last = max(new_last, cid)
    state["last_comment_id"] = new_last
    save_state(state)
    print(f"processed {processed} new report(s); last_comment_id={new_last}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
