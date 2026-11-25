---
id: mau-adr
title: "Mẫu ADR"
type: template
level: L2
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Mẫu ADR (Architecture Decision Record)

## Khi nào dùng

Khi đưa ra một quyết định **khó đảo ngược** hoặc **người sau sẽ thắc mắc vì sao**: chọn kiến trúc, chọn database, chọn cổng thanh toán, đổi cách lưu dữ liệu. Ví dụ đã viết: [các quyết định của case study](../decisions/README.md).

ADR không bị sửa sau khi chốt. Nếu đổi ý, viết ADR mới và đánh dấu ADR cũ là "bị thay thế".

## Mẫu

```markdown
---
id: adr-NNNN
title: "NNNN. <Quyết định, viết như một câu khẳng định>"
type: decision
level: chung
status: done
updated: YYYY-MM-DD
review_by: YYYY-MM-DD
owner: "Người quyết định"
---

# NNNN. <Quyết định>

Trạng thái: Đề xuất | Đã chấp nhận | Bị thay thế bởi NNNN
Ngày: YYYY-MM-DD

## Bối cảnh
<Vấn đề gì, ràng buộc gì, vì sao phải quyết bây giờ>

## Các phương án
1. <Phương án A>: ưu, nhược
2. <Phương án B>: ưu, nhược

## Quyết định
<Chọn gì>

## Hệ quả
- Tốt: <...>
- Phải chấp nhận: <...>
- Việc cần làm theo: <...>
```
