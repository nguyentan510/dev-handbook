---
id: review-code-ai
title: "Review code AI viết"
type: how-to
level: L1
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Review code AI viết

Review code AI như review code của một người lạ rất giỏi nhưng không biết dự án của bạn: viết nhanh, tự tin, và đôi khi bịa.

## Checklist

- [ ] Chạy được và test qua, không chỉ "trông đúng".
- [ ] Không gọi hàm hay thư viện không tồn tại.
- [ ] Dữ liệu đầu vào được kiểm tra, lỗi trả đúng [mô hình lỗi](../03-reference/api-dat-hang.md).
- [ ] Chỉ chủ đơn mới xem và sửa được đơn của mình.
- [ ] Không lộ secret hay thông tin cá nhân trong code và log.
- [ ] Không thêm thư viện lạ, không sửa ngoài phạm vi task.
- [ ] Không có truy vấn lặp trong vòng lặp (N+1).
- [ ] Dùng đúng [thuật ngữ](../03-reference/thuat-ngu.md) và [quy ước](../03-reference/quy-uoc.md) của dự án.
- [ ] Với phần chạm tiền: tiền là số nguyên, có idempotency, chỉ chuyển trạng thái hợp lệ.

## Dấu hiệu cần dừng lại

- Diff dài hơn nhiều so với việc được giao.
- Test bị sửa cho khớp với code, thay vì code sửa cho khớp test.
- Code bắt lỗi rồi bỏ qua im lặng.
- AI giải thích rất trơn tru một phần bạn không chạy thử được.

Gặp một trong các dấu hiệu này: quay về commit trước, chia task nhỏ hơn, giao lại.
