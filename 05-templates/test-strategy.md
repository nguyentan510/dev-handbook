---
id: mau-test-strategy
title: "Mẫu test strategy"
type: template
level: L2
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Mẫu test strategy

## Khi nào dùng

Mục 7 của mỗi module. Quyết định test gì ở tầng nào, để không viết thừa E2E chậm mà vẫn thiếu test cho quy tắc quan trọng.

## Nguyên tắc

- **Unit test** cho quy tắc nghiệp vụ: nhiều, nhanh, chạy mỗi lần commit.
- **Integration test** cho API và database: vừa phải.
- **Contract test** cho chỗ nói chuyện với bên ngoài (cổng thanh toán, frontend).
- **E2E** chỉ cho vài luồng quan trọng nhất.
- Test được viết **cùng lát cắt** với tính năng, không dồn về cuối.

## Mẫu

```markdown
## Test strategy: <module>

| Tầng | Test gì | Công cụ | Ai viết |
|---|---|---|---|
| Unit | <quy tắc> | <...> | AI viết, người nêu trường hợp |
| Integration | <API + DB> | <...> | <...> |
| Contract | <với ai> | <...> | <...> |
| E2E | <luồng nào> | <...> | <...> |

Trường hợp biên bắt buộc:
- <...>

Test đồng thời hoặc bảo mật đặc biệt:
- <ví dụ: hai người mua món cuối; truy cập đơn của người khác>

Dữ liệu test: <tạo thế nào, không dùng dữ liệu thật>
Chạy ở đâu: <CI mỗi pull request, nightly>
```
