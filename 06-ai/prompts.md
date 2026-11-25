---
id: ai-prompts
title: "Prompt mẫu"
type: how-to
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Prompt mẫu

Prompt tốt nói rõ: làm gì, dựa trên tài liệu nào, ràng buộc gì, và thế nào là xong. Các mẫu dưới đây giả định AI đã đọc [AGENTS.md](agents-md.md).

## Tạo endpoint theo contract

```text
Tạo endpoint POST /api/v1/orders theo contract trong
dev-handbook/03-reference/api-dat-hang.md.
- Đặt code theo layer: controller, service, repository.
- Kiểm tra đầu vào, trả lỗi theo mô hình lỗi chuẩn.
- Hỗ trợ Idempotency-Key như contract mô tả.
- Chưa gọi cổng thanh toán, để một hàm giả.
Xong khi: integration test cho 201, 400, 409, 422 đều qua.
Không sửa file nào ngoài module Order.
```

## Viết test từ spec

```text
Đọc spec voucher dưới đây. Viết unit test cho từng quy tắc và từng
trường hợp biên. Chưa viết code xử lý. Liệt kê những chỗ spec còn
mơ hồ thay vì tự đoán.
<dán spec>
```

## Review bảo mật

```text
Review diff này với vai trò người kiểm tra bảo mật. Chỉ ra:
truy cập chéo giữa người dùng, dữ liệu đầu vào chưa kiểm tra,
thông tin cá nhân bị ghi log, secret trong code.
Với mỗi vấn đề: dòng nào, vì sao nguy hiểm, cách sửa.
Không sửa code.
```

## Giải thích code lạ

```text
Giải thích file này cho một người mới: nó làm gì, được gọi từ đâu,
gọi tới đâu, và phần nào rủi ro nếu sửa. Dùng đúng thuật ngữ trong
dev-handbook/03-reference/thuat-ngu.md.
```

## Refactor không đổi hành vi

```text
Tách hàm calculateTotal thành các hàm nhỏ. Không đổi hành vi:
toàn bộ test hiện có phải qua mà không sửa test nào.
Nếu thấy test thiếu, liệt kê ra trước khi refactor.
```
