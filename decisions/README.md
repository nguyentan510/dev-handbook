---
id: quyet-dinh
title: "Quyết định kiến trúc (ADR)"
type: overview
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Quyết định kiến trúc (ADR)

Mỗi quyết định khó đảo ngược được ghi lại: bối cảnh, các phương án, lựa chọn và hệ quả. Sau hai năm vẫn biết vì sao hệ thống được làm như vậy. Viết ADR mới bằng [mẫu ADR](../05-templates/adr.md).

| Số | Quyết định | Trạng thái |
|---|---|---|
| [0001](0001-monolith-theo-layer.md) | Bắt đầu bằng monolith theo layer | Đã chấp nhận |
| [0002](0002-guest-checkout.md) | Cho khách mua không cần đăng nhập | Đã chấp nhận |
| [0003](0003-webhook-xac-nhan-thanh-toan.md) | Chỉ webhook và đối soát mới xác nhận thanh toán | Đã chấp nhận |
| [0004](0004-giu-hang-khi-tao-don.md) | Giữ hàng khi tạo đơn, không giữ khi thêm vào giỏ | Đề xuất |
| [0005](0005-dung-trang-thanh-toan-cua-cong.md) | Dùng trang thanh toán của cổng, qua một adapter | Đề xuất |
| [0006](0006-phien-dang-nhap-luu-o-server.md) | Phiên đăng nhập lưu ở server, gửi qua cookie | Đề xuất |

Các ADR này thuộc case study và là ví dụ. ADR "Đề xuất" chờ người có thẩm quyền chấp nhận.
