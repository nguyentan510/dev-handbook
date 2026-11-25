---
id: adr-0006
title: "0006. Phiên đăng nhập lưu ở server, gửi qua cookie"
type: decision
level: chung
status: draft
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# 0006. Phiên đăng nhập lưu ở server, gửi qua cookie

Trạng thái: Đề xuất · Ngày: 25/11/2026

## Bối cảnh

Ứng dụng là một monolith ([ADR 0001](0001-monolith-theo-layer.md)), frontend và API cùng tên miền. Cần đăng xuất có hiệu lực ngay, đăng xuất mọi thiết bị khi đổi mật khẩu, và vô hiệu tài khoản tức thì.

## Các phương án

1. **Phiên lưu ở server, mã phiên ngẫu nhiên trong cookie `HttpOnly`:** thu hồi ngay được, mã không đọc được từ JavaScript. Mỗi request phải tra phiên.
2. **JWT ký sẵn, lưu trong trình duyệt:** không cần tra database, hợp với nhiều dịch vụ. Nhưng khó thu hồi trước khi hết hạn, và nếu lưu ở `localStorage` thì mã độc trên trang đọc được.
3. **Dịch vụ quản lý danh tính bên ngoài:** có sẵn đăng nhập mạng xã hội, hai lớp; thêm chi phí và phụ thuộc bên ngoài.

## Quyết định

Đề xuất **1**, dùng thư viện phiên của framework. Xem lại khi cần đăng nhập mạng xã hội hoặc có ứng dụng mobile.

## Hệ quả

- Đăng xuất, đổi mật khẩu, vô hiệu tài khoản có tác dụng ngay.
- Cần chống CSRF vì trình duyệt tự gửi cookie: `SameSite=Lax`, kiểm `Origin`, mã CSRF.
- Mỗi request tra bảng `sessions`; cần chỉ mục, có thể cache ngắn khi lượng truy cập tăng.
- App mobile sau này có thể cần một cơ chế mã khác, và cần ADR mới.
