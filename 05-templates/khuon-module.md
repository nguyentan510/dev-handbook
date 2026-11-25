---
id: mau-khuon-module
title: "Khuôn module 10 mục"
type: template
level: L2
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Khuôn module 10 mục

Khuôn chung để thiết kế một module ở L2. Mọi module trong [case study L2](../01-tutorials/l2/README.md) đều theo khuôn này, nên người đọc biết tìm gì ở đâu.

## Khi nào dùng

Trước khi bắt đầu code một module mới, hoặc khi cần viết lại tài liệu cho một module đã có. Không cần điền hết trong một lần: điền mục 1 đến 4 trước khi code, các mục còn lại trong lúc làm.

## Cách điền

- Mỗi mục ngắn, dùng bảng và danh sách. Dẫn link sang mẫu chi tiết thay vì chép lại.
- Ghi rõ những gì **chưa quyết** thay vì đoán.
- Mỗi mục có người review khác người viết.

## Mẫu

```markdown
---
id: l2-ten-module
title: "Module: Tên module"
type: tutorial
level: L2
status: draft
updated: YYYY-MM-DD
review_by: YYYY-MM-DD
owner: "Tên người phụ trách"
---

# Module: Tên module

Một câu: module này làm gì, cho ai.

## 1. Yêu cầu nghiệp vụ và acceptance criteria
- Ai dùng, để làm gì.
- Tiêu chí chấp nhận dạng: Khi <tình huống>, thì <kết quả nhìn thấy được>.
- Trạng thái giao diện: đang tải, trống, lỗi, thành công.
- Accessibility: dùng bằng bàn phím, nhãn cho trình đọc màn hình.
- Ngoài phạm vi.

## 2. Phân loại domain
- Core, supporting hay generic, và lý do theo lợi thế cạnh tranh.
- Tự làm hay dùng giải pháp có sẵn.

## 3. Mô hình dữ liệu
- Bảng, cột, ràng buộc. Sơ đồ quan hệ.
- Kế hoạch migration và quay lui.

## 4. API contract
- Endpoint, request, response, mã lỗi, phân trang, quyền truy cập.
- Dẫn link tới contract chi tiết.

## 5. Trạng thái
- Danh sách trạng thái, bước chuyển hợp lệ, ai hoặc cái gì kích hoạt.
- Ghi "không có" nếu module không có vòng đời trạng thái.

## 6. Threat model
- Tài sản cần bảo vệ, ai có thể tấn công, tấn công thế nào, cách chặn.

## 7. Test strategy
- Unit, integration, contract, E2E: test gì ở tầng nào.
- Danh sách trường hợp biên.

## 8. Vận hành
- Log cần có, metric, cảnh báo, job nền.

## 9. Quyết định (ADR)
- Danh sách ADR liên quan và quyết định còn để ngỏ.

## 10. Ranh giới giao việc cho AI
- Phần nào AI làm, phần nào AI nháp người duyệt, phần nào người quyết.
- Checklist review riêng của module (nếu có).
```
