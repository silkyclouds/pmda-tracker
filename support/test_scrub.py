"""No character of a secret reaches this public repository.

PMDA up to v1004 masked a secret setting as its first four characters and an
ellipsis ("abcd…"), and its startup config dump went through that mask, so
every support bundle's log tail carried the start of the Navidrome password
and of each API key. 10 of the first 28 bundles committed here did. v1005
masks fully, but old clients keep sending, so the intake scrubs every bundle
before it commits it (support/scrub.py, called by intake._commit_bundle).

The bundle below is shaped like a v1004 one: the startup lines are written
with v1004's own format and v1004's own mask, applied to fake secrets. The
test goes through the intake's commit door, not only the scrub function, and
asserts that no character sequence a secret showed survives, that the file
still parses, and that what is not a secret is left alone.

Run: python3 support/test_scrub.py
"""

from __future__ import annotations

import base64
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import intake  # noqa: E402
import scrub  # noqa: E402


def v1004_mask(value: str) -> str:
    """pmda_core/settings_runtime.mask_secret_value as v1004 shipped it."""
    if not value:
        return ""
    if len(value) <= 4:
        return "****"
    return value[:4] + "…"


def config_line(key: str, value: str, source: str) -> str:
    """One line of v1004's startup dump: 'Config %-15s = %-30s (source: %s)'."""
    return "2026-09-27 21:14:03,512 INFO [MainThread] Config %-15s = %-30s (source: %s)" % (key, value, source)


# Fake secrets. Their first four characters are what v1004 published.
SECRETS = {
    "NAVIDROME_PASSWORD": "Qz7!fake-navidrome-password",
    "LASTFM_API_KEY": "Xk4~fakefakefakefakefakefake0001",
    "LASTFM_API_SECRET": "Wj2^fakefakefakefakefakefake0002",
    "DISCOGS_USER_TOKEN": "Vh8%fakeDiscogsUserTokenValue0003",
    "ACOUSTID_API_KEY": "Ug5=fakeAcoustid",
    "FANART_API_KEY": "Tf3+fakefakefakefakefakefake0004",
    "SERPER_API_KEY": "Sd6@fakefakefakefakefakefake0005",
    "THEAUDIODB_API_KEY": "523",
}
# Secrets that reach a log line in clear through other shapes.
URL_PASSWORD = "Rc9fakeUrlPassword"
WEBHOOK_TOKEN = "Pb1fakeWebhookTokenAbCdEf"
BEARER_TOKEN = "Na0fakeBearerToken1234567"
QUERY_KEY = "Mz4fakeLastfmQueryKey99"

LOG_LINES = [config_line(k, v1004_mask(v), "sqlite") for k, v in SECRETS.items()] + [
    config_line("NAVIDROME_URL", "http://navidrome:4533", "env"),
    config_line("GOOGLE_API_KEY", "", "default"),
    "2026-09-27 21:14:09,001 INFO [scan] ping http://admin:%s@navidrome:4533/rest/ping.view" % URL_PASSWORD,
    "2026-09-27 21:14:10,002 WARNING [notify] POST https://discord.com/api/webhooks/123456789/%s failed: 404" % WEBHOOK_TOKEN,
    "2026-09-27 21:14:11,003 DEBUG [http] headers={'Authorization': 'Bearer %s'}" % BEARER_TOKEN,
    "2026-09-27 21:14:12,004 INFO [lastfm] GET https://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=%s&format=json" % QUERY_KEY,
    "2026-09-27 21:14:13,005 INFO [mirror] musicbrainz-mirror --token-file /config/managed-runtime/secrets/musicbrainz_replication_token.txt",
    "2026-09-27 21:14:14,006 INFO [http] Settings saved to settings.db: ['DISCOGS_USER_TOKEN', 'LASTFM_API_KEY']",
    "2026-09-27 21:14:15,007 INFO [scan] Enya - The Memory of Trees - Secret Garden (3 tracks)",
]

BUNDLE = {
    "kind": "pmda-support-bundle",
    "bundle_version": 4,
    "pmda_version": "v1004",
    "generated_at": "2026-09-27T21:15:00Z",
    "description": "music never leaves the intake folder",
    "anonymized": ["url credentials", "webhook tokens", "system usernames", "ip addresses", "email addresses"],
    "context": {"screen": "/settings/support", "settings": {
        "LASTFM_API_KEY": v1004_mask(SECRETS["LASTFM_API_KEY"]),
        "LASTFM_API_KEY_SET": True,
        "NAVIDROME_URL": "http://navidrome:4533",
    }},
    "duplicates": {"classification": {"EXACT_DUPE": 2}},
    "incompletes": [],
    "actionable_tracks": [],
    "inbox": {"albums": []},
    "scan": {"workflow_mode": "move", "toggles": {"USE_DISCOGS": True}},
    "recent_moves": [],
    "log_tail": LOG_LINES,
    "log_by_subsystem": {"startup": LOG_LINES[:10], "scan": LOG_LINES[10:]},
    "mirror": {},
}

