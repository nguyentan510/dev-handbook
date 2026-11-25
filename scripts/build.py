#!/usr/bin/env python3
"""Dựng trang web từ các file Markdown của dev-handbook.

Chạy từ gốc repo:  python3 scripts/build.py
Cần:               pip install markdown
Kết quả:           site/content.js (mở site/index.html để xem)

Script cũng kiểm tra: frontmatter đủ trường, id không trùng, link .md không hỏng,
mọi file đều có trong menu, trang nào đã quá ngày review_by.
"""
import datetime, json, os, posixpath, re, sys
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Thứ tự menu. Thêm trang mới thì thêm đường dẫn vào đúng nhóm.
NAV = [
    ("Bắt đầu", ["README.md", "00-lo-trinh/README.md", "00-lo-trinh/l1-nhap-mon.md",
                 "00-lo-trinh/l2-thiet-ke-mvp.md", "00-lo-trinh/l3-production.md"]),
    ("Hướng dẫn học", ["01-tutorials/luong-dat-hang.md", "01-tutorials/l2/README.md",
                       "01-tutorials/l2/catalog.md", "01-tutorials/l2/order.md", "01-tutorials/l2/payment.md",
                       "01-tutorials/l2/auth.md", "01-tutorials/l2/notify.md"]),
    ("Cách làm", ["02-how-to/lap-roadmap-mvp.md", "02-how-to/giao-viec-cho-ai.md", "02-how-to/review-code-ai.md",
                  "02-how-to/chong-ban-vuot-ton-kho.md", "02-how-to/migration-an-toan.md"]),
    ("Tra cứu", ["03-reference/thuat-ngu.md", "03-reference/tieu-chi-ke-hoach.md", "03-reference/mo-hinh-du-lieu.md",
                 "03-reference/api-dat-hang.md", "03-reference/trang-thai.md", "03-reference/quy-uoc.md"]),
    ("Giải thích", ["04-explanation/bon-truc.md", "04-explanation/chieu-phu-thuoc.md", "04-explanation/phan-loai-domain.md",
                    "04-explanation/phu-thuoc-tu-yeu-cau.md", "04-explanation/thanh-toan-bat-dong-bo.md"]),
    ("Mẫu", ["05-templates/README.md", "05-templates/khuon-module.md", "05-templates/spec-tinh-nang.md",
             "05-templates/api-contract.md", "05-templates/adr.md", "05-templates/threat-model.md",
             "05-templates/test-strategy.md", "05-templates/ke-hoach-trien-khai.md"]),
    ("Làm việc với AI", ["06-ai/nguyen-tac.md", "06-ai/agents-md.md", "06-ai/prompts.md", "06-ai/tools.md"]),
    ("Quyết định (ADR)", ["decisions/README.md", "decisions/0001-monolith-theo-layer.md",
                          "decisions/0002-guest-checkout.md", "decisions/0003-webhook-xac-nhan-thanh-toan.md",
                          "decisions/0004-giu-hang-khi-tao-don.md", "decisions/0005-dung-trang-thanh-toan-cua-cong.md",
                          "decisions/0006-phien-dang-nhap-luu-o-server.md"]),
    ("Về tài liệu", ["CONTRIBUTING.md", "CHANGELOG.md"]),
]
REQUIRED = ["id", "title", "type", "level", "status", "updated", "review_by", "owner"]


def read_page(path):
    text = open(os.path.join(ROOT, path), encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit(f"Thiếu frontmatter: {path}")
    meta = {}
    for line in m.group(1).splitlines():
        line = line.split(" #")[0].rstrip()
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    missing = [k for k in REQUIRED if not meta.get(k)]
    if missing:
        raise SystemExit(f"{path}: thiếu {', '.join(missing)}")
    return meta, text[m.end():]


def main():
    nav_paths = [p for _, ps in NAV for p in ps]
    all_md = sorted(
        posixpath.relpath(os.path.join(d, f), ROOT).replace(os.sep, "/")
        for d, _, fs in os.walk(ROOT) for f in fs
        if f.endswith(".md") and "/site" not in d and "/scripts" not in d)
    problems = []
    for p in all_md:
        if p not in nav_paths:
            problems.append(f"Chưa có trong menu: {p}")

    pages, id_of = {}, {}
    for p in nav_paths:
        meta, body = read_page(p)
        if meta["id"] in pages:
            raise SystemExit(f"Trùng id {meta['id']}: {p}")
        id_of[p] = meta["id"]
        pages[meta["id"]] = {"meta": meta, "body": body, "path": p}

    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    today = datetime.date.today().isoformat()
    out = {}
    for pid, pg in pages.items():
        md.reset()
        html = md.convert(pg["body"])

        def fix(m):
            href = m.group(1)
            if re.match(r"^[a-z]+:", href) or href.startswith("#"):
                return m.group(0)
            target = posixpath.normpath(posixpath.join(posixpath.dirname(pg["path"]), href))
            if target not in id_of:
                problems.append(f"Link hỏng trong {pg['path']}: {href}")
                return m.group(0)
            return f'href="#{id_of[target]}"'

        html = re.sub(r'href="([^"]+)"', fix, html)
        html = re.sub(r"<li>\[ \] ", '<li class="task">', html)
        if pg["meta"]["review_by"] < today:
            problems.append(f"Quá hạn xem lại ({pg['meta']['review_by']}): {pg['path']}")
        out[pid] = dict(pg["meta"], path=pg["path"], html=html)

    data = {"built": today, "nav": [{"group": g, "items": [id_of[p] for p in ps]} for g, ps in NAV], "pages": out}
    js = "window.HANDBOOK=" + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + ";\n"
    open(os.path.join(ROOT, "site", "content.js"), "w", encoding="utf-8").write(js)
    print(f"Đã dựng {len(out)} trang vào site/content.js")
    for x in problems:
        print("  !", x)
    return 1 if any(x.startswith(("Link hỏng", "Chưa có")) for x in problems) else 0


if __name__ == "__main__":
    sys.exit(main())
