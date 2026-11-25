---
id: l2-thiet-ke-mvp
title: "L2 · Thiết kế MVP thực tế"
type: roadmap
level: L2
status: skeleton
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# L2 · Thiết kế MVP thực tế

> Trạng thái: **khung**. Mục lục, khuôn và mẫu đã có. Nội dung chi tiết từng module sẽ được viết dần.

## Học xong bạn làm được

1. Viết yêu cầu nghiệp vụ và acceptance criteria cho một module, gồm cả trạng thái lỗi và accessibility.
2. Thiết kế ERD có ràng buộc và kế hoạch migration.
3. Viết API contract trước khi code: request, response, mô hình lỗi, phân trang, phân quyền.
4. Vẽ state diagram và chỉ ra các bước chuyển hợp lệ.
5. Lập threat model và test strategy cho từng module.
6. Ghi quyết định bằng ADR và xác định ranh giới giao việc cho AI.

## Điều kiện bắt đầu

Đã xong [L1](l1-nhap-mon.md) và trả lời được phần tự kiểm tra.

## Đầu ra cho mỗi module

Mỗi module được thiết kế theo [khuôn 10 mục](../05-templates/khuon-module.md):

1. Yêu cầu nghiệp vụ và acceptance criteria
2. Phân loại domain kèm lý do
3. Mô hình dữ liệu (ERD)
4. API contract
5. Trạng thái (state diagram)
6. Threat model
7. Test strategy
8. Vận hành: log, metric, cảnh báo
9. Quyết định (ADR)
10. Ranh giới giao việc cho AI

## Thứ tự module

Theo yêu cầu cho khách mua không cần đăng nhập ([ADR 0002](../decisions/0002-guest-checkout.md)):

1. [Catalog](../01-tutorials/l2/catalog.md): nền cho mọi thứ khác
2. [Order](../01-tutorials/l2/order.md): giá trị cốt lõi của MVP
3. [Payment](../01-tutorials/l2/payment.md): rủi ro cao nhất
4. [Auth](../01-tutorials/l2/auth.md): làm song song với Order
5. [Notify](../01-tutorials/l2/notify.md): sau khi có sự kiện thanh toán

Xem bảng trạng thái ở [Case study L2](../01-tutorials/l2/README.md).

## Mẫu dùng trong L2

[Khuôn module](../05-templates/khuon-module.md) · [Spec tính năng](../05-templates/spec-tinh-nang.md) · [API contract](../05-templates/api-contract.md) · [ADR](../05-templates/adr.md) · [Threat model](../05-templates/threat-model.md) · [Test strategy](../05-templates/test-strategy.md)

## Hoàn thành L2 khi

- Cả 5 module có đủ 10 mục, mỗi mục được một người khác review.
- Contract của Order và Payment có contract test.
- Có ít nhất một ADR cho mỗi quyết định khó đảo ngược.
