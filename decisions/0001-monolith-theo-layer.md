---
id: adr-0001
title: "0001. Bắt đầu bằng monolith theo layer"
type: decision
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# 0001. Bắt đầu bằng monolith theo layer

Trạng thái: Đã chấp nhận · Ngày: 25/11/2026

## Bối cảnh

Nhóm 3-4 người, cần MVP trong 8 tuần. Lượng truy cập dự kiến nhỏ. Nhóm dùng AI để viết nhiều code, nên cần cấu trúc dễ đoán để AI đặt code đúng chỗ.

## Các phương án

1. **Microservices:** mỗi module một dịch vụ. Tách biệt tốt, nhưng tốn công vận hành, giao dịch giữa các dịch vụ phức tạp.
2. **Monolith theo layer:** một ứng dụng, chia controller, service, repository; module là thư mục. Đơn giản, một database, transaction dễ.
3. **Monolith theo ports and adapters:** như 2 nhưng lõi nghiệp vụ không phụ thuộc database. Sạch hơn, nhưng nhiều lớp hơn cho người mới.

## Quyết định

Chọn **2**, nhưng module Payment dùng một adapter riêng cho cổng thanh toán (theo tinh thần của 3), vì khả năng đổi cổng là có thật.

## Hệ quả

- Tốt: một repository, một database, transaction trong một đơn hàng đơn giản.
- Phải chấp nhận: các module có thể dính nhau nếu không giữ kỷ luật. Quy ước: module chỉ gọi nhau qua service.
- Việc cần làm theo: xem lại khi có hơn 8 người hoặc một module cần mở rộng riêng.
