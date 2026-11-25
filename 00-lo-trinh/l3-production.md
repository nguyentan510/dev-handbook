---
id: l3-production
title: "L3 · Production và vận hành"
type: roadmap
level: L3
status: skeleton
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# L3 · Production và vận hành

> Trạng thái: **khung**. Mới có danh sách chủ đề.

## Chủ đề dự kiến

| Chủ đề | Nội dung chính |
|---|---|
| Thanh toán phân tán | Authorize và capture, outbox và inbox, retry có backoff, đối soát theo báo cáo cổng, hoàn tiền một phần |
| Đo lường | SLI và SLO, error budget, chính sách cảnh báo, dashboard cho luồng đặt hàng |
| Quan sát | Log có cấu trúc, tracing, correlation ID xuyên suốt |
| Dữ liệu | Sao lưu, diễn tập khôi phục, RTO và RPO, migration trên bảng lớn |
| Bảo mật vận hành | Xoay vòng secret, quét thư viện liên tục, audit log, xử lý PII |
| Sự cố | Runbook, phân loại mức độ, postmortem không đổ lỗi |
| Phát hành | Feature flag, phát hành dần, quay lui |

## Điều kiện bắt đầu

Đã xong L2 cho ít nhất [Order](../01-tutorials/l2/order.md) và [Payment](../01-tutorials/l2/payment.md).
