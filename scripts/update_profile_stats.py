#!/usr/bin/env python3
"""
Refresh the live Job Observatory numbers in this profile README.

How it works:
- Fetches one JSON file from the live site (the source of truth).
  Default: https://jobobservatory.dev/api/profile-stats.json
  Override with PROFILE_STATS_URL env var for testing.
- Rewrites ONLY the text between these markers in README.md:
    <!-- OBSERVATORY_STATS:START --> ... <!-- OBSERVATORY_STATS:END -->
    <!-- OBSERVATORY_INSIGHTS:START --> ... <!-- OBSERVATORY_INSIGHTS:END -->
  and the number inside any inline board-count marker:
    <!--PROFILE:boards-->51<!--/PROFILE:boards-->
  (the comments are invisible when the page renders; only the number
  between them is shown, and it always matches boards_enabled)
- Regenerates assets/projects/job-observatory-stats.svg from the same JSON,
  so the stats card image never goes stale either.
- Safety: if the fetch fails, a field is missing, or a number looks
  impossible (negative, coverage over 100%), it exits non-zero and
  changes nothing. The last good numbers stay up.
- If nothing changed, it exits 0 without touching the files, so the
  GitHub Action only commits when the numbers actually moved.

Expected JSON shape (produced by the Job Observatory publish step):
{
  "boards_enabled": 51,
  "open_jobs": 148,
  "employers_with_open_jobs": 29,
  "kept_jobs_total": 259,
  "extracted_jobs": 166,
  "extracted_total": 167,
  "junior_pct": 10,
  "senior_pct": 84,
  "genai_pct": 27,
  "last_published_at": "2026-11-05"
}
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
STATS_SVG = ROOT / "assets" / "projects" / "job-observatory-stats.svg"
DEFAULT_URL = "https://jobobservatory.dev/api/profile-stats.json"

REQUIRED = [
    "boards_enabled", "open_jobs", "employers_with_open_jobs",
    "kept_jobs_total", "extracted_jobs", "extracted_total",
    "junior_pct", "senior_pct", "genai_pct", "last_published_at",
]


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "profile-stats-bot"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def validate(d: dict) -> None:
    missing = [k for k in REQUIRED if k not in d]
    if missing:
        raise ValueError(f"missing fields: {missing}")
    if d["boards_enabled"] <= 0 or d["open_jobs"] < 0:
        raise ValueError("impossible board/open-job counts")
    if d["extracted_total"] > 0:
        cov = d["extracted_jobs"] / d["extracted_total"]
        if cov > 1:
            raise ValueError("extraction coverage over 100%")
    for k in ("junior_pct", "senior_pct", "genai_pct"):
        if not (0 <= d[k] <= 100):
            raise ValueError(f"{k} out of range: {d[k]}")


def stats_block(d: dict) -> str:
    cov_pct = round(100 * d["extracted_jobs"] / d["extracted_total"]) if d["extracted_total"] else 0
    return (
        f"{d['boards_enabled']} employer boards checked twice a day · "
        f"{d['open_jobs']} open jobs tracked right now · "
        f"{d['kept_jobs_total']} jobs kept in total · "
        f"requirements extracted on {d['extracted_jobs']} of {d['extracted_total']} kept postings ({cov_pct}%) · "
        f"updated {d['last_published_at']}"
    )


def insights_block(d: dict) -> str:
    return (
        f"Of the {d['open_jobs']} open data, analytics, and software jobs I track in Dallas-Fort Worth, "
        f"Houston, and remote-for-Texas ({d['employers_with_open_jobs']} employers, collected through "
        f"{d['last_published_at']}), only {d['junior_pct']}% of those with a clear level are junior and "
        f"{d['senior_pct']}% are senior or above. {d['genai_pct']}% mention generative AI. "
        f"It is a small group of employers and a single snapshot, so it describes these listings, "
        f"not the whole market."
    )


def fill_boards(text: str, boards_enabled: int) -> str:
    """Rewrite the number inside every inline board-count marker."""
    pattern = re.compile(r"(<!--PROFILE:boards-->)\d+(<!--/PROFILE:boards-->)")
    return pattern.sub(lambda m: f"{m.group(1)}{boards_enabled}{m.group(2)}", text)


def replace_block(text: str, name: str, new_body: str) -> str:
    pattern = re.compile(
        rf"(<!-- {name}:START -->).*?(<!-- {name}:END -->)", re.DOTALL
    )
    if not pattern.search(text):
        print(f"note: no {name} markers in README yet, skipping that block")
        return text
    return pattern.sub(lambda m: f"{m.group(1)}\n{new_body}\n{m.group(2)}", text, count=1)


def stats_svg(d: dict) -> str:
    items = [
        ("Boards tracked", str(d["boards_enabled"])),
        ("Open jobs now", str(d["open_jobs"])),
        ("Employers", str(d["employers_with_open_jobs"])),
        ("Updated", str(d["last_published_at"])),
    ]
    cells = ""
    for i, (label, value) in enumerate(items):
        x = 20 + i * 290
        cells += (
            f'<text x="{x}" y="52" font-family="Arial, sans-serif" font-size="30" '
            f'font-weight="bold" fill="#ffffff">{value}</text>'
            f'<text x="{x}" y="80" font-family="Arial, sans-serif" font-size="16" '
            f'fill="#cfe3ea">{label}</text>'
        )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="100" viewBox="0 0 1200 100">'
        '<rect width="1200" height="100" rx="12" fill="#0B1F3A"/>'
        f"{cells}</svg>\n"
    )


def main() -> int:
    url = os.environ.get("PROFILE_STATS_URL", DEFAULT_URL)
    try:
        data = fetch(url)
        validate(data)
    except Exception as e:
        print(f"fetch/validate failed, leaving README unchanged: {e}", file=sys.stderr)
        return 1

    original = README.read_text(encoding="utf-8")
    updated = replace_block(original, "OBSERVATORY_STATS", stats_block(data))
    updated = replace_block(updated, "OBSERVATORY_INSIGHTS", insights_block(data))
    updated = fill_boards(updated, data["boards_enabled"])

    changed = False
    if updated != original:
        README.write_text(updated, encoding="utf-8")
        changed = True

    svg = stats_svg(data)
    if not STATS_SVG.exists() or STATS_SVG.read_text(encoding="utf-8") != svg:
        STATS_SVG.parent.mkdir(parents=True, exist_ok=True)
        STATS_SVG.write_text(svg, encoding="utf-8")
        changed = True

    print("updated" if changed else "no change")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
