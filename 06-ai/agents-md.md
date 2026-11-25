---
id: ai-agents-md
title: "File ngữ cảnh AGENTS.md"
type: how-to
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# File ngữ cảnh AGENTS.md

File đặt ở gốc dự án, mô tả những gì AI cần biết trước khi sửa code. Tên phổ biến là `AGENTS.md` hoặc `CLAUDE.md`, tùy công cụ. Giữ file ngắn: AI đọc nó mỗi phiên, file dài thì những ý quan trọng bị chìm.

## Mẫu

```markdown
# AGENTS.md

## Dự án
App bán hàng online. Monolith theo layer:
controller → service → repository.
Tài liệu: dev-handbook/ (đọc 03-reference trước khi sửa code).

## Lệnh
- Cài: npm install
- Test: npm test
- Lint: npm run lint

## Thuật ngữ
Dùng đúng tên trong dev-handbook/03-reference/thuat-ngu.md:
Order, OrderItem, Payment, Inventory.

## Quy ước
- Tiền là số nguyên VND. Thời gian lưu UTC.
- Mọi endpoint mới phải có validation, mô hình lỗi chuẩn và test.

## Không tự quyết
- Auth, phân quyền, thanh toán, migration trên dữ liệu thật:
  dừng lại và hỏi người.
- Không thêm thư viện mới khi chưa được đồng ý.
- Không đưa secret vào code hoặc log.

## Xong là khi
Test và lint qua, docs liên quan đã cập nhật.
```

## Giải thích từng phần

| Phần | Vì sao cần |
|---|---|
| Dự án | AI biết kiến trúc để đặt code đúng chỗ |
| Lệnh | AI tự chạy test thay vì đoán |
| Thuật ngữ | Tránh mỗi file gọi một tên |
| Quy ước | Code mới giống code cũ |
| Không tự quyết | Ranh giới an toàn, quan trọng nhất |
| Xong là khi | AI biết khi nào dừng |
