---
id: api-dat-hang
title: "API đặt hàng"
type: reference
level: L1
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# API đặt hàng

Contract là thỏa thuận giữa frontend, backend và cả AI: gửi gì, nhận gì, lỗi trông thế nào. Viết contract trước giúp AI sinh code khớp nhau ở cả hai phía. Mẫu để viết contract mới: [API contract](../05-templates/api-contract.md).

## Tạo đơn

```http
POST /api/v1/orders
Idempotency-Key: 7f3c9a1e-...
Authorization: Bearer ...     (bỏ trống nếu là khách vãng lai)
Content-Type: application/json

{
  "items": [{ "productId": "p_123", "quantity": 2 }],
  "guestEmail": "an@example.com",
  "shippingAddress": { "name": "Nguyễn An", "phone": "0900000000",
                       "line1": "12 Lê Lợi", "city": "TP.HCM" },
  "voucherCode": "QUA50"
}
```

```http
201 Created

{
  "id": "ord_789",
  "status": "pending_payment",
  "items": [{ "productId": "p_123", "name": "Hộp quà gỗ",
              "unitPrice": 150000, "quantity": 2 }],
  "subtotal": 300000, "discount": 50000,
  "shippingFee": 0, "total": 250000, "currency": "VND",
  "payment": { "id": "pay_456", "status": "pending",
               "redirectUrl": "https://..." },
  "expiresAt": "2026-11-25T10:15:00+07:00"
}
```

Gửi lại cùng `Idempotency-Key` với cùng nội dung thì nhận lại đúng đơn cũ, không tạo đơn mới.

## Xem danh sách đơn

```http
GET /api/v1/orders?status=paid&limit=20&cursor=...

200 OK
{ "data": [ ... ], "nextCursor": "..." }
```

Chỉ trả đơn của người đang đăng nhập. Phân trang bằng cursor để không bị lệch khi có đơn mới.

## Mô hình lỗi thống nhất

```json
{
  "error": {
    "code": "OUT_OF_STOCK",
    "message": "Sản phẩm đã hết hàng",
    "details": [{ "field": "items[0].quantity", "issue": "Chỉ còn 1" }],
    "requestId": "req_abc123"
  }
}
```

| Mã HTTP | Khi nào | Ví dụ `code` |
|---|---|---|
| 400 | Dữ liệu sai định dạng, thiếu trường | `VALIDATION_FAILED` |
| 401 | Chưa đăng nhập ở endpoint bắt buộc đăng nhập | `UNAUTHENTICATED` |
| 404 | Không tìm thấy, hoặc đơn không phải của bạn (không tiết lộ là có tồn tại) | `NOT_FOUND` |
| 409 | Idempotency-Key đã dùng với nội dung khác | `IDEMPOTENCY_CONFLICT` |
| 422 | Đúng định dạng nhưng sai quy tắc | `OUT_OF_STOCK`, `VOUCHER_INVALID` |

## Quy ước

- Có `/v1` trong đường dẫn để sau này đổi contract mà không làm hỏng app cũ.
- Tiền là số nguyên VND. Thời gian theo ISO 8601 có múi giờ.
- Mỗi endpoint có contract test để phát hiện khi một bên đổi mà bên kia không biết.
