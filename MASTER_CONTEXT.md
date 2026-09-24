# MASTER_CONTEXT

> **Học phần:** Quản trị & Chiến lược Ngân hàng — Đại học Kinh tế TP. Hồ Chí Minh (UEH)  
> **Khung pháp lý & Chuẩn mực tham chiếu:** Luật Các Tổ chức Tín dụng số 32/2024/QH15, Luật Chứng khoán 2019, Thông tư 14/2025/TT-NHNN & Thông tư 41/2016/TT-NHNN (Tỷ lệ CAR), Hiệp ước An toàn Vốn Basel II / Basel III, Khung phân tích giám sát CAMEL(S).  
> **Nguyên tắc cốt lõi:** `DEFINE ONCE → EXPAND LATER → LINK WHEN NECESSARY` | `HIERARCHY FIRST → RELATIONSHIP SECOND → DETAIL LAST`

---

## 1. Entity Registry

| Entity ID | Tên Thực thể (Entity Name) | Nhóm Phân loại Thể chế | Định danh / Đại diện Tiêu biểu | Vai trò Cốt lõi trong Hệ thống |
| :---: | :--- | :--- | :--- | :--- |
| **[E1]** | **Ngân hàng Trung ương** (NHNN / SBV) | Quản lý Tiền tệ & Giám sát Hệ thống | Ngân hàng Nhà nước Việt Nam | Cơ quan ngang Bộ thuộc Chính phủ, điều hành CSTT, quản lý an toàn hệ thống TCTD; ban hành quy chuẩn CAR tối thiểu 8%, trần LDR 85%; thanh tra toàn diện CAMELS; Người cho vay cuối cùng (LoLR); yêu cầu Bức tường lửa (Firewalls). |
| **[E2]** | **Bộ Tài chính** (MoF) | Quản lý Tài chính công & TTCK | Bộ Tài chính Việt Nam (UBCKNN, Cục QLGSBH) | Quản lý ngân sách, tài sản công, nợ quốc gia; điều hành chính sách tài khóa, phát hành TPCP cung ứng Tài sản thanh khoản chất lượng cao (HQLA) cho hệ thống ngân hàng; trực tiếp quản lý TTCK và cấp phép, giám sát hoạt động của các CTCK qua UBCKNN. |
| **[E3]** | **Định chế nhận tiền gửi (NHTM cốt lõi)** | Depository Institutions | Vietcombank, BIDV, VietinBank, MB, Techcombank, ACB | Đặc quyền huy động tiền gửi cá nhân; độc quyền cung ứng dịch vụ thanh toán qua tài khoản; biến đổi kỳ hạn (Maturity Transformation); cỗ máy nhân bản bút tệ; bệ đỡ vốn rẻ trong Universal Banking; chủ thể thực thi quản trị rủi ro toàn diện theo khung CAMELS. |
| **[E4]** | **Bên thừa vốn (Surplus Units)** | Chủ thể Cung ứng Vốn & Đầu tư | Hộ gia đình, Cá nhân gửi tiền, Nhà đầu tư tổ chức, HNWIs | Cung ứng nguồn vốn nhàn rỗi cho nền kinh tế (Inflows tiền gửi); tìm kiếm lãi suất và bảo toàn gốc; đối tượng thụ hưởng tấm đệm an toàn vốn chữ C và thanh khoản chữ L; tham gia thị trường vốn qua cổ phiếu, trái phiếu, CCQ, ETFs. |
| **[E5]** | **Bên thiếu vốn (Deficit Units)** | Chủ thể Cầu vốn & Tổ chức Phát hành | Doanh nghiệp sản xuất kinh doanh, Tập đoàn, Chính phủ | Hấp thụ dòng tín dụng (Outflows tín dụng); nguồn gốc phát sinh rủi ro nợ xấu NPL (chữ A), tài sản sinh lời IEA (chữ E) và tài sản nhạy cảm lãi suất RSA (chữ S); huy động vốn dài hạn qua IPO/trái phiếu từ NHĐT. |
| **[E6]** | **Mạng lưới an toàn thể chế (Safety Net)** | Cơ chế Bảo vệ Niềm tin & Cứu trợ | Bảo hiểm Tiền gửi Việt Nam (DIV) & Cơ chế LoLR | Bảo vệ người gửi tiền nhỏ lẻ (hạn mức 125 triệu đồng); ngăn chặn hiệu ứng rút tiền hàng loạt (Bank Run) theo mô hình Diamond & Dybvig (1983); dập tắt sụp đổ dây chuyền khi hệ thống chịu cú sốc thanh khoản. |
| **[E7]** | **Định chế phi tiền gửi (Non-depository / NHĐT)** | Non-depository Institutions | Khối IB của CTCK (SSI, TCBS, Vietcap), Bulge Bracket (Goldman Sachs, Morgan Stanley), Quỹ đầu tư (Dragon Capital) | Kiến trúc sư thị trường vốn; cung cấp giải pháp tài chính "may đo" (customized), bảo lãnh phát hành, tư vấn M&A, môi giới, tự doanh Trading Book và quản lý tài sản; tuyệt đối BỊ CẤM nhận tiền gửi cá nhân và BỊ CẤM thanh toán qua tài khoản. |
| **[E8]** | **Định chế công nghệ & Nền tảng số (Fintech)** | Fintech Platforms & Super-Apps | Ví MoMo, ZaloPay, VNPay, Grab, Cake by VPBank, VCB Digibank | Cầu nối hạ tầng kỹ thuật phân phối sản phẩm số; khai thác Big Data & AI; cung cấp thanh toán, BNPL; kênh liên kết phân phối/chiến lược kinh doanh của NHTM; cạnh tranh P2P Lending; nguy cơ rút tiền mili-giây đe dọa thanh khoản. |

---

## 2. System Hierarchy

