<!--
---
id: trang-chu
title: "dev-handbook"
type: overview
level: chung
status: done
updated: 2026-11-25
review_by: 2027-02-25
owner: "(điền tên)"
---
-->

<img class="logo" src="assets/logo-mark.svg" alt="" width="88" height="88">

# dev-handbook

Tài liệu nhập môn cho Dev FullStack thời AI. Một tính năng như "Đặt hàng" đi qua nhiều layer và module. Biết nó đi qua đâu và rủi ro nằm ở chỗ nào thì mới lập kế hoạch đúng và giao việc cho AI đúng.

**Xem online:** https://nguyentan510.github.io/dev-handbook/

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img alt="Bản đồ luồng Đặt hàng: 9 bước đi qua 6 layer và 5 module, tô màu theo mức rủi ro" src="assets/hero-light.svg" width="100%">
</picture>

> Đây không phải blueprint production. Case study app bán hàng và mọi con số (thời gian, SLO, ngưỡng) là ví dụ minh họa.

## Hệ thống trong case study

Một app bán hàng online cho shop quà tặng: monolith chia theo layer, năm module, nói chuyện với hai dịch vụ bên ngoài. Màu là mức rủi ro của module.

```mermaid
flowchart LR
  K([Khách]) --> UI
  AD([Admin]) --> UI
  subgraph APP["Ứng dụng: monolith theo layer"]
    UI["UI"] --> API["API"]
    API --> CAT["Catalog<br/>sản phẩm, giỏ, tồn kho"]:::low
    API --> ORD["Order<br/>tạo đơn, tính tiền"]:::mid
    API --> PAY["Payment<br/>giao dịch, đối soát"]:::high
    API --> AUTH["Auth<br/>đăng nhập, phân quyền"]:::high
    ORD --> CAT
    ORD --> PAY
    PAY -- "sự kiện qua outbox" --> NOT["Notify<br/>email giao dịch"]:::low
    JOB["Job nền<br/>hết hạn, đối soát, gửi email"] --> PAY
  end
  CAT --> DB[("Database")]
  ORD --> DB
  PAY --> DB
  AUTH --> DB
  NOT --> DB
  PAY <--> GW(["Cổng thanh toán"])
  NOT --> MAIL(["Dịch vụ email"])
  classDef low fill:#d9f2e6,stroke:#0b7f56,color:#0b3d2a
  classDef mid fill:#fbeccf,stroke:#b06a00,color:#4d2f00
  classDef high fill:#f9d9de,stroke:#c02a40,color:#5c1020
```

## Luồng đặt hàng theo module

Bước 5 và bước 7 mỗi bước là một DB transaction. Gọi cổng thanh toán nằm ngoài transaction, nên cần webhook và đối soát. Chi tiết: [Luồng "Đặt hàng"](01-tutorials/luong-dat-hang.md).

```mermaid
flowchart TB
  subgraph B["Trình duyệt"]
    direction LR
    s1["1 · Bấm đặt hàng"]:::low
  end
  subgraph O["Order · transaction 1 ở bước 5"]
    direction LR
    s2["2 · Gửi request<br/>Idempotency-Key"]:::low --> s3["3 · Xác định<br/>người mua"]:::high --> s4["4 · Tính tiền"]:::high --> s5["5 · Giữ hàng,<br/>tạo đơn"]:::mid
  end
  subgraph P["Payment · transaction 2 ở bước 7"]
    direction LR
    s6["6 · Sang cổng<br/>thanh toán"]:::high --> s7["7 · Nhận webhook"]:::high
    s6 -. "webhook trễ hoặc mất" .-> s8["8 · Đối soát"]:::high
  end
  subgraph N["Notify"]
    direction LR
    s9["9 · Gửi email"]:::low
  end
  s1 --> s2
  s5 --> s6
  s7 --> s9
  s8 --> s9
  classDef low fill:#d9f2e6,stroke:#0b7f56,color:#0b3d2a
  classDef mid fill:#fbeccf,stroke:#b06a00,color:#4d2f00
  classDef high fill:#f9d9de,stroke:#c02a40,color:#5c1020
```

## Lộ trình học

```mermaid
flowchart LR
  L1["L1 · Nhập môn<br/>Đọc luồng, layer × module,<br/>roadmap MVP"]:::done --> L2["L2 · Thiết kế MVP<br/>Spec, ERD, API, threat model,<br/>test cho từng module"]:::wip --> L3["L3 · Production<br/>SLO, tracing, runbook,<br/>đối soát thật"]:::todo
  classDef done fill:#d9f2e6,stroke:#0b7f56,color:#0b3d2a
  classDef wip fill:#fbeccf,stroke:#b06a00,color:#4d2f00
  classDef todo fill:#eef0f2,stroke:#8a9399,color:#2b3135
```

Xanh: hoàn thành. Vàng: đang viết (4/5 module đã có bản nháp). Xám: mới có khung.

