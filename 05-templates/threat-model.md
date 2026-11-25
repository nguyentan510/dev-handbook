---
id: mau-threat-model
title: "Mẫu threat model"
type: template
level: L2
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Mẫu threat model

## Khi nào dùng

Ở đầu dự án (P0) cho toàn hệ thống, và ở mục 6 của mỗi module. Mục tiêu là tìm ra cách bị tấn công **trước khi** viết code, không phải liệt kê mọi lỗ hổng có thể có.

## Bốn câu hỏi

1. Chúng ta đang xây gì? (vẽ luồng dữ liệu đơn giản)
2. Điều gì có thể sai?
3. Chúng ta làm gì để chặn?
4. Đã làm đủ chưa? (kiểm bằng test hoặc review)

## Mẫu

```markdown
## Threat model: <module hoặc hệ thống>

Tài sản cần bảo vệ:
- <ví dụ: thông tin cá nhân khách, trạng thái thanh toán, tồn kho>

Điểm vào:
- <ví dụ: POST /orders, webhook từ cổng, trang admin>

| Mối đe dọa | Ví dụ cụ thể | Ảnh hưởng | Cách chặn | Kiểm bằng |
|---|---|---|---|---|
| Giả mạo | Gửi webhook giả báo "đã thanh toán" | Cao | Kiểm chữ ký | Test webhook sai chữ ký |
| Xem trái phép | Đổi mã đơn trên URL để xem đơn người khác | Cao | Kiểm quyền sở hữu, trả 404 | Test truy cập chéo |
| Lạm dụng | Spam tạo đơn để giữ hết hàng | Vừa | Giới hạn tần suất, giữ hàng có hạn | Test tải |
| Lộ dữ liệu | Ghi email, số điện thoại vào log | Vừa | Che thông tin trong log | Review log mẫu |

Câu hỏi còn mở:
- <...>
```
