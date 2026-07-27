"""
Redraw the contribution calendar as a hand-rolled, self-animating SVG grid.
No badge service involved -- the data comes from assets/contributions.json
(written by pull_contributions.py) and every square/animation is generated
here as plain SVG + SMIL, matching the tokyonight blue/purple accent already
used across the profile.
"""
import json

DATA_PATH = "assets/contributions.json"
OUT_PATH = "graph.svg"

# empty -> top intensity, tokyonight blue/purple ramp
LEVELS = ["#161b22", "#24345e", "#2f5aa8", "#70a5fd", "#bf91f3"]

CELL = 11
GAP = 3
STEP = CELL + GAP
MARGIN_L = 28
MARGIN_T = 14
LEGEND_H = 22
STATS_H = 26

MONTH_ABBR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def month_labels(days):
    """Return {week_index: 'Mon'} for the first week each new month appears in."""
    labels = {}
    seen_months = set()
    for d in days:
        y, m, _ = d["date"].split("-")
        key = (y, m)
        if key not in seen_months:
            seen_months.add(key)
            labels[d["week"]] = MONTH_ABBR[int(m) - 1]
    return labels


def main():
    data = json.load(open(DATA_PATH))
    days = data["days"]
    n_weeks = max(d["week"] for d in days) + 1

    width = MARGIN_L + n_weeks * STEP + GAP
    height = MARGIN_T + 7 * STEP + LEGEND_H + STATS_H

    labels = month_labels(days)

    svg = []
    svg.append(
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="JetBrains Mono, SFMono-Regular, Consolas, monospace">'
    )
    svg.append(
        '<style>'
        '.gcell{stroke:rgba(255,255,255,0.04);stroke-width:1;}'
        '.mlabel{fill:#8b949e;font-size:9px;}'
        '.legend-label{fill:#8b949e;font-size:9px;}'
        '.stats{fill:#c9d1d9;font-size:11px;}'
        '.stats .accent{fill:#70a5fd;}'
        '</style>'
    )

    # month labels along the top
    for week, label in labels.items():
        x = MARGIN_L + week * STEP
        svg.append(f'<text class="mlabel" x="{x}" y="{MARGIN_T - 4}">{label}</text>')

    # weekday row squares, animated in column-by-column (per week)
    for d in days:
        week, wd, level = d["week"], d["weekday"], d["level"]
        x = MARGIN_L + week * STEP
        y = MARGIN_T + wd * STEP
        color = LEVELS[level]
        delay = round(week * 0.028, 3)
        title = f"{d['count']} contributions on {d['date']}"
        svg.append(
            f'<rect class="gcell" x="{x}" y="{y}" width="{CELL}" height="{CELL}" '
            f'rx="2.5" ry="2.5" fill="{color}" opacity="0">'
            f'<title>{title}</title>'
            f'<animate attributeName="opacity" from="0" to="1" '
            f'begin="{delay}s" dur="0.35s" fill="freeze" />'
            f'<animateTransform attributeName="transform" type="scale" '
            f'from="0.4" to="1" begin="{delay}s" dur="0.35s" '
            f'additive="sum" fill="freeze" />'
            f'</rect>'
        )

    # legend: Less [swatches] More
    ly = MARGIN_T + 7 * STEP + 14
    lx = MARGIN_L
    svg.append(f'<text class="legend-label" x="{lx}" y="{ly + 8}">Less</text>')
    lx += 32
    for i, color in enumerate(LEVELS):
        svg.append(
            f'<rect class="gcell" x="{lx + i * (CELL + 3)}" y="{ly}" '
            f'width="{CELL}" height="{CELL}" rx="2.5" ry="2.5" fill="{color}" />'
        )
    lx += len(LEVELS) * (CELL + 3) + 6
    svg.append(f'<text class="legend-label" x="{lx}" y="{ly + 8}">More</text>')

    # stats line
    sy = ly + LEGEND_H + 4
    stats_text = (
        f'<tspan class="accent">{data["total_contributions"]}</tspan> contributions this year   '
        f'\u00b7   current streak <tspan class="accent">{data["current_streak"]}d</tspan>'
        f'   \u00b7   longest streak <tspan class="accent">{data["longest_streak"]}d</tspan>'
        f'   \u00b7   busiest day <tspan class="accent">{data["busiest_day"]}</tspan>'
    )
    svg.append(f'<text class="stats" x="{MARGIN_L}" y="{sy}">{stats_text}</text>')

    svg.append('</svg>')

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"wrote {OUT_PATH} ({width}x{height}, {n_weeks} weeks)")


if __name__ == "__main__":
    main()
