---
id: l2-case-study
title: "Case study L2: thiết kế từng module"
type: tutorial
level: L2
status: draft
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Case study L2: thiết kế từng module

> Trạng thái: **nháp**. Catalog, Order, Payment và Auth đã có bản nháp đủ 10 mục, chờ review. Notify mới có câu hỏi cần trả lời.

Mỗi module được thiết kế theo [khuôn 10 mục](../../05-templates/khuon-module.md). Thứ tự làm và lý do ở [Lộ trình L2](../../00-lo-trinh/l2-thiet-ke-mvp.md).

## Bảng trạng thái

Số cột là mục trong khuôn: 1 Yêu cầu · 2 Domain · 3 Dữ liệu · 4 API · 5 Trạng thái · 6 Threat model · 7 Test · 8 Vận hành · 9 ADR · 10 Ranh giới AI.

| Module | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| [Catalog](catalog.md) | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp |
| [Order](order.md) | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp |
| [Payment](payment.md) | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp |
| [Auth](auth.md) | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp | Nháp |
| [Notify](notify.md) | Khung | Khung | Khung | Khung | Khung | Khung | Khung | Khung | Khung | Khung |

Giá trị: Khung → Nháp → Đã review. Cập nhật bảng này mỗi khi một mục đổi trạng thái.

## Cách học một module

1. Đọc phần "Điểm riêng cần làm rõ" của module.
2. Tự trả lời các câu hỏi ở từng mục, dùng mẫu được dẫn link.
3. So với nội dung tham khảo ở L1: [mô hình dữ liệu](../../03-reference/mo-hinh-du-lieu.md), [API đặt hàng](../../03-reference/api-dat-hang.md), [trạng thái](../../03-reference/trang-thai.md).
4. Nhờ một người khác review từng mục.
