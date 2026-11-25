---
id: lap-roadmap-mvp
title: "Lập roadmap MVP"
type: how-to
level: L1
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Lập roadmap MVP cắt dọc theo module

Roadmap xếp theo **module** (giá trị và rủi ro). Layer chỉ xuất hiện ở tầng task bên trong mỗi giai đoạn. Đừng làm xong hết UI rồi hết API rồi hết DB: đến cuối mới ghép thì lỗi lộ muộn và tuần nào cũng không có gì để demo.

## Tám bước

1. **Viết mục tiêu đo được.** Có con số hoặc kết quả kiểm chứng được.
2. **Viết phạm vi, kể cả phần không làm.**
3. **Viết yêu cầu rồi mới suy ra phụ thuộc.** Xem [Phụ thuộc đến từ yêu cầu](../04-explanation/phu-thuoc-tu-yeu-cau.md).
4. **Xếp module theo giá trị và rủi ro.** Module cốt lõi và module rủi ro cao làm sớm. Việc rủi ro cao bắt đầu bằng một spike 1-2 ngày.
5. **Chia task theo layer trong mỗi module.** Mỗi task có người phụ trách và [mức giao AI](giao-viec-cho-ai.md), hai nhãn này tách biệt.
6. **Viết tiêu chí xong cho mỗi giai đoạn**, kèm một thứ demo được.
7. **Lập sổ rủi ro.** Mỗi rủi ro có khả năng, ảnh hưởng, cách giảm và người phụ trách.
8. **Thêm thời gian dự phòng và lịch rà soát.** 15-30% tùy kinh nghiệm của nhóm, rà soát hằng tuần.

Bảo mật và test có mặt trong **mọi** giai đoạn: threat model từ P0, mỗi lát cắt tự có test. Giai đoạn cuối chỉ rà soát tổng.

Dùng [mẫu kế hoạch triển khai](../05-templates/ke-hoach-trien-khai.md) để bắt đầu, rồi tự chấm bằng [8 tiêu chí](../03-reference/tieu-chi-ke-hoach.md).

## Ví dụ: roadmap 8 tuần cho app bán hàng

### Mục tiêu đo được (ví dụ)

- Khách đặt và thanh toán online được, kể cả khi chưa có tài khoản.
- 0 đơn lệch trạng thái giữa hệ thống và cổng thanh toán, kiểm bằng đối soát.
- Tỷ lệ đặt hàng lỗi do hệ thống dưới 1%.
- 95% lượt tạo đơn phản hồi dưới 800 ms.

### Ngoài phạm vi bản đầu

- App mobile, đa ngôn ngữ, tích điểm.
- Nhiều kho hàng, trả góp.
- Hóa đơn điện tử: cần hỏi kế toán về yêu cầu pháp lý trước khi phát hành thật.

### Dòng thời gian

| Tuần | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Giai đoạn | P0 | P1 | P1 | P2 | P2 | P3 | P4 | Dự phòng |

Test, bảo mật và review code chạy trong mọi giai đoạn.

### P0 · Nền móng (Tuần 1)

- **Mục tiêu:** Khung chạy được trên staging, CI tự chạy test, có threat model ban đầu.
- **Demo được:** Đẩy code lên, CI chạy test và quét thư viện, tự deploy staging.

| Phần | Việc | Phụ trách | Mức giao AI |
|---|---|---|---|
| Hạ tầng | Khởi tạo project, CI chạy lint, test và quét thư viện có lỗ hổng | Tech lead | AI làm |
| Kiến trúc | ADR đầu tiên: monolith theo layer, chọn database, chọn cổng thanh toán dự kiến | Tech lead | Người quyết |
| Bảo mật | Threat model ban đầu: dữ liệu nhạy cảm, điểm có thể bị tấn công | Tech lead | Người quyết |
| Dữ liệu | ERD bản đầu, migration cho products và inventory | Backend | AI nháp, người duyệt |
| Vận hành | Log có request ID, gom lỗi về một nơi | Backend | AI làm |

**Xong giai đoạn khi:** CI xanh, staging chạy, ADR và threat model đã được review, đã đăng ký tài khoản cổng thanh toán.

### P1 · Lát cắt Catalog và Order (Tuần 2-3)

- **Mục tiêu:** Khách (vãng lai hoặc đã đăng nhập) đặt được đơn "chờ thanh toán", tồn kho được giữ đúng.
- **Demo được:** Chọn hàng, đặt đơn, thấy đơn và số tồn giảm.

| Phần | Việc | Phụ trách | Mức giao AI |
|---|---|---|---|
| UI | Trang sản phẩm, giỏ, đặt hàng, đủ trạng thái loading, empty, error, dùng được bằng bàn phím | Frontend | AI làm |
| API | GET /products, POST /orders có Idempotency-Key, GET /orders có phân trang và chỉ trả đơn của mình | Backend | AI nháp, người duyệt |
| Service | Quy tắc tính tiền, chụp giá vào order_items | Backend | Người quyết |
| Dữ liệu | orders, order_items, giữ tồn kho có điều kiện | Backend | AI nháp, người duyệt |
| Auth | Đăng ký, đăng nhập bằng thư viện có sẵn, mật khẩu được hash, làm song song | Backend | Người quyết |
| Test | Unit cho tính tiền, integration cho POST /orders, 1 E2E luồng đặt hàng | QA | AI nháp, người duyệt |

