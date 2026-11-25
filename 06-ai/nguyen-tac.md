---
id: ai-nguyen-tac
title: "Nguyên tắc làm việc với AI"
type: explanation
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Nguyên tắc làm việc với AI

Các nguyên tắc này ít thay đổi dù công cụ AI thay đổi rất nhanh. Hướng dẫn cho từng công cụ nằm riêng ở [Ghi chú theo công cụ](tools.md).

1. **Rủi ro quyết định mức giao, không phải độ khó.** Xem [ba mức giao](../02-how-to/giao-viec-cho-ai.md).
2. **Spec trước, code sau.** AI làm đúng điều bạn viết ra, không làm đúng điều bạn nghĩ trong đầu.
3. **Ngữ cảnh đủ và ổn định.** File [AGENTS.md](agents-md.md), [thuật ngữ](../03-reference/thuat-ngu.md) và [quy ước](../03-reference/quy-uoc.md) là thứ AI đọc trước mỗi phiên.
4. **Task nhỏ, commit thường.** Mỗi task review được trong 15 phút. Hỏng thì quay lại commit trước.
5. **Test là hợp đồng.** Bạn nêu trường hợp biên, AI viết test. Không để AI sửa test cho khớp với code.
6. **Review như code của người lạ.** Dùng [checklist](../02-how-to/review-code-ai.md), chạy thử thay vì tin lời giải thích.
7. **Tài liệu là một phần của "xong".** AI viết nháp tài liệu, người duyệt.
8. **Người chịu trách nhiệm luôn là người.** AI viết code, nhưng mỗi task có một người ký tên.
