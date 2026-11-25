#!/usr/bin/env python3
"""Vẽ logo dev-handbook.

Ý tưởng: lưới 3 × 3 là layer × module; đường gấp khúc là một luồng tính năng đi
xuyên qua các tầng, bắt đầu ở UI và kết thúc ở dữ liệu.

Chạy: python3 scripts/make_logo.py [đường-dẫn-font.woff2]
Font chữ: Be Vietnam Pro 700. Chữ được đổi thành đường nét nên SVG hiển thị
giống nhau ở mọi nơi (GitHub, trình duyệt) mà không cần cài font.
"""
import os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets")
GREEN = {"light": "#0b7f56", "dark": "#3fbf8a"}
INK = {"light": "#16191b", "dark": "#e6e9eb"}
MUTE = {"light": "#5b6368", "dark": "#9aa3a9"}


def mark(x=0, y=0, s=64, bg="#0b7f56"):
    """Biểu tượng vuông, cạnh s, góc trên trái (x, y)."""
    k = s / 64
    cells = []
    for r in range(3):
        for c in range(3):
            cx, cy = 14 + c * 18, 14 + r * 18
            cells.append(f'<rect x="{x + (cx - 5) * k:.2f}" y="{y + (cy - 5) * k:.2f}" width="{10 * k:.2f}" height="{10 * k:.2f}" rx="{3 * k:.2f}" fill="#ffffff" fill-opacity=".28"/>')
    # đường đi: (cột 1, hàng 0) -> (1, 1) -> (2, 1) -> (2, 2)
    pts = [(32, 14), (32, 32), (50, 32), (50, 50)]
    d = "M" + " L".join(f"{x + px * k:.2f} {y + py * k:.2f}" for px, py in pts)
    return (f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{15 * k:.2f}" fill="{bg}"/>' + "".join(cells) +
            f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="{6 * k:.2f}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="{x + 32 * k:.2f}" cy="{y + 14 * k:.2f}" r="{6.5 * k:.2f}" fill="#ffffff"/>'
            f'<circle cx="{x + 50 * k:.2f}" cy="{y + 50 * k:.2f}" r="{6.5 * k:.2f}" fill="#ffffff"/>'
            f'<circle cx="{x + 50 * k:.2f}" cy="{y + 50 * k:.2f}" r="{2.6 * k:.2f}" fill="{bg}"/>')


def text_path(font, text, x, baseline, size):
    gs, cmap = font.getGlyphSet(), font.getBestCmap()
    upm = font["head"].unitsPerEm
    hmtx = font["hmtx"]
    scale = size / upm
    pen = SVGPathPen(gs)
    cur = 0
    for ch in text:
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (scale, 0, 0, -scale, x + cur * scale, baseline))
        gs[g].draw(tp)
        cur += hmtx[g][0]
    return pen.getCommands(), cur * scale


def main():
    font_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/fnt/package/files/be-vietnam-pro-latin-700-normal.woff2"
    font = TTFont(font_path)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "logo-mark.svg"), "w").write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64"><title>dev-handbook</title>' + mark() + "</svg>")
    for t in ("light", "dark"):
        d1, w1 = text_path(font, "dev-", 0, 0, 40)
        d2, w2 = text_path(font, "handbook", 0, 0, 40)
        W = 64 + 18 + w1 + w2 + 4
        dev, hb = text_path(font, "dev-", 82, 45, 40)[0], text_path(font, "handbook", 82 + w1, 45, 40)[0]
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} 64" width="{W:.0f}" height="64"><title>dev-handbook</title>'
               + mark(bg=GREEN[t]) + f'<path d="{dev}" fill="{GREEN[t]}"/><path d="{hb}" fill="{INK[t]}"/></svg>')
        open(os.path.join(OUT, f"logo-{t}.svg"), "w").write(svg)
    print("Đã vẽ assets/logo-mark.svg, assets/logo-light.svg, assets/logo-dark.svg")


if __name__ == "__main__":
    main()
