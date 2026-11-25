---
id: luong-dat-hang
title: "Luồng "Đặt hàng" đi qua những đâu"
type: tutorial
level: L1
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Luồng "Đặt hàng" đi qua 6 layer và 5 module

Khách bấm "Đặt hàng" trên một app bán hàng online. Trang này đi qua từng việc xảy ra phía sau, và với mỗi việc chỉ ra nó thuộc [layer, module, domain và loại việc](../04-explanation/bon-truc.md) nào, rủi ro ra sao và nên giao cho AI đến đâu.

Trên trang web, bản đồ layer × module bên cạnh sẽ sáng lên theo bước bạn đang đọc. Trong bản Markdown, xem dòng "Ô trên bản đồ" ở mỗi bước.

<div data-widget="flow-map"></div>

Giả định: shop cho khách mua không cần đăng nhập ([ADR 0002](../decisions/0002-guest-checkout.md)), domain được phân loại theo cột "shop quà tặng" ở [Phân loại domain](../04-explanation/phan-loai-domain.md).

## Các bước

### 1. Khách xem giỏ và bấm Đặt hàng

- **Tầng:** UI
- **Module:** Catalog, Order
- **Domain:** Supporting
- **Loại việc:** UI
- **Rủi ro:** thấp
- **Ô trên bản đồ:** UI/Catalog, UI/Order

Giao diện cần đủ trạng thái: đang tải, giỏ trống, lỗi mạng. Khóa nút sau lần bấm đầu để tránh đặt hai lần. Dùng được bằng bàn phím và trình đọc màn hình.

> **Giao AI:** Giao AI. Bạn tự thử các trạng thái lỗi và thao tác bằng bàn phím.

### 2. Gửi request kèm Idempotency-Key

- **Tầng:** API
- **Module:** Order
- **Domain:** Supporting
- **Loại việc:** CRUD
- **Rủi ro:** thấp
- **Ô trên bản đồ:** API/Order

Gọi POST /api/v1/orders theo contract. Server kiểm tra dữ liệu đầu vào và trả lỗi theo mô hình lỗi thống nhất. Cùng một key gửi lại thì trả lại đúng đơn cũ.

> **Giao AI:** Giao AI theo contract đã viết. Bạn đọc kỹ phần kiểm tra đầu vào.

### 3. Xác định người mua

- **Tầng:** API, Service
- **Module:** Auth
- **Domain:** Generic
- **Loại việc:** Bảo mật
- **Rủi ro:** cao
- **Ô trên bản đồ:** API/Auth, Service/Auth, Repository/Auth

Theo yêu cầu B, khách vãng lai đặt được bằng email và số điện thoại. Nếu khách đăng nhập thì kiểm token. Sau này chỉ chủ đơn mới xem được đơn của mình.

> **Giao AI:** Người quyết. Dùng thư viện xác thực có sẵn, không để AI tự chế. Review từng dòng phần phân quyền.

### 4. Tính tiền theo quy tắc của shop

- **Tầng:** Service
- **Module:** Order
- **Domain:** Core
- **Loại việc:** Business logic
- **Rủi ro:** cao
- **Ô trên bản đồ:** Service/Order

Voucher không cộng dồn, đơn từ 500.000đ miễn phí ship, giảm tối đa 50%. Đây là quy tắc riêng của shop, AI không thể tự biết.

> **Giao AI:** Bạn viết spec quy tắc. AI viết code và test theo spec, bạn kiểm từng trường hợp biên.

### 5. Giữ hàng và tạo đơn trong một DB transaction

- **Tầng:** Service, Repository, DB
- **Module:** Catalog, Order, Payment
- **Domain:** Supporting
- **Loại việc:** CRUD, đồng thời
- **Rủi ro:** vừa
- **Ô trên bản đồ:** Service/Catalog, Repository/Catalog, Repository/Order, Repository/Payment, Database/Catalog, Database/Order, Database/Payment

