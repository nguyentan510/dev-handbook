---
id: adr-0004
title: "0004. Giữ hàng khi tạo đơn, không giữ khi thêm vào giỏ"
type: decision
level: chung
status: draft
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# 0004. Giữ hàng khi tạo đơn, không giữ khi thêm vào giỏ

Trạng thái: Đề xuất · Ngày: 25/11/2026

## Bối cảnh

Shop có nhiều mặt hàng số lượng ít (hộp quà theo dịp). Cần tránh bán vượt tồn kho, nhưng cũng không để hàng bị "giam" trong giỏ của người chỉ xem.

## Các phương án

1. **Giữ khi thêm vào giỏ:** khách chắc chắn mua được món đã chọn, nhưng giỏ bỏ quên giam hàng rất lâu, dễ bị lợi dụng.
2. **Giữ khi tạo đơn, có hạn 15 phút:** hàng chỉ bị giữ khi khách thật sự đặt; hết hạn thì nhả.
3. **Không giữ, trừ khi thanh toán thành công:** đơn giản, nhưng hai người cùng trả tiền cho món cuối, một người phải được hoàn tiền.

## Quyết định

Đề xuất **2**.

## Hệ quả

- Khách có thể thấy "hết hàng" ở bước đặt dù lúc thêm vào giỏ còn hàng. Giao diện phải báo rõ món nào.
- Cần job nhả hàng của đơn hết hạn, và job đó phải hỏi Payment trước khi hủy.
- Cần giới hạn số đơn "chờ thanh toán" mỗi email để chống giữ hàng hàng loạt.
- Cần kiểm chứng 15 phút đủ cho thanh toán bằng mã QR.
