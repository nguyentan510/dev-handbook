---
id: mau-api-contract
title: "Mẫu API contract"
type: template
level: L2
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Mẫu API contract

## Khi nào dùng

Trước khi code một endpoint mới, để frontend, backend và AI cùng làm theo một thỏa thuận. Ví dụ đã điền: [API đặt hàng](../03-reference/api-dat-hang.md).

## Mẫu

```markdown
## <PHƯƠNG THỨC> /api/v1/<tài-nguyên>

Mục đích: <một câu>
Ai được gọi: <khách vãng lai, người đăng nhập, admin>
Quyền: <ví dụ: chỉ chủ sở hữu tài nguyên>
Idempotency: <có hoặc không, header nào>

Request:
- Header: <...>
- Body: <trường, kiểu, bắt buộc, ràng buộc>

Response thành công: <mã HTTP>, <các trường>

Lỗi:
| Mã HTTP | code | Khi nào |
|---|---|---|
| 400 | VALIDATION_FAILED | <...> |
| 404 | NOT_FOUND | <...> |
| 422 | <...> | <...> |

Phân trang: <cursor hoặc không>
Giới hạn tần suất: <ví dụ: 30 lần mỗi phút mỗi IP>
Contract test: <đường dẫn file test>
```
