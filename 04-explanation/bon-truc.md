---
id: bon-truc
title: "Bốn trục để nhìn một hệ thống"
type: explanation
level: L1
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Bốn trục để nhìn một hệ thống

Mỗi đoạn code đều có thể được mô tả theo bốn trục cùng lúc. Nhầm trục này với trục kia là nguồn gốc của nhiều kế hoạch sai, ví dụ gọi "CRUD" là một layer hay gọi "thanh toán" là một domain.

| Trục | Trả lời câu hỏi | Ví dụ trong app bán hàng |
|---|---|---|
| **Layer** (tầng) | Code nằm ở đâu về mặt kỹ thuật? | UI, API, Service, Job nền, Repository, Database |
| **Module** (phân hệ) | Code phục vụ chức năng gì? | Catalog, Order, Payment, Auth, Notify |
| **Domain** (miền nghiệp vụ) | Phần này quan trọng thế nào với doanh nghiệp? | Core, supporting, generic, tùy doanh nghiệp |
| **Loại việc** | Đây là kiểu công việc gì? | Boilerplate, CRUD, business logic, tích hợp, test, bảo mật |

Thêm một nhóm nữa là **cross-cutting concern**: những thứ áp dụng cho mọi layer và module như log, bảo mật, xử lý lỗi và test. Chúng không nằm ở một ô cố định nào.

## Cách nhớ

- **Layer là chiều ngang**, như các tầng của một tòa nhà.
- **Module là chiều dọc**, như các căn hộ chạy từ tầng trệt lên tầng thượng.
- **Domain là bối cảnh** quyết định căn nào quan trọng nhất với chủ nhà.
- **Loại việc là kiểu công việc**, không phải một vị trí trong code.

## Vì sao điều này quan trọng khi vibe code

Kế hoạch nên cắt theo **module** (mỗi giai đoạn làm trọn một module qua mọi layer, gọi là vertical slice). Mức giao cho AI nên quyết theo **rủi ro**, mà rủi ro phụ thuộc vào cả module, domain và loại việc. Ví dụ: CRUD cho bảng sản phẩm thì giao AI được, còn CRUD cho bảng thanh toán thì phải duyệt kỹ.

Xem cả bốn trục trong một luồng thật ở [Luồng "Đặt hàng"](../01-tutorials/luong-dat-hang.md).