## Roadmap mẫu 8 tuần

Cắt dọc theo module, mỗi giai đoạn kết thúc bằng một thứ demo được. Chi tiết: [Lập roadmap MVP](02-how-to/lap-roadmap-mvp.md).

```mermaid
flowchart LR
  P0["P0 · Tuần 1<br/>Nền móng, CI,<br/>threat model"] --> P1["P1 · Tuần 2-3<br/>Catalog + Order"] --> P2["P2 · Tuần 4-5<br/>Payment"]:::high --> P3["P3 · Tuần 6<br/>Notify, voucher"] --> P4["P4 · Tuần 7<br/>Sẵn sàng phát hành"] --> B["Tuần 8<br/>Dự phòng"]:::buf
  X["Test, bảo mật, review code: trong mọi giai đoạn"]:::all
  classDef high fill:#f9d9de,stroke:#c02a40,color:#5c1020
  classDef buf fill:#ffffff,stroke:#8a9399,stroke-dasharray:4 3,color:#2b3135
  classDef all fill:#fbeccf,stroke:#b06a00,color:#4d2f00
```

## Tìm đúng trang

```mermaid
flowchart TB
  Q{"Bạn đang cần gì?"}
  Q -->|"Học, làm theo từng bước"| T["01-tutorials<br/>Hướng dẫn học"]
  Q -->|"Hiểu vì sao"| E["04-explanation<br/>Giải thích"]
  Q -->|"Làm một việc cụ thể"| H["02-how-to<br/>Cách làm"]
  Q -->|"Tra nhanh, chính xác"| R["03-reference<br/>Tra cứu"]
  Q -->|"Khung để điền"| M["05-templates<br/>Mẫu"]
  Q -->|"Làm việc với AI"| AI["06-ai"]
  Q -->|"Vì sao hệ thống như vậy"| D["decisions<br/>ADR"]
```

## Ba cấp độ

| Cấp | Tên | Học xong làm được gì | Trạng thái |
|---|---|---|---|
| L1 | [Nhập môn](00-lo-trinh/l1-nhap-mon.md) | Đọc luồng một tính năng, phân biệt layer, module, domain, lập roadmap MVP | Hoàn thành |
| L2 | [Thiết kế MVP thực tế](00-lo-trinh/l2-thiet-ke-mvp.md) | Tự viết spec, ERD, API contract, threat model, test strategy cho một module | Đang viết: 4/5 module có bản nháp |
| L3 | [Production và vận hành](00-lo-trinh/l3-production.md) | Đưa hệ thống có thanh toán thật lên production an toàn | Khung |

## Bắt đầu từ đâu

- **Người mới:** đọc [Lộ trình L1](00-lo-trinh/l1-nhap-mon.md), rồi đi theo [Luồng đặt hàng](01-tutorials/luong-dat-hang.md).
- **Cần tra một từ:** [Bảng thuật ngữ](03-reference/thuat-ngu.md).
- **Đang lập kế hoạch:** [Lập roadmap MVP](02-how-to/lap-roadmap-mvp.md), rồi tự chấm bằng [8 tiêu chí](03-reference/tieu-chi-ke-hoach.md).
- **Đang vibe code:** [Giao việc cho AI](02-how-to/giao-viec-cho-ai.md) và [Review code AI viết](02-how-to/review-code-ai.md).
- **Bắt đầu thiết kế một module:** [Khuôn module 10 mục](05-templates/khuon-module.md).

## Tài liệu được chia thế nào

Mỗi trang chỉ thuộc một loại, theo cách chia của Diátaxis. Trộn nhiều loại vào một trang làm người mới thấy rối, còn người cần tra cứu thì không tìm được.

| Thư mục | Loại | Dùng khi |
|---|---|---|
| `00-lo-trinh` | Lộ trình | Muốn biết học gì, theo thứ tự nào |
| `01-tutorials` | Hướng dẫn học | Học qua case study, làm theo từng bước |
| `02-how-to` | Cách làm | Cần làm một việc cụ thể |
| `03-reference` | Tra cứu | Cần tra nhanh, chính xác |
| `04-explanation` | Giải thích | Muốn hiểu vì sao |
| `05-templates` | Mẫu | Cần khung để điền |
| `06-ai` | Làm việc với AI | Nguyên tắc, file ngữ cảnh, prompt |
| `decisions` | Quyết định (ADR) | Muốn biết vì sao hệ thống được làm như vậy |

## Thông tin tài liệu

| | |
|---|---|
| Phiên bản | 1.5 ([nhật ký thay đổi](CHANGELOG.md)) |
| Người đọc | Người mới, junior, người vibe code, dev chuyển sang fullstack |
| Case study | App bán hàng online của một shop quà tặng (ví dụ) |
| Cách đóng góp | [Cách viết và bảo trì tài liệu](CONTRIBUTING.md) |
