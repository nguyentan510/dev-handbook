---
id: thuat-ngu
title: "Bảng thuật ngữ"
type: reference
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---

# Bảng thuật ngữ

Nguồn chuẩn duy nhất cho thuật ngữ của dự án. Trang khác dùng đúng tên ở đây và dẫn link về, không tự định nghĩa lại. Trên trang web, bạn có thể tìm (có dấu hay không dấu đều được) và lọc theo nhóm.

<div data-widget="glossary"></div>

| Thuật ngữ | Tên khác | Nhóm | Định nghĩa | Ví dụ |
|---|---|---|---|---|
| **Frontend** | Phía người dùng | Cấu trúc | Phần người dùng nhìn thấy và thao tác, chạy trên trình duyệt hoặc điện thoại. | Trang giỏ hàng, nút Đặt hàng. |
| **Backend** | Phía máy chủ | Cấu trúc | Phần chạy trên server, xử lý nghiệp vụ và dữ liệu. | Tính tiền, lưu đơn. |
| **Fullstack** |  | Cấu trúc | Người hoặc ứng dụng làm cả frontend lẫn backend. | Tự làm cả form đặt hàng lẫn API lưu đơn. |
| **UI** | Giao diện | Cấu trúc | Layer hiển thị: màn hình, nút, form, bảng. | Form đăng nhập, danh sách đơn. |
| **API** |  | Cấu trúc | Cổng để hai phần mềm giao tiếp theo quy ước chung. | Giao diện gọi API để tạo đơn. |
| **Endpoint** | Điểm cuối | Cấu trúc | Một địa chỉ cụ thể của API, ứng với một thao tác. | POST /api/v1/orders. |
| **Controller** |  | Cấu trúc | Nhận request, kiểm tra cơ bản, gọi service rồi trả kết quả. | OrderController nhận yêu cầu đặt hàng. |
| **Service** | Lớp dịch vụ | Cấu trúc | Nơi chứa business logic. | OrderService tính tiền, áp voucher. |
| **Repository** | Lớp truy cập dữ liệu | Cấu trúc | Nơi gom việc đọc ghi dữ liệu. Nhiều dự án quy ước chỉ lớp này được chạm database, nhưng đây là một lựa chọn kiến trúc, không bắt buộc. | Hàm lưu đơn, tìm đơn theo mã. |
| **Job nền** | Background job, worker | Cấu trúc | Code chạy định kỳ hoặc chạy ngầm, không gắn với request của người dùng. | Đối soát thanh toán mỗi 5 phút. |
| **Database** | DB | Cấu trúc | Nơi lưu dữ liệu lâu dài, thường chia thành bảng. | Bảng orders, payments. |
| **Schema** | Lược đồ | Cấu trúc | Thiết kế cấu trúc dữ liệu: bảng, cột, ràng buộc. | orders có status, total. |
| **Migration** |  | Cấu trúc | Tập lệnh có phiên bản để thay đổi cấu trúc database có kiểm soát. | Thêm cột expires_at vào orders. |
| **Middleware** | Lớp trung gian | Cấu trúc | Code chạy trước khi request tới controller. | Kiểm tra token đăng nhập. |
| **Model / Entity** | Thực thể | Cấu trúc | Đối tượng đại diện cho một thứ có thật trong nghiệp vụ. | Order, Product. |
| **DTO** | Data Transfer Object | Cấu trúc | Dạng dữ liệu riêng để gửi qua lại giữa các layer hoặc qua API. | Dữ liệu tạo đơn không có các trường nội bộ. |
| **Component** | Thành phần giao diện | Cấu trúc | Mảnh UI đóng gói sẵn để dùng lại. | Thẻ sản phẩm. |
| **State** | Trạng thái | Cấu trúc | Dữ liệu ứng dụng đang giữ lúc chạy. | Số món trong giỏ. |
| **Dependency direction** | Chiều phụ thuộc | Cấu trúc | Phần nào được phép gọi, biết đến phần nào. Quy tắc nghiệp vụ không nên phụ thuộc chi tiết kỹ thuật. | Service không biết đang dùng PostgreSQL hay MySQL. |
| **Ports and adapters** | Hexagonal, clean architecture | Cấu trúc | Kiểu kiến trúc mà lõi nghiệp vụ định nghĩa giao diện nó cần, còn database và dịch vụ ngoài là adapter cắm vào. | Đổi cổng thanh toán chỉ cần viết adapter mới. |
| **Layer** | Tầng | Tổ chức | Lớp kỹ thuật theo chiều ngang: code nằm ở đâu. | UI, API, Service, Repository. |
| **Module** | Phân hệ | Tổ chức | Nhóm chức năng theo chiều dọc, cắt qua mọi layer. | Order, Payment. |
| **Feature** | Tính năng | Tổ chức | Một khả năng người dùng thấy được, thường nằm trong một module. | Áp voucher thuộc Order. |
| **Domain** | Miền nghiệp vụ | Tổ chức | Bối cảnh kinh doanh mà phần mềm phục vụ. | Thương mại điện tử. |
| **Core domain** | Miền cốt lõi | Tổ chức | Phần tạo lợi thế cạnh tranh. Tùy doanh nghiệp, không theo tên module. | Shop quà: gợi ý quà. Ví điện tử: thanh toán. |
| **Supporting domain** | Miền hỗ trợ | Tổ chức | Cần cho nghiệp vụ nhưng không tạo khác biệt. | Quản lý tồn kho. |
| **Generic domain** | Miền chung | Tổ chức | Doanh nghiệp nào cũng cần, nên ưu tiên giải pháp có sẵn. Generic vẫn có thể rủi ro cao. | Đăng nhập, gửi email, thường cả thanh toán. |
| **Business logic** | Quy tắc nghiệp vụ | Tổ chức | Các quy tắc riêng của việc kinh doanh, viết thành code. | Voucher không cộng dồn. |
| **Cross-cutting concern** | Mối quan tâm cắt ngang | Tổ chức | Thứ áp dụng cho mọi layer và module. | Log, bảo mật, test. |
| **Vertical slice** | Lát cắt dọc | Tổ chức | Làm trọn một chức năng từ UI xuống DB trong một lần. | P1 làm trọn luồng đặt hàng. |
| **Monolith** | Nguyên khối | Tổ chức | Toàn bộ ứng dụng triển khai chung một khối. | Một app chứa cả Order và Payment. |
| **Microservices** | Vi dịch vụ | Tổ chức | Nhiều dịch vụ nhỏ chạy độc lập, giao tiếp qua mạng. | Thường chưa cần cho MVP. |
| **Guest checkout** | Mua không cần đăng nhập | Tổ chức | Cho khách đặt hàng chỉ bằng email và số điện thoại. | Làm Order không phụ thuộc Auth. |
| **ERD** | Sơ đồ quan hệ thực thể | Dữ liệu và thanh toán | Sơ đồ các bảng và quan hệ giữa chúng. | orders 1–n order_items. |
| **Cardinality** | Bản số quan hệ | Dữ liệu và thanh toán | Một bản ghi bên này nối với bao nhiêu bản ghi bên kia: 1–1, 1–n, n–n. | products 1–1 inventory. |
| **Constraint** | Ràng buộc | Dữ liệu và thanh toán | Quy tắc database tự bảo vệ: duy nhất, khóa ngoại, điều kiện. | quantity phải lớn hơn 0. |
| **Transaction** | Giao dịch DB | Dữ liệu và thanh toán | Nhóm thao tác database thành công hết hoặc không có gì xảy ra. | Tạo đơn, món hàng và giữ tồn kho cùng lúc. |
| **Price snapshot** | Chụp giá | Dữ liệu và thanh toán | Lưu lại giá tại thời điểm mua để đơn cũ không đổi khi giá đổi. | order_items.unit_price_snapshot. |
| **Race condition** | Tranh chấp đồng thời | Dữ liệu và thanh toán | Lỗi khi hai thao tác chạy cùng lúc và kết quả phụ thuộc ai đến trước. | Hai người cùng mua món cuối. |
| **Idempotency** | Tính lũy đẳng | Dữ liệu và thanh toán | Làm lại một yêu cầu nhiều lần vẫn chỉ ra một kết quả. | Bấm đặt hàng hai lần chỉ tạo một đơn. |
| **Idempotency key** |  | Dữ liệu và thanh toán | Mã duy nhất client gửi kèm để server nhận ra yêu cầu lặp lại. | Header Idempotency-Key. |
| **State machine** | Máy trạng thái | Dữ liệu và thanh toán | Danh sách trạng thái và các bước chuyển được phép giữa chúng. | Đang chờ → Thành công, không được quay ngược. |
| **Webhook** |  | Dữ liệu và thanh toán | Hệ thống bên ngoài gọi ngược lại ứng dụng khi có sự kiện. | Cổng báo khách đã trả tiền. |
| **Reconciliation** | Đối soát | Dữ liệu và thanh toán | So khớp dữ liệu của mình với dữ liệu bên ngoài để tìm chỗ lệch. | Đối chiếu báo cáo cuối ngày của cổng. |
| **Eventual consistency** | Nhất quán sau cùng | Dữ liệu và thanh toán | Dữ liệu ở hai nơi có thể tạm lệch nhưng sẽ tự khớp lại. | Đơn "đang xử lý" vài giây trước khi webhook về. |
| **Outbox pattern** |  | Dữ liệu và thanh toán | Ghi sự kiện vào bảng outbox cùng transaction với thay đổi dữ liệu, rồi worker gửi đi sau. | Đã thanh toán thì chắc chắn có email. |
| **Boilerplate** | Code khung | Loại việc | Code lặp lại gần giống nhau ở mọi dự án. | Khởi tạo project, cấu hình. |
| **CRUD** |  | Loại việc | Bốn thao tác cơ bản: tạo, đọc, sửa, xóa. | Quản lý sản phẩm. |
| **Unit test** |  | Loại việc | Kiểm tra một hàm nhỏ chạy độc lập. | Hàm tính voucher. |
| **Integration test** | Test tích hợp | Loại việc | Kiểm tra nhiều phần phối hợp với nhau. | Gọi API tạo đơn rồi kiểm database. |
| **Contract test** |  | Loại việc | Kiểm tra hai bên vẫn đúng thỏa thuận API của nhau. | Phát hiện cổng đổi định dạng webhook. |
| **E2E test** | End-to-end | Loại việc | Kiểm tra cả luồng như người dùng thật. | Chọn hàng, đặt, thanh toán. |
| **Refactor** | Tái cấu trúc | Loại việc | Sắp xếp lại code mà không đổi hành vi. | Tách hàm tính tiền dài. |
| **Debug** | Gỡ lỗi | Loại việc | Tìm nguyên nhân và sửa lỗi. | Đơn bị tính sai khi dùng voucher. |
| **Spike** | Thử nghiệm ngắn | Loại việc | Việc thử 1-2 ngày để giảm bất định. | Chạy thử sandbox cổng thanh toán. |
| **Integration** | Tích hợp | Loại việc | Nối ứng dụng với dịch vụ bên ngoài. | Cổng thanh toán, dịch vụ email. |
| **Threat model** | Mô hình mối đe dọa | Loại việc | Liệt kê ai có thể tấn công, tấn công vào đâu và cách chặn. Làm từ đầu dự án. | Người lạ đoán mã đơn để xem đơn người khác. |
| **Roadmap** | Lộ trình | Kế hoạch | Các giai đoạn theo thời gian, làm gì trước, làm gì sau. | Roadmap 8 tuần ở trên. |
| **Phase** | Giai đoạn | Kế hoạch | Khoảng thời gian có mục tiêu và kết quả riêng. | P2 Payment. |
| **Milestone** | Mốc | Kế hoạch | Điểm kiểm tra: tới đây phải có thứ hoàn thành. | Cuối tuần 3 đặt được đơn. |
| **MVP** | Bản tối thiểu | Kế hoạch | Bản nhỏ nhất đủ để kiểm chứng giá trị với người dùng thật. | Đặt và trả tiền được, chưa có tích điểm. |
| **Scope** | Phạm vi | Kế hoạch | Làm gì và không làm gì. | Không làm app mobile ở bản đầu. |
| **Acceptance criteria** | Tiêu chí chấp nhận | Kế hoạch | Điều kiện để một tính năng được coi là đúng yêu cầu, nhìn từ phía người dùng. | Voucher hết hạn thì hiện thông báo rõ ràng. |
| **Definition of Done** | DoD | Kế hoạch | Điều kiện kỹ thuật để coi một task là xong. | Test qua, review xong, docs cập nhật. |
| **Backlog** | Danh sách việc chờ | Kế hoạch | Việc chờ làm, xếp theo ưu tiên. | Tích điểm, đánh giá sản phẩm. |
| **Dependency** | Phụ thuộc | Kế hoạch | Việc A xong thì việc B mới làm được. Nên xuất phát từ yêu cầu. | Bắt buộc đăng nhập thì Auth trước Order. |
| **Critical path** | Đường găng | Kế hoạch | Chuỗi việc phụ thuộc quyết định thời gian ngắn nhất của dự án. | Catalog, Order, Payment, phát hành. |
| **Buffer** | Thời gian dự phòng | Kế hoạch | Thời gian cộng thêm để chứa việc phát sinh. | Tuần 8 dự phòng. |
| **Risk register** | Sổ rủi ro | Kế hoạch | Bảng rủi ro kèm khả năng, ảnh hưởng, cách giảm và người phụ trách. | Bảng sổ rủi ro ở phần Roadmap. |
| **Owner** | Người chịu trách nhiệm | Kế hoạch | Một người cụ thể chịu trách nhiệm kết quả. Khác với việc ai hay AI viết code. | Backend lead phụ trách webhook. |
| **ADR** | Architecture Decision Record | Kế hoạch | Ghi chép một quyết định kiến trúc: bối cảnh, lựa chọn, lý do. | Vì sao chọn monolith. |
| **Sprint** |  | Kế hoạch | Chu kỳ làm việc 1-2 tuần, kết thúc bằng kết quả xem được. | Mỗi sprint một lát cắt. |
| **CI/CD** |  | Vận hành | Tự chạy test khi có code mới (CI) và tự đưa code lên môi trường (CD). | Đẩy code thì test chạy, qua thì deploy staging. |
| **Environment** | Môi trường | Vận hành | Nơi ứng dụng chạy, mỗi nơi có cấu hình riêng. | dev, staging, production. |
| **Staging** | Môi trường thử | Vận hành | Bản giống production để kiểm tra trước khi phát hành. | Test thanh toán bằng sandbox. |
| **Production** | Môi trường thật | Vận hành | Bản người dùng thật đang dùng. | Website đang bán hàng. |
| **Deploy** | Triển khai | Vận hành | Đưa code lên môi trường để chạy. | Deploy bản mới lên staging. |
| **Rollback** | Quay lui | Vận hành | Trả hệ thống về phiên bản trước khi bản mới lỗi. | Quay về bản hôm qua trong vài phút. |
| **Monitoring** | Giám sát | Vận hành | Theo dõi lỗi và hiệu năng để phát hiện sớm vấn đề. | Cảnh báo khi lỗi thanh toán tăng. |
| **Log** | Nhật ký | Vận hành | Bản ghi những gì hệ thống đã làm. | Mỗi lần gọi cổng và kết quả. |
| **Request ID** | Correlation ID | Vận hành | Mã gắn vào mỗi request để lần theo nó qua mọi log. | Tìm mọi log của một lần đặt hàng lỗi. |
| **SLI / SLO** | Chỉ số và mục tiêu mức dịch vụ | Vận hành | SLI là thứ đo được, SLO là mục tiêu cho thứ đó. | 99,5% lượt đặt hàng thành công trong 30 ngày. |
| **RTO / RPO** |  | Vận hành | RTO: tối đa bao lâu để khôi phục. RPO: tối đa mất bao nhiêu dữ liệu. | RTO 1 giờ, RPO 5 phút. |
| **Runbook** | Sổ tay vận hành | Vận hành | Hướng dẫn từng bước xử lý một sự cố cụ thể. | Cổng thanh toán ngừng hoạt động thì làm gì. |
| **Rate limit** | Giới hạn tần suất | Vận hành | Giới hạn số request trong một khoảng thời gian. | Tối đa 5 lần đăng nhập sai mỗi phút. |
| **Secret / API key** | Khóa bí mật | Vận hành | Chuỗi bí mật để truy cập dịch vụ, không viết vào code. | Khóa cổng để trong biến môi trường. |
| **Xác thực và phân quyền** | Authentication, authorization | Vận hành | Xác thực: bạn là ai. Phân quyền: bạn được làm gì. | Đăng nhập đúng nhưng chỉ xem được đơn của mình. |
| **PII** | Thông tin cá nhân | Vận hành | Dữ liệu nhận diện được một người, cần bảo vệ và hạn chế ghi log. | Email, số điện thoại, địa chỉ. |
| **Accessibility** | a11y, khả năng tiếp cận | Vận hành | Thiết kế để mọi người dùng được, kể cả người dùng bàn phím hoặc trình đọc màn hình. | Nút có nhãn rõ, đủ độ tương phản. |
| **Prompt** | Câu lệnh | Làm với AI | Yêu cầu viết cho AI. Càng cụ thể kết quả càng sát. | Tạo POST /orders theo contract trong docs/api. |
| **Context** | Ngữ cảnh | Làm với AI | Thông tin AI đang thấy: file, quy ước, yêu cầu. | Cho AI đọc AGENTS.md trước. |
| **AGENTS.md** | File ngữ cảnh | Làm với AI | File ở gốc dự án mô tả kiến trúc, lệnh, quy ước và điều cấm cho AI. | Mẫu ở phần Làm việc với AI. |
| **Spec** | Đặc tả | Làm với AI | Mô tả rõ thứ cần làm, kèm quy tắc và trường hợp biên. | Spec voucher ở phần Làm việc với AI. |
| **Hallucination** | Ảo giác AI | Làm với AI | AI bịa ra thứ không có thật nhưng nói rất tự tin. | Gọi một hàm không tồn tại. |
| **Code review** |  | Làm với AI | Đọc và kiểm tra code trước khi chấp nhận, kể cả code AI viết. | Dùng checklist review. |
| **Diff** |  | Làm với AI | Phần thay đổi so với phiên bản trước. | Xem AI sửa những dòng nào. |
| **Commit** |  | Làm với AI | Lưu một mốc thay đổi vào Git. | Commit sau mỗi task nhỏ. |

Thiếu một thuật ngữ? Thêm một dòng vào bảng này theo [cách viết tài liệu](../CONTRIBUTING.md).