```text
HỆ THỐNG TÀI CHÍNH & MÔ HÌNH HOẠT ĐỘNG KINH DOANH NGÂN HÀNG
│
├── 1. TẦNG QUẢN LÝ VĨ MÔ & ĐIỀU TIẾT THỂ CHẾ
│   ├── [E1] Ngân hàng Trung ương (NHNN Việt Nam)
│   │   ├── 1.1 Vị thế pháp lý & Mục tiêu phi lợi nhuận (Cơ quan ngang Bộ)
│   │   ├── 1.2 Công cụ điều tiết CSTT (OMO, Tái cấp vốn, Dự trữ bắt buộc d=10%)
│   │   ├── 1.3 Khung giám sát an toàn (Chuẩn Basel, Thông tư 14/2025/TT-NHNN CAR ≥ 8%, trần LDR 85%, trần sở hữu CP Đ.63)
│   │   ├── 1.4 Khung thanh tra toàn diện CAMELS (Đánh giá sức khỏe tổng thể 6 khía cạnh)
│   │   ├── 1.5 Chức năng Người cho vay cuối cùng (LoLR cứu trợ thanh khoản Đ.192, 193)
│   │   └── 1.6 Thiết lập Bức tường lửa (Firewalls) ngăn ngừa rủi ro tự doanh lây lan sang NHTM
│   └── [E2] Bộ Tài chính (MoF)
│       ├── 2.1 Quản lý Tài chính công, Ngân sách & Trần nợ công quốc gia
│       ├── 2.2 Chính sách Tài khóa & Cung ứng Trái phiếu Chính phủ (Tài sản chuẩn HQLA cho đệm thanh khoản chữ L)
│       ├── 2.3 Cơ quan quản lý Nhà nước TTCK (UBCKNN) & Bảo hiểm (Cục QLGSBH)
│       │   ├── Cấp phép và giám sát hoạt động của các Công ty Chứng khoán / Khối IB
│       │   └── Giám sát tính minh bạch, công bố thông tin và phòng ngừa gian lận thị trường vốn
│       └── 2.4 Phối hợp vĩ mô Tài khóa - Tiền tệ (Kiểm soát hiệu ứng Crowding-out)
│
├── 2. TẦNG BẢO VỆ AN TOÀN HỆ THỐNG
│   └── [E6] Mạng lưới an toàn thể chế (Safety Net)
│       ├── 6.1 Sứ mệnh triệt tiêu trạng thái cân bằng xấu Diamond & Dybvig (1983)
│       ├── 6.2 Bảo hiểm tiền gửi (Hạn mức chi trả 125 triệu đồng cho cá nhân tại NHTM)
│       ├── 6.3 Cơ chế cho vay đặc biệt khẩn cấp hỗ trợ TCTD kiểm soát đặc biệt
│       └── 6.4 Giới hạn đạo đức (Moral Hazard) & Kỷ luật thị trường
│
├── 3. TẦNG TRUNG GIAN DẪN VỐN & VẬN HÀNH KINH DOANH CỐT LÕI
│   ├── [E4] Bên thừa vốn (Surplus Units)
│   │   ├── 4.1 Động cơ tài chính: Bảo toàn gốc 100%, tối ưu hóa lãi suất, thanh khoản cao
│   │   ├── 4.2 Dòng tiền Inflows tiền gửi: CASA không kỳ hạn (~0%), Tiết kiệm có kỳ hạn, Chứng chỉ tiền gửi (CDs)
│   │   ├── 4.3 Kênh phân bổ thị trường vốn: Mua cổ phiếu niêm yết, Trái phiếu DN, Chứng chỉ quỹ (CCQ), ETFs
│   │   └── 4.4 Rủi ro hệ thống: Rút tiền hàng loạt (Bank Run) khi ngân hàng suy giảm thanh khoản chữ L & Rủi ro biến động giá trên TTCK
│   │
│   ├── [E3] Định chế nhận tiền gửi (NHTM cốt lõi) ── [TRỤC ĐÀO SÂU CH02a, CH03 & CH04]
│   │   ├── 3.1 Vị thế pháp lý & Bản chất TCTD (Luật Các TCTD 2024: Cha-Con, Mục tiêu lợi nhuận, Độc quyền tiền gửi cá nhân & thanh toán)
│   │   ├── 3.2 Ba Chức năng Cốt lõi & Cơ chế Tạo tiền (Trung gian TC hóa giải Hicks 1939, Trung gian thanh toán, Tạo tiền bút tệ $S_n, S_\infty, k=1/d$)
│   │   ├── 3.3 Hệ thống phân loại NHTM (Sở hữu Big 4, 31 NHTMCP, Liên doanh, Ngoại; Chiến lược Bán buôn/Bán lẻ; Bản chất Ngân hàng số)
│   │   ├── 3.4 Cơ cấu tổ chức & Quản trị thượng tầng (Mạng lưới Hội sở/Chi nhánh/PGD; Mô hình 3 sảnh Front-Middle-Back; Ủy ban ALCO)
│   │   ├── 3.5 Bốn Hoạt động kinh doanh chủ yếu (Huy động vốn, Cấp tín dụng, Dịch vụ thanh toán/ngân quỹ, Kinh doanh khác)
│   │   ├── 3.6 Đánh đổi Rủi ro - Lợi nhuận & Phương pháp luận Tỷ số (Risk-Return Tradeoff, Số tuyệt đối vs Tỷ số, ROA & ROE, 3 Trụ cột phân tích)
│   │   ├── 3.7 Khung Phân tích Toàn diện CAMEL(S) (6 Khía cạnh sức khỏe ngân hàng: C-A-M-E-L-S)
│   │   └── 3.8 Hoạch định Chiến lược Kinh doanh Ngân hàng (Quy trình 11 Bước, Ma trận 3x3 GE/McKinsey & Kiểm tra Chiến lược)
│   │       ├── I. Tổng quan & Quan hệ Vĩ mô: Khái niệm, 3 câu hỏi cốt lõi, 4 tác dụng, Chiến lược vs Tác nghiệp, Mối liên hệ NHTM [E3] vs NHTW [E1]
│   │       ├── II. Điều kiện cần & Phân cấp Quản trị: 2 yêu cầu, 6 cơ sở nền tảng, 3 cấp hoạch định (HĐQT - Ban điều hành - Cơ sở), 3 quan hệ (Top-down, Phê duyệt, Bottom-up)
│   │       ├── III. Quy trình Hoạch định 11 Bước:
│   │       │   ├── Giai đoạn 1 (Bước 1-5): Mục tiêu & Chính sách, Thị trường mục tiêu (3 yếu tố), Phân khúc Doanh nghiệp [E5] (Lớn vs SME), Phân khúc Cá nhân [E4] (VIP vs Mass, AI/Big Data), Đặc điểm ngành (Cầu vs Cung)
│   │       │   ├── Giai đoạn 2 (Bước 6-9): Đánh giá SWOT & 4 câu hỏi rà soát, Vị thế cạnh tranh (3 trụ cột, Top 3 đối thủ), Đo lường tính hấp dẫn (10 thước đo), Phân tích môi trường PESTLE & Độ nhạy
│   │       │   └── Giai đoạn 3 (Bước 10-11): Ma trận Danh mục Thị trường Chiến lược (Ma trận 3x3, 9 ô định hướng, Cân đối dòng tiền), Kế hoạch Phân khúc 4Ps & Vòng lặp phản hồi
│   │       └── IV. Kiểm tra Chiến lược: Khái niệm, 3 mục đích cốt lõi, 3 chức năng điều chỉnh/nhận diện mâu thuẫn, 3 nguyên tắc tư tưởng (Tích cực, Không trừng phạt, Linh hoạt)
│   │
│   └── [E5] Bên thiếu vốn (Deficit Units - Tổ chức Phát hành)
│       ├── 5.1 Nhu cầu tài trợ dài hạn: Vốn lưu động, Máy móc thiết bị, Dự án hạ tầng, Mua bán sáp nhập (M&A)
│       ├── 5.2 Dòng tiền Outflows tín dụng: Tiếp nhận vốn vay; nguồn gốc tài sản sinh lời IEA và tài sản nhạy cảm lãi suất RSA
│       ├── 5.3 Kênh tiếp cận vốn trực tiếp: Thuê NHĐT bảo lãnh phát hành cổ phiếu IPO, Trái phiếu doanh nghiệp
│       └── 5.4 Nghĩa vụ pháp lý: Hoàn trả nợ vay (đối mặt nợ xấu NPL chữ A) hoặc nghĩa vụ trả lãi trái phiếu/cổ tức
│
└── 4. TẦNG ĐỊNH CHẾ CHUYÊN BIỆT & NỀN TẢNG SỐ MỞ RỘNG
    ├── [E7] Định chế phi tiền gửi (Non-depository / NHĐT) ── [TRỤC CHÍNH ĐÀO SÂU CH02b]
    │   ├── 7.1 Vị thế thể chế & Triết lý vận hành của NHĐT
    │   │   ├── Khái niệm: Định chế tài chính trung gian phi nhận tiền gửi chuyên cung cấp dịch vụ phức tạp cho DN lớn & chính phủ
    │   │   ├── Định nghĩa loại trừ Giuliano Iannotta: "Investment banking is the banking activity not classifiable as commercial banking"
    │   │   ├── Triết lý sản phẩm: Hàng "May đo" (Customized - thiết kế riêng bản) vs. Hàng "May sẵn" (Standardized đại trà của NHTM)
    │   │   └── 4 Đặc điểm cốt lõi: Hoạt động vì lợi nhuận, huy động vốn bằng chứng khoán của chính mình, trung gian thuần túy (NĐT tự chịu rủi ro vốn), vận hành bằng Danh tiếng (Reputation là tài sản quý giá nhất)
    │   ├── 7.2 So sánh đối chuẩn toàn diện: NHTM vs. NHĐT
    │   │   ├── Vai trò trung gian: Người gửi tiền - Người đi vay (NHTM) vs. Tổ chức phát hành - Nhà đầu tư (NHĐT)
    │   │   ├── Phân bổ rủi ro: NHTM chịu rủi ro tín dụng & thanh khoản; NHĐT chịu rủi ro danh tiếng (Reputation Risk)
    │   │   ├── Cơ cấu doanh thu & Bảng CĐKT: NHTM phụ thuộc NII (70-83%) trên Banking Book; NHĐT phụ thuộc Phí dịch vụ (~49%) và Tự doanh (~32%) trên Trading Book (Mark-to-Market)
    │   │   └── Khẩu vị rủi ro: NHTM khẩu vị thấp (bảo vệ người gửi tiền); NHĐT chấp nhận rủi ro rất cao (đầu cơ, phái sinh, cam kết chắc chắn)
    │   ├── 7.3 Bốn Hoạt động kinh doanh chủ yếu của NHĐT
    │   │   ├── I. Bảo lãnh phát hành (Securities Underwriting): Cổ phiếu IPO & Trái phiếu DN; 3 giá trị nghệ thuật (Mạng lưới Network, Kỹ năng định giá Pricing, Bảo chứng danh tiếng Reputation); 3 hình thức: Cam kết chắc chắn (Firm Commitment), Cố gắng tối đa (Best Effort), Tất cả hoặc không (All or None)
    │   │   ├── II. Dịch vụ Tư vấn tài chính (Financial Advisory): Tư vấn M&A (định giá, đàm phán, thâu tóm/phòng thủ), Tái cấu trúc doanh nghiệp (Corporate Restructuring); do khối IB của CTCK đảm nhiệm
    │   │   ├── III. Môi giới (Brokerage) & Tự doanh (Proprietary Trading): Khớp lệnh thu hoa hồng, dịch vụ Margin; Tự doanh dùng vốn tự có tìm kiếm lợi vốn (Capital Gain) trên Trading Book
    │   │   └── IV. Dịch vụ Quản lý tài sản (Asset Management): Dòng tiền Quỹ đầu tư (mua CCQ ➔ đầu tư đa tài sản ➔ phân phối lợi tức ➔ thu phí QLQ); Hóa giải 3 rào cản NĐT nhỏ lẻ (Vốn ít, Phí cao, Thiếu chuyên môn); Hệ thống quỹ (Mutual Funds, Hedge Funds, Venture Capital) & Tiêu điểm Quỹ hoán đổi danh mục (ETF)
    │   ├── 7.4 Các định chế toàn cầu Bulge Bracket & Kiểm soát xung đột lợi ích
    │   │   ├── Nhóm Bulge Bracket Phố Wall & Châu Âu: Goldman Sachs, JP Morgan Chase, Barclays, BofA Merrill Lynch, Morgan Stanley, Deutsche Bank, Credit Suisse, UBS, HSBC
    │   │   ├── Lợi thế cạnh tranh: Mạng lưới khách hàng tổ chức khổng lồ, năng lực bao tiêu hàng chục tỷ USD & Rào cản danh tiếng
    │   │   └── Bức tường Trung Hoa (Chinese Walls): Cách ly tuyệt đối thông tin giữa khối Tư vấn M&A/Bảo lãnh (nắm thông tin nội gián riêng tư) và khối Tự doanh/Môi giới/Nghiên cứu (giao dịch công khai)
    │   └── 7.5 Chiến lược thực thi tại Việt Nam: Mô hình Universal Banking
    │       ├── Đánh giá 3 lựa chọn: NHTM thuần túy (vốn rẻ nhưng NIM hẹp), NHĐT thuần túy (thị trường vốn chưa đủ sâu, khung pháp lý chưa có NHĐT độc lập), Mô hình Hỗn hợp Universal Banking
    │       ├── Khuyến nghị tối ưu cho nhà đầu tư nhiều vốn: Thiết lập Tập đoàn Universal Banking 3 chân kiềng (NHTM nền tảng vốn CASA rẻ + CTCK/IB + CTQL Quỹ)
    │       ├── Bán chéo (Cross-selling) trọn vòng đời DN: Khởi nghiệp vay tín dụng SME ➔ Tăng trưởng IPO/Trái phiếu ➔ M&A mở rộng ➔ Quản lý tài sản gia tộc
    │       └── Minh họa thực tiễn: Techcombank - TCBS - Techcom Capital; Vietcombank - VCBS - VCBF
    │
    └── [E8] Định chế công nghệ & Nền tảng số (Fintech & Super-Apps)
        ├── 8.1 Vị thế hệ sinh thái: Cầu nối hạ tầng kỹ thuật (Platform), Open API, Phân tích dữ liệu lớn (Big Data)
        ├── 8.2 Chiến lược Siêu ứng dụng (Super-App): Tích lũy hành vi khách hàng, giữ chân người dùng trọn đời
        ├── 8.3 Phân định bản chất sản phẩm & Ngân hàng số:
        │   ├── Ngân hàng số (Cake by VPBank, VCB Digibank): Kênh phân phối/chiến lược của ngân hàng mẹ
        │   ├── Tiết kiệm Online liên kết: Vốn chuyển về NHTM đối tác (ĐƯỢC Bảo hiểm tiền gửi)
        │   ├── Túi hợp tác kinh doanh: Bản chất ủy thác đầu tư (KHÔNG ĐƯỢC Bảo hiểm tiền gửi)
        │   ├── P2P Lending: Rủi ro bùng nợ người cho vay tự chịu (kém an toàn hơn NHTM cam kết trả nợ 100%)
        │   └── Mua trước trả sau (BNPL): Bản chất cấp tín dụng tiêu dùng tín chấp
        └── 8.4 Rủi ro trồi hiện: Rút tiền Mili-giây qua Bot API đánh sập giả định LCR 30 ngày của Basel III
```

---

## 3. Entity Knowledge

### [E1] Ngân hàng Trung ương (NHNN Việt Nam)
- **Bản chất & Vị thế:** Cơ quan ngang Bộ thuộc Chính phủ, thực hiện chức năng quản lý nhà nước về tiền tệ, hoạt động ngân hàng và ngoại hối; thực hiện chức năng của Ngân hàng Trung ương về phát hành tiền, ngân hàng của các tổ chức tín dụng và cung ứng dịch vụ tiền tệ cho Chính phủ. Hoạt động phi thương mại, hoàn toàn không vì mục tiêu lợi nhuận.
- **Công cụ điều hành CSTT:** 
  - Nghiệp vụ thị trường mở (OMO) bơm/hút thanh khoản ngắn hạn.
  - Tái cấp vốn và cho vay chiết khấu giấy tờ có giá.
  - Quy định tỷ lệ Dự trữ bắt buộc (RRR, ví dụ $d = 10\%$) kiểm soát hệ số nhân tiền $k = 1/d$.
  - Quản lý hạn mức tăng trưởng tín dụng (Room tín dụng) định hướng dòng vốn vào các lĩnh vực ưu tiên và kiểm soát lạm phát.