# Every character sequence a secret showed in the bundle as sent.
VISIBLE = [v[:4] + "…" for v in SECRETS.values() if len(v) > 4] + [
    v[:4] for v in SECRETS.values() if len(v) > 4
] + [URL_PASSWORD, WEBHOOK_TOKEN, BEARER_TOKEN, QUERY_KEY]

# What is not a secret and must come through untouched.
KEPT = [
    config_line("NAVIDROME_URL", "http://navidrome:4533", "env"),
    config_line("GOOGLE_API_KEY", "", "default"),
    "--token-file /config/managed-runtime/secrets/musicbrainz_replication_token.txt",
    "Settings saved to settings.db: ['DISCOGS_USER_TOKEN', 'LASTFM_API_KEY']",
    "Secret Garden (3 tracks)",
    "&format=json",
]


def committed_through_intake(raw: bytes) -> bytes | None:
    """What intake._commit_bundle would PUT into the repository, or None."""
    captured = {}

    def fake_api(path, method="GET", body=None):
        captured["body"] = body
        return {}

    real = intake._api
    intake._api = fake_api
    try:
        intake._commit_bundle("1553806972388905003", raw)
    finally:
        intake._api = real
    body = captured.get("body")
    return base64.b64decode(body["content"]) if body else None


def main() -> int:
    bad = []
    sent = json.dumps(BUNDLE).encode("utf-8")
    # The fixture must actually carry what v1004 published, or the test
    # proves nothing.
    sent_decoded = json.dumps(BUNDLE, ensure_ascii=False)
    for i, seq in enumerate(VISIBLE):
        if seq not in sent_decoded:
            bad.append(f"fixture does not carry visible sequence #{i}")
    if not scrub.findings(BUNDLE):
        bad.append("detector finds nothing in a v1004-shaped bundle")

    out = committed_through_intake(sent)
    if out is None:
        bad.append("intake committed nothing for a valid bundle")
        out = b"{}"
    try:
        committed = json.loads(out.decode("utf-8"))
    except ValueError:
        bad.append("committed bundle is not valid JSON")
        committed = {}
    decoded = json.dumps(committed, ensure_ascii=False)
    raw = out.decode("utf-8")
    for i, seq in enumerate(VISIBLE):
        if seq in decoded or seq in raw:
            bad.append(f"visible secret sequence #{i} survived the intake (length {len(seq)})")
    if scrub.findings(committed):
        names = sorted({f"{r}:{k}" for r, k in scrub.findings(committed)})
        bad.append(f"detector still finds secrets after the intake: {names}")
    for key in SECRETS:
        line = next((ln for ln in committed.get("log_tail", []) if f"Config {key} " in ln), "")
        if scrub.SECRET_MASK not in line:
            bad.append(f"{key}: its Config line does not carry the fixed mask")
    if (committed.get("context") or {}).get("settings", {}).get("LASTFM_API_KEY") != scrub.SECRET_MASK:
        bad.append("a secret-named JSON key kept its value")
    if (committed.get("context") or {}).get("settings", {}).get("LASTFM_API_KEY_SET") is not True:
        bad.append("the _SET flag beside a secret was altered")
    for text in KEPT:
        if text not in decoded:
            bad.append(f"non-secret text was altered: {text[:60]!r}")
    for section in ("kind", "pmda_version", "duplicates", "scan"):
        if committed.get(section) != BUNDLE[section]:
            bad.append(f"section {section!r} changed")

    # Scrubbing twice changes nothing.
    if scrub.scrub_bundle_bytes(out) != out:
        bad.append("the scrub is not idempotent")

    # Fails closed: a bundle the scrub cannot vouch for is not committed.
    try:
        if committed_through_intake(b"not json: Config NAVIDROME_PASSWORD = Qz7!\xe2\x80\xa6") is not None:
            bad.append("a bundle the scrub could not vouch for was committed")
    except scrub.SecretSurvived as exc:
        if "Qz7" in str(exc):
            bad.append("the refusal message repeats a secret")

    # Every bundle already in this repository shows nothing.
    for path in sorted(glob.glob(os.path.join(HERE, "bundles", "*.json"))):
        with open(path, encoding="utf-8") as f:
            left = scrub.findings(json.load(f))
        if left:
            bad.append(f"{os.path.basename(path)}: {sorted({f'{r}:{k}' for r, k in left})}")

    for line in bad:
        print(f"FAIL {line}")
    if bad:
        print(f"\n{len(bad)} failing")
        return 1
    print(f"ok: a v1004-shaped bundle goes through the intake with none of {len(VISIBLE)} visible "
          f"secret sequences left; {len(KEPT)} non-secret texts kept; repository bundles clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
