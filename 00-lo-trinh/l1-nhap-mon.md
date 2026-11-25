---
id: l1-nhap-mon
title: "L1 · Nhập môn"
type: roadmap
level: L1
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# L1 · Nhập môn: cắt lát hệ thống và lập roadmap MVP

## Học xong bạn làm được

1. Đọc một luồng tính năng và chỉ ra nó đi qua layer và module nào.
2. Phân biệt layer, module, domain và loại việc.
3. Biết phần nào rủi ro cao và nên giao cho AI đến đâu.
4. Hiểu vì sao thanh toán là quy trình bất đồng bộ.
5. Lập một roadmap MVP cắt dọc theo module, có mốc demo và sổ rủi ro.

## Thứ tự đọc

1. [Bốn trục để nhìn một hệ thống](../04-explanation/bon-truc.md)
2. [Luồng "Đặt hàng" đi qua những đâu](../01-tutorials/luong-dat-hang.md)
3. [Chiều phụ thuộc và kiến trúc](../04-explanation/chieu-phu-thuoc.md)
4. [Phân loại domain theo lợi thế cạnh tranh](../04-explanation/phan-loai-domain.md)
5. [Phụ thuộc đến từ yêu cầu](../04-explanation/phu-thuoc-tu-yeu-cau.md)
6. [Thanh toán là quy trình bất đồng bộ](../04-explanation/thanh-toan-bat-dong-bo.md)
7. [Lập roadmap MVP](../02-how-to/lap-roadmap-mvp.md)
8. [8 tiêu chí của một kế hoạch bài bản](../03-reference/tieu-chi-ke-hoach.md)
9. [Giao việc cho AI theo mức rủi ro](../02-how-to/giao-viec-cho-ai.md)
10. [Starter, scaffold, skeleton: khởi tạo dự án](../04-explanation/khoi-tao-du-an.md)

Tra cứu khi cần: [Thuật ngữ](../03-reference/thuat-ngu.md), [Mô hình dữ liệu](../03-reference/mo-hinh-du-lieu.md), [API đặt hàng](../03-reference/api-dat-hang.md), [Trạng thái đơn và thanh toán](../03-reference/trang-thai.md).

## Bài tập

1. **Vẽ luồng "Hủy đơn".** Dùng bản đồ layer × module, ghi từng bước đi qua ô nào và rủi ro ở đâu. Gợi ý: đơn đã thanh toán thì hủy kéo theo hoàn tiền.
2. **Phân loại domain cho một doanh nghiệp bạn biết.** Phần nào là core, vì sao?
3. **Chấm roadmap của chính bạn** bằng 8 tiêu chí. Viết lại phần đạt dưới mức "một phần".

## Tự kiểm tra

- Vì sao không thể ghi đơn hàng và giao dịch của cổng thanh toán trong cùng một transaction?
- Khi nào Auth phải làm trước Order, khi nào không cần?
- Vì sao "generic domain" vẫn có thể rủi ro cao?
- Hai người cùng mua món cuối cùng thì hệ thống làm gì để không bán vượt?
- Việc nào bạn không giao cho AI tự quyết, và vì sao?

Trả lời được cả năm câu thì chuyển sang [L2](l2-thiet-ke-mvp.md).