Cùng một transaction: tạo đơn "chờ thanh toán", lưu món hàng kèm giá lúc mua, giữ tồn kho có điều kiện, tạo bản ghi thanh toán "đang chờ". Cổng thanh toán không nằm trong transaction này.

> **Giao AI:** AI viết phần CRUD. Bạn duyệt schema, ràng buộc và test hai người cùng mua món cuối.

### 6. Chuyển khách sang cổng thanh toán

- **Tầng:** Service, UI
- **Module:** Payment
- **Domain:** Generic
- **Loại việc:** Tích hợp
- **Rủi ro:** cao
- **Ô trên bản đồ:** Service/Payment, UI/Payment

Gọi cổng ngoài transaction để lấy đường dẫn thanh toán. Hết thời gian chờ thì giữ "đang chờ", không tự kết luận là thất bại. Trang kết quả chỉ hiển thị "đang xử lý" cho tới khi có webhook.

> **Giao AI:** Người quyết. Đọc tài liệu cổng, chạy thử sandbox trước.

### 7. Nhận webhook và cập nhật trạng thái

- **Tầng:** API, Service, DB
- **Module:** Payment, Notify
- **Domain:** Generic
- **Loại việc:** Tích hợp, bảo mật
- **Rủi ro:** rất cao
- **Ô trên bản đồ:** API/Payment, Service/Payment, Repository/Payment, Database/Payment, Repository/Notify, Database/Notify

Kiểm chữ ký. Lưu event_id, trùng thì bỏ qua. Chỉ chuyển trạng thái hợp lệ. Cập nhật đơn và ghi sự kiện gửi email vào outbox trong cùng một transaction.

> **Giao AI:** Người viết hoặc duyệt từng dòng. Test webhook trùng, đến trễ, sai chữ ký.

### 8. Đối soát và nhả hàng định kỳ

- **Tầng:** Job nền
- **Module:** Payment, Catalog
- **Domain:** Generic
- **Loại việc:** Vận hành
- **Rủi ro:** cao
- **Ô trên bản đồ:** Job nền/Payment, Job nền/Catalog

Mỗi vài phút hỏi lại cổng các giao dịch "đang chờ" quá 15 phút. Đơn hết hạn thì hủy và nhả tồn kho. Mỗi ngày đối chiếu với báo cáo của cổng.

> **Giao AI:** AI viết nháp job, bạn duyệt logic và cảnh báo khi phát hiện lệch.

### 9. Gửi email xác nhận

- **Tầng:** Job nền, Service
- **Module:** Notify
- **Domain:** Generic
- **Loại việc:** Tích hợp
- **Rủi ro:** thấp
- **Ô trên bản đồ:** Job nền/Notify, Service/Notify

Worker đọc outbox và gửi email, lỗi thì thử lại. Nhờ outbox, đơn đã thanh toán thì chắc chắn có email, và không gửi trùng.

> **Giao AI:** Giao AI. Kiểm không gửi nhầm người và không lộ thông tin không cần thiết.

### 10. Test và quan sát xuyên suốt

- **Tầng:** Mọi layer
- **Module:** Mọi module
- **Domain:** Mọi domain
- **Loại việc:** Test, log
- **Rủi ro:** cắt ngang
- **Ô trên bản đồ:** không cố định (cắt ngang)

Không nằm ở một ô cố định. Unit test cho quy tắc, integration test cho API và DB, contract test với cổng, vài E2E cho luồng chính. Mỗi request có request ID để lần theo trong log.

> **Giao AI:** AI viết test rất nhanh. Bạn nêu các trường hợp biên và tự đọc test của phần rủi ro cao.

## Đọc tiếp

- Vì sao bước 5 đến 8 được thiết kế như vậy: [Thanh toán là quy trình bất đồng bộ](../04-explanation/thanh-toan-bat-dong-bo.md)
- Dữ liệu phía sau: [Mô hình dữ liệu](../03-reference/mo-hinh-du-lieu.md) và [API đặt hàng](../03-reference/api-dat-hang.md)
- Biến luồng này thành kế hoạch: [Lập roadmap MVP](../02-how-to/lap-roadmap-mvp.md)
