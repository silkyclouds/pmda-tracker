"""No character of a secret reaches the public tracker.

PMDA builds up to v1004 masked a secret setting by keeping its first four
characters ("abcd…"), and the startup config dump in pmda.log went through
that mask. Every support bundle carries a log tail, so every bundle an old
client sends holds the start of the Navidrome password and of each API key.
v1005 writes one fixed marker instead, but old clients keep sending, and this
repository is public: the intake scrubs a bundle before it commits it.

The rules are PMDA's own (pmda_core/config.py SECRET_SCRUB_PATTERNS, v1005),
plus the credential shapes a log line can carry in a URL or a header:

- the value of a secret setting in a "Config KEY = value (source: ...)" line
  becomes SECRET_MASK, the fixed marker v1005 shows for every secret;
- any "Config" value still in the old four-character mask shape, whatever
  its key is called;
- credentials in a URL (user:pass@host) and Discord-style webhook tokens,
  replaced exactly as v1005's bundle scrubber replaces them;
- "Bearer <token>", and the value of a secret query parameter or key=value
  pair (token=, api_key=, password=, secret=, ...);
- a JSON key named like a secret, when its value is a string.

Nothing here reads a secret back or logs one: `findings` returns rule and
key names only.
"""

from __future__ import annotations

import json
import re
from typing import Any

#: What v1005 shows for any set secret (pmda_core/config.py SECRET_MASK).
SECRET_MASK = "•" * 8

#: PMDA's own name rule (pmda_core/config.py SENSITIVE_KEY_MARKERS, v1005).
SENSITIVE_KEY_MARKERS = ("TOKEN", "API_KEY", "SECRET", "PASSWORD", "WEBHOOK", "APPRISE", "SESSION_KEY")

# Names PMDA's rule does not cover but a credential goes by elsewhere.
_EXTRA_SECRET_NAME = re.compile(r"APIKEY|PASSWD|CREDENTIAL|PRIVATE_KEY|(?:^|_)(?:PASS|PWD)(?:_|$)")

# Values that carry no character of a secret.
_NO_SECRET_VALUES = {"", "none", "null", "<secret>", "<token>", "<credentials>", SECRET_MASK}

# The pre-v1005 mask: up to four characters of the value, then an ellipsis.
_OLD_MASK_SHAPE = re.compile(r"\S{1,4}…")

_CONFIG_LINE = re.compile(
    r"(?P<head>\bConfig\s+(?P<key>[A-Za-z0-9_]+)\s*=[ \t]*)"
    r"(?!\(source:)(?P<val>[^\n]*?)"
    r"(?P<tail>[ \t]+\(source:[^\n]*)?$",
    re.MULTILINE,
)

_URL_CREDENTIALS = re.compile(r"://[^/\s:@\"']+:[^/\s@\"']+@")
_WEBHOOK_TOKEN = re.compile(r"(/api/webhooks/)[^\s\"')]+", re.IGNORECASE)
_BEARER = re.compile(r"(\bBearer[ \t]+|\bAuthorization[\"']?[ \t]*[:=][ \t]*[\"']?(?:Bot|Token|Basic)[ \t]+)([A-Za-z0-9._~+/=-]{8,})", re.IGNORECASE)
_SECRET_PARAM = re.compile(
    r"(?P<head>(?<![A-Za-z0-9])(?P<name>[A-Za-z0-9_.-]*?"
    r"(?:api[_-]?key|apikey|access[_-]?token|auth[_-]?token|refresh[_-]?token|session[_-]?key"
    r"|token|password|passwd|pwd|secret|x-plex-token|api[_-]?sig)"
    r")[\"']?[ \t]*(?P<sep>=|:)[ \t]*(?P<quote>[\"']?))"
    r"(?P<val>(?![(<])[^\s&\"',;)}\]]+)",
    re.IGNORECASE,
)


def key_is_secret(name: str) -> bool:
    """True when a setting or JSON key of this name holds a credential."""

    upper = str(name or "").upper()
    if upper.endswith("_SET"):
        return False
    return any(m in upper for m in SENSITIVE_KEY_MARKERS) or bool(_EXTRA_SECRET_NAME.search(upper))


def _carries_characters(value: str) -> bool:
    v = str(value or "").strip()
    if v.lower() in _NO_SECRET_VALUES:
        return False
    if set(v) <= {"*", "•"}:
        return False
    return True


def _is_old_mask(value: str) -> bool:
    return bool(_OLD_MASK_SHAPE.fullmatch(str(value or "").strip()))


def _config_line_sub(match: re.Match, hits: list | None) -> str:
    key, val = match.group("key"), match.group("val")
    stripped = val.strip()
    if not stripped:
        return match.group(0)
    secret_named = key_is_secret(key)
    if not (secret_named or _is_old_mask(stripped)):
        return match.group(0)
    if stripped == SECRET_MASK:
        return match.group(0)
    if stripped.lower() in {"none", "null"} and secret_named:
        return match.group(0)
    if hits is not None:
        if _is_old_mask(stripped):
            kind = "config-value-prefix"
        elif _carries_characters(stripped):
            kind = "config-value-clear"
        else:
            kind = "config-value-length-mask"
        hits.append((kind, key))
    return match.group("head") + SECRET_MASK + (match.group("tail") or "")


