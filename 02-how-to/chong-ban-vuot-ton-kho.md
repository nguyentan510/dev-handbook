---
id: chong-ban-vuot-ton-kho
title: "Chống bán vượt tồn kho"
type: how-to
level: L1
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Chống bán vượt tồn kho

## Vấn đề

Còn 1 hộp quà, hai khách bấm đặt cùng lúc. Nếu code đọc tồn kho, thấy còn 1, rồi mới trừ, thì cả hai đều thấy "còn 1" và cả hai đều đặt được. Đây là **race condition**.

## Cách làm: cập nhật có điều kiện

Gộp kiểm tra và giữ hàng vào một câu lệnh, để database tự xử lý tranh chấp:

```sql
UPDATE inventory
SET reserved = reserved + :qty
WHERE product_id = :id
  AND on_hand - reserved >= :qty;
-- 0 dòng bị ảnh hưởng: hết hàng, trả lỗi 422 OUT_OF_STOCK
```

Câu lệnh này chạy trong cùng transaction với việc tạo đơn. Nếu bất kỳ món nào hết hàng, rollback cả đơn.

Cách khác là khóa dòng bằng `SELECT ... FOR UPDATE` rồi mới cập nhật. Cách này rõ ràng hơn nhưng giữ khóa lâu hơn.

## Giữ hàng có hạn

- Đơn "chờ thanh toán" có `expires_at`, ví dụ 15 phút.
- Job nền định kỳ hủy đơn hết hạn và trả `reserved` về.
- Thanh toán thành công thì trừ `on_hand` và `reserved` cùng lúc.

## Test

Viết test chạy song song nhiều request mua món cuối cùng. Kết quả đúng: đúng một request thành công, các request còn lại nhận `OUT_OF_STOCK`, và `reserved` không bao giờ lớn hơn `on_hand`.

Mức giao AI: **AI nháp, người duyệt**. AI viết được câu lệnh, nhưng bạn phải tự đọc điều kiện WHERE và tự chạy test đồng thời.