- **Khung an toàn thể chế & Thanh tra giám sát CAMELS:**
  - Quy chuẩn an toàn vốn tối thiểu: CAR ≥ 8% theo Thông tư 14/2025/TT-NHNN và Thông tư 41/2016/TT-NHNN (Basel II/III).
  - Khống chế trần tỷ lệ dư nợ cho vay trên tổng tiền gửi (LDR ≤ 85%) và các tỷ lệ thanh khoản LCR, NSFR.
  - Áp dụng khung thanh tra toàn diện CAMELS (Capital, Asset Quality, Management, Earnings, Liquidity, Sensitivity to Market Risk) để xếp hạng và giám sát mức độ lành mạnh của các NHTM.
  - Giảm tỷ lệ sở hữu cổ phần nhằm triệt tiêu sở hữu chéo: Cổ đông cá nhân ≤ 5%, cổ đông tổ chức ≤ 10%, cổ đông và người có liên quan ≤ 15% (Điều 63 Luật Các TCTD 2024).
  - Giới hạn cấp tín dụng cho một khách hàng và người có liên quan theo lộ trình giảm dần (Điều 136).
- **Chức năng Người cho vay cuối cùng (LoLR):**
  - Cung cấp cho vay đặc biệt đối với TCTD bị rút tiền hàng loạt hoặc đặt vào tình trạng kiểm soát đặc biệt (Điều 192, 193).
  - Ngăn ngừa nguy cơ đổ vỡ thanh khoản dây chuyền (Systemic Contagion), đồng thời duy trì giám sát vi mô để hạn chế Rủi ro đạo đức (Moral Hazard).
- **Yêu cầu Bức tường lửa (Firewalls):**
  - Bắt buộc các tập đoàn tài chính/NHTM mẹ phải thiết lập ranh giới độc lập về vốn, nhân sự và hạch toán giữa ngân hàng nhận tiền gửi và các công ty con kinh doanh chứng khoán, đầu tư mạo hiểm; ngăn chặn rủi ro tự doanh thua lỗ lây lan sang làm sụp đổ ngân hàng mẹ.

### [E2] Bộ Tài chính (MoF)
- **Bản chất & Vai trò:** Cơ quan thuộc Chính phủ quản lý nền tài chính quốc gia, ngân sách nhà nước, thuế, hải quan, tài sản công, nợ công và dự trữ tài chính nhà nước. Quản lý vĩ mô hướng tới phân bổ nguồn lực công và ổn định phát triển kinh tế - xã hội.
- **Công cụ & Cơ chế điều hành:**
  - Chính sách tài khóa: Thu thuế, phân bổ chi thường xuyên và giải ngân đầu tư công.
  - Phát hành Trái phiếu Chính phủ (TPCP) bù đắp bội chi ngân sách và tài trợ dự án quốc gia.
  - Cung ứng Tài sản thanh khoản chất lượng cao (HQLA) cho hệ thống ngân hàng; định hình đường cong lợi suất phi rủi ro (Risk-free Benchmark Yield Curve) làm căn cứ định giá toàn bộ thị trường tài chính; cung cấp lớp đệm tài sản an toàn cho chữ L (Liquidity) của các NHTM.
- **Phạm vi quản lý chuyên ngành đối với Thị trường Chứng khoán:**
  - Trực tiếp quản lý Nhà nước đối với Thị trường Chứng khoán thông qua Ủy ban Chứng khoán Nhà nước (UBCKNN).
  - Cấp phép, quản lý và thanh tra toàn diện hoạt động của các Công ty Chứng khoán (đóng vai trò NHĐT tại Việt Nam) và các Công ty Quản lý quỹ theo Luật Chứng khoán 2019.
  - Giám sát việc phát hành chứng khoán ra công chúng, hồ sơ IPO, niêm yết và giao dịch trên các Sở giao dịch chứng khoán (HOSE, HNX).
  - Bảo đảm tính công khai, minh bạch, công bằng của thị trường; phát hiện và xử lý các hành vi thao túng giá, giao dịch nội gián (Insider Trading).
- **Phối hợp vĩ mô Tài khóa - Tiền tệ:** Phối hợp nhịp nhàng với NHNN để duy trì thanh khoản hệ thống, tránh hiện tượng phát hành nợ công quá mức gây hiệu ứng chèn lấn nguồn vốn tín dụng của khu vực tư nhân (Crowding-out effect).

### [E3] Định chế nhận tiền gửi (NHTM cốt lõi)
- **Vị thế pháp lý & Bản chất TCTD (Luật Các TCTD 2024):**
  - *Quan hệ Cha - Con:* TCTD là khái niệm mẹ/rộng; NHTM là loại hình TCTD đặc thù được thực hiện đầy đủ toàn bộ hoạt động ngân hàng vì mục tiêu tối đa hóa lợi nhuận.
  - *Hai thành trì độc quyền tối thượng:* Độc quyền nhận tiền gửi từ cá nhân (nguồn vốn rẻ nhất CASA ~0%) và Độc quyền cung ứng dịch vụ thanh toán qua tài khoản (vốn pháp định tối thiểu 3.000 tỷ, thực tế 40.000 - 80.000 tỷ).
  - *Phân định rạch ròi các định chế khác:* TCTD phi ngân hàng bị CẤM nhận tiền gửi cá nhân và CẤM mở tài khoản thanh toán; Tổ chức tài chính vi mô chỉ cho vay hộ nghèo/SME; QTDND tương trợ nội bộ.
- **Ba Chức năng Cốt lõi & Bốn Hoạt động Kinh doanh:**
  - *Trung gian Tài chính:* Hóa giải xung đột kỳ hạn Hicks (1939) ("Constitutional Weakness"); phân tán rủi ro; cỗ máy tạo thu nhập NIM/Spread (chiếm 70-80% lợi nhuận); ưu thế cam kết hoàn trả 100% trước P2P Lending.
  - *Trung gian Thanh toán:* Thủ quỹ của nền kinh tế; đảm bảo huyết mạch giao dịch thương mại; nhận lương thực chất là gửi CASA giá rẻ.
  - *Tạo tiền bút tệ (Money Creation):* Công thức cấp số nhân $S_n = \frac{U(1-q^n)}{1-q}$; hệ số nhân $k = 1/d = 10$; $S_\infty = U/d$; các yếu tố rò rỉ (dự trữ vượt mức, rút tiền mặt).
  - *Bốn hoạt động kinh doanh:* Huy động vốn (CASA, tiết kiệm, GTCG); Cấp tín dụng (Cho vay, Bảo lãnh, Leasing, Factoring, Chiết khấu); Dịch vụ thanh toán & ngân quỹ; Hoạt động khác (Bancassurance, kinh doanh ngoại hối, ngân hàng giám sát).
