"""
A small terminal "system info" panel -- not trying to mimic a real CLI tool's
output, just its own labeled-rows design. This is where context that the
contribution graph can't show lives: what's actually being worked on right
now, not just how often commits land.
"""

OUT = "sysinfo.svg"

BG = "#0d1117"
PANEL_BG = "#161b22"
BORDER = "#2f3b52"
HEADER_TXT = "#c9d1d9"
LABEL = "#8b949e"
VALUE = "#c9d1d9"
ACCENT_BLUE = "#70a5fd"
ACCENT_PURPLE = "#bf91f3"
DOT_COLORS = ["#f77669", "#e5c07b", "#9ece6a"]

ROWS = [
    ("user", "G-Deepak-05"),
    ("role", "Backend Engineer"),
    ("focus", "Distributed Systems"),
    ("stack", "Java 17 \u00b7 Go \u00b7 Kafka \u00b7 K8s"),
    ("now", "Building a distributed KV store in Go"),
]

W = 460
HEADER_H = 34
ROW_H = 30
PAD_X = 18
TOP_PAD = 14
BOTTOM_PAD = 14
H = HEADER_H + TOP_PAD + len(ROWS) * ROW_H + BOTTOM_PAD

ROW_DELAY = 0.28
ROW_DUR = 0.35


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    svg = []
    svg.append(
        f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'font-family="JetBrains Mono, SFMono-Regular, Consolas, monospace">'
    )
    svg.append(
        '<style>'
        f'.panel{{fill:{PANEL_BG};stroke:{BORDER};stroke-width:1.2;}}'
        f'.hdrtxt{{fill:{HEADER_TXT};font-size:12px;}}'
        f'.label{{fill:{LABEL};font-size:12.5px;}}'
        f'.value{{fill:{VALUE};font-size:12.5px;}}'
        f'.rowline{{stroke:{BORDER};stroke-width:1;}}'
        '</style>'
    )

    # panel background + border
    svg.append(f'<rect class="panel" x="1" y="1" width="{W - 2}" height="{H - 2}" rx="8" ry="8" />')

    # header bar
    svg.append(f'<rect x="1" y="1" width="{W - 2}" height="{HEADER_H}" rx="8" ry="8" fill="{BORDER}" opacity="0.35" />')
    svg.append(f'<rect x="1" y="{HEADER_H - 7}" width="{W - 2}" height="7" fill="{PANEL_BG}" />')
    cx = PAD_X
    for c in DOT_COLORS:
        svg.append(f'<circle cx="{cx}" cy="{HEADER_H / 2 + 1}" r="4.2" fill="{c}" />')
        cx += 14
    svg.append(f'<text class="hdrtxt" x="{W / 2}" y="{HEADER_H / 2 + 5}" text-anchor="middle">sysinfo</text>')

    # rows, each fades + slides in, staggered
    y0 = HEADER_H + TOP_PAD
    label_x = PAD_X
    value_x = PAD_X + 92

    for i, (label, value) in enumerate(ROWS):
        row_y = y0 + i * ROW_H
        text_y = row_y + ROW_H * 0.62
        delay = round(0.3 + i * ROW_DELAY, 3)
        g_id = f"row{i}"
        svg.append(f'<g id="{g_id}" opacity="0">')
        svg.append(
            f'<animate xlink:href="#{g_id}" attributeName="opacity" '
            f'from="0" to="1" begin="{delay}s" dur="{ROW_DUR}s" fill="freeze" />'
        )
        svg.append(
            f'<animateTransform xlink:href="#{g_id}" attributeName="transform" '
            f'type="translate" from="-10 0" to="0 0" begin="{delay}s" '
            f'dur="{ROW_DUR}s" fill="freeze" calcMode="spline" keySplines="0.2 0 0.2 1" />'
        )
        svg.append(f'<text class="label" x="{label_x}" y="{text_y}">{esc(label)}</text>')
        svg.append(f'<text class="value" x="{value_x}" y="{text_y}">{esc(value)}</text>')
        # blinking cursor on the very last row only, appears once its row lands
        if i == len(ROWS) - 1:
            cursor_delay = round(delay + ROW_DUR, 3)
            cursor_x = value_x + len(value) * 7.7 + 4
            svg.append(
                f'<rect x="{cursor_x:.1f}" y="{text_y - 11:.1f}" width="7" height="13" '
                f'fill="{ACCENT_BLUE}" opacity="0">'
                f'<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.01;0.5;0.51;1" '
                f'begin="{cursor_delay}s" dur="1s" repeatCount="indefinite" />'
                f'</rect>'
            )
        svg.append('</g>')
        if i < len(ROWS) - 1:
            svg.append(
                f'<line class="rowline" x1="{PAD_X}" y1="{row_y + ROW_H - 3}" '
                f'x2="{W - PAD_X}" y2="{row_y + ROW_H - 3}" opacity="0.4" />'
            )

    svg.append('</svg>')

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
