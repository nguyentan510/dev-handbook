---
id: l2-notify
title: "Module Notify"
type: tutorial
level: L2
status: skeleton
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Module Notify

> Trạng thái: **khung**. Xem [bảng trạng thái L2](README.md).

- **Vai trò:** Gửi email giao dịch: xác nhận đơn, thanh toán, giao hàng.
- **Domain (ví dụ shop quà tặng):** Generic: dùng dịch vụ gửi email có sẵn.
- **Phụ thuộc:** Phụ thuộc sự kiện từ Payment và Order qua outbox.

## Điểm riêng cần làm rõ

- Ghi outbox cùng transaction với thay đổi trạng thái.
- Worker gửi lại khi lỗi, không gửi trùng.
- Mẫu nội dung email, không lộ thông tin thừa.
- Tách email giao dịch khỏi email quảng cáo (có hủy đăng ký).
- Không ghi email và số điện thoại đầy đủ vào log.

## 1. Yêu cầu nghiệp vụ và acceptance criteria

_Chưa viết._ Câu hỏi cần trả lời:

- Ai dùng module này, để làm gì?
- Tiêu chí chấp nhận viết dạng "Khi..., thì...".
- Trạng thái giao diện: đang tải, trống, lỗi, thành công.
- Accessibility: dùng được bằng bàn phím và trình đọc màn hình.
- Ngoài phạm vi.

Mẫu: [Spec tính năng](../../05-templates/spec-tinh-nang.md)

## 2. Phân loại domain

_Chưa viết._ Câu hỏi cần trả lời:

- Core, supporting hay generic, và lý do theo lợi thế cạnh tranh.
- Tự làm hay dùng giải pháp có sẵn?

## 3. Mô hình dữ liệu

_Chưa viết._ Câu hỏi cần trả lời:

- Bảng, cột, ràng buộc, quan hệ.
- Kế hoạch migration và quay lui.

## 4. API contract

_Chưa viết._ Câu hỏi cần trả lời:

- Endpoint, request, response, mã lỗi.
- Phân trang, quyền truy cập, idempotency.

Mẫu: [API contract](../../05-templates/api-contract.md)

## 5. Trạng thái

_Chưa viết._ Câu hỏi cần trả lời:

- Danh sách trạng thái và bước chuyển hợp lệ.
- Ai hoặc cái gì kích hoạt mỗi bước chuyển.

## 6. Threat model

_Chưa viết._ Câu hỏi cần trả lời:

- Tài sản cần bảo vệ, điểm vào.
- Ai có thể tấn công, tấn công thế nào, cách chặn, kiểm bằng gì.

Mẫu: [Threat model](../../05-templates/threat-model.md)

## 7. Test strategy

_Chưa viết._ Câu hỏi cần trả lời:

- Test gì ở unit, integration, contract, E2E.
- Trường hợp biên bắt buộc.

Mẫu: [Test strategy](../../05-templates/test-strategy.md)

## 8. Vận hành

_Chưa viết._ Câu hỏi cần trả lời:

- Log, metric, cảnh báo cần có.
- Job nền và cách theo dõi nó.

## 9. Quyết định (ADR)

_Chưa viết._ Câu hỏi cần trả lời:

- Quyết định đã chốt và quyết định còn để ngỏ.

Mẫu: [ADR](../../05-templates/adr.md)

## 10. Ranh giới giao việc cho AI

_Chưa viết._ Câu hỏi cần trả lời:

- Phần nào AI làm, AI nháp người duyệt, người quyết.
- Checklist review riêng của module.