- **Cơ cấu Tổ chức & Ủy ban ALCO:** Hội sở (Back/Middle Office), Chi nhánh (Front Office), PGD; Mô hình 3 sảnh Front - Middle độc lập - Back; Ủy ban ALCO (CFO làm Chủ tịch) quyền lực nhất điều phối ALM, LCR/NSFR, IRRBB, FTP.
- **Quản trị Hoạt động Kinh doanh & Khung Phân tích CAMEL(S) (Đào sâu từ CH03):**
  - *1. Nguyên lý Đánh đổi Rủi ro - Lợi nhuận (Risk-Return Tradeoff):* Lợi nhuận càng cao thì rủi ro càng lớn; quản trị ngân hàng là nghệ thuật cân bằng giữa tối đa hóa lợi nhuận cho cổ đông (ROE) và bảo đảm an toàn hệ thống (Solvency & Liquidity).
  - *2. Phương pháp luận Chỉ số tỷ số (Ratio Analysis):*
    + Số tuyệt đối chỉ phản ánh quy mô (Ví dụ: Vietcombank năm 2025 có tổng tài sản hơn 2,4 triệu tỷ đồng ~ 93 tỷ USD, xấp xỉ 1/5 GDP Việt Nam), nhưng bất lực trong việc phản ánh hiệu quả vận hành.
    + Chỉ số tỷ số giúp chuẩn hóa quy mô, cho phép đối chuẩn khách quan giữa các ngân hàng.
    + 3 Trụ cột phân tích: Phân tích xu hướng (Trend Analysis 3-5 năm), Phân tích đối chuẩn (Benchmarking so với Peer Group và Industry Average), và Phân tích cấu trúc Bảng CĐKT & Khẩu vị rủi ro (Risk Appetite).
  - *3. Chữ C (Capital Adequacy - An toàn vốn):*
    + Tử số: Vốn tự có (Regulatory Capital) gồm Vốn cấp 1 (Tier 1 core capital: vốn điều lệ, thặng dư vốn, quỹ dự trữ, LN chưa phân phối) và Vốn cấp 2 (Tier 2 nợ thứ cấp dài hạn).
    + Mẫu số: Tổng tài sản có rủi ro (Risk-Weighted Assets - RWA) gồm tài sản nội bảng và ngoại bảng nhân hệ số rủi ro tương ứng $w_i$.
    + *Ví dụ "Ly nước mía" của giảng viên:* Cam kết ngoại bảng (bảo lãnh, L/C, cam kết cho vay) giống như lời hứa bao 70 bạn ly nước mía 10k (tổng 700k) khi ví chỉ có 500k; hiện tại chưa phát sinh dòng tiền ra nhưng chỉ cần điều kiện kích hoạt xảy ra là lập tức biến thành nghĩa vụ chi trả thực tế ➔ Bắt buộc phải nhân hệ số chuyển đổi và tính vào RWA.
    + *Ẩn dụ "Ăn kem - Chạy bộ":* Nhà quản lý không cấm ngân hàng kinh doanh mảng rủi ro cao để kiếm lời lớn (ăn kem), nhưng luật chơi là ăn 1 cây kem thì phải chạy bộ 2 km (cổ đông phải nộp thêm vốn tự có tương ứng vào tử số). Đây là cơ chế điều tiết rủi ro tự động bằng chính túi tiền cổ đông.
    + Chuẩn CAR: Basel quy định CAR $\ge 8\%$; Việt Nam (Thông tư 14/2025/TT-NHNN) quy định tối thiểu 8%.
    + Bất đối xứng thông tin & Proxy Indicator: Chuyên gia bên ngoài dùng chỉ số thay thế nhanh *Vốn chủ sở hữu / Tổng tài sản (Equity / Assets)* để đo mức độ đòn bẩy.
  - *4. Chữ A (Asset Quality - Chất lượng tài sản):*
    + Khía cạnh khó phân tích nhất do bất đối xứng thông tin, người ngoài chỉ thấy số liệu dư nợ thô.
    + Tỷ trọng dư nợ theo ngành/địa bàn: Nhận diện mức độ tập trung rủi ro vào các lĩnh vực nhạy cảm chu kỳ (Bất động sản, xây dựng, BOT hạ tầng).
    + Tỷ lệ nợ xấu (NPL Ratio) = Nợ nhóm 3, 4, 5 / Tổng dư nợ $\times 100$ (ngưỡng an toàn chuẩn < 3%).
    + Tỷ lệ dự phòng RRTD / Dư nợ và Tỷ lệ bao phủ nợ xấu ($LLR = \text{Dự phòng} / \text{NPL} \times 100$): Đo lường độ dày tấm đệm phòng thủ; LLR > 100% (hoặc 200% như Vietcombank) cho thấy khả năng hấp thụ rủi ro tín dụng vượt trội mà không làm tổn thương vốn tự có.
  - *5. Chữ M (Management Soundness - Lành mạnh quản trị):*
    + Đánh giá định tính: Văn hóa kiểm soát rủi ro, chiến lược kinh doanh, năng lực thượng tầng HĐQT/Ban điều hành.
    + Đánh giá định lượng:
      * Tỷ lệ chi phí (CIR - Cost-to-Income Ratio) = Tổng chi phí hoạt động / Tổng thu nhập hoạt động $\times 100$; CIR càng thấp (chuẩn tốt 30% - 40%) thể hiện vận hành càng tinh gọn, ứng dụng chuyển đổi số thành công.
      * Thu nhập trên một nhân viên = Lợi nhuận trước thuế / Tổng số nhân viên; thước đo năng suất lao động.
      * Tốc độ mở rộng chi nhánh/PGD: Sự đánh đổi giữa chiếm lĩnh thị phần và gia tăng chi phí cố định/rủi ro quản trị phân tán.
  - *6. Chữ E (Earnings & Profitability - Thu nhập & Lợi nhuận):*
    + Cơ cấu thu nhập: Thu nhập từ Lãi (NII chiếm 70% - 80% lợi nhuận) vs Thu nhập ngoài lãi (Phí dịch vụ, thanh toán, FX, kinh doanh chứng khoán, Bancassurance).
    + 5 chỉ tiêu tài chính cốt lõi:
      * $ROA = \frac{\text{LNST}}{\text{Tổng tài sản bình quân}} \times 100$ (chuẩn Mỹ > 1%, VN 1% - 2%).
      * $ROE = \frac{\text{LNST}}{\text{Vốn CSH bình quân}} \times 100$ (chuẩn tốt 15% - 20%). Mô hình DuPont: $ROE = ROA \times EM$.
      * $NIM = \frac{\text{Thu nhập lãi thuần (NII)}}{\text{Tổng tài sản sinh lời BQ (IEA)}} \times 100$ (VN thường 3% - 4.5%).
      * $NIIR = \frac{\text{Thu nhập lãi thuần}}{\text{Tổng thu nhập thuần}} \times 100$ (mức độ phụ thuộc vào tín dụng).
      * $\text{Earning Spread} = \text{Lãi suất đầu ra BQ} - \text{Lãi suất đầu vào BQ}$.
  - *7. Chữ L (Liquidity Indicators - Phân tích khả năng thanh khoản):*
    + Bản chất dòng tiền: Inflows (tiền gửi vào) vs Outflows (rút tiền & giải ngân cho vay). Mục tiêu kép: Sẵn sàng chi trả tiền gửi và đáp ứng cam kết tín dụng với chi phí vốn tối ưu.
    + Tỷ lệ tài sản thanh khoản = (Tiền mặt & tương đương + Tiền gửi NHNN) / Tổng tài sản.
    + Tỷ lệ LDR truyền thống = $\frac{\text{Tổng dư nợ cho vay}}{\text{Tiền gửi khách hàng}} \times 100$: Tiền gửi liên ngân hàng KHÔNG được tính vào mẫu số do tính chất ngắn hạn, biến động.
    + Thực tiễn VN 2025: Khối Big 4 LDR < 100% (90% - 95%) nhờ tiền gửi dân cư dồi dào; Khối NHTMCP tư nhân LDR truyền thống vọt lên rất cao (> 100%).
    + Tỷ lệ LDR mở rộng = $\frac{\text{Tổng dư nợ cho vay}}{\text{Tiền gửi KH} + \text{Tiền gửi/Vay TCTD khác} + \text{Phát hành GTCG}} \times 100$: Kéo LDR tư nhân về 77% - 90% nhưng chi phí vốn cao và kém ổn định.
    + Xung đột mục tiêu: An toàn xã hội (NHNN muốn thanh khoản cao, LDR thấp) vs Tối ưu hóa cổ đông (Ngân hàng muốn cho vay tối đa đẩy LDR cao để tăng ROE).
  - *8. Chữ S (Sensitivity to Market Risk - Độ nhạy rủi ro thị trường):*
    + Rủi ro thị trường: Biến động giá chứng khoán Trading Book, rủi ro tỷ giá do Trạng thái ngoại tệ mở (NOP).
    + Rủi ro lãi suất (IRRBB) & Khe hở lãi suất: $GAP = RSA - RSL$ (Tài sản nhạy cảm lãi suất trừ Nợ nhạy cảm lãi suất).
    + Bài toán thực nghiệm từ bài giảng:
      * Khi $RSA > RSL$: Lãi suất thị trường TĂNG là tin tốt (Thu nhập cho vay tăng nhanh hơn chi phí trả lãi ➔ NII tăng).
      * Khi $RSA < RSL$: Lãi suất thị trường GIẢM mới là tin tốt (Chi phí trả lãi tiền gửi giảm mạnh hơn thu nhập cho vay ➔ Lợi nhuận cải thiện / giảm lỗ).
    + Sự điều chỉnh không đồng bộ (Asymmetric Adjustment): Khi căng thẳng thanh khoản, lãi suất huy động vọt tăng ngay lập tức, trong khi lãi suất cho vay bị ghìm lại do hợp đồng kỳ hạn ➔ Bóp nghẹt biên lãi thuần NIM.
    + Tình huống chiến lược: Lựa chọn đầu tư vào Ngân hàng A (thận trọng, CAR vượt chuẩn, LDR thấp, ROE khiêm tốn) vs Ngân hàng B (tối đa hóa ROE, đòn bẩy cao, LDR sát trần); khi chu kỳ thắt chặt tiền tệ ập đến, Ngân hàng A là lựa chọn an toàn bền vững vượt qua giông bão.
- **Hoạch định Chiến lược Kinh doanh Ngân hàng (Đào sâu từ CH04):**
  - *1. Khái niệm Chiến lược & 3 Câu hỏi "Xương sống":*
    + Khái niệm: Chương trình hành động dài hạn nhằm tối ưu hóa các mục tiêu cốt lõi: tối đa hóa lợi nhuận, kiểm soát rủi ro, tăng trưởng thị phần và nâng cao giá trị ngân hàng.
    + 3 Câu hỏi nền tảng: (1) Ngân hàng đang ở đâu? (Đánh giá vị thế qua SWOT); (2) Ngân hàng muốn đến đâu? (Tầm nhìn, sứ mệnh, mục tiêu); (3) Đạt đến đó bằng cách nào? (Chương trình hành động, điều phối nguồn lực).
    + 4 Tác dụng cốt lõi: Cầu nối hình thành & thực thi; Nhận dạng cơ hội & thích nghi môi trường; Định hướng hoạt động thống nhất; Công cụ kiểm tra & đánh giá quản trị.
    + Phân loại: Hoạch định Chiến lược (3-5 năm, toàn hệ thống, HĐQT & BĐH) vs Hoạch định Tác nghiệp (ngắn hạn năm/quý/tháng, từng phòng ban/chi nhánh, KPI cụ thể).
  - *2. Mối liên hệ Thể chế Vĩ mô với NHTW [E1]:* Chiến lược của NHTM là bộ phận thực thi chiến lược vĩ mô của NHTW; mục tiêu kinh doanh của NHTM không được đi ngược lại chính sách tiền tệ, trần Room tín dụng và định hướng cơ cấu ngành ưu tiên của NHNN.
  - *3. Điều kiện cần & Phân cấp Quản trị Hoạch định:*
    + 2 Yêu cầu cốt lõi: Sự tham gia đa chiều và liên cấp + Tính linh hoạt và thích ứng liên tục.
    + 6 Cơ sở nền tảng: (1) Đội ngũ nhân viên (yếu tố con người - quan trọng nhất); (2) Nguồn vốn ngân hàng; (3) Cơ sở vật chất & Công nghệ số; (4) Uy tín & Thương hiệu; (5) Vị thế hiện tại & Mục tiêu tương lai; (6) Môi trường kinh doanh.
    + 3 Tầng phân cấp: Cấp cao (HĐQT - kiến tạo tầm nhìn, mô hình, cấp ngân sách) ➔ Cấp trung (Ban điều hành - vạch lộ trình, phân bổ chỉ tiêu) ➔ Cấp cơ sở (Chi nhánh/PGD - trực tiếp tiếp xúc khách hàng, thực thi bán hàng & phản hồi dữ liệu thị trường).
    + 3 Luồng quan hệ: Chuyển giao nhiệm vụ Top-Down; Phê duyệt & Kiểm soát; Báo cáo & Phản hồi Bottom-Up.
  - *4. Quy trình Hoạch định 11 Bước (Chu trình lặp tuần hoàn 3 giai đoạn):*
    + *Giai đoạn 1 (Bước 1–5): Mục tiêu & Phân khúc Thị trường:* Thiết lập mục tiêu SMART, Tuyên bố Sứ mệnh (xác định "sân chơi"), Hoạch định Chính sách (xác định "quy tắc trò chơi"); Xác định Thị trường mục tiêu Served Market (giao thoa 3 yếu tố: Nhóm KH, Nhu cầu KH, Công nghệ/Sản phẩm) & Ma trận Nhu cầu/Sản phẩm; Phân khúc Doanh nghiệp [E5] (Lớn có Account Plan may đo vs SME chuẩn hóa); Phân khúc Bán lẻ [E4] (Priority/VIP vs Mass, Big Data & AI [E8]); Phân tích Đặc điểm ngành (Cầu vs Cung/Chi phí).
    + *Giai đoạn 2 (Bước 6–9): Nội tại, Cạnh tranh & Môi trường:* Đánh giá vị trí hiện tại qua SWOT & 4 Câu hỏi rà soát kế hoạch; 3 Trụ cột đo lường Sức mạnh Vị thế Cạnh tranh (Chỉ số nội tại, Đối chuẩn Top 3 đối thủ lớn nhất, Năng lực định vị / Moat phòng thủ); Đo lường Tính hấp dẫn thị trường qua 10 thước đo cốt lõi & Phương pháp chấm điểm tổng hợp (Trục Y); Phân tích 5 nhóm yếu tố PESTLE, Giả định rõ ràng & Phân tích Độ nhạy (Sensitivity Analysis).
    + *Giai đoạn 3 (Bước 10–11): Ma trận Chiến lược & Kế hoạch Hành động:* Ma trận Danh mục Thị trường Chiến lược 3x3 (GE/McKinsey: Vị thế cạnh tranh Trục X vs Tính hấp dẫn Trục Y); Định hướng chi tiết trong 9 ô chiến lược; Nguyên lý Cân đối Dòng tiền (lấy dòng tiền thu hoạch từ ô vị thế mạnh/thị trường bão hòa tài trợ cho ô tăng trưởng dẫn đầu tương lai); Phát triển Kế hoạch phân khúc cụ thể hóa Marketing-mix (4Ps) & Vòng lặp phản hồi (Feedback Loop).
  - *5. Kiểm tra Chiến lược (Strategic Control & Audit):*
    + 3 Mục đích cốt lõi: Đánh giá sự phù hợp thị trường; Đo lường mức độ hoàn thành KPI; Nhận diện sớm sai lệch và rủi ro trồi hiện.
    + 3 Chức năng điều chỉnh: Nhận diện mâu thuẫn nội tại; Cơ sở đánh giá lại và cập nhật liên tục; Thiết lập dòng thông tin phản hồi.
    + 3 Nguyên tắc tư tưởng văn hóa quản trị: Tư tưởng tích cực (Positive Philosophy); Nguyên tắc "Không trừng phạt - Không áp đặt"; Nguyên tắc linh hoạt & Cải tiến liên tục.