def _param_sub(match: re.Match, hits: list | None) -> str:
    val = match.group("val")
    if not _carries_characters(val) or val.startswith("<"):
        return match.group(0)
    # Prose ("replication token: configured") is not a value: after a colon
    # only a quoted value counts. After "=" (a query string, a key=value log
    # field) any value does, except a path.
    if match.group("sep") == ":" and not match.group("quote"):
        return match.group(0)
    if not match.group("quote") and val.startswith("/"):
        return match.group(0)
    if hits is not None:
        hits.append(("secret-parameter", match.group("name").lower()))
    return match.group("head") + SECRET_MASK


def scrub_text(text: str, hits: list | None = None) -> str:
    """The text with every secret shape replaced. `hits` collects (rule, name)."""

    out = str(text)

    def _url(m: re.Match) -> str:
        if hits is not None:
            hits.append(("url-credentials", "user:pass@host"))
        return "://<credentials>@"

    def _hook(m: re.Match) -> str:
        if m.group(0).endswith("<token>"):
            return m.group(0)
        if hits is not None:
            hits.append(("webhook-token", "/api/webhooks/"))
        return m.group(1) + "<token>"

    def _bearer(m: re.Match) -> str:
        if hits is not None:
            hits.append(("authorization-header", m.group(1).strip()))
        return m.group(1) + SECRET_MASK

    out = _URL_CREDENTIALS.sub(lambda m: m.group(0) if m.group(0) == "://<credentials>@" else _url(m), out)
    out = _WEBHOOK_TOKEN.sub(_hook, out)
    out = _CONFIG_LINE.sub(lambda m: _config_line_sub(m, hits), out)
    out = _BEARER.sub(_bearer, out)
    out = _SECRET_PARAM.sub(lambda m: _param_sub(m, hits), out)
    return out


def scrub_value(value: Any, hits: list | None = None, key: str | None = None) -> Any:
    """The same scrub over a parsed bundle, in any nesting."""

    if isinstance(value, str):
        if key is not None and key_is_secret(key) and _carries_characters(value):
            if hits is not None:
                hits.append(("json-key", key))
            return SECRET_MASK
        return scrub_text(value, hits)
    if isinstance(value, list):
        return [scrub_value(v, hits) for v in value]
    if isinstance(value, dict):
        return {k: scrub_value(v, hits, key=k) for k, v in value.items()}
    return value


_JSON_STRING = re.compile(r'"(?:[^"\\]|\\.)*"')


def scrub_json_text(raw: str, hits: list | None = None) -> str:
    """Scrub a serialized bundle in place, string literal by string literal.

    Only the strings that change are re-encoded, so every other byte of the
    file stays as it was; the result parses to scrub_value(json.loads(raw)).
    """

    out: list[str] = []
    pos = 0
    key: str | None = None
    key_end = -1
    for m in _JSON_STRING.finditer(raw):
        token = m.group(0)
        j = m.end()
        while j < len(raw) and raw[j] in " \t\r\n":
            j += 1
        if j < len(raw) and raw[j] == ":":
            try:
                key = json.loads(token)
            except ValueError:
                key = None
            key_end = j + 1
            continue
        try:
            value = json.loads(token)
        except ValueError:
            continue
        owner = key if (key is not None and raw[key_end:m.start()].strip() == "") else None
        new = scrub_value(value, hits, key=owner)
        key = None
        if new != value:
            out.append(raw[pos:m.start()])
            out.append(json.dumps(new))
            pos = m.end()
    out.append(raw[pos:])
    return "".join(out)


def findings(obj: Any) -> list[tuple[str, str]]:
    """(rule, key name) for every secret still visible in a parsed bundle."""

    hits: list[tuple[str, str]] = []
    scrub_value(obj, hits)
    return hits


class SecretSurvived(ValueError):
    """A bundle still showed a secret after the scrub. Carries no value."""


def scrub_bundle_bytes(data: bytes) -> bytes:
    """What the intake commits: the bundle with no secret character left.

    Fails closed. A bundle that does not parse after the scrub, or in which
    the detector still finds a secret, raises SecretSurvived and is not
    committed; the message names the rules and keys, never a value.
    """

    text = data.decode("utf-8", errors="replace")
    scrubbed = scrub_json_text(text)
    try:
        obj = json.loads(scrubbed)
    except ValueError as exc:
        raise SecretSurvived("bundle is not JSON after the scrub") from exc
    left = findings(obj)
    if left:
        names = ", ".join(sorted({f"{rule}:{key}" for rule, key in left}))
        raise SecretSurvived(f"a secret survived the scrub ({names}); bundle not committed")
    return scrubbed.encode("utf-8")
