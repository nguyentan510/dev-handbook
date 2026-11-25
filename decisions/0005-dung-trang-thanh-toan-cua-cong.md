---
id: adr-0005
title: "0005. Dùng trang thanh toán của cổng, qua một adapter"
type: decision
level: chung
status: draft
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# 0005. Dùng trang thanh toán của cổng, qua một adapter

Trạng thái: Đề xuất · Ngày: 25/11/2026

## Bối cảnh

Shop cần nhận thẻ, QR và ví. Nhóm nhỏ, không có chuyên gia bảo mật thẻ. Phí và chất lượng của các cổng thay đổi, có thể phải đổi cổng sau này.

## Các phương án

1. **Form nhập thẻ ngay trên trang của shop, gọi API của cổng:** trải nghiệm liền mạch, nhưng số thẻ đi qua hệ thống của shop, phạm vi tuân thủ PCI DSS lớn.
2. **Chuyển khách sang trang thanh toán của cổng (hosted page):** số thẻ không chạm hệ thống của shop, cổng lo phần lớn bảo mật thẻ; khách rời trang một lúc.
3. **Gọi thẳng SDK của một cổng trong code nghiệp vụ:** nhanh nhất lúc đầu, nhưng đổi cổng phải sửa khắp nơi.

## Quyết định

Đề xuất **2**, và bọc cổng sau một port gồm năm thao tác (tạo, kiểm webhook, hỏi trạng thái, hoàn tiền, lấy báo cáo). Mỗi cổng là một adapter.

## Hệ quả

- Không lưu số thẻ, CVV; phạm vi tuân thủ nhỏ hơn nhiều so với phương án 1.
- Khách rời trang của shop khi trả tiền; trang quay về phải xử lý được trạng thái "đang xử lý".
- Đổi cổng chỉ cần viết adapter mới và chạy lại contract test.
- Cần chọn cổng có sandbox tốt và có báo cáo đối soát qua API.
