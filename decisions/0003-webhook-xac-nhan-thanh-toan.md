---
id: adr-0003
title: "0003. Chỉ webhook và đối soát mới xác nhận thanh toán"
type: decision
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# 0003. Chỉ webhook và đối soát mới xác nhận thanh toán

Trạng thái: Đã chấp nhận · Ngày: 25/11/2026

## Bối cảnh

Sau khi trả tiền, cổng chuyển khách về trang của shop kèm tham số trạng thái. Tham số này đi qua trình duyệt nên có thể bị sửa, và khách có thể đóng trình duyệt trước khi quay về.

## Các phương án

1. **Tin trang quay về:** đơn giản, nhưng có thể bị giả mạo và bỏ sót.
2. **Chỉ tin webhook có chữ ký, kèm đối soát định kỳ:** phức tạp hơn, nhưng là nguồn sự thật đáng tin.

## Quyết định

Chọn **2**. Trang quay về chỉ hiển thị "đang xử lý" và hỏi trạng thái từ server.

## Hệ quả

- Cần bảng `webhook_events` với `event_id` duy nhất để chống trùng.
- Cần state machine cho Payment và Order (xem [Trạng thái](../03-reference/trang-thai.md)).
- Cần job đối soát mỗi vài phút và đối chiếu báo cáo cuối ngày.
- Giao diện phải xử lý được trạng thái "đang xử lý" kéo dài vài giây đến vài phút.
