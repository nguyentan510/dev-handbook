---
id: quy-uoc
title: "Quy ước của dự án"
type: reference
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Quy ước của dự án

Quy ước giúp người và AI viết code giống nhau. Đưa trang này vào ngữ cảnh khi giao việc cho AI.

## Đặt tên

| Thứ | Quy ước | Ví dụ |
|---|---|---|
| Tên trong code | Tiếng Anh, đúng [thuật ngữ](thuat-ngu.md) | `Order`, `OrderItem`, `Payment` |
| Bảng database | Chữ thường, số nhiều, gạch dưới | `order_items` |
| Endpoint | Danh từ số nhiều, có phiên bản | `/api/v1/orders` |
| Trường JSON | camelCase | `shippingFee` |
| Mã lỗi | CHỮ_HOA_GẠCH_DƯỚI | `OUT_OF_STOCK` |
| Trạng thái | chữ thường gạch dưới | `pending_payment` |

## Dữ liệu

- Tiền: số nguyên theo đồng, kèm `currency`.
- Thời gian: lưu UTC, trả về ISO 8601 có múi giờ, hiển thị giờ Việt Nam.
- ID trả ra ngoài: có tiền tố theo loại (`ord_`, `pay_`) và không đoán được.

## Git

- Nhánh: `feat/order-voucher`, `fix/webhook-duplicate`.
- Commit: `feat(order): áp voucher khi đặt hàng`. Loại: feat, fix, refactor, test, docs, chore.
- Mỗi commit một việc. Không commit secret, file `.env` hay dữ liệu thật.

## Định nghĩa xong (Definition of Done) mặc định

- Test qua, lint qua.
- Có test cho trường hợp biên đã nêu trong spec.
- Đã review theo [checklist](../02-how-to/review-code-ai.md).
- Tài liệu liên quan đã cập nhật.
