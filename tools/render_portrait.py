"""
Map the cleaned portrait to a character grid, then emit an SVG where each
row is wrapped in its own clip rect that animates from width 0 -> full,
staggered ~40ms apart, so the portrait appears to draw itself top to bottom.
Single accent color only -- multi-color ASCII reads as noise.
"""
from PIL import Image, ImageOps

SRC = "assets/photo-ready.png"
OUT = "out/portrait.svg"

GLYPHS = " '.,:;~+*xXO#"   # light/empty -> dense/dark
ACCENT = "#70a5fd"          # tokyonight blue, matches sysinfo/graph accent

COLS = 78
CHAR_W = 7.2
CHAR_H = 13.5
ROW_DELAY = 0.04  # seconds between each row starting its draw-in


def main():
    im = Image.open(SRC).convert("L")
    w, h = im.size

    # monospace glyphs are taller than wide -- correct the aspect ratio so
    # the character grid maps back to a natural-looking portrait
    char_aspect = CHAR_W / CHAR_H
    rows = max(1, round((h / w) * COLS * char_aspect))
    small = im.resize((COLS, rows), Image.LANCZOS)

    # extra contrast push so the white background reliably lands on the
    # emptiest glyph and skin/hair/guitar shadow reliably lands on the densest
    small = ImageOps.autocontrast(small, cutoff=2)
    pixels = small.load()

    n = len(GLYPHS) - 1
    grid = []
    for y in range(rows):
        row_chars = []
        for x in range(COLS):
            v = pixels[x, y] / 255.0
            idx = min(n, int((1 - v) * (n + 1)))
            row_chars.append(GLYPHS[idx])
        grid.append("".join(row_chars))

    svg_w = COLS * CHAR_W + 20
    svg_h = rows * CHAR_H + 20

    svg = []
    svg.append(
        f'<svg viewBox="0 0 {svg_w:.1f} {svg_h:.1f}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="JetBrains Mono, SFMono-Regular, Consolas, monospace">'
    )
    svg.append(f'<rect width="100%" height="100%" fill="none" />')
    svg.append(
        f'<style>.arow{{fill:{ACCENT};font-size:{CHAR_H * 0.92:.1f}px;'
        f'white-space:pre;letter-spacing:0px;}}</style>'
    )

    for i, row in enumerate(grid):
        y = 14 + i * CHAR_H
        row_w = COLS * CHAR_W
        clip_id = f"rowclip{i}"
        delay = round(i * ROW_DELAY, 3)
        escaped = (
            row.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        svg.append(f'<clipPath id="{clip_id}">')
        svg.append(
            f'<rect x="10" y="{y - CHAR_H + 2:.1f}" width="0" height="{CHAR_H:.1f}">'
            f'<animate attributeName="width" from="0" to="{row_w:.1f}" '
            f'begin="{delay}s" dur="0.5s" fill="freeze" calcMode="spline" '
            f'keySplines="0.2 0 0.2 1" />'
            f'</rect>'
        )
        svg.append('</clipPath>')
        svg.append(f'<g clip-path="url(#{clip_id})">')
        svg.append(f'<text class="arow" x="10" y="{y:.1f}" xml:space="preserve">{escaped}</text>')
        svg.append('</g>')

    svg.append('</svg>')

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"wrote {OUT} ({COLS}x{rows} chars, {svg_w:.0f}x{svg_h:.0f}px)")


if __name__ == "__main__":
    main()
