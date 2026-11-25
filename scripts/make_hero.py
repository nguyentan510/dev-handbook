#!/usr/bin/env python3
"""Vẽ hình bản đồ luồng "Đặt hàng" (layer x module) cho README.

Chạy: python3 scripts/make_hero.py  ->  assets/hero-light.svg, assets/hero-dark.svg
Sửa dữ liệu trong STEPS và CELLS rồi chạy lại khi luồng thay đổi.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYERS = ["UI", "API", "Service", "Job nền", "Repository", "Database"]
MODS = ["Catalog", "Order", "Payment", "Auth", "Notify"]
CELLS = {
    "UI|Catalog": "Sản phẩm, giỏ", "UI|Order": "Đặt hàng", "UI|Payment": "Trang kết quả", "UI|Auth": "Đăng nhập",
    "API|Catalog": "GET /products", "API|Order": "POST /orders", "API|Payment": "Webhook", "API|Auth": "Xác thực",
    "Service|Catalog": "Giữ tồn kho", "Service|Order": "Tính tiền", "Service|Payment": "Gọi cổng", "Service|Auth": "Quyền sở hữu", "Service|Notify": "Soạn email",
    "Job nền|Catalog": "Nhả hàng", "Job nền|Payment": "Đối soát", "Job nền|Notify": "Gửi email",
    "Repository|Catalog": "Tồn có điều kiện", "Repository|Order": "Lưu đơn", "Repository|Payment": "Lưu giao dịch", "Repository|Auth": "Tìm user", "Repository|Notify": "Outbox",
    "Database|Catalog": "inventory", "Database|Order": "orders", "Database|Payment": "payments", "Database|Auth": "users", "Database|Notify": "outbox",
}
# (số bước, ô đại diện trên đường đi, mức rủi ro, tên ngắn, các ô khác bước này chạm tới)
STEPS = [
    (1, "UI|Order", "low", "Bấm đặt hàng", ["UI|Catalog"]),
    (2, "API|Order", "low", "Gửi request", []),
    (3, "API|Auth", "high", "Xác định người mua", ["Service|Auth", "Repository|Auth"]),
    (4, "Service|Order", "high", "Tính tiền", []),
    (5, "Repository|Order", "mid", "Giữ hàng, tạo đơn", ["Service|Catalog", "Repository|Catalog", "Repository|Payment", "Database|Catalog", "Database|Order", "Database|Payment"]),
    (6, "Service|Payment", "high", "Sang cổng thanh toán", ["UI|Payment"]),
    (7, "API|Payment", "high", "Nhận webhook", ["Service|Payment", "Repository|Payment", "Database|Payment", "Repository|Notify", "Database|Notify"]),
    (8, "Job nền|Payment", "high", "Đối soát", ["Job nền|Catalog"]),
    (9, "Job nền|Notify", "low", "Gửi email", ["Service|Notify"]),
]
PAL = {
    "light": dict(bg="#ffffff", ink="#16191b", mute="#5b6368", cell="#f3f5f6", line="#d5dadd", touch="#e3f3ec", touchline="#9fd4bd",
                  route="#0b7f56", low="#0b7f56", mid="#b06a00", high="#c02a40", halo="#ffffff"),
    "dark": dict(bg="#0d1117", ink="#e6e9eb", mute="#9aa3a9", cell="#161b22", line="#2b3238", touch="#132a20", touchline="#2f7a58",
                 route="#4cc795", low="#4cc795", mid="#e3a84e", high="#f2808e", halo="#0d1117"),
}
W, H = 1200, 556
LX, TY = 132, 96          # góc trên trái của lưới
CW, CH, GAP = 200, 62, 6  # kích thước ô
RISK = {"low": "Rủi ro thấp", "mid": "Rủi ro vừa", "high": "Rủi ro cao"}


def center(key):
    l, m = key.split("|")
    return LX + MODS.index(m) * (CW + GAP) + CW / 2, TY + LAYERS.index(l) * (CH + GAP) + CH / 2


def svg(theme):
    p = PAL[theme]
    labels = []
    touched = {s[1] for s in STEPS} | {k for s in STEPS for k in s[4]}
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Be Vietnam Pro, Segoe UI, system-ui, sans-serif">',
         f'<title>Bản đồ luồng Đặt hàng: 9 bước đi qua 6 layer và 5 module</title>',
         f'<rect width="{W}" height="{H}" rx="16" fill="{p["bg"]}"/>',
         f'<text x="{LX}" y="40" font-size="22" font-weight="700" fill="{p["ink"]}">Luồng "Đặt hàng" đi qua 6 layer × 5 module</text>',
         f'<text x="{LX}" y="66" font-size="14" fill="{p["mute"]}">Số là thứ tự bước. Màu là mức rủi ro, quyết định bạn giao việc cho AI đến đâu.</text>']
    for i, m in enumerate(MODS):
        o.append(f'<text x="{LX + i*(CW+GAP) + 10}" y="{TY - 10}" font-size="14" font-weight="700" fill="{p["ink"]}">{m}</text>')
    for j, l in enumerate(LAYERS):
        y = TY + j*(CH+GAP)
        o.append(f'<text x="{LX - 14}" y="{y + CH/2 + 5}" font-size="14" font-weight="600" text-anchor="end" fill="{p["mute"]}">{l}</text>')
        for i, m in enumerate(MODS):
            k, x = f"{l}|{m}", LX + i*(CW+GAP)
            on = k in touched
            o.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="9" fill="{p["touch"] if on else p["cell"]}" stroke="{p["touchline"] if on else p["line"]}"/>')
            if k in CELLS:
                labels.append(f'<text x="{x + 12}" y="{y + CH - 12}" font-size="13" fill="{p["ink"] if on else p["mute"]}" stroke="{p["touch"] if on else p["cell"]}" stroke-width="5" paint-order="stroke" stroke-linejoin="round">{CELLS[k]}</text>')
    pts = " ".join(f"{center(s[1])[0]:.0f},{center(s[1])[1] - 8:.0f}" for s in STEPS)
    o.append(f'<polyline points="{pts}" fill="none" stroke="{p["halo"]}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>')
    o.append(f'<polyline points="{pts}" fill="none" stroke="{p["route"]}" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round" opacity=".85"/>')
    o.extend(labels)
    for n, k, r, _, _ in STEPS:
        cx, cy = center(k)
        o.append(f'<circle cx="{cx:.0f}" cy="{cy - 8:.0f}" r="15" fill="{p[r]}" stroke="{p["halo"]}" stroke-width="3"/>')
        o.append(f'<text x="{cx:.0f}" y="{cy - 3:.0f}" font-size="14" font-weight="700" text-anchor="middle" fill="{p["bg"]}">{n}</text>')
    ly = TY + 6*(CH+GAP) + 22
    x = LX
    for r in ("low", "mid", "high"):
        o.append(f'<circle cx="{x + 7}" cy="{ly - 5}" r="7" fill="{p[r]}"/><text x="{x + 20}" y="{ly}" font-size="14" fill="{p["ink"]}">{RISK[r]}</text>')
        x += 140
    o.append(f'<rect x="{x}" y="{ly - 13}" width="16" height="16" rx="4" fill="{p["touch"]}" stroke="{p["touchline"]}"/><text x="{x + 24}" y="{ly}" font-size="14" fill="{p["ink"]}">Ô có bước đi qua</text>')
    o.append("</svg>")
    return "\n".join(o)


for t in PAL:
    open(os.path.join(ROOT, "assets", f"hero-{t}.svg"), "w", encoding="utf-8").write(svg(t))
print("Đã vẽ assets/hero-light.svg, assets/hero-dark.svg")
