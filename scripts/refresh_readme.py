#!/usr/bin/env python3
"""Regenerate the README issue table and the four dashboard charts from the live issues.

    python3 scripts/refresh_readme.py            # rewrite README.md and charts/*.svg
    python3 scripts/refresh_readme.py --dry-run  # print what would change, write nothing

Standard library only. Issues and comments are read through `gh api` with
pagination, so `gh` must be installed and authenticated.

What is kept and what is rewritten
----------------------------------
The table between <!-- issue-table:start --> and <!-- issue-table:end --> has one
section per area and one row per issue. For an issue that already has a row, the
row's area, wording (title) and reporter are kept exactly as written: they may have
been corrected by hand. Only the state is recomputed:

    closed                           -> FIXED       "Shipped & closed — reopen welcome"
    open, label needs-info           -> NEEDS INFO  "Waiting on details"
    open, label needs-testing        -> IN BETA     "Awaiting reporter confirmation"
    open, anything else              -> BACKLOG     "—"

The Fix column keeps its version while the state does not change. When a row moves
to FIXED or IN BETA without a version, the version is read from the maintainer's
comments ("shipped in v1002", "What changes in v1001", ...), newest comment first.

A new issue gets its area from its `area:` labels (first in section order), then
from `documentation` (Deployment & docs), then from its content: the area whose
vocabulary its title (weighted) and body share most. Nothing matching means Other.
Its title is the GitHub title, cut to 93 characters plus an ellipsis past 96. Its
reporter is its `reporter:` labels, or the GitHub login that opened it.

Rows are ordered open first, then closed, each by number descending. A section is
<details open> while it has an open row. The counts in the summary lines are
recomputed from the rows; the prose around them is left as it is.

The charts
----------
They count reports: every issue except the engineering improvements we filed
ourselves (titles starting with "[scanner]"), which the progress chart tallies on a
line of their own.

    progress.svg  confirmed = closed reports, awaiting = open with needs-testing
    status.svg    donut: awaiting, confirmed, queued, and waiting on reporter
                  (needs-info) when there is one
    severity.svg  open reports labelled `bug`, by `severity:` label, else "unrated"
    areas.svg     open reports by `area:` label (an issue with two counts twice),
                  else by the area of its table row
"""

import argparse
import json
import math
import os
import re
import subprocess
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
CHARTS = os.path.join(ROOT, "charts")

START = "<!-- issue-table:start -->"
END = "<!-- issue-table:end -->"

# Section name, in table order, and the `area:` label it stands for.
AREAS = [
    ("UI / UX", "ui"),
    ("Scanner & pipeline", "scan"),
    ("Duplicates", "duplicates"),
    ("Metadata & matching", "metadata"),
    ("Mobile apps", "mobile"),
    ("Player & playback", "player"),
    ("Providers & integrations", "providers"),
    ("Settings & onboarding", "settings"),
    ("Deployment & docs", "deployment"),
    ("Sharing & social", "sharing"),
    ("Other", "other"),
]
SECTION_OF_LABEL = {key: name for name, key in AREAS}
LABEL_OF_SECTION = {name: key for name, key in AREAS}
SECTION_ORDER = [name for name, _ in AREAS]

# Vocabulary for placing a new issue that carries no area label. Each entry is a
# regular expression matched at the start of a word, on lowercase text.
AREA_VOCABULARY = {
    "UI / UX": ["page", "layout", "theme", "button", "navigat", "sidebar", "scroll",
                "contrast", "font", "screen\\b", "view\\b", "click", "modal", "dialog",
                "menu", "home\\b", "light mode", "dark mode"],
    "Scanner & pipeline": ["scan", "intake", "inbox", "pipeline", "import", "watcher",
                           "reindex", "index\\b"],
    "Duplicates": ["duplicate", "dupe", "quarantin"],
    "Metadata & matching": ["tag\\b", "tags\\b", "musicbrainz", "metadata", "match",
                            "identif", "edition", "cover", "artwork", "genre",
                            "release", "catalogue"],
    "Mobile apps": ["ios\\b", "android", "iphone", "ipad", "mobile", "carplay",
                    "widget", "testflight", "play store"],
    "Player & playback": ["playback", "player", "queue", "stream", "radio", "subsonic",
                          "lyric", "gapless"],
    "Providers & integrations": ["provider", "spotify", "last\\.?fm", "lidarr",
                                 "discogs", "integration", "webhook", "apprise", "plex",
                                 "navidrome", "jellyfin", "notification"],
    "Settings & onboarding": ["setting", "wizard", "onboarding", "configur", "setup",
                              "sub-?menu"],
    "Deployment & docs": ["docker", "unraid", "network", "reverse proxy", "container",
                          "install", "documentation", "readme", "compose"],
    "Sharing & social": ["share", "sharing", "invit", "remote librar", "multi-server",
                         "friend"],
}