### [E4] Bên thừa vốn (Surplus Units)
- **Bản chất:** Các cá nhân, hộ gia đình, tổ chức kinh tế sở hữu nguồn vốn tiết kiệm thặng dư.
- **Đặc trưng hành vi & Kỳ vọng:**
  - Nhóm gửi tiền NHTM: Cung ứng dòng tiền Inflows tiền gửi; đòi hỏi cam kết hoàn trả 100% vốn gốc kèm lãi suất sinh lời, ưu tiên thanh khoản cao; thụ hưởng trực tiếp tấm đệm an toàn vốn chữ C và khả năng thanh khoản chữ L của ngân hàng; nhạy cảm với tin đồn rút tiền hàng loạt (Bank Run).
  - Nhóm đầu tư thị trường vốn (khách hàng của NHĐT): Nhà đầu tư tổ chức và HNWIs chấp nhận mức độ rủi ro cao hơn để tìm kiếm tỷ suất sinh lời vượt trội (lợi vốn, cổ tức); tự gánh chịu rủi ro sụt giảm NAV.
- **Giải pháp tiếp cận thị trường vốn qua Quỹ đầu tư:** Mua Chứng chỉ quỹ (CCQ) hoặc Quỹ hoán đổi danh mục (ETF) do công ty quản lý quỹ của NHĐT vận hành để phân tán rủi ro và tối ưu hóa chi phí.
- **Phân khúc Khách hàng Cá nhân trong Hoạch định Chiến lược (Từ CH04):**
  - Mô hình Phân khúc Bán lẻ Nhị phân:
    + *Khách hàng Ưu tiên (Priority / VIP Customer):* Thu nhập cao, tài sản tích lũy lớn, số dư tiền gửi CASA cao; ưu tiên bảo toàn vốn, dịch vụ chuyên biệt (Private Lounge, RM riêng), sản phẩm quản lý tài sản, thẻ kim loại cao cấp.
    + *Khách hàng Phổ thông (Standard / Mass):* Thu nhập trung bình; ưu tiên tiện lợi, phí thấp, giao dịch online 24/7; sản phẩm chuẩn hóa (eKYC, vay tiêu dùng, thẻ tín dụng).
  - Ứng dụng Big Data & AI [E8]: Chấm điểm tín dụng tự động, cá nhân hóa trải nghiệm theo thời gian thực (Hyper-personalization).

### [E5] Bên thiếu vốn (Deficit Units - Tổ chức Phát hành)
- **Bản chất:** Các doanh nghiệp sản xuất kinh doanh, tập đoàn lớn, công ty khởi nghiệp và chính phủ cần huy động vốn đầu tư.
- **Đặc trưng nhu cầu & Vai trò đối với Quản trị Ngân hàng:**
  - Hấp thụ dòng tiền Outflows tín dụng từ NHTM; hình thành nên Tài sản sinh lời (IEA đo lường chữ E) và Tài sản nhạy cảm lãi suất (RSA đo lường chữ S).
  - Nguồn phát sinh rủi ro nợ xấu (NPL chữ A): Sự đổ vỡ hoặc suy thoái kinh doanh của bên vay sẽ trực tiếp làm tăng tỷ lệ nợ xấu, bào mòn quỹ dự phòng rủi ro tín dụng và đe dọa tỷ lệ an toàn vốn CAR của ngân hàng.
  - Vòng đời phát triển: Tiếp cận vốn ngắn/trung hạn từ NHTM ➔ Phát hành cổ phiếu IPO/trái phiếu qua NHĐT ➔ Tái cấu trúc và M&A mở rộng.
- **Phân khúc Khách hàng Doanh nghiệp trong Hoạch định Chiến lược (Từ CH04):**
  - *Doanh nghiệp lớn (Large Corporates / Big Accounts):* Số lượng ít nhưng chiếm tỷ trọng dư nợ/doanh thu khổng lồ; đòi hỏi chiến lược riêng biệt (Account Plan may đo), giám đốc quan hệ khách hàng (RM) chuyên trách, giải pháp tài chính tổng thể (Syndicated Loan, bảo lãnh, FX, tài trợ thương mại).
  - *Doanh nghiệp vừa và nhỏ (SME):* Số lượng áp đảo; phân khúc theo ngành nghề (sản xuất, thương mại, logistics), vùng địa lý; sản phẩm đóng gói chuẩn hóa, tinh gọn quy trình thẩm định.

### [E6] Mạng lưới an toàn thể chế (Safety Net)
- **Bản chất & Sứ mệnh:** Được thiết kế để triệt tiêu trạng thái cân bằng xấu trong mô hình kinh tế toán học Diamond & Dybvig (1983). Bảo vệ người gửi tiền nhỏ lẻ tại các định chế nhận tiền gửi qua Bảo hiểm tiền gửi (hạn mức 125 triệu đồng) và cơ chế Người cho vay cuối cùng (LoLR) của NHNN.
- **Vai trò trong Quản trị Thanh khoản (Chữ L):** Safety Net đóng vai trò là "chốt chặn niềm tin" giúp ngân hàng tránh khỏi các cơn hoảng loạn rút tiền hàng loạt vô căn cứ của người gửi tiền cá nhân khi xuất hiện tin đồn thất thiệt.

### [E7] Định chế phi tiền gửi (Non-depository / NHĐT)
- **Vị thế thể chế & Triết lý vận hành:**
  - *Định chế phi tiền gửi (Non-depository):* Tuyệt đối KHÔNG ĐƯỢC PHÉP nhận tiền gửi cá nhân từ công chúng và TUYỆT ĐỐI BỊ CẤM cung ứng dịch vụ thanh toán qua tài khoản khách hàng. Huy động vốn kinh doanh bằng cách phát hành cổ phiếu, trái phiếu của chính mình và vay mượn trên thị trường vốn bán buôn.
  - *Định nghĩa loại trừ nổi tiếng của GS. Giuliano Iannotta:* *"Investment banking is the banking activity not classifiable as commercial banking"*.
  - *Triết lý sản phẩm - Hàng "May đo" (Customized) vs. Hàng "May sẵn" (Standardized):* NHTM là hàng "May sẵn" (đại trà, đóng gói chuẩn hóa); NHĐT là hàng "May đo" (cá nhân hóa cao cấp cho từng thương vụ).
  - *Bốn đặc điểm hoạt động cốt lõi:* Hoạt động vì lợi nhuận; huy động vốn bằng công cụ nợ/vốn của chính mình; hoạt động trung gian thuần túy (nhà đầu tư tự chịu rủi ro vốn); vận hành bằng **Danh tiếng (Reputation)** là tài sản quý giá nhất.
- **So sánh đối chuẩn toàn diện: NHTM vs. NHĐT:**
  - *Vai trò trung gian:* NHTM kết nối Người gửi tiền - Người đi vay (dòng vốn gián tiếp); NHĐT kết nối Tổ chức phát hành - Nhà đầu tư (dòng vốn trực tiếp).
  - *Cơ chế rủi ro:* NHTM chịu rủi ro tín dụng vỡ nợ (NPL) và rủi ro thanh khoản; NHĐT chịu rủi ro danh tiếng (Reputation Risk).
  - *Cơ cấu doanh thu & Bảng cân đối:* NHTM phụ thuộc NII (70-83%) trên **Banking Book**; NHĐT phụ thuộc Phí dịch vụ (~49%) và Tự doanh (~32%) trên **Trading Book** (Mark-to-Market).
  - *Khẩu vị rủi ro:* NHTM khẩu vị thấp (bảo vệ người gửi tiền); NHĐT khẩu vị rủi ro rất cao.
- **Bốn Hoạt động Kinh doanh Chủ yếu của NHĐT:**
  - Bảo lãnh phát hành (Securities Underwriting) với 3 giá trị (Network, Pricing, Reputation) và 3 hình thức (Firm Commitment, Best Effort, All or None).
  - Dịch vụ Tư vấn tài chính (Financial Advisory): M&A và Tái cấu trúc doanh nghiệp.
  - Môi giới (Brokerage) & Tự doanh (Proprietary Trading) trên Trading Book.
  - Dịch vụ Quản lý tài sản (Asset Management): Dòng tiền Quỹ đầu tư, giải quyết 3 rào cản NĐT nhỏ lẻ qua CCQ và Quỹ ETF.
- **Bulge Bracket & Universal Banking:** Top 9 Bulge Bracket toàn cầu; Bức tường Trung Hoa (Chinese Walls); Mô hình Ngân hàng Hỗn hợp (Universal Banking) 3 chân kiềng (NHTM CASA rẻ + CTCK/IB + CTQL Quỹ) bán chéo trọn vòng đời doanh nghiệp (Techcombank-TCBS, Vietcombank-VCBS).

### [E8] Định chế công nghệ & Nền tảng số (Fintech & Super-Apps)
- **Bản chất & Vị thế:** Các công ty công nghệ cung cấp giải pháp tài chính số hóa dựa trên nền tảng (Platform), Open API, Trí tuệ nhân tạo (AI) và Phân tích dữ liệu lớn (Big Data).
- **Mối quan hệ với Quản trị Thanh khoản & Tín dụng:**
  - Kênh phân phối số: Hợp tác với NHTM phân phối sản phẩm số và tài khoản thanh toán; giúp giảm tỷ lệ chi phí CIR (chữ M) của ngân hàng.
  - Nguy cơ Rút tiền mili-giây: Mạng lưới Open API và bot tự động hóa tạo ra nguy cơ rút tiền tức thời với quy mô lớn chỉ trong vài giây, thách thức nghiêm trọng giả định quản trị thanh khoản 30 ngày (LCR) của Basel III.
  - Cạnh tranh P2P Lending: Kết nối trực tiếp người vay và người cho vay; rủi ro người cho vay tự chịu mất vốn, kém an toàn hơn cam kết hoàn trả 100% của NHTM.
- **Vai trò trong Hoạch định Chiến lược & Phân khúc Khách hàng (Từ CH04):**
  - *Động lực công nghệ vĩ mô (yếu tố T trong phân tích PESTLE):* Vừa là đối thủ cạnh tranh disintermediation, vừa là đối tác liên kết công nghệ số trong chiến lược chuyển đổi số của ngân hàng.
  - *Ứng dụng Big Data & Trí tuệ Nhân tạo (AI):* Cung cấp công cụ phân tích dữ liệu hành vi giao dịch khách hàng cá nhân [E4], chấm điểm tín dụng số (Alternative Credit Scoring), tự động hóa quy trình phân khúc và cá nhân hóa trải nghiệm theo thời gian thực (Hyper-personalization).

---

## 4. Relationship Registry

