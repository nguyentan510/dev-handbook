---
id: phan-loai-domain
title: "Phân loại domain theo lợi thế cạnh tranh"
type: explanation
level: L1
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Phân loại domain theo lợi thế cạnh tranh

Cùng một module, mỗi doanh nghiệp có thể xếp vào loại khác nhau. Đừng phân loại theo tên module, hãy hỏi: **phần nào làm khách chọn mình thay vì đối thủ?**

| Loại | Nghĩa | Nên làm gì |
|---|---|---|
| **Core** | Tạo lợi thế cạnh tranh | Tự thiết kế kỹ, người quyết, đầu tư nhiều nhất |
| **Supporting** | Cần cho nghiệp vụ, không tạo khác biệt | Làm vừa đủ, có thể giao nhiều cho AI |
| **Generic** | Doanh nghiệp nào cũng cần | Dùng giải pháp có sẵn, không tự chế |

## Hai doanh nghiệp, hai cách phân loại

| Module | Shop quà tặng | Ví điện tử có bán hàng |
|---|---|---|
| Khuyến mãi, gợi ý quà | **Core** | Supporting |
| Order, tồn kho | Supporting | Supporting |
| Payment | Generic | **Core** |
| Auth, Notify | Generic | Generic |

Tài liệu này dùng cột "shop quà tặng" làm ví dụ.

## Generic không có nghĩa là dễ

Thanh toán là generic với shop quà tặng, nhưng vẫn rủi ro rất cao: sai là mất tiền. "Generic" chỉ nói rằng bạn nên **dùng giải pháp có sẵn** (cổng thanh toán, thư viện xác thực), không nói rằng phần đó đơn giản hay giao hết cho AI được. Mức rủi ro được đánh giá riêng, xem [Giao việc cho AI](../02-how-to/giao-viec-cho-ai.md).