**Xong giai đoạn khi:** API đúng contract. Hai request trùng key chỉ tạo một đơn. Hai người mua món cuối thì chỉ một người thành công.

### P2 · Payment (Tuần 4-5)

- **Mục tiêu:** Thu tiền thật an toàn, trạng thái đơn luôn khớp với cổng.
- **Demo được:** Thanh toán thành công, thất bại, đóng trình duyệt giữa chừng, webhook gửi hai lần: tất cả đều ra trạng thái đúng.

| Phần | Việc | Phụ trách | Mức giao AI |
|---|---|---|---|
| Spike | 1-2 ngày chạy thử sandbox, đọc tài liệu webhook và đối soát của cổng | Backend | Người quyết |
| Service | State machine cho Payment và Order, chỉ cho chuyển trạng thái hợp lệ | Backend | Người quyết |
| API | Webhook: kiểm chữ ký, chống trùng theo event_id | Backend | Người quyết |
| Job nền | Đối soát giao dịch chờ quá 15 phút, nhả hàng đơn hết hạn | Backend | AI nháp, người duyệt |
| UI | Trang chuyển sang cổng, trang kết quả: đang xử lý, thành công, thất bại | Frontend | AI làm |
| Test | Contract test với sandbox, test webhook trùng, trễ, sai chữ ký | QA | AI nháp, người duyệt |

**Xong giai đoạn khi:** Không có đơn "đã thanh toán" nào thiếu giao dịch thành công tương ứng. Xử lý lại cùng một webhook không làm đổi kết quả.

### P3 · Notify và khuyến mãi (Tuần 6)

- **Mục tiêu:** Email xác nhận gửi đúng một lần, voucher đúng quy tắc.
- **Demo được:** Đặt đơn có voucher, nhận email xác nhận.

| Phần | Việc | Phụ trách | Mức giao AI |
|---|---|---|---|
| Dữ liệu | Outbox: ghi sự kiện cùng transaction với cập nhật đơn | Backend | AI nháp, người duyệt |
| Job nền | Worker gửi email từ outbox, thử lại khi lỗi | Backend | AI làm |
| Service | Quy tắc voucher và miễn ship (core) theo spec | Backend + PO | Người quyết |
| Test | Voucher hết hạn, cộng dồn, đơn sát ngưỡng miễn ship | QA | AI nháp, người duyệt |

**Xong giai đoạn khi:** Mọi trường hợp trong spec voucher có test và đều qua. Email không gửi trùng khi worker chạy lại.

### P4 · Sẵn sàng phát hành (Tuần 7)

- **Mục tiêu:** Đo được, khôi phục được, quay lui được.
- **Demo được:** Chạy trọn luồng trên production với nhóm người dùng thử.

| Phần | Việc | Phụ trách | Mức giao AI |
|---|---|---|---|
| Vận hành | SLO ví dụ: 99,5% lượt đặt hàng thành công trong 30 ngày. Cảnh báo khi lỗi thanh toán trên 2% trong 10 phút | Tech lead | Người quyết |
| Vận hành | Diễn tập sao lưu và khôi phục, ghi RTO và RPO mục tiêu | Backend | AI nháp, người duyệt |
| Vận hành | Runbook xử lý sự cố thanh toán | Tech lead | AI nháp, người duyệt |
| Bảo mật | Rà soát cuối: thư viện, secret, phân quyền | Tech lead | Người quyết |
| Phát hành | Test tải luồng đặt hàng, deploy production có kế hoạch quay lui | Backend | AI nháp, người duyệt |

**Xong giai đoạn khi:** Đạt mục tiêu đo được ở trên trong môi trường staging, đã diễn tập khôi phục thành công, có runbook.

### Tuần 8 · Dự phòng

Khoảng 15%. Không xếp việc mới. Nhóm làm lần đầu nên dự phòng 20-30%.

### Sổ rủi ro

| Rủi ro | Khả năng | Ảnh hưởng | Cách giảm | Phụ trách |
|---|---|---|---|---|
| Cổng thanh toán duyệt tài khoản chậm | Vừa | Cao | Đăng ký từ tuần 1, spike sandbox ở P2 | Tech lead |
| Bán vượt tồn kho | Vừa | Cao | [Cập nhật tồn có điều kiện](chong-ban-vuot-ton-kho.md), test đồng thời | Backend |
| Webhook trùng, trễ hoặc mất | Cao | Cao | event_id duy nhất, state machine, đối soát | Backend |
| AI sinh code sai phân quyền | Vừa | Cao | [Checklist review](review-code-ai.md), test quyền sở hữu đơn | Reviewer |
| Ước lượng sai | Cao | Vừa | Tuần 8 dự phòng, rà soát 30 phút mỗi thứ Hai | PM |

Vai trò (Tech lead, Backend, Frontend, QA, PM) cần được thay bằng tên người thật.