```text
[E1] NHNN ──(Phối hợp CSTK & CSTT)── [E2] MoF
[E1] NHNN ──(CSTT, Dự trữ BB d=10%, Giám sát CAMELS, CAR ≥ 8%, trần LDR 85%)──► [E3] NHTM
[E3] NHTM ──(Ký gửi Dự trữ BB, Báo cáo an toàn vĩ mô & Tỷ số tài chính)──► [E1] NHNN
[E1] NHNN ──(Định hướng CSTT vĩ mô, áp trần room tín dụng & giám sát an toàn)──► [E3] NHTM (CH04 G1.4)
[E3] NHTM ──(Chiến lược kinh doanh là bộ phận thực thi chiến lược vĩ mô của NHTW)──► [E1] NHNN (CH04 G1.4)
[E2] MoF ──(Phát hành TPCP cung ứng HQLA bảo đảm thanh khoản chữ L)──► [E3] NHTM
[E2] MoF / UBCKNN ──(Luật Chứng khoán, cấp phép CTCK, giám sát minh bạch)──► [E7] NHĐT
[E1] NHNN ──(Yêu cầu Bức tường lửa Firewalls ngăn ngừa rủi ro lây lan)──► [E7] NHĐT
[E4] Bên thừa vốn ──(Dòng tiền Inflows tiền gửi & CASA giá rẻ ~0%)──► [E3] NHTM (G4.1 & G5.1)
[E3] NHTM ──(Chi trả lãi suất, Tấm đệm vốn chữ C & Thanh khoản chữ L bảo vệ tiền gửi)──► [E4] Bên thừa vốn
[E3] NHTM ──(Phân khúc khách hàng cá nhân Mass vs Priority/VIP, sản phẩm may đo)──► [E4] Bên thừa vốn (CH04 G3.4)
[E3] NHTM ──(Dòng tiền Outflows tín dụng, Tài sản sinh lời IEA chữ E & RSA chữ S)──► [E5] Bên thiếu vốn
[E5] Bên thiếu vốn ──(Hoàn trả nợ gốc & Lãi vay, Rủi ro nợ xấu NPL chữ A)──► [E3] NHTM
[E3] NHTM ──(Phân khúc doanh nghiệp lớn Account Plan riêng vs SME đóng gói chuẩn)──► [E5] Bên thiếu vốn (CH04 G3.3)
[E3] NHTM ──(Bệ đỡ vốn rẻ CASA, tài khoản thanh toán trong Universal Banking)──► [E7] NHĐT
[E7] NHĐT ──(Bảo lãnh phát hành cổ phiếu IPO & Trái phiếu DN huy động vốn dài hạn)──► [E5] Bên thiếu vốn
[E5] Bên thiếu vốn ──(Thuê tư vấn định giá, tái cấu trúc & đàm phán thương vụ M&A)──► [E7] NHĐT
[E7] NHĐT ──(Phát hành Chứng chỉ quỹ CCQ & Quỹ ETF)──► [E4] Bên thừa vốn
[E4] Bên thừa vốn ──(Mở tài khoản, nộp tiền giao dịch cổ phiếu & Margin)──► [E7] NHĐT
[E7] NHĐT ──(Bán chéo trọn vòng đời: Vay SME ➔ Phát hành cổ phiếu/trái phiếu ➔ M&A)──► [E5] Bên thiếu vốn
[E3] NHTM ──(Góp vốn lập CT con CTCK, Bảo hiểm, Quản lý quỹ - Bán chéo Bancassurance)──► [E7] Định chế phi TG
[E3] NHTM ──(Mô hình Universal Banking & Bán chéo đa dạng hóa danh mục)──► [E7] Định chế phi TG (CH04 G5.1)
[E3] NHTM ──(Nộp phí Bảo hiểm tiền gửi định kỳ)──► [E6] Safety Net
[E6] Safety Net ──(Bảo vệ thanh khoản chữ L, hạn mức chi trả 125tr triệt tiêu Bank Run)──► [E4] Bên thừa vốn
[E1] NHNN ──(Cho vay đặc biệt LoLR Đ.192, 193 bơm thanh khoản khẩn cấp)──► [E6] Safety Net
[E8] Fintech ──(Cạnh tranh Disintermediation - P2P vs NHTM cam kết trả nợ 100%)──► [E3] NHTM
[E3] NHTM ──(Bảo trợ pháp lý ngân hàng số Cake/VCB Digibank làm kênh phân phối)──► [E8] Fintech
[E8] Fintech ──(Hạ tầng số, Open API, Nguy cơ rút tiền mili-giây đe dọa thanh khoản chữ L)──► [E3] NHTM
[E8] Fintech ──(Trải nghiệm Super-App, Ví điện tử, Dịch vụ BNPL)──► [E4] Bên thừa vốn
[E8] Fintech ──(Ứng dụng Big Data & AI phân khúc khách hàng bán lẻ & chấm điểm TD)──► [E3] NHTM (CH04 G3.4)
[E8] Fintech ──(Tác nhân công nghệ vĩ mô PESTLE thúc đẩy chuyển đổi số ngân hàng)──► [E3] NHTM (CH04 G4.4)
```

### Bảng Diễn giải Quan hệ Chi tiết (Bao gồm các liên kết mở rộng từ CH03 & CH04)

| Chiều Quan hệ (Flow) | Loại Liên kết (Type) | Căn cứ Nội dung & Cơ chế Vận hành Thực tế |
| :--- | :--- | :--- |
| **[E1] ↔ [E2]** | Phối hợp Vĩ mô | Phối hợp Chính sách Tiền tệ (NHNN) và Chính sách Tài khóa (Bộ Tài chính) nhằm giữ vững ổn định kinh tế vĩ mô, kiểm soát lạm phát và ngăn chặn hiệu ứng chèn lấn tín dụng (Crowding-out). |
| **[E1] → [E3]** | Giám sát CAMELS & Điều tiết | NHNN điều tiết CSTT qua OMO, Tái cấp vốn, Dự trữ bắt buộc ($d = 10\%$); áp chuẩn an toàn vốn CAR ≥ 8% (Thông tư 14/2025/TT-NHNN), khống chế trần LDR 85%; thực hiện thanh tra toàn diện 6 khía cạnh CAMELS để bảo đảm an toàn hệ thống. |
| **[E3] → [E1]** | Tuân thủ & Ký gửi | NHTM mở tài khoản và ký gửi dự trữ bắt buộc tại NHNN; thực hiện nghĩa vụ báo cáo thống kê định kỳ về an toàn vốn (chữ C), chất lượng tài sản (chữ A), thanh khoản (chữ L) và rủi ro thị trường (chữ S). |
| **[E1] → [E3]** *(Từ CH04)* | Định hướng Vĩ mô & Trần Room | NHNN ban hành chỉ tiêu định hướng chính sách tiền tệ, áp trần room tín dụng và định hướng cơ cấu ngành ưu tiên (nông nghiệp, công nghệ cao); chiến lược của NHTM bắt buộc phải là bộ phận thực thi chính sách vĩ mô của NHTW. |
| **[E3] → [E1]** *(Từ CH04)* | Thích ứng & Tuân thủ Chiến lược | NHTM tái cấu trúc danh mục cho vay và kế hoạch kinh doanh nhằm tuân thủ nghiêm ngặt chỉ tiêu tăng trưởng tín dụng và định hướng lãi suất của NHNN. |
| **[E2] → [E3]** | Cung ứng Tài sản HQLA | Kho bạc Nhà nước (Bộ Tài chính) phát hành Trái phiếu Chính phủ; NHTM đầu tư nắm giữ TPCP để hình thành tài sản thanh khoản chất lượng cao (HQLA) bảo đảm đệm thanh khoản chữ L đáp ứng chuẩn LCR Basel III. |
| **[E2] → [E7]** | Quản lý Chuyên ngành | Bộ Tài chính trực tiếp quản lý TTCK thông qua UBCKNN; cấp phép hoạt động, thanh tra an toàn vốn và giám sát tính minh bạch, công bố thông tin của các Công ty Chứng khoán (khối IB) theo Luật Chứng khoán 2019. |
| **[E1] → [E7]** | Thiết lập Bức tường lửa | NHNN yêu cầu thiết lập ranh giới "Bức tường lửa" (Firewalls) độc lập về vốn, nhân sự và hạch toán; ngăn chặn rủi ro thua lỗ từ mảng tự doanh chứng khoán lây lan sang làm sụp đổ NHTM mẹ. |
| **[E4] → [E3]** | Dòng tiền Inflows Tiền gửi | Người gửi tiền cá nhân & tổ chức cung ứng nguồn vốn nhàn rỗi (Inflows tiền gửi) qua tài khoản CASA (~0%) và tiết kiệm có kỳ hạn; chấp nhận lãi suất thấp để đổi lấy sự an toàn tuyệt đối và thanh khoản cao. |
| **[E3] → [E4]** | An toàn Vốn & Thanh khoản | NHTM duy trì tấm đệm an toàn vốn CAR (chữ C) và khả năng thanh khoản (chữ L) để bảo đảm nghĩa vụ hoàn trả 100% tiền gửi vô điều kiện khi đến hạn hoặc khi khách hàng yêu cầu rút tiền; chi trả lãi suất tiền gửi. |
| **[E3] → [E4]** *(Từ CH04)* | Phân khúc Khách hàng Bán lẻ | NHTM phân khúc khách hàng cá nhân thành Khách hàng Phổ thông (Mass - tiện lợi online 24/7, eKYC, phí thấp) và Khách hàng Ưu tiên (Priority/VIP - may đo giải pháp bảo toàn vốn, Private Lounge, thẻ kim loại, RM riêng). |
| **[E3] → [E5]** | Cấp tín dụng Outflows | NHTM cung cấp dòng tín dụng (Outflows) qua các hình thức: Cho vay, Bảo lãnh, Leasing, Factoring, Chiết khấu; tạo ra Tài sản sinh lời (IEA chữ E) và Tài sản nhạy cảm lãi suất (RSA chữ S). |
| **[E5] → [E3]** | Trả nợ & Rủi ro Nợ xấu NPL | Bên vay hoàn trả nợ gốc và lãi vay định kỳ; tạo ra Thu nhập lãi thuần (NII); nếu bên vay mất khả năng thanh toán sẽ trực tiếp kích hoạt rủi ro nợ xấu NPL (chữ A), buộc ngân hàng trích lập dự phòng và bào mòn vốn tự có. |
| **[E3] → [E5]** *(Từ CH04)* | Phân khúc Khách hàng Doanh nghiệp | NHTM phân loại khách hàng doanh nghiệp thành Doanh nghiệp lớn (Account Plan riêng biệt, RM chuyên trách, tài trợ theo chuỗi giá trị) và SME (sản phẩm đóng gói chuẩn hóa, quy trình tinh gọn). |
| **[E3] → [E7]** | Hợp tác Universal Banking | NHTM đóng vai trò bệ đỡ vốn huy động giá rẻ (CASA) và dịch vụ thanh toán, chuyển giao tệp khách hàng doanh nghiệp lớn cho CTCK/NHĐT để triển khai bán chéo các sản phẩm thị trường vốn. |
| **[E7] → [E5]** | Bảo lãnh Phát hành Chứng khoán | Khối IB của NHĐT thực hiện thẩm định, định giá và bảo lãnh phát hành cổ phiếu IPO hoặc trái phiếu doanh nghiệp, giúp doanh nghiệp huy động nguồn vốn dài hạn quy mô hàng nghìn tỷ đồng từ thị trường. |
| **[E5] → [E7]** | Thuê Tư vấn M&A & Tái cấu trúc | Doanh nghiệp ký hợp đồng thuê khối IB tư vấn chiến lược định giá, tìm kiếm đối tác sáp nhập, đàm phán thâu tóm hoặc tái cơ cấu nguồn vốn và mô hình tập đoàn; chi trả phí tư vấn độc lập. |
| **[E7] → [E4]** | Phát hành Chứng chỉ quỹ & ETF | Công ty Quản lý quỹ của NHĐT phát hành Chứng chỉ quỹ (CCQ) và Quỹ hoán đổi danh mục (ETF), giúp nhà đầu tư cá nhân nhỏ lẻ vượt qua rào cản vốn ít để sở hữu danh mục đa tài sản chuyên nghiệp. |
| **[E4] → [E7]** | Giao dịch Chứng khoán & Margin | Nhà đầu tư mở tài khoản giao dịch tại CTCK, nộp tiền mua bán cổ phiếu/trái phiếu trên sàn thứ cấp, sử dụng dịch vụ cho vay ký quỹ (Margin) và chi trả phí giao dịch, lãi vay margin. |
| **[E7] → [E5]** | Bán chéo Trọn Vòng đời DN | Tập đoàn tài chính đồng hành cùng doanh nghiệp từ giai đoạn SME (vay vốn tín dụng tại NHTM) đến giai đoạn mở rộng (phát hành trái phiếu/cổ phiếu tại NHĐT) và thâu tóm mở rộng (tư vấn M&A). |
| **[E3] → [E7]** | Universal Banking & Bán chéo | NHTM mẹ thành lập/mua lại công ty con bảo hiểm, chứng khoán, quản lý quỹ, leasing để hoàn thiện mô hình Universal Banking và đẩy mạnh bán chéo (Bancassurance) gia tăng thu nhập ngoài lãi. |
| **[E3] → [E6]** | Nộp phí Bảo hiểm | NHTM nhận tiền gửi có nghĩa vụ trích nộp phí bảo hiểm tiền gửi định kỳ theo quy định của Luật Bảo hiểm Tiền gửi. |
| **[E6] → [E4]** | Bảo vệ Niềm tin Công chúng | Cơ quan Bảo hiểm Tiền gửi cam kết hạn mức chi trả bảo hiểm (125 triệu đồng) khi ngân hàng mất khả năng thanh toán, triệt tiêu động cơ rút tiền hoảng loạn hàng loạt (Bank Run) khi gặp rủi ro thanh khoản chữ L. |
| **[E1] → [E6]** | Cứu trợ Thanh khoản Khẩn cấp | NHNN thực thi vai trò Người cho vay cuối cùng (LoLR) qua nghiệp vụ tái cấp vốn đặc biệt (Điều 192, 193 Luật Các TCTD 2024), hỗ trợ thanh khoản tối thượng cho Safety Net bảo vệ hệ thống. |
| **[E8] → [E3]** | Cạnh tranh Disintermediation | Fintech phát triển mô hình P2P Lending cạnh tranh loại bỏ trung gian (Disintermediation); tuy nhiên P2P tiềm ẩn rủi ro bùng nợ/sập app người cho vay tự gánh, trong khi NHTM cam kết trả nợ 100%. |
| **[E3] → [E8]** | Bảo trợ Pháp lý Ngân hàng số | NHTM phát triển các thương hiệu Ngân hàng số (Cake by VPBank, VCB Digibank) không phải là pháp nhân độc lập mà là kênh phân phối kỹ thuật số tiếp cận giới trẻ dưới giấy phép của ngân hàng mẹ. |
| **[E8] → [E3]** | Hạ tầng số & Nguy cơ Rút tiền | Fintech cung cấp giải pháp Open API kết nối thanh toán giúp giảm CIR (chữ M); đồng thời mạng lưới API Bots tự động hóa tạo nguy cơ rút tiền mili-giây đe dọa thanh khoản chữ L của ngân hàng. |
| **[E8] → [E4]** | Trải nghiệm Siêu ứng dụng | Fintech cung cấp giao diện Super-App tiện ích, tích hợp thanh toán, chấm điểm tín dụng AI và giải pháp Mua trước trả sau (BNPL) cho người dùng cá nhân. |
| **[E8] → [E3]** *(Từ CH04)* | Big Data & AI Phân khúc KH | Fintech cung cấp hạ tầng dữ liệu và thuật toán AI giúp NHTM chấm điểm tín dụng tự động, cá nhân hóa trải nghiệm khách hàng bán lẻ [E4] và tối ưu hóa ma trận nhu cầu sản phẩm. |
| **[E8] → [E3]** *(Từ CH04)* | Động lực Công nghệ PESTLE | Fintech đại diện cho yếu tố công nghệ vĩ mô thúc đẩy ngân hàng số hóa toàn diện, gia tăng tính cạnh tranh và thay đổi kỳ vọng người dùng tài chính. |