STATUS_BADGE = {
    "FIXED": ("badge-fixed", "FIXED"),
    "IN BETA": ("badge-beta", "IN BETA"),
    "BACKLOG": ("badge-backlog", "BACKLOG"),
    "NEEDS INFO": ("badge-info", "NEEDS INFO"),
}
VALIDATION = {
    "FIXED": "Shipped & closed — reopen welcome",
    "IN BETA": "Awaiting reporter confirmation",
    "BACKLOG": "—",
    "NEEDS INFO": "Waiting on details",
}
DASH = "—"

TITLE_MAX = 96
TITLE_CUT = 93

# Engineering improvements we opened ourselves; the charts keep them out of the reports.
ENGINEERING_TITLE = re.compile(r"^\[scanner\]")

# How the maintainer names the version that shipped a fix.
VERSION_IN_COMMENT = re.compile(
    r"(?:shipped|ships|fixed|landed|released|lands)\s+(?:in|on|with)\s+v(\d{2,5})\b"
    r"|what\s+(?:changes|changed)\s+in\s+v(\d{2,5})\b"
    r"|\b(?:since|as\s+of|from)\s+v(\d{2,5})\b"
    # "v1006 is out now, and it changes ..." / "v1006 (out now): ..."
    r"|\bv(\d{2,5})\s+(?:is\s+out\b|\(out\s+now\))",
    re.IGNORECASE,
)

# A title that quotes an absolute path from someone's install must be reworded by hand.
PATH_IN_TITLE = re.compile(r"(?:^|[\s(\"'`])/(?:mnt|home|users|volumes|data|media|music|srv|opt|share)\b",
                           re.IGNORECASE)


# --------------------------------------------------------------------------- GitHub

def gh_paginated(path):
    """Every item of a paginated GitHub list endpoint, through `gh api --paginate`."""
    out = subprocess.run(["gh", "api", "--paginate", path],
                         check=True, capture_output=True, text=True).stdout
    # --paginate prints one JSON array per page, back to back.
    decoder = json.JSONDecoder()
    items, pos, text = [], 0, out.strip()
    while pos < len(text):
        page, pos = decoder.raw_decode(text, pos)
        items.extend(page)
        while pos < len(text) and text[pos].isspace():
            pos += 1
    return items


def fetch_issues(repo):
    items = gh_paginated(f"repos/{repo}/issues?state=all&per_page=100")
    return {i["number"]: i for i in items if "pull_request" not in i}


def fetch_comments(repo, number):
    return gh_paginated(f"repos/{repo}/issues/{number}/comments?per_page=100")


def labels_of(issue):
    return [label["name"] for label in issue["labels"]]


# --------------------------------------------------------------------------- README table

ROW = re.compile(r"^\| \[#(\d+)\]\(")


def split_row(line):
    cells = re.split(r"(?<!\\)\|", line.strip())[1:-1]
    return [c.strip() for c in cells]


def parse_table(block):
    """Existing rows, by issue number: area, title, reporter, status, fix."""
    rows, section = {}, None
    for line in block.splitlines():
        m = re.match(r"<summary><b>(.*?)</b>", line)
        if m:
            section = m.group(1)
            continue
        m = ROW.match(line)
        if not m:
            continue
        number = int(m.group(1))
        cells = split_row(line)
        if len(cells) != 6:
            sys.exit(f"README row #{number} does not have six cells: {line}")
        alt = re.search(r'alt="([^"]+)"', cells[3])
        rows[number] = {
            "area": section,
            "title": cells[1],
            "reporter": cells[2],
            "status": alt.group(1) if alt else cells[3],
            "fix": cells[4],
            "line": line,
        }
    return rows


