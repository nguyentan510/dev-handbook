---
id: mau-spec
title: "Mẫu spec tính năng"
type: template
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Mẫu spec tính năng

Spec vừa là yêu cầu cho AI, vừa là tài liệu cho người đến sau. Một spec tốt đủ để người khác (hoặc AI) làm mà không phải hỏi lại.

## Khi nào dùng

Trước khi giao bất kỳ tính năng nào có quy tắc nghiệp vụ hoặc có rủi ro vừa trở lên.

## Mẫu

```markdown
## Tính năng: <tên>

Mục tiêu: <người dùng làm được gì, vì sao cần>

Quy tắc:
- <quy tắc 1, viết sao cho kiểm tra được>
- <quy tắc 2>

Trường hợp biên:
- <trường hợp 1> → <kết quả mong đợi>
- <trường hợp 2> → <kết quả mong đợi>

Lỗi trả về: <mã lỗi và khi nào>

Không làm: <những gì cố ý để ngoài>

Liên quan: <contract, ADR, module>

Xong là khi: <test nào phải qua, demo được gì>
```

## Ví dụ

```markdown
## Tính năng: Áp voucher khi đặt hàng

Mục tiêu: khách nhập mã, thấy giá giảm trước khi trả tiền.

Quy tắc:
- Mỗi đơn tối đa 1 voucher, không cộng dồn.
- Giảm tối đa 50% giá trị đơn.
- Voucher hết hạn hoặc hết lượt thì báo lỗi.

Trường hợp biên:
- Giỏ trống → không cho áp.
- Voucher hết hạn đúng lúc thanh toán → giữ giá lúc tạo đơn.
- Đơn đúng ngưỡng miễn ship sau khi giảm → tính theo giá sau giảm.

Lỗi trả về: 422 VOUCHER_INVALID.

Không làm: voucher theo nhóm khách.

Xong là khi: test cho mọi trường hợp trên đều qua.
```