---

## 5. Chapter Coverage

| Mã Chương | Tên Chương & Trọng tâm Học phần | Danh mục Entity Bao phủ | Mức độ Đào sâu & Vai trò trong Toàn bộ Học phần | Trạng thái & File Sản phẩm |
| :---: | :--- | :--- | :--- | :--- |
| **CH01** | **Mô hình hoạt động Kinh doanh ngân hàng & Các định chế tài chính** | `[E1]`, `[E2]`, `[E3]`, `[E4]`, `[E5]`, `[E6]`, `[E7]`, `[E8]` | **Chương Nền tảng Vĩ mô & Toàn cảnh Hệ thống (Baseline Macro System Map):** Thiết lập cấu trúc tổng thể 8 Entity; phân định rạch ròi Nhận tiền gửi vs Phi tiền gửi; cơ chế biến đổi kỳ hạn ALM; cấu trúc BHC/FHC; 6 mô hình kinh doanh ngân hàng; mạng lưới an toàn và dịch chuyển tư duy chiến lược sau khủng hoảng. | **HOÀN THÀNH**<br/>`CH01.drawio`<br/>(78 cells, 34 vertices, 42 edges) |
| **CH02a** | **Các hoạt động kinh doanh chủ yếu của Ngân hàng thương mại** | `[E3]` *(Trục cốt lõi - Đào sâu)*, liên kết `[E1]`, `[E4]`, `[E5]`, `[E7]`, `[E8]` | **Đào sâu Toàn diện Nghiệp vụ Cốt lõi của [E3] NHTM:**<br/>• **1.0 Vị thế pháp lý:** Ranh giới cha-con TCTD vs NHTM, mục tiêu lợi nhuận, 2 thành trì độc quyền (tiền gửi cá nhân & thanh toán qua TK), so sánh TCTD phi NH/vi mô/QTDND theo Luật Các TCTD 2024.<br/>• **2.0 Ba Chức năng Cốt lõi:** Trung gian tài chính (Hicks 1939, NIM/Spread 70-80% LN, ưu thế trước P2P), Trung gian thanh toán (thủ quỹ kinh tế, CASA), Tạo tiền bút tệ ($S_n = \frac{U(1-q^n)}{1-q}$, $k = 1/d = 10$, $S_\infty = U/d$, rò rỉ thanh khoản).<br/>• **3.0 Hệ thống phân loại:** Sở hữu (Big 4 chiếm 70-80% thị phần, 31 NHTMCP, liên doanh, ngoại), Chiến lược (Bán buôn, Bán lẻ, Bản chất Ngân hàng số Cake/VCB Digibank là kênh phân phối), Lĩnh vực (NHTM Banking Book NII 83% vs IB Trading Book Mark-to-market).<br/>• **4.0 Cơ cấu & Quản trị:** Mạng lưới (Hội sở, Chi nhánh, PGD), Mô hình 3 sảnh (Front - Middle độc lập - Back), Thượng tầng (HĐQT, CEO, Ủy ban ALCO quyền lực nhất quản trị ALM/FTP/IRRBB, UB Chính sách tín dụng).<br/>• **5.0 Bốn hoạt động kinh doanh:** I. Huy động vốn (CASA ~0%, tiết kiệm, GTCG, liên ngân hàng), II. Cấp tín dụng (Cho vay, Bảo lãnh, Leasing, Factoring, Chiết khấu; 70% LN, rủi ro NPL & The Gap), III. Dịch vụ thanh toán & ngân quỹ (Séc, UNC, Thẻ, L/C, Thu/Chi hộ UEH, Fee income), IV. Hoạt động khác (Universal Banking & Bancassurance, Thị trường tiền tệ & Phái sinh, Ngân hàng giám sát Custodian Bank cho quỹ 5k-7k tỷ). | **HOÀN THÀNH**<br/>`CH02a.drawio`<br/>(60 cells, 29 vertices, 29 edges, 5 cột dọc cân đối, 0 va chạm) |
| **CH02b** | **Các hoạt động kinh doanh chủ yếu của Ngân hàng đầu tư** | `[E7]` *(Trục cốt lõi - Đào sâu)*, liên kết `[E5]`, `[E4]`, `[E3]`, `[E2]`, `[E1]` | **Đào sâu Phân khúc Phi tiền gửi & Ngân hàng Đầu tư [E7] (Investment Banking / CTCK):**<br/>• **1.0 Vị thế thể chế & Triết lý vận hành:** Định chế phi nhận tiền gửi, định nghĩa loại trừ của GS. Giuliano Iannotta, triết lý hàng "May đo" (Customized) vs "May sẵn" (Standardized), 4 đặc điểm cốt lõi, Danh tiếng (Reputation) là tài sản quý giá nhất.<br/>• **2.0 So sánh đối chuẩn toàn diện: NHTM vs. NHĐT:** Cơ chế luân chuyển dòng vốn gián tiếp vs trực tiếp; Phân bổ rủi ro tín dụng/thanh khoản vs rủi ro danh tiếng; Cơ cấu doanh thu Trading Book & Phí (~81%) vs Banking Book & NII (~83%); Khẩu vị rủi ro chấp nhận mạo hiểm cao.<br/>• **3.0 Bốn hoạt động kinh doanh chủ yếu:** I. Bảo lãnh phát hành (3 giá trị: Network, Pricing, Reputation; 3 hình thức: Firm Commitment, Best Effort, All or None), II. Dịch vụ Tư vấn tài chính (M&A và Tái cấu trúc doanh nghiệp), III. Môi giới & Tự doanh (Proprietary Trading trên Trading Book), IV. Dịch vụ Quản lý tài sản (Dòng tiền Quỹ đầu tư, giải quyết 3 rào cản NĐT nhỏ lẻ qua CCQ, Tiêu điểm Quỹ ETF).<br/>• **4.0 Định chế Bulge Bracket & Kiểm soát xung đột:** Top 9 Bulge Bracket toàn cầu (Goldman Sachs, JP Morgan, Morgan Stanley...), Lợi thế mạng lưới phân phối & rào cản danh tiếng, Cơ chế Bức tường Trung Hoa (Chinese Walls) ngăn ngừa giao dịch nội gián (Insider Trading).<br/>• **5.0 Chiến lược thực thi tại Việt Nam (Universal Banking):** Đánh giá 3 mô hình, Khuyến nghị tối ưu xây dựng Tập đoàn Ngân hàng Hỗn hợp 3 chân kiềng (NHTM vốn rẻ + CTCK/IB + CTQL Quỹ), Chiến lược bán chéo trọn vòng đời doanh nghiệp từ SME đến IPO/M&A, Thực tiễn Techcombank-TCBS và Vietcombank-VCBS. | **HOÀN THÀNH**<br/>`CH02b.drawio`<br/>(64 cells, 31 vertices, 31 edges, 5 cột dọc cân đối, 0 va chạm) |
| **CH03** | **Quản trị hoạt động kinh doanh ngân hàng** | `[E3]` *(Đào sâu Quản trị)*, liên kết `[E1]`, `[E6]`, `[E2]`, `[E4]`, `[E5]` | **Đào sâu Năng lực Quản trị Chiến lược & Rủi ro Toàn diện tại [E3] NHTM:**<br/>• **1.0 Đánh đổi Rủi ro - Lợi nhuận & Chỉ số Tỷ số:** Nguyên lý Risk-Return Tradeoff; Sự đánh lừa của số tuyệt đối (quy mô) vs Sức mạnh của tỷ số (hiệu quả) qua thực tế Vietcombank 2025 quy mô 2,4 triệu tỷ đồng (~1/5 GDP); Hai tỷ số cốt lõi ROA & ROE (Mô hình đòn bẩy DuPont: $ROE = ROA \times EM$); 3 Trụ cột phân tích tỷ số (Xu hướng Trend 3-5 năm, Đối chuẩn Benchmarking Peer Group/Ngành, Cấu trúc Bảng CĐKT & Khẩu vị rủi ro).<br/>• **2.0 Chữ C (An toàn vốn) & Chữ A (Chất lượng tài sản):**<br/>  - Chữ C: Vốn tự có (Tier 1 vs Tier 2), Mẫu số RWA (nội bảng & ngoại bảng nhân hệ số rủi ro $w_i$); Ví dụ thực tế "Ly nước mía" (cam kết ngoại bảng chưa phát sinh dòng tiền ra nhưng là rủi ro tiềm tàng); Ẩn dụ "Ăn kem - Chạy bộ" (cơ chế trừng phạt tự động bằng túi tiền cổ đông khi tăng tài sản rủi ro); Chuẩn CAR Basel & Việt Nam Thông tư 14/2025/TT-NHNN ($\ge 8\%$); Proxy Indicator (Vốn CSH / Tổng tài sản).<br/>  - Chữ A: Khía cạnh khó phân tích nhất do bất đối xứng thông tin; Tập trung dư nợ theo ngành/địa bàn; Tỷ lệ nợ xấu NPL (nhóm 3,4,5 / Tổng dư nợ, chuẩn < 3%); Tỷ lệ dự phòng RRTD / Dư nợ & Tỷ lệ bao phủ nợ xấu ($LLR = \text{Dự phòng} / \text{NPL}$, chuẩn tốt > 100%, Vietcombank ~200%).<br/>• **3.0 Chữ M (Lành mạnh quản trị) & Chữ E (Hiệu quả thu nhập):**<br/>  - Chữ M: Tiếp cận định tính & Định lượng; Tỷ lệ chi phí (CIR / Cost-to-Income, chuẩn tốt 30%-40%); Thu nhập trên một nhân viên (năng suất lao động); Tốc độ mở rộng chi nhánh/PGD (đánh đổi giữa thị phần và chi phí cố định/rủi ro quản trị).<br/>  - Chữ E: Cơ cấu thu nhập từ Lãi (NII 70-80% LN) vs Thu nhập ngoài lãi (Phí dịch vụ, FX, Chứng khoán, Bancassurance); 5 chỉ tiêu tài chính cốt lõi: ROA, ROE, NIM (Net Interest Margin = NII / IEA, VN 3%-4.5%), NIIR (NII / Tổng thu nhập thuần), Earning Spread (Lãi suất đầu ra BQ - Lãi suất đầu vào BQ).<br/>• **4.0 Chữ L (Khả năng thanh khoản & Quản trị LDR):**<br/>  - Dòng tiền hai chiều Inflows (tiền gửi) vs Outflows (rút tiền & cấp tín dụng); Tỷ lệ tài sản thanh khoản (Tiền mặt + TG NHNN / Tổng tài sản);<br/>  - Tỷ lệ LDR truyền thống (Dư nợ cho vay / Tiền gửi KH): Tiền gửi liên ngân hàng không được tính vào mẫu số; Thực tiễn VN 2025: Big 4 < 100% (90-95%) vs NHTMCP tư nhân > 100%;<br/>  - Tỷ lệ LDR mở rộng (Cho vay / Tổng nguồn vốn huy động gồm Tiền gửi KH + Vay liên ngân hàng + GTCG): Kéo LDR tư nhân về 77-90% nhưng chi phí vốn cao và kém ổn định;<br/>  - Xung đột mục tiêu: An toàn xã hội (NHNN muốn thanh khoản cao, LDR thấp) vs Tối ưu hóa cổ đông (Ngân hàng muốn tối đa cho vay để tăng ROE).<br/>• **5.0 Chữ S (Độ nhạy rủi ro thị trường) & Quản trị Lãi suất (IRRBB):**<br/>  - Khái niệm Rủi ro thị trường, Trạng thái ngoại tệ mở (NOP), Rủi ro danh mục Trading Book;<br/>  - Rủi ro lãi suất (IRRBB) & Mô hình Khe hở lãi suất $GAP = RSA - RSL$;<br/>  - Bài toán thực nghiệm từ bài giảng: Trường hợp 1 $RSA > RSL$ (Lãi suất TĂNG là tin tốt, NII tăng) vs Trường hợp 2 $RSA < RSL$ (Lãi suất GIẢM mới là tin tốt, giảm lỗ);<br/>  - Sự điều chỉnh không đồng bộ (Asymmetric Adjustment: Lãi suất huy động tăng nhanh hơn lãi suất cho vay ➔ bóp nghẹt NIM);<br/>  - Tình huống chiến lược: Lựa chọn Ngân hàng A (thận trọng, CAR vượt chuẩn, LDR thấp) vs Ngân hàng B (tối đa ROE, đòn bẩy lớn) khi chu kỳ thắt chặt tiền tệ. | **HOÀN THÀNH**<br/>`CH03.drawio`<br/>(67 cells, 33 vertices, 32 edges, 5 cột dọc cân đối, 0 va chạm) |
| **CH04** | **Hoạch định chiến lược kinh doanh Ngân hàng** | `[E3]` *(Trục cốt lõi - Đào sâu)*, liên kết `[E1]`, `[E4]`, `[E5]`, `[E8]`, `[E7]` | **Đào sâu Quy trình Hoạch định Chiến lược Toàn diện tại [E3] NHTM:**<br/>• **1.0 Tổng quan Hoạch định & Thể chế Vĩ mô:** Khái niệm Chiến lược kinh doanh NHTM; 3 Câu hỏi "Xương sống" (Đang ở đâu - Muốn đến đâu - Đạt bằng cách nào); 4 Tác dụng cốt lõi; Phân loại Chiến lược (3-5 năm, HĐQT) vs Tác nghiệp (ngắn hạn, chi nhánh); Mối liên hệ vĩ mô: Chiến lược NHTM là bộ phận thực thi chính sách tiền tệ và trần room tín dụng của NHTW [E1].<br/>• **2.0 Điều kiện cần & Phân cấp Hoạch định:** 2 Yêu cầu cốt lõi (Tham gia đa chiều liên cấp & Linh hoạt thích ứng); 6 Cơ sở nguồn lực nền tảng (Đội ngũ nhân sự quan trọng nhất, Nguồn vốn, Công nghệ, Uy tín/Thương hiệu, Vị thế, Môi trường); Phân cấp 3 tầng quản trị (HĐQT vẽ bản đồ & cấp kinh phí, Ban điều hành vạch lộ trình & điều phối, Cấp cơ sở trực tiếp lái xe về đích); 3 Luồng quan hệ vận hành (Chuyển giao Top-Down, Phê duyệt & Kiểm soát, Báo cáo & Phản hồi Bottom-Up).<br/>• **3.0 Mục tiêu & Phân khúc Thị trường (Bước 1–5):** Thiết lập mục tiêu SMART, Sứ mệnh ("sân chơi"), Chính sách ("quy tắc trò chơi"); Thị trường mục tiêu Served Market (giao thoa Nhóm KH, Nhu cầu KH, Công nghệ/Sản phẩm) & Ma trận Nhu cầu/Sản phẩm; Phân khúc Doanh nghiệp [E5] (Lớn có Account Plan may đo vs SME chuẩn hóa); Phân khúc Bán lẻ [E4] (Priority/VIP vs Mass, Big Data & AI [E8]); Đặc điểm Cầu vs Cung/Chi phí ngành.<br/>• **4.0 Nội tại, Cạnh tranh & Môi trường (Bước 6–9):** Đánh giá vị thế hiện tại qua SWOT & 4 Câu hỏi rà soát kế hoạch chiến lược; 3 Trụ cột đo lường Vị thế Cạnh tranh (Chỉ số nội tại, Đối chuẩn Top 3 đối thủ lớn nhất, Năng lực định vị / Moat phòng thủ); Hệ thống 10 Thước đo Tính hấp dẫn thị trường (Quy mô, tăng trưởng, biên LN, mức độ tập trung...) & Phương pháp chấm điểm tổng hợp (Trục Y); Phân tích 5 nhóm yếu tố PESTLE, Giả định rõ ràng & Phân tích Độ nhạy (Sensitivity Analysis).<br/>• **5.0 Ma trận Chiến lược & Kiểm tra (Bước 10–11 & Part IV):** Ma trận Danh mục Thị trường Chiến lược 3x3 (GE/McKinsey: Vị thế cạnh tranh X vs Tính hấp dẫn Y); Chi tiết 9 ô chiến lược định hướng; Nguyên lý cân đối dòng tiền (thu hoạch mảng già cỗi tái đầu tư mảng tăng trưởng); Phát triển Kế hoạch phân khúc Marketing-mix 4Ps & Vòng lặp phản hồi tuần hoàn; Kiểm tra chiến lược (Strategic Control & Audit): 3 mục đích cốt lõi, 3 chức năng điều chỉnh/xung đột nội tại, 3 nguyên tắc văn hóa quản trị (Tư tưởng tích cực, Không trừng phạt - không áp đặt, Linh hoạt & cải tiến liên tục). | **HOÀN THÀNH**<br/>`CH04.drawio`<br/>(67 cells, 33 vertices, 32 edges, 5 cột dọc cân đối, 0 va chạm) |
| **CH05** | **Quản trị Rủi ro Tín dụng & Quản trị Rủi ro Hoạt động** | `[E3]`, `[E5]`, `[E1]`, `[E6]` | **Quản trị Rủi ro Trọng yếu trong Kinh doanh Ngân hàng:** Khung quản trị rủi ro tín dụng theo chuẩn Basel (PD, LGD, EAD), quy trình thẩm định xếp hạng tín dụng nội bộ, xử lý nợ xấu, và khung kiểm soát rủi ro hoạt động (Operational Risk) tại các TCTD. | **DỰ KIẾN KẾ TIẾP** |

---

*Ghi chú duy trì tính liên tục (Continuity Note):* File này là bộ nhớ dùng chung xuyên suốt toàn bộ học phần. Khi thực hiện các chương kế tiếp (`CH05`...), tuyệt đối không thay đổi mã số của các Entity đã được định danh (`E1` đến `E8`). Các chương sau chỉ bổ sung kiến thức chuyên sâu vào Entity tương ứng và cập nhật bảng Chapter Coverage.
