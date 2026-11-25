---
id: cach-viet-tai-lieu
title: "Cách viết và bảo trì tài liệu"
type: how-to
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Cách viết và bảo trì tài liệu

Tài liệu này được viết theo kiểu **docs-as-code**: Markdown trong Git, sửa bằng pull request và được review như code.

## Mỗi trang một loại, một ý

Trước khi viết, chọn đúng một loại cho trang: lộ trình, hướng dẫn học, cách làm, tra cứu, giải thích, mẫu hoặc quyết định. Nếu thấy trang đang ôm hai loại, tách thành hai trang và dẫn link qua lại.

Trang ngắn dễ cho cả người lẫn AI tìm đúng chỗ. Một trang nên đọc xong trong 5-10 phút.

## Frontmatter bắt buộc

Mọi file bắt đầu bằng khối thông tin:

```yaml
---
id: luong-dat-hang          # duy nhất, chữ thường không dấu, gạch nối
title: "Luồng Đặt hàng"
type: tutorial              # overview, roadmap, tutorial, how-to, reference, explanation, template, decision
level: L1                   # L1, L2, L3 hoặc chung
status: done                # done, draft, skeleton
updated: 2026-11-25
review_by: 2027-02-25       # quá ngày này thì phải xem lại
owner: "Tên người phụ trách"
---
```

## Thuật ngữ có một nguồn duy nhất

Định nghĩa chỉ nằm trong [Bảng thuật ngữ](03-reference/thuat-ngu.md). Trang khác dùng đúng tên đó và dẫn link về, không tự định nghĩa lại. Gọi chỗ này "Order", chỗ kia "Đơn hàng", chỗ khác "Purchase" sẽ làm AI sinh code lẫn lộn.

## Tách phần bền khỏi phần dễ cũ

- **Bền:** nguyên lý, khái niệm, quy trình. Xem lại mỗi 3-6 tháng.
- **Dễ cũ:** hướng dẫn cho một công cụ AI hay một thư viện cụ thể. Chỉ để trong [Ghi chú theo công cụ](06-ai/tools.md), `review_by` không quá 3 tháng.

## Quy trình sửa

1. Tạo nhánh, sửa file Markdown.
2. Chạy `python3 scripts/build.py` để kiểm tra link hỏng và dựng lại trang web.
3. Mở pull request, cần một người duyệt.
4. Ghi một dòng vào [nhật ký thay đổi](CHANGELOG.md) nếu thay đổi đáng kể.

Cập nhật tài liệu liên quan là một phần của Definition of Done: task chưa xong nếu tài liệu chưa cập nhật. AI có thể viết nháp, người duyệt.

## Rà soát định kỳ

Mỗi quý, lọc các trang quá `review_by`. Với mỗi trang: cập nhật, đánh dấu `status: draft` nếu cần viết lại, hoặc xóa nếu không còn đúng.

## Đặt tên file

Chữ thường, không dấu, nối bằng gạch ngang: `chong-ban-vuot-ton-kho.md`. ADR đánh số bốn chữ số: `0004-ten-quyet-dinh.md`.

## Trang web

`scripts/build.py` đọc toàn bộ Markdown, chuyển link `.md` thành link trong trang, và xuất `site/content.js`. Mở `site/index.html` để xem. Thứ tự menu được khai báo trong biến `NAV` của script.

`site/content.js` là file sinh ra nên không được commit. Mỗi lần đẩy lên nhánh `main`, GitHub Actions (`.github/workflows/pages.yml`) chạy script, dừng lại nếu có link hỏng, rồi đăng thư mục `site/` lên GitHub Pages.