def status_of(issue):
    if issue["state"] == "closed":
        return "FIXED"
    labels = labels_of(issue)
    if "needs-info" in labels:
        return "NEEDS INFO"
    if "needs-testing" in labels or "fix-shipped" in labels:
        return "IN BETA"
    return "BACKLOG"


def clean_body(text):
    text = re.sub(r"```.*?```", " ", text or "", flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    return text.lower()


def area_by_content(issue):
    """The section whose vocabulary the issue shares most; Other when none clearly wins."""
    title = issue["title"].lower()
    body = clean_body(issue.get("body"))
    scores = {}
    for section, words in AREA_VOCABULARY.items():
        in_title = sum(1 for w in words if re.search(r"\b" + w, title))
        in_body = sum(1 for w in words if re.search(r"\b" + w, body))
        scores[section] = (3 * in_title + in_body, in_title)
    ranked = sorted(scores.items(), key=lambda kv: (-kv[1][0], -kv[1][1], SECTION_ORDER.index(kv[0])))
    (best, (score, _)), (_, (runner_up, _)) = ranked[0], ranked[1]
    if score < 2 or score == runner_up and scores[best][1] == ranked[1][1][1]:
        return "Other"
    return best


def area_of_new(issue):
    labels = labels_of(issue)
    sections = [SECTION_OF_LABEL[l[6:]] for l in labels
                if l.startswith("area: ") and l[6:] in SECTION_OF_LABEL]
    if sections:
        return min(sections, key=SECTION_ORDER.index)
    if "documentation" in labels:
        return "Deployment & docs"
    return area_by_content(issue)


def reporter_of_new(issue):
    names = [l[len("reporter: "):] for l in labels_of(issue) if l.startswith("reporter: ")]
    if names:
        return ", ".join(sorted(names, key=str.lower))
    return issue["user"]["login"].replace("[bot]", "")


def title_of_new(issue):
    title = " ".join(issue["title"].split()).replace("|", "\\|")
    if len(title) > TITLE_MAX:
        title = title[:TITLE_CUT] + "…"
    return title


def shipped_version(repo, issue, owner):
    for comment in sorted(fetch_comments(repo, issue["number"]),
                          key=lambda c: c["created_at"], reverse=True):
        if comment["user"]["login"] != owner:
            continue
        m = VERSION_IN_COMMENT.search(comment["body"] or "")
        if m:
            return "v" + next(g for g in m.groups() if g)
    return DASH


def render_row(repo, number, entry):
    badge, alt = STATUS_BADGE[entry["status"]]
    return (f"| [#{number}](https://github.com/{repo}/issues/{number}) | {entry['title']} | "
            f"{entry['reporter']} | <img src=\"charts/badges/{badge}.svg\" alt=\"{alt}\" height=\"18\"/> | "
            f"{entry['fix']} | {VALIDATION[entry['status']]} |")


def build_entries(repo, issues, old_rows, owner):
    entries, changes = {}, []
    for number, issue in sorted(issues.items()):
        status = status_of(issue)
        old = old_rows.get(number)
        if old:
            entry = {"area": old["area"], "title": old["title"], "reporter": old["reporter"],
                     "status": status, "fix": old["fix"]}
            if status != old["status"]:
                if status in ("BACKLOG", "NEEDS INFO"):
                    entry["fix"] = DASH
                elif entry["fix"] == DASH:
                    entry["fix"] = shipped_version(repo, issue, owner)
                changes.append(f"#{number}: {old['status']} -> {status} (fix {entry['fix']})")
        else:
            entry = {"area": area_of_new(issue), "title": title_of_new(issue),
                     "reporter": reporter_of_new(issue), "status": status, "fix": DASH}
            if status in ("FIXED", "IN BETA"):
                entry["fix"] = shipped_version(repo, issue, owner)
            if PATH_IN_TITLE.search(entry["title"]):
                sys.exit(f"#{number}: the title quotes a path. Give it a row by hand in README.md "
                         f"with the path reworded, then run this again.")
            changes.append(f"#{number}: new row in {entry['area']}, {status} (fix {entry['fix']})")
        entries[number] = entry
    dropped = sorted(set(old_rows) - set(issues))
    for number in dropped:
        changes.append(f"#{number}: row dropped, the issue no longer exists")
    return entries, changes


def render_block(repo, old_block, entries):
    head_end = old_block.index("<details")
    head = old_block[len(START):head_end]
    fixed = sum(1 for e in entries.values() if e["status"] == "FIXED")
    open_ = len(entries) - fixed
    head, n = re.subn(r"^_(\d+) fixed · (\d+) open",
                      f"_{fixed} fixed · {open_} open", head, count=1, flags=re.MULTILINE)
    if n != 1:
        sys.exit("The '_N fixed · M open' line was not found above the table.")

    order = list(SECTION_ORDER)
    for e in entries.values():
        if e["area"] not in order:
            order.insert(len(order) - 1, e["area"])

    parts = [START, head]
    for section in order:
        members = [(num, e) for num, e in entries.items() if e["area"] == section]
        if not members:
            continue
        members.sort(key=lambda ne: (ne[1]["status"] == "FIXED", -ne[0]))
        opened = sum(1 for _, e in members if e["status"] != "FIXED")
        parts.append("<details open>\n" if opened else "<details>\n")
        parts.append(f"<summary><b>{section}</b> — {len(members)} report(s), {opened} open</summary>\n\n")
        parts.append("| # | Issue | Reporter | Status | Fix | Validation |\n")
        parts.append("|---|-------|----------|--------|-----|------------|\n")
        for number, e in members:
            parts.append(render_row(repo, number, e) + "\n")
        parts.append("\n</details>\n\n")
    parts.append(END)
    return "".join(parts)


def check_block(block, issues, old_block):
    """The invariants the README must hold after a refresh."""
    rows = parse_table(block)
    numbers = [int(m.group(1)) for m in (ROW.match(l) for l in block.splitlines()) if m]
    duplicated = sorted(n for n, c in Counter(numbers).items() if c > 1)
    missing = sorted(set(issues) - set(numbers))
    unknown = sorted(set(numbers) - set(issues))
    problems = []
    if duplicated:
        problems.append(f"issues listed more than once: {duplicated}")
    if missing:
        problems.append(f"issues missing from the table: {missing}")
    if unknown:
        problems.append(f"rows for issues that do not exist: {unknown}")

    fixed = sum(1 for r in rows.values() if r["status"] == "FIXED")
    m = re.search(r"^_(\d+) fixed · (\d+) open", block, re.MULTILINE)
    if (int(m.group(1)), int(m.group(2))) != (fixed, len(rows) - fixed):
        problems.append("the summary line does not match the rows")
    live_open = sum(1 for i in issues.values() if i["state"] == "open")
    if len(rows) - fixed != live_open:
        problems.append(f"{len(rows) - fixed} open rows, {live_open} open issues")
    for section, total, opened in re.findall(r"<summary><b>(.*?)</b> — (\d+) report\(s\), (\d+) open</summary>", block):
        members = [r for r in rows.values() if r["area"] == section]
        if (int(total), int(opened)) != (len(members), sum(1 for r in members if r["status"] != "FIXED")):
            problems.append(f"the {section} summary does not match its rows")

    # Every line of hand-written text survives; only digits may move.
    def prose(text):
        return {re.sub(r"\d+", "#", l) for l in text.splitlines() if l and not ROW.match(l)}
    lost = prose(old_block) - prose(block)
    if lost:
        problems.append(f"text lines changed: {sorted(lost)}")
    return problems


# --------------------------------------------------------------------------- charts

SANS = "-apple-system,Segoe UI,Helvetica,Arial,sans-serif"
MONO = "SFMono-Regular,Consolas,Liberation Mono,monospace"
BG, TRACK, INK, MUTED = "#141210", "#1c1917", "#f2ede5", "#8a8175"
ORANGE, GREEN, GREY, AMBER = "#f2703a", "#4ec98a", "#5a544c", "#e0b25e"
SEVERITY_COLOR = {"blocker": "#ff5d4f", "major": "#f2703a", "minor": "#e0c65e",
                  "cosmetic": "#9aa2ad", "unrated": "#8a8175"}


def frame(height, title):
    return (f"<svg xmlns='http://www.w3.org/2000/svg' width='660' height='{height}' viewBox='0 0 660 {height}'>"
            f"<rect width='660' height='{height}' fill='{BG}'/>"
            f"<rect x='0' y='0' width='660' height='2' fill='{ORANGE}'/>"
            f"<text x='24' y='40' font-family='{MONO}' font-size='11' letter-spacing='3' fill='{ORANGE}'>{title}</text>")


def bar_chart(title, bars):
    """bars: [(name, count, color)], drawn in the order given."""
    top = max((count for _, count, _ in bars), default=0)
    svg = [frame(78 + 36 * len(bars), title)]
    for k, (name, count, color) in enumerate(bars):
        y = 66 + 36 * k
        width = int(450 * count / top) if top else 0
        svg.append(f"<text x='136' y='{y + 15}' font-family='{SANS}' font-size='13' fill='{INK}' text-anchor='end'>{name}</text>"
                   f"<rect x='150' y='{y}' width='450' height='22' fill='{TRACK}'/>"
                   f"<rect x='150' y='{y}' width='{width}' height='22' fill='{color}'/>"
                   f"<text x='{150 + width + 10}' y='{y + 15}' font-family='{MONO}' font-size='13' fill='{MUTED}'>{count}</text>")
    svg.append("</svg>")
    return "".join(svg)


def progress_chart(total, confirmed, awaiting, engineering):
    green = int(612 * confirmed / total) if total else 0
    orange = int(612 * awaiting / total) if total else 0
    pct = round(100 * confirmed / total) if total else 0
    pct_all = round(100 * (confirmed + awaiting) / total) if total else 0
    svg = [frame(190, "PROGRESS"),
           f"<rect x='24' y='92' width='612' height='26' fill='{TRACK}'/>",
           f"<rect x='24' y='92' width='{green}' height='26' fill='{GREEN}'/>",
           f"<rect x='{24 + green}' y='92' width='{orange}' height='26' fill='{ORANGE}'/>",
           f"<text x='24' y='76' font-family='{SANS}' font-size='26' font-weight='700' fill='{INK}'>{pct}% confirmed fixed</text>",
           f"<text x='636' y='76' font-family='{SANS}' font-size='14' fill='{MUTED}' text-anchor='end'>{pct_all}% incl. awaiting confirmation</text>",
           f"<rect x='24' y='136' width='10' height='10' fill='{GREEN}'/>",
           f"<text x='42' y='145' font-family='{SANS}' font-size='12' fill='{MUTED}'>confirmed by the reporter</text>",
           f"<rect x='244' y='136' width='10' height='10' fill='{ORANGE}'/>",
           f"<text x='262' y='145' font-family='{SANS}' font-size='12' fill='{MUTED}'>fixed and shipped, waiting on its reporter</text>"]
    if engineering:
        svg.append(f"<text x='24' y='170' font-family='{SANS}' font-size='12' fill='{MUTED}'>plus {engineering} engineering "
                   f"improvements delivered and closed, counted separately from reports</text>")
    svg.append("</svg>")
    return "".join(svg)


def status_chart(slices):
    """slices: [(label, count, color)]; empty slices are left out."""
    slices = [s for s in slices if s[1]]
    total = sum(count for _, count, _ in slices)
    circumference = 2 * math.pi * 88
    svg = [frame(280, "ALL REPORTS BY STATUS")]
    start = 0.0
    for _, count, color in slices:
        arc = circumference * count / total
        dash = max(arc - 3, 0)
        svg.append(f"<circle cx='150' cy='158' r='88' fill='none' stroke='{color}' stroke-width='34' "
                   f"stroke-dasharray='{dash:.2f} {circumference - dash:.2f}' stroke-dashoffset='-{start:.2f}' "
                   f"transform='rotate(-90 150 158)'/>")
        start += arc
    svg.append(f"<text x='150' y='154' font-family='{SANS}' font-size='40' font-weight='700' fill='{INK}' text-anchor='middle'>{total}</text>"
               f"<text x='150' y='180' font-family='{MONO}' font-size='10' letter-spacing='2' fill='{MUTED}' text-anchor='middle'>REPORTS</text>")
    for k, (label, count, color) in enumerate(slices):
        y = 82 + 34 * k
        svg.append(f"<rect x='320' y='{y}' width='12' height='12' fill='{color}'/>"
                   f"<text x='344' y='{y + 11}' font-family='{SANS}' font-size='14' fill='{INK}'>{label}</text>"
                   f"<text x='636' y='{y + 11}' font-family='{MONO}' font-size='13' fill='{MUTED}' text-anchor='end'>"
                   f"{count} · {round(100 * count / total)}%</text>")
    svg.append("</svg>")
    return "".join(svg)


def build_charts(issues, entries):
    newest_first = [issues[n] for n in sorted(issues, reverse=True)]
    reports = [i for i in newest_first if not ENGINEERING_TITLE.match(i["title"])]
    engineering = sum(1 for i in newest_first
                      if ENGINEERING_TITLE.match(i["title"]) and i["state"] == "closed")

    tally = Counter()
    for issue in reports:
        status = status_of(issue)
        tally[{"FIXED": "confirmed", "IN BETA": "awaiting",
               "NEEDS INFO": "waiting", "BACKLOG": "queued"}[status]] += 1

    areas, severities = Counter(), Counter()
    for issue in reports:
        if issue["state"] != "open":
            continue
        labels = labels_of(issue)
        keys = [l[6:] for l in labels if l.startswith("area: ")]
        if not keys:
            keys = [LABEL_OF_SECTION.get(entries[issue["number"]]["area"], "other")]
        for key in keys:
            areas[key] += 1
        if "bug" in labels:
            rated = [l[10:] for l in labels if l.startswith("severity: ")]
            severities[rated[0] if rated else "unrated"] += 1

    figures = {"reports": len(reports), "engineering": engineering, **tally,
               "areas": areas.most_common(), "severities": severities.most_common()}
    charts = {
        "progress.svg": progress_chart(len(reports), tally["confirmed"], tally["awaiting"], engineering),
        "status.svg": status_chart([("Fixed, awaiting tester", tally["awaiting"], ORANGE),
                                    ("Resolved and confirmed", tally["confirmed"], GREEN),
                                    ("Queued", tally["queued"], GREY),
                                    ("Waiting on reporter", tally["waiting"], AMBER)]),
        "severity.svg": bar_chart("OPEN BUGS BY SEVERITY",
                                  [(k, n, SEVERITY_COLOR.get(k, MUTED)) for k, n in severities.most_common()]),
        "areas.svg": bar_chart("OPEN WORK BY AREA", [(k, n, ORANGE) for k, n in areas.most_common()]),
    }
    return charts, figures


# --------------------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", default="silkyclouds/pmda-tracker")
    parser.add_argument("--dry-run", action="store_true", help="print the changes, write nothing")
    args = parser.parse_args()
    owner = args.repo.split("/")[0]

    with open(README, encoding="utf-8") as f:
        readme = f.read()
    a, b = readme.find(START), readme.find(END)
    if a < 0 or b < a:
        sys.exit("The issue-table markers are missing from README.md.")
    old_block = readme[a:b + len(END)]

    issues = fetch_issues(args.repo)
    old_rows = parse_table(old_block)
    entries, changes = build_entries(args.repo, issues, old_rows, owner)
    block = render_block(args.repo, old_block, entries)

    problems = check_block(block, issues, old_block)
    if problems:
        sys.exit("Refusing to write:\n  " + "\n  ".join(problems))

    charts, figures = build_charts(issues, entries)

    print(f"{len(issues)} issues, {len(changes)} row change(s)")
    for line in changes:
        print("  " + line)
    print("charts:", json.dumps(figures))

    if args.dry_run:
        return
    with open(README, "w", encoding="utf-8") as f:
        f.write(readme[:a] + block + readme[b + len(END):])
    for name, svg in charts.items():
        with open(os.path.join(CHARTS, name), "w", encoding="utf-8") as f:
            f.write(svg)


if __name__ == "__main__":
    main()
