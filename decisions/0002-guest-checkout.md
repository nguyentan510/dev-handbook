---
id: adr-0002
title: "0002. Cho khách mua không cần đăng nhập"
type: decision
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# 0002. Cho khách mua không cần đăng nhập

Trạng thái: Đã chấp nhận · Ngày: 25/11/2026

## Bối cảnh

Shop quà tặng có nhiều khách mua một lần để tặng. Bắt đăng ký trước khi mua làm mất khách ở bước thanh toán.

## Các phương án

1. **Bắt buộc đăng nhập:** dữ liệu khách sạch, nhưng thêm một bước cản.
2. **Cho mua không cần đăng nhập (guest checkout):** khách chỉ cần email và số điện thoại. Có thể tạo tài khoản sau.

## Quyết định

Chọn **2**.

## Hệ quả

- `orders.user_id` cho phép rỗng, có thêm `guest_email`.
- Order chỉ phụ thuộc Catalog; Auth làm song song (xem [Phụ thuộc đến từ yêu cầu](../04-explanation/phu-thuoc-tu-yeu-cau.md)).
- Khách vãng lai xem lại đơn qua đường dẫn có mã bí mật gửi qua email, không qua mã đơn đoán được.
- Cần giới hạn tần suất tạo đơn để chống spam giữ hàng.
