"""
Pull GitHub's public contribution-calendar HTML fragment (no token needed --
this is the same markup https://github.com/<user> itself consumes) and parse
it into structured JSON: per-day level/count, current & longest streak, and a
busiest-day-of-week breakdown.
"""
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime

import httpx
from lxml import html as lhtml

GITHUB_USERNAME = os.environ.get("GITHUB_USERNAME", "G-Deepak-05")
CONTRIB_URL = f"https://github.com/users/{GITHUB_USERNAME}/contributions"
OUT_PATH = "assets/contributions.json"

COUNT_RE = re.compile(r"^(No|\d+)\s+contributions?", re.IGNORECASE)


def parse_count(tooltip_text: str) -> int:
    tooltip_text = tooltip_text.strip()
    m = COUNT_RE.match(tooltip_text)
    if not m:
        return 0
    token = m.group(1)
    return 0 if token.lower() == "no" else int(token)


def main():
    resp = httpx.get(
        CONTRIB_URL,
        headers={"User-Agent": "Mozilla/5.0 (living-terminal-readme-bot)"},
        timeout=20,
        follow_redirects=True,
    )
    resp.raise_for_status()
    doc = lhtml.fromstring(resp.text)

    cells = doc.xpath('//td[contains(@class,"ContributionCalendar-day")]')
    tooltips = {
        t.get("for"): (t.text_content() or "")
        for t in doc.xpath('//tool-tip[@for]')
    }

    days = []
    for td in cells:
        date_str = td.get("data-date")
        if not date_str:
            continue
        level = int(td.get("data-level", "0"))
        cell_id = td.get("id") or ""
        count = parse_count(tooltips.get(cell_id, ""))
        days.append({"date": date_str, "level": level, "count": count})

    days.sort(key=lambda d: d["date"])

    # GitHub's calendar always starts the range on a Sunday, so the list is a
    # contiguous run of days beginning at weekday 0 -- grid coords are just
    # the running index, no need to trust the DOM's own week/day numbering.
    first_weekday = datetime.strptime(days[0]["date"], "%Y-%m-%d").isoweekday() % 7
    assert first_weekday == 0, "expected calendar to start on a Sunday"
    for i, d in enumerate(days):
        d["week"] = i // 7
        d["weekday"] = i % 7

    # streaks
    longest = 0
    current = 0
    running = 0
    today = days[-1]["date"] if days else None
    for d in days:
        if d["count"] > 0:
            running += 1
            longest = max(longest, running)
        else:
            running = 0
    # current streak = trailing run ending at the most recent day with data
    for d in reversed(days):
        if d["count"] > 0:
            current += 1
        else:
            break

    dow_totals = defaultdict(int)
    for d in days:
        wd = datetime.strptime(d["date"], "%Y-%m-%d").strftime("%A")
        dow_totals[wd] += d["count"]
    busiest_day = max(dow_totals, key=dow_totals.get) if dow_totals else None

    total = sum(d["count"] for d in days)

    out = {
        "total_contributions": total,
        "current_streak": current,
        "longest_streak": longest,
        "busiest_day": busiest_day,
        "days": days,
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print(f"total={total} current_streak={current} longest_streak={longest} busiest={busiest_day}")
    print(f"wrote {OUT_PATH} ({len(days)} days)")


if __name__ == "__main__":
    main()
