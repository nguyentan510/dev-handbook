---
id: migration-an-toan
title: "Thay đổi database an toàn"
type: how-to
level: L1
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Thay đổi database an toàn

## Mở rộng rồi thu hẹp

Đừng đổi tên hay xóa cột trong một bước. Làm theo bốn bước, mỗi bước deploy riêng:

1. **Mở rộng:** thêm cột hoặc bảng mới, cho phép rỗng.
2. **Ghi hai nơi:** code mới ghi cả chỗ cũ lẫn chỗ mới.
3. **Chuyển dữ liệu:** chép dữ liệu cũ sang, theo từng lô nếu bảng lớn.
4. **Thu hẹp:** code chỉ đọc chỗ mới, rồi mới xóa chỗ cũ.

Như vậy bước nào cũng quay lui được mà không mất dữ liệu.

## Trước khi chạy trên dữ liệu thật

- [ ] Chạy thử trên bản sao dữ liệu production đã che thông tin cá nhân.
- [ ] Đo thời gian chạy. Câu lệnh khóa bảng lâu cần làm theo lô.
- [ ] Có sẵn migration quay lui, đã chạy thử.
- [ ] Đã sao lưu, và biết cách khôi phục.
- [ ] Có người thứ hai duyệt.

Mức giao AI: **AI nháp, người duyệt**. Không để AI tự chạy migration trên dữ liệu thật.
