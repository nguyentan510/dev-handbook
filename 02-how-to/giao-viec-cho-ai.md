---
id: giao-viec-cho-ai
title: "Giao việc cho AI theo mức rủi ro"
type: how-to
level: L1
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Giao việc cho AI theo mức rủi ro, không theo độ khó

AI viết code khó rất nhanh. Câu hỏi đúng không phải "AI làm được không" mà là "**nếu AI làm sai thì mất gì**".

## Ba mức giao

| Mức | Loại việc | Cách giao |
|---|---|---|
| **AI làm** | UI, boilerplate, CRUD đơn giản, khung test, tài liệu nháp | AI viết, người chạy thử và đọc lướt diff |
| **AI nháp, người duyệt** | Schema, migration, truy vấn, tích hợp email, job nền | AI viết theo spec, người review kỹ và chạy trên dữ liệu thử |
| **Người quyết** | Auth, phân quyền, thanh toán, quy tắc core, xóa dữ liệu | Người thiết kế và quyết. AI hỗ trợ viết theo spec, review từng dòng, test bắt buộc |

## Quy trình một task

1. **Viết spec** bằng [mẫu spec](../05-templates/spec-tinh-nang.md): mục tiêu, quy tắc, trường hợp biên, phần không làm.
2. **Cho AI đủ ngữ cảnh:** [AGENTS.md](../06-ai/agents-md.md), contract liên quan, file cần sửa.
3. **Giao task nhỏ**, mỗi lần một việc có thể review trong 15 phút.
4. **Chạy test**, kể cả test do bạn tự nêu trường hợp biên.
5. **Review diff** bằng [checklist](review-code-ai.md).
6. **Commit** sau mỗi task, để quay lại được nếu bước sau hỏng.

## Vùng không để AI tự quyết

- Thiết kế phân quyền và cách lưu mật khẩu.
- Mọi thứ chạm tới tiền: tính tiền, thanh toán, hoàn tiền.
- Migration chạy trên dữ liệu thật, và mọi lệnh xóa dữ liệu.
- Thêm thư viện mới vào dự án.

Nguyên tắc chi tiết ở [Nguyên tắc làm việc với AI](../06-ai/nguyen-tac.md).
