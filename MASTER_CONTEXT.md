# MASTER_CONTEXT

> **Học phần:** Quản trị & Chiến lược Ngân hàng — Đại học Kinh tế TP. Hồ Chí Minh (UEH)  
> **Khung pháp lý & Chuẩn mực tham chiếu:** Luật Các Tổ chức Tín dụng số 32/2024/QH15, Luật Chứng khoán 2019, Hiệp ước An toàn Vốn Basel II / Basel III, Khung pháp lý BHC Act 1956 & Gramm-Leach-Bliley Act 1999.  
> **Nguyên tắc cốt lõi:** `DEFINE ONCE → EXPAND LATER → LINK WHEN NECESSARY` | `HIERARCHY FIRST → RELATIONSHIP SECOND → DETAIL LAST`

---

## 1. Entity Registry

| Entity ID | Tên Thực thể (Entity Name) | Nhóm Phân loại Thể chế | Định danh / Đại diện Tiêu biểu | Vai trò Cốt lõi trong Hệ thống |
| :---: | :--- | :--- | :--- | :--- |
| **[E1]** | **Ngân hàng Trung ương** (NHNN / SBV) | Quản lý Tiền tệ & Giám sát Hệ thống | Ngân hàng Nhà nước Việt Nam | Cơ quan ngang Bộ thuộc Chính phủ, điều hành CSTT, quản lý an toàn hệ thống TCTD, Người cho vay cuối cùng (LoLR), yêu cầu Bức tường lửa (Firewalls). |
| **[E2]** | **Bộ Tài chính** (MoF) | Quản lý Tài chính công & TTCK | Bộ Tài chính Việt Nam (UBCKNN, Cục QLGSBH) | Quản lý ngân sách, tài sản công, nợ quốc gia; điều hành chính sách tài khóa, phát hành TPCP; trực tiếp quản lý TTCK và cấp phép, giám sát hoạt động của các Công ty Chứng khoán qua UBCKNN. |
| **[E3]** | **Định chế nhận tiền gửi (NHTM cốt lõi)** | Depository Institutions | Vietcombank, BIDV, VietinBank, MB, Techcombank, ACB | Đặc quyền huy động tiền gửi cá nhân; độc quyền cung ứng dịch vụ thanh toán qua tài khoản; biến đổi kỳ hạn (Maturity Transformation); cỗ máy nhân bản bút tệ; bệ đỡ vốn rẻ trong Universal Banking. |
| **[E4]** | **Bên thừa vốn (Surplus Units)** | Chủ thể Cung ứng Vốn & Đầu tư | Hộ gia đình, Cá nhân gửi tiền, Nhà đầu tư tổ chức, HNWIs | Cung ứng nguồn vốn nhàn rỗi cho nền kinh tế; tìm kiếm lãi suất và lợi vốn; phân bổ vốn qua kênh tiền gửi NHTM (CASA, tiết kiệm) và thị trường vốn (cổ phiếu, trái phiếu, CCQ, ETFs). |
| **[E5]** | **Bên thiếu vốn (Deficit Units)** | Chủ thể Cầu vốn & Tổ chức Phát hành | Doanh nghiệp sản xuất kinh doanh, Tập đoàn, Chính phủ | Hấp thụ vốn cho sản xuất, đầu tư hạ tầng, mở rộng kinh doanh; tiếp cận vốn qua tín dụng NHTM hoặc phát hành chứng khoán (IPO, trái phiếu) và thuê dịch vụ tư vấn M&A từ NHĐT. |
| **[E6]** | **Mạng lưới an toàn thể chế (Safety Net)** | Cơ chế Bảo vệ Niềm tin & Cứu trợ | Bảo hiểm Tiền gửi Việt Nam (DIV) & Cơ chế LoLR | Bảo vệ người gửi tiền nhỏ lẻ; ngăn chặn hiệu ứng rút tiền hàng loạt (Bank Run) theo mô hình Diamond & Dybvig (1983); dập tắt sụp đổ dây chuyền. |
| **[E7]** | **Định chế phi tiền gửi (Non-depository / NHĐT)** | Non-depository Institutions | Khối IB của CTCK (SSI, TCBS, Vietcap), Bulge Bracket (Goldman Sachs, Morgan Stanley), Quỹ đầu tư (Dragon Capital) | Kiến trúc sư thị trường vốn; cung cấp giải pháp tài chính "may đo" (customized), bảo lãnh phát hành, tư vấn M&A, môi giới, tự doanh Trading Book và quản lý tài sản; tuyệt đối BỊ CẤM nhận tiền gửi cá nhân và BỊ CẤM thanh toán qua tài khoản. |
| **[E8]** | **Định chế công nghệ & Nền tảng số (Fintech)** | Fintech Platforms & Super-Apps | Ví MoMo, ZaloPay, VNPay, Grab, Cake by VPBank, VCB Digibank | Cầu nối hạ tầng kỹ thuật phân phối sản phẩm số; khai thác Big Data & AI; cung cấp thanh toán, BNPL; kênh liên kết phân phối/chiến lược kinh doanh của NHTM; cạnh tranh P2P Lending. |

---

## 2. System Hierarchy

```text
HỆ THỐNG TÀI CHÍNH & MÔ HÌNH HOẠT ĐỘNG KINH DOANH NGÂN HÀNG
│
├── 1. TẦNG QUẢN LÝ VĨ MÔ & ĐIỀU TIẾT THỂ CHẾ
│   ├── [E1] Ngân hàng Trung ương (NHNN Việt Nam)
│   │   ├── 1.1 Vị thế pháp lý & Mục tiêu phi lợi nhuận (Cơ quan ngang Bộ)
│   │   ├── 1.2 Công cụ điều tiết CSTT (OMO, Tái cấp vốn, Dự trữ bắt buộc d=10%)
│   │   ├── 1.3 Khung giám sát an toàn (Chuẩn Basel, CAR ≥ 8%, trần LDR 85%, trần sở hữu CP Đ.63)
│   │   ├── 1.4 Chức năng Người cho vay cuối cùng (LoLR cứu trợ thanh khoản Đ.192, 193)
│   │   └── 1.5 Thiết lập Bức tường lửa (Firewalls) ngăn ngừa rủi ro tự doanh lây lan sang NHTM
│   └── [E2] Bộ Tài chính (MoF)
│       ├── 2.1 Quản lý Tài chính công, Ngân sách & Trần nợ công quốc gia
│       ├── 2.2 Chính sách Tài khóa & Cung ứng Trái phiếu Chính phủ (Tài sản chuẩn HQLA)
│       ├── 2.3 Cơ quan quản lý Nhà nước TTCK (UBCKNN) & Bảo hiểm (Cục QLGSBH)
│       │   ├── Cấp phép và giám sát hoạt động của các Công ty Chứng khoán / Khối IB
│       │   └── Giám sát tính minh bạch, công bố thông tin và phòng ngừa gian lận thị trường vốn
│       └── 2.4 Phối hợp vĩ mô Tài khóa - Tiền tệ (Kiểm soát hiệu ứng Crowding-out)
│
├── 2. TẦNG BẢO VỆ AN TOÀN HỆ THỐNG
│   └── [E6] Mạng lưới an toàn thể chế (Safety Net)
│       ├── 6.1 Sứ mệnh triệt tiêu trạng thái cân bằng xấu Diamond & Dybvig (1983)
│       ├── 6.2 Bảo hiểm tiền gửi (Hạn mức chi trả 125 triệu đồng cho cá nhân)
│       ├── 6.3 Cơ chế cho vay đặc biệt khẩn cấp hỗ trợ TCTD kiểm soát đặc biệt
│       └── 6.4 Giới hạn đạo đức (Moral Hazard) & Kỷ luật thị trường
│
├── 3. TẦNG TRUNG GIAN DẪN VỐN & VẬN HÀNH KINH DOANH CỐT LÕI
│   ├── [E4] Bên thừa vốn (Surplus Units)
│   │   ├── 4.1 Động cơ tài chính: Bảo toàn gốc 100%, tối ưu hóa lãi suất, thanh khoản cao
│   │   ├── 4.2 Kênh phân bổ tiền gửi: CASA không kỳ hạn (~0%), Tiết kiệm có kỳ hạn, Chứng chỉ tiền gửi (CDs)
│   │   ├── 4.3 Kênh phân bổ thị trường vốn: Mua cổ phiếu niêm yết, Trái phiếu DN, Chứng chỉ quỹ (CCQ), ETFs
│   │   └── 4.4 Rủi ro hệ thống: Tâm lý bầy đàn (Bank Run tại NHTM) & Tự chịu rủi ro biến động giá trên TTCK
│   │
│   ├── [E3] Định chế nhận tiền gửi (NHTM cốt lõi) ── [TRỤC ĐÀO SÂU CH02a]
│   │   ├── 3.1 Vị thế pháp lý & Bản chất TCTD (Luật Các TCTD 2024: Cha-Con, Mục tiêu lợi nhuận, Độc quyền tiền gửi cá nhân & thanh toán)
│   │   ├── 3.2 Ba Chức năng Cốt lõi & Cơ chế Tạo tiền (Trung gian TC hóa giải Hicks 1939, Trung gian thanh toán, Tạo tiền bút tệ $S_n, S_\infty, k=1/d$)
│   │   ├── 3.3 Hệ thống phân loại NHTM (Sở hữu Big 4, 31 NHTMCP, Liên doanh, Ngoại; Chiến lược Bán buôn/Bán lẻ; Bản chất Ngân hàng số)
│   │   ├── 3.4 Cơ cấu tổ chức & Quản trị thượng tầng (Mạng lưới Hội sở/Chi nhánh/PGD; Mô hình 3 sảnh Front-Middle-Back; Ủy ban ALCO)
│   │   └── 3.5 Bốn Hoạt động kinh doanh chủ yếu (Huy động vốn, Cấp tín dụng, Dịch vụ thanh toán/ngân quỹ, Kinh doanh khác)
│   │
│   └── [E5] Bên thiếu vốn (Deficit Units - Tổ chức Phát hành)
│       ├── 5.1 Nhu cầu tài trợ dài hạn: Vốn lưu động, Máy móc thiết bị, Dự án hạ tầng, Mua bán sáp nhập (M&A)
│       ├── 5.2 Kênh tiếp cận vốn gián tiếp: Tín dụng NHTM, Cho vay hợp vốn (Syndicated Loans)
│       ├── 5.3 Kênh tiếp cận vốn trực tiếp: Thuê NHĐT bảo lãnh phát hành cổ phiếu IPO, Trái phiếu doanh nghiệp
│       └── 5.4 Nghĩa vụ pháp lý: Hoàn trả nợ vay (đối mặt nợ xấu NPL) hoặc nghĩa vụ trả lãi trái phiếu/cổ tức
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
- **Khung an toàn thể chế (Luật Các TCTD 2024 & Chuẩn Basel):**
  - Giám sát tỷ lệ an toàn vốn tối thiểu (CAR ≥ 8%).
  - Khống chế trần tỷ lệ dư nợ cho vay trên tổng tiền gửi (LDR ≤ 85%).
  - Giảm tỷ lệ sở hữu cổ phần nhằm triệt tiêu sở hữu chéo: Cổ đông cá nhân ≤ 5%, cổ đông tổ chức ≤ 10%, cổ đông và người có liên quan ≤ 15% (Điều 63).
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
  - Cung ứng Tài sản thanh khoản chất lượng cao (HQLA) cho hệ thống ngân hàng; định hình đường cong lợi suất phi rủi ro (Risk-free Benchmark Yield Curve) làm căn cứ định giá toàn bộ thị trường tài chính.
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
- **Ba Chức năng Cốt lõi:**
  - *Trung gian Tài chính:* Hóa giải xung đột kỳ hạn Hicks (1939) ("Constitutional Weakness"); phân tán rủi ro; cỗ máy tạo thu nhập NIM/Spread (chiếm 70-80% lợi nhuận); ưu thế cam kết hoàn trả 100% trước P2P Lending.
  - *Trung gian Thanh toán:* Thủ quỹ của nền kinh tế; đảm bảo huyết mạch giao dịch thương mại; nhận lương thực chất là gửi CASA giá rẻ.
  - *Tạo tiền bút tệ (Money Creation):* Công thức cấp số nhân $S_n = \frac{U(1-q^n)}{1-q}$; hệ số nhân $k = 1/d = 10$; $S_\infty = U/d$; các yếu tố rò rỉ (dự trữ vượt mức, rút tiền mặt).
- **Cơ cấu Tổ chức & Ủy ban ALCO:** Hội sở (Back/Middle Office), Chi nhánh (Front Office), PGD; Mô hình 3 sảnh Front - Middle độc lập - Back; Ủy ban ALCO (CFO làm Chủ tịch) quyền lực nhất điều phối ALM, LCR/NSFR, IRRBB, FTP.
- **Vai trò trong Mô hình Universal Banking:** NHTM đóng vai trò là "chân kiềng nền móng" cung cấp nguồn vốn huy động giá rẻ khổng lồ, mạng lưới phân phối triệu khách hàng và tài khoản thanh toán; làm bệ phóng vững chắc để liên kết bán chéo các sản phẩm chứng khoán và quản lý tài sản của NHĐT.

### [E4] Bên thừa vốn (Surplus Units)
- **Bản chất:** Các cá nhân, hộ gia đình, tổ chức kinh tế sở hữu nguồn vốn tiết kiệm thặng dư.
- **Đặc trưng hành vi & Kỳ vọng:**
  - Nhóm gửi tiền NHTM: Ngại rủi ro (Risk-averse), đòi hỏi cam kết hoàn trả 100% vốn gốc kèm lãi suất sinh lời, ưu tiên thanh khoản cao; cung cấp nguồn vốn CASA giá rẻ cho ngân hàng.
  - Nhóm đầu tư thị trường vốn (khách hàng của NHĐT): Nhà đầu tư tổ chức (quỹ hưu trí, quỹ bảo hiểm) và nhà đầu tư cá nhân giàu có (HNWIs) chấp nhận mức độ rủi ro cao hơn để tìm kiếm tỷ suất sinh lời vượt trội (lợi vốn, cổ tức); tự gánh chịu rủi ro sụt giảm giá trị tài sản ròng (NAV).
- **Giải pháp tiếp cận thị trường vốn qua Quỹ đầu tư:** Nhà đầu tư cá nhân nhỏ lẻ bị rào cản vốn ít, chi phí cao, thiếu chuyên môn ➔ Lựa chọn mua Chứng chỉ quỹ (CCQ) hoặc Quỹ hoán đổi danh mục (ETF) do công ty quản lý quỹ của NHĐT vận hành để phân tán rủi ro và tối ưu hóa chi phí.

### [E5] Bên thiếu vốn (Deficit Units - Tổ chức Phát hành)
- **Bản chất:** Các doanh nghiệp sản xuất kinh doanh, tập đoàn lớn, công ty khởi nghiệp và chính phủ cần huy động vốn đầu tư.
- **Đặc trưng nhu cầu & Vòng đời phát triển:**
  - *Giai đoạn ban đầu (Khởi nghiệp / SME):* Vay vốn lưu động ngắn hạn và trung hạn từ NHTM; tài sản bảo đảm là máy móc, nhà xưởng, bất động sản.
  - *Giai đoạn mở rộng quy mô:* Nhu cầu vốn dài hạn cực lớn vượt quá hạn mức tín dụng ngân hàng (do trần Điều 136 Luật Các TCTD) ➔ Chuyển sang thuê NHĐT tư vấn phát hành Trái phiếu Doanh nghiệp hoặc phát hành cổ phiếu lần đầu ra công chúng (IPO) để huy động vốn trực tiếp từ công chúng.
  - *Giai đoạn thâu tóm & Tái thiết:* Thuê khối IB của NHĐT thực hiện tư vấn định giá, đàm phán mua bán - sáp nhập (M&A) hoặc tái cấu trúc nguồn vốn.

### [E6] Mạng lưới an toàn thể chế (Safety Net)
- **Bản chất & Sứ mệnh:** Được thiết kế để triệt tiêu trạng thái cân bằng xấu trong mô hình kinh tế toán học Diamond & Dybvig (1983). Bảo vệ người gửi tiền nhỏ lẻ tại các định chế nhận tiền gửi qua Bảo hiểm tiền gửi (hạn mức 125 triệu đồng) và cơ chế Người cho vay cuối cùng (LoLR) của NHNN.
- **Lưu ý thể chế:** Safety Net chỉ bảo vệ tiền gửi tại NHTM; hoàn toàn KHÔNG bảo hiểm cho các khoản đầu tư chứng khoán, cổ phiếu, trái phiếu doanh nghiệp hay chứng chỉ quỹ tại NHĐT.

### [E7] Định chế phi tiền gửi (Non-depository / NHĐT) — [ĐÀO SÂU TOÀN DIỆN TỪ CH02b]
- **Vị thế thể chế & Triết lý vận hành:**
  - *Định chế phi tiền gửi (Non-depository):* Tuyệt đối KHÔNG ĐƯỢC PHÉP nhận tiền gửi cá nhân từ công chúng và TUYỆT ĐỐI BỊ CẤM cung ứng dịch vụ thanh toán qua tài khoản khách hàng. Huy động vốn kinh doanh bằng cách phát hành cổ phiếu, trái phiếu của chính mình và vay mượn trên thị trường vốn bán buôn.
  - *Định nghĩa loại trừ nổi tiếng của GS. Giuliano Iannotta:* *"Investment banking is the banking activity not classifiable as commercial banking"*. Phản ánh tính linh hoạt, sáng tạo và mở rộng liên tục của NHĐT; mọi hoạt động tài chính phức tạp trên thị trường vốn không thuộc nghiệp vụ nhận tiền gửi/cho vay truyền thống đều thuộc phạm vi NHĐT.
  - *Triết lý sản phẩm - Hàng "May đo" (Customized) vs. Hàng "May sẵn" (Standardized):*
    - NHTM là hàng "May sẵn": Sản phẩm đại trà, đóng gói theo khung tiêu chuẩn sẵn có (gói tiết kiệm kỳ hạn, khoản vay tiêu dùng).
    - NHĐT là hàng "May đo": Sản phẩm cá nhân hóa cao cấp; thiết kế riêng biệt cho cấu trúc vốn đặc thù của từng thương vụ IPO, từng phương án M&A hay công cụ phái sinh cấu trúc phức tạp.
  - *Bốn đặc điểm hoạt động cốt lõi:*
    1. Hoạt động vì mục tiêu tối đa hóa lợi nhuận cho cổ đông.
    2. Không nhận tiền gửi truyền thống, huy động vốn bằng công cụ nợ/vốn của chính mình.
    3. Hoạt động trung gian thuần túy: Không dùng vốn tự có gánh rủi ro tín dụng như NHTM; kết nối trực tiếp tổ chức phát hành và nhà đầu tư; nhà đầu tư tự chịu trách nhiệm rủi ro vốn.
    4. Vận hành bằng **Danh tiếng (Reputation)**: Danh tiếng là tài sản quý giá nhất, là bảo chứng độc lập giúp thuyết phục thị trường; định giá sai hoặc thiếu minh bạch sẽ hủy hoại danh tiếng và làm mất khách hàng vĩnh viễn.
- **So sánh đối chuẩn toàn diện: NHTM vs. NHĐT:**
  - *Vai trò trung gian:* NHTM kết nối Người gửi tiền - Người đi vay (dòng vốn gián tiếp, biến đổi kỳ hạn và tạo tiền); NHĐT kết nối Tổ chức phát hành - Nhà đầu tư (dòng vốn trực tiếp, khơi thông thị trường vốn).
  - *Cơ chế rủi ro:* NHTM gánh chịu rủi ro tín dụng vỡ nợ (NPL) và rủi ro thanh khoản; NHĐT gánh chịu rủi ro danh tiếng (Reputation Risk).
  - *Cơ cấu doanh thu & Bảng cân đối:*
    - NHTM phụ thuộc vào Thu nhập lãi thuần (NII chiếm ~83%) hạch toán trên **Banking Book** (giữ đến ngày đáo hạn, giá trị danh nghĩa ổn định).
    - NHĐT phụ thuộc vào Phí dịch vụ (~49%) và Tự doanh (~32%) hạch toán trên **Trading Book** (định giá lại theo giá thị trường hàng ngày - Mark-to-Market). NII chiếm tỷ trọng không đáng kể.
  - *Khẩu vị rủi ro:* NHTM khẩu vị thấp do chịu ràng buộc an toàn vốn ngặt nghèo (CAR, LCR, NSFR, LDR); NHĐT khẩu vị rủi ro rất cao, sẵn sàng tham gia tự doanh phái sinh, đầu cơ và bảo lãnh cam kết chắc chắn để tìm kiếm siêu lợi nhuận.
- **Bốn Hoạt động Kinh doanh Chủ yếu của NHĐT:**
  - *1. Dịch vụ Bảo lãnh phát hành (Securities Underwriting):*
    - Hoạt động cốt lõi hàng đầu: Giúp doanh nghiệp và chính phủ huy động vốn qua cổ phiếu (Equity/IPO) và trái phiếu (Debt).
    - Ba giá trị gia tăng nghệ thuật: Mạng lưới phân phối tổ chức (Network) ➔ Kỹ năng định giá chuẩn xác (Pricing) ➔ Bảo chứng danh tiếng (Reputation).
    - Ba hình thức bảo lãnh:
      + Cam kết chắc chắn (Firm Commitment): NHĐT cam kết mua toàn bộ đợt phát hành; gánh chịu toàn bộ rủi ro tồn đọng nếu thị trường không hấp thụ hết.
      + Cố gắng tối đa (Best Effort): NHĐT làm đại lý nỗ lực phân phối tối đa, không cam kết mua lại phần dư, rủi ro thuộc về tổ chức phát hành.
      + Tất cả hoặc không (All or None): Điều kiện ngặt nghèo phải bán hết 100%; nếu không bán hết thì toàn bộ thương vụ bị hủy bỏ và hoàn tiền cho nhà đầu tư.
  - *2. Dịch vụ Tư vấn tài chính (Financial Advisory):*
    - Tư vấn Mua bán & Sáp nhập (M&A): Định giá doanh nghiệp mục tiêu, xây dựng chiến lược thâu tóm/phòng thủ, tìm kiếm đối tác chiến lược, đàm phán hợp đồng.
    - Tái cấu trúc doanh nghiệp (Corporate Restructuring): Tái cơ cấu nguồn vốn, hoán đổi nợ - cổ phần, tinh gọn mô hình tập đoàn.
    - Thực tế tại Việt Nam: Do khối IB của các công ty chứng khoán lớn đảm nhiệm và thu phí tư vấn độc lập; NHTM truyền thống thường chỉ tư vấn lồng ghép khi bán tín dụng.
  - *3. Hoạt động Môi giới (Brokerage) & Tự doanh (Proprietary Trading):*
    - Môi giới: Trung gian khớp lệnh trực tiếp giữa người mua và người bán, cung cấp đòn bẩy ký quỹ (Margin) và thu phí hoa hồng giao dịch.
    - Tự doanh: NHĐT dùng chính nguồn vốn và tài khoản của mình để mua bán chứng khoán tìm kiếm lợi vốn (Capital Gain) trên Trading Book; đòi hỏi năng lực đo lường giá trị chịu rủi ro (VaR) cao.
  - *4. Dịch vụ Quản lý tài sản (Asset Management):*
    - Cơ chế dòng tiền Quỹ đầu tư: Nhà đầu tư mua Chứng chỉ quỹ (CCQ) ➔ Công ty Quản lý quỹ mang vốn đầu tư danh mục đa tài sản (cổ phiếu, trái phiếu, hàng hóa, BĐS) ➔ Cổ tức/lợi vốn chảy về Quỹ ➔ Thu phí quản lý quỹ.
    - Hóa giải 3 rào cản của nhà đầu tư nhỏ lẻ: Vốn ít, Chi phí giao dịch cao, Thiếu chuyên môn ➔ Đầu tư qua CCQ giúp phân tán rủi ro, giảm chi phí quy mô và hưởng năng lực chuyên gia.
    - Hệ thống quỹ: Quỹ tương hỗ (Mutual Funds), Quỹ phòng hộ (Hedge Funds), Quỹ hưu trí, Quỹ đầu tư mạo hiểm (Venture Capital).
    - Tiêu điểm Quỹ hoán đổi danh mục (ETF): Mô phỏng chỉ số (VN30, Diamond), niêm yết và giao dịch trực tiếp trên sở giao dịch chứng khoán như cổ phiếu thường, chi phí quản lý cực thấp.
- **Các Định chế Toàn cầu Bulge Bracket & Kiểm soát Xung đột Lợi ích:**
  - *Nhóm Bulge Bracket:* Goldman Sachs, JP Morgan Chase, Barclays, Bank of America Merrill Lynch, Morgan Stanley, Deutsche Bank, Credit Suisse, UBS, HSBC. Chiếm lĩnh thị trường IPO và M&A nghìn tỷ USD nhờ bề dày lịch sử và mạng lưới khách hàng tổ chức khổng lồ.
  - *Bức tường Trung Hoa (Chinese Walls):* Cơ chế bắt buộc ngăn ngừa xung đột lợi ích và giao dịch nội gián (Insider Trading); cách ly tuyệt đối về vật lý, hệ thống CNTT và trao đổi thông tin giữa Khối Tư vấn M&A/Bảo lãnh (nắm thông tin mật) và Khối Tự doanh/Môi giới/Phân tích nghiên cứu (giao dịch công khai trên thị trường).
- **Chiến lược Thực thi tại Việt Nam: Mô hình Universal Banking:**
  - *Đánh giá 3 lựa chọn cho nhà đầu tư nhiều vốn:* NHTM thuần túy (NIM ngày càng hẹp), NHĐT thuần túy (khó tồn tại do thị trường vốn VN chưa đủ sâu, pháp lý chưa công nhận pháp nhân NHĐT độc lập), Mô hình Hỗn hợp (Universal Banking).
  - *Khuyến nghị tối ưu:* Xây dựng Tập đoàn Universal Banking 3 chân kiềng vững chắc:
    1. Trụ cột nền móng: NHTM có công nghệ mạnh thu hút tiền gửi CASA giá rẻ và tệp triệu khách hàng.
    2. Trụ cột thị trường vốn: Công ty Chứng khoán (đóng vai trò NHĐT) thực hiện bảo lãnh phát hành, tư vấn M&A, tự doanh.
    3. Trụ cột quản lý tài sản: Công ty Quản lý quỹ phát hành CCQ và ETFs thu hút tiền nhàn rỗi.
  - *Cơ chế bán chéo trọn vòng đời (Cross-selling):* Phục vụ doanh nghiệp từ khi còn nhỏ vay vốn lưu động SME ➔ Tăng trưởng IPO và phát hành trái phiếu ➔ M&A mở rộng ➔ Quản lý tài sản gia tộc cho chủ doanh nghiệp.
  - *Minh họa thực tiễn:* Techcombank - TCBS - Techcom Capital; Vietcombank - VCBS - VCBF; BIDV - BSC.

### [E8] Định chế công nghệ & Nền tảng số (Fintech & Super-Apps)
- **Bản chất & Vị thế:** Các công ty công nghệ cung cấp giải pháp tài chính số hóa dựa trên nền tảng (Platform), Open API, Trí tuệ nhân tạo (AI) và Phân tích dữ liệu lớn (Big Data).
- **Mối quan hệ với Thị trường vốn & NHĐT:**
  - Ứng dụng Wealthtech (như Tikop, Finhay, MoMo Túi Thần Tài): Đóng vai trò là kênh phân phối bán lẻ các sản phẩm chứng chỉ quỹ (CCQ) và trái phiếu của các Công ty Quản lý quỹ và CTCK thuộc NHĐT.
  - Nền tảng giao dịch chứng khoán số: Tích hợp Open API cho phép nhà đầu tư mở tài khoản eKYC và giao dịch cổ phiếu tức thời mà không cần đến quầy.
  - Cạnh tranh mô hình P2P Lending: Mô hình kết nối trực tiếp người vay và người cho vay; tiềm ẩn rủi ro vỡ nợ rất cao và người cho vay tự chịu mất vốn nếu người vay bùng nợ hoặc nền tảng sụp đổ.

---

## 4. Relationship Registry

```text
[E1] NHNN ──(Phối hợp CSTK & CSTT)── [E2] MoF
[E1] NHNN ──(CSTT, Dự trữ BB d=10%, Basel CAR/LDR, Room tín dụng)──► [E3] NHTM
[E3] NHTM ──(Ký gửi Dự trữ BB, Báo cáo an toàn vĩ mô)──► [E1] NHNN
[E2] MoF ──(Phát hành TPCP cung ứng HQLA)──► [E3] NHTM
[E2] MoF / UBCKNN ──(Luật Chứng khoán, cấp phép CTCK, giám sát minh bạch)──► [E7] NHĐT
[E1] NHNN ──(Yêu cầu Bức tường lửa Firewalls ngăn ngừa rủi ro lây lan)──► [E7] NHĐT
[E4] Bên thừa vốn ──(Gửi tiền tiết kiệm & CASA giá rẻ ~0%)──► [E3] NHTM (G5.1 Huy động vốn)
[E3] NHTM ──(Chi trả lãi suất tiền gửi, Thanh toán yêu cầu)──► [E4] Bên thừa vốn
[E3] NHTM (G5.2 Cấp tín dụng) ──(Cho vay, Bảo lãnh, Leasing, Chiết khấu)──► [E5] Bên thiếu vốn
[E5] Bên thiếu vốn ──(Hoàn trả nợ gốc & Lãi vay, Rủi ro nợ xấu NPL)──► [E3] NHTM (G5.2 Cấp tín dụng)
[E3] NHTM ──(Bệ đỡ vốn rẻ CASA, tài khoản thanh toán trong Universal Banking)──► [E7] NHĐT (G5.2)
[E7] NHĐT (G3.1 Bảo lãnh) ──(Bảo lãnh phát hành cổ phiếu IPO & Trái phiếu DN huy động vốn dài hạn)──► [E5] Bên thiếu vốn
[E5] Bên thiếu vốn ──(Thuê tư vấn định giá, tái cấu trúc & đàm phán thương vụ M&A)──► [E7] NHĐT (G3.2 Tư vấn)
[E7] NHĐT (G3.4 QLTS) ──(Phát hành Chứng chỉ quỹ CCQ & Quỹ ETF)──► [E4] Bên thừa vốn
[E4] Bên thừa vốn ──(Mở tài khoản, nộp tiền giao dịch cổ phiếu & Margin)──► [E7] NHĐT (G3.3 Môi giới)
[E7] NHĐT (G5.3 Bán chéo) ──(Bán chéo trọn vòng đời: Vay SME ➔ Phát hành cổ phiếu/trái phiếu ➔ M&A)──► [E5] Bên thiếu vốn
[E3] NHTM (G5.4 HĐ khác) ──(Góp vốn lập CT con CTCK, Bảo hiểm, Leasing - Bán chéo Bancassurance)──► [E7] Định chế phi TG
[E3] NHTM ──(Nộp phí Bảo hiểm tiền gửi định kỳ)──► [E6] Safety Net
[E6] Safety Net ──(Cam kết hạn mức chi trả 125tr triệt tiêu Bank Run)──► [E4] Bên thừa vốn
[E1] NHNN ──(Cho vay đặc biệt LoLR Đ.192, 193 bơm thanh khoản khẩn cấp)──► [E6] Safety Net
[E8] Fintech ──(Cạnh tranh Disintermediation - P2P vs NHTM cam kết trả nợ 100%)──► [E3] NHTM (G2.1 Chức năng TGTC)
[E3] NHTM (G3.2 Chiến lược) ──(Bảo trợ pháp lý ngân hàng số Cake/VCB Digibank làm kênh phân phối)──► [E8] Fintech
[E8] Fintech ──(Hạ tầng thanh toán, Open API, Rủi ro rút tiền mili-giây)──► [E3] NHTM
[E8] Fintech ──(Trải nghiệm Super-App, Ví điện tử, Dịch vụ BNPL)──► [E4] Bên thừa vốn
```

### Bảng Diễn giải Quan hệ Chi tiết (Bao gồm các liên kết mở rộng từ CH02a & CH02b)

| Chiều Quan hệ (Flow) | Loại Liên kết (Type) | Căn cứ Nội dung & Cơ chế Vận hành Thực tế |
| :--- | :--- | :--- |
| **[E1] ↔ [E2]** | Phối hợp Vĩ mô | Phối hợp Chính sách Tiền tệ (NHNN) và Chính sách Tài khóa (Bộ Tài chính) nhằm giữ vững ổn định kinh tế vĩ mô, kiểm soát lạm phát và ngăn chặn hiệu ứng chèn lấn tín dụng (Crowding-out). |
| **[E1] → [E3]** | Giám sát & Điều tiết | NHNN điều tiết cung ứng tiền tệ qua OMO, Tái cấp vốn, Dự trữ bắt buộc ($d = 10\%$); thiết lập chuẩn mực Basel (CAR ≥ 8%, siết LDR 85%); áp trần sở hữu cổ phần theo Luật Các TCTD 2024 để ngăn ngừa sở hữu chéo. |
| **[E3] → [E1]** | Tuân thủ & Ký gửi | NHTM mở tài khoản và ký gửi dự trữ bắt buộc tại NHNN; thực hiện nghĩa vụ báo cáo thống kê định kỳ phục vụ giám sát an toàn vĩ mô và vi mô. |
| **[E2] → [E3]** | Cung ứng Tài sản HQLA | Kho bạc Nhà nước (Bộ Tài chính) phát hành Trái phiếu Chính phủ; NHTM đầu tư nắm giữ TPCP để hình thành tài sản thanh khoản chất lượng cao (HQLA) đáp ứng chuẩn LCR Basel III. |
| **[E2] → [E7]** | Quản lý Chuyên ngành | Bộ Tài chính trực tiếp quản lý TTCK thông qua UBCKNN; cấp phép hoạt động, thanh tra an toàn vốn và giám sát tính minh bạch, công bố thông tin của các Công ty Chứng khoán (khối IB) theo Luật Chứng khoán 2019. |
| **[E1] → [E7]** | Thiết lập Bức tường lửa | NHNN yêu cầu thiết lập ranh giới "Bức tường lửa" (Firewalls) độc lập về vốn, nhân sự và hạch toán; ngăn chặn rủi ro thua lỗ từ mảng tự doanh chứng khoán lây lan sang làm sụp đổ NHTM mẹ. |
| **[E4] → [E3] (G5.1)** | Dẫn vốn Tiền gửi Rẻ nhất | Người gửi tiền cá nhân & tổ chức cung ứng thặng dư nhàn rỗi thông qua tài khoản CASA (lãi suất ~0%) và sổ tiết kiệm có kỳ hạn; chấp nhận lãi suất thấp để đổi lấy sự an toàn tuyệt đối và thanh khoản cao. |
| **[E3] → [E4]** | Dịch vụ & Hoàn trả | NHTM có nghĩa vụ pháp lý hoàn trả 100% tiền gửi vô điều kiện khi đến hạn hoặc khi khách hàng yêu cầu rút tiền; chi trả lãi suất tiền gửi; cung cấp dịch vụ thanh toán 24/7. |
| **[E3] (G5.2) → [E5]** | Cấp tín dụng Đa dạng | NHTM cung cấp vốn qua các hình thức: Cho vay ngắn/trung/dài hạn, Bảo lãnh ngân hàng, Bao thanh toán (Factoring), Chiết khấu GTCG, Cho thuê tài chính (Leasing); thực hiện biến đổi kỳ hạn (Maturity Transformation). |
| **[E5] → [E3] (G5.2)** | Trả nợ & Rủi ro Tín dụng | Bên vay hoàn trả nợ gốc và lãi vay định kỳ; tạo ra Thu nhập lãi thuần (NII chiếm ~70% lợi nhuận ngân hàng); nếu bên vay mất khả năng thanh toán sẽ trực tiếp kích hoạt rủi ro nợ xấu (NPL). |
| **[E3] → [E7] (G5.2)** | Hợp tác Universal Banking | NHTM đóng vai trò bệ đỡ vốn huy động giá rẻ (CASA) và dịch vụ thanh toán, chuyển giao tệp khách hàng doanh nghiệp lớn cho CTCK/NHĐT để triển khai bán chéo các sản phẩm thị trường vốn. |
| **[E7] (G3.1) → [E5]** | Bảo lãnh Phát hành Chứng khoán | Khối IB của NHĐT thực hiện thẩm định, định giá và bảo lãnh phát hành cổ phiếu IPO hoặc trái phiếu doanh nghiệp, giúp doanh nghiệp huy động nguồn vốn dài hạn quy mô hàng nghìn tỷ đồng từ thị trường. |
| **[E5] → [E7] (G3.2)** | Thuê Tư vấn M&A & Tái cấu trúc | Doanh nghiệp ký hợp đồng thuê khối IB tư vấn chiến lược định giá, tìm kiếm đối tác sáp nhập, đàm phán thâu tóm hoặc tái cơ cấu nguồn vốn và mô hình tập đoàn; chi trả phí tư vấn độc lập. |
| **[E7] (G3.4) → [E4]** | Phát hành Chứng chỉ quỹ & ETF | Công ty Quản lý quỹ của NHĐT phát hành Chứng chỉ quỹ (CCQ) và Quỹ hoán đổi danh mục (ETF), giúp nhà đầu tư cá nhân nhỏ lẻ vượt qua rào cản vốn ít để sở hữu danh mục đa tài sản chuyên nghiệp. |
| **[E4] → [E7] (G3.3)** | Giao dịch Chứng khoán & Margin | Nhà đầu tư mở tài khoản giao dịch tại CTCK, nộp tiền mua bán cổ phiếu/trái phiếu trên sàn thứ cấp, sử dụng dịch vụ cho vay ký quỹ (Margin) và chi trả phí giao dịch, lãi vay margin. |
| **[E7] (G5.3) → [E5]** | Bán chéo Trọn Vòng đời DN | Tập đoàn tài chính đồng hành cùng doanh nghiệp từ giai đoạn SME (vay vốn tín dụng tại NHTM) đến giai đoạn mở rộng (phát hành trái phiếu/cổ phiếu tại NHĐT) và thâu tóm mở rộng (tư vấn M&A). |
| **[E3] (G5.4) → [E7]** | Universal Banking & Bán chéo | NHTM mẹ thành lập/mua lại công ty con bảo hiểm, chứng khoán, quản lý quỹ, leasing để hoàn thiện mô hình Universal Banking và đẩy mạnh bán chéo (Bancassurance) gia tăng thu nhập ngoài lãi. |
| **[E3] → [E6]** | Nộp phí Bảo hiểm | NHTM nhận tiền gửi có nghĩa vụ trích nộp phí bảo hiểm tiền gửi định kỳ theo quy định của Luật Bảo hiểm Tiền gửi. |
| **[E6] → [E4]** | Bảo vệ Niềm tin Công chúng | Cơ quan Bảo hiểm Tiền gửi cam kết hạn mức chi trả bảo hiểm (125 triệu đồng) khi ngân hàng mất khả năng thanh toán, triệt tiêu động cơ rút tiền hoảng loạn hàng loạt (Bank Run). |
| **[E1] → [E6]** | Cứu trợ Thanh khoản Khẩn cấp | NHNN thực thi vai trò Người cho vay cuối cùng (LoLR) qua nghiệp vụ tái cấp vốn đặc biệt (Điều 192, 193 Luật Các TCTD 2024), hỗ trợ thanh khoản tối thượng cho Safety Net bảo vệ hệ thống. |
| **[E8] → [E3] (G2.1)** | Cạnh tranh Disintermediation | Fintech phát triển mô hình P2P Lending cạnh tranh loại bỏ trung gian (Disintermediation); tuy nhiên P2P tiềm ẩn rủi ro bùng nợ/sập app người cho vay tự gánh, trong khi NHTM cam kết trả nợ 100%. |
| **[E3] (G3.2) → [E8]** | Bảo trợ Pháp lý Ngân hàng số | NHTM phát triển các thương hiệu Ngân hàng số (Cake by VPBank, VCB Digibank) không phải là pháp nhân độc lập mà là kênh phân phối kỹ thuật số tiếp cận giới trẻ dưới giấy phép của ngân hàng mẹ. |
| **[E8] → [E3]** | Hạ tầng số & Nguy cơ Rút tiền | Fintech cung cấp giải pháp Open API kết nối thanh toán và phân phối sản phẩm số cho NHTM; đồng thời mạng lưới API Bots tự động hóa tạo nguy cơ rút tiền mili-giây đe dọa thanh khoản. |
| **[E8] → [E4]** | Trải nghiệm Siêu ứng dụng | Fintech cung cấp giao diện Super-App tiện ích, tích hợp thanh toán, chấm điểm tín dụng AI và giải pháp Mua trước trả sau (BNPL) cho người dùng cá nhân. |

---

## 5. Chapter Coverage

| Mã Chương | Tên Chương & Trọng tâm Học phần | Danh mục Entity Bao phủ | Mức độ Đào sâu & Vai trò trong Toàn bộ Học phần | Trạng thái & File Sản phẩm |
| :---: | :--- | :--- | :--- | :--- |
| **CH01** | **Mô hình hoạt động Kinh doanh ngân hàng & Các định chế tài chính** | `[E1]`, `[E2]`, `[E3]`, `[E4]`, `[E5]`, `[E6]`, `[E7]`, `[E8]` | **Chương Nền tảng Vĩ mô & Toàn cảnh Hệ thống (Baseline Macro System Map):** Thiết lập cấu trúc tổng thể 8 Entity; phân định rạch ròi Nhận tiền gửi vs Phi tiền gửi; cơ chế biến đổi kỳ hạn ALM; cấu trúc BHC/FHC; 6 mô hình kinh doanh ngân hàng; mạng lưới an toàn và dịch chuyển tư duy chiến lược sau khủng hoảng. | **HOÀN THÀNH**<br/>`CH01.drawio`<br/>(78 cells, 34 vertices, 42 edges) |
| **CH02a** | **Các hoạt động kinh doanh chủ yếu của Ngân hàng thương mại** | `[E3]` *(Trục cốt lõi - Đào sâu)*, liên kết `[E1]`, `[E4]`, `[E5]`, `[E7]`, `[E8]` | **Đào sâu Toàn diện Nghiệp vụ Cốt lõi của [E3] NHTM:**<br/>• **1.0 Vị thế pháp lý:** Ranh giới cha-con TCTD vs NHTM, mục tiêu lợi nhuận, 2 thành trì độc quyền (tiền gửi cá nhân & thanh toán qua TK), so sánh TCTD phi NH/vi mô/QTDND theo Luật Các TCTD 2024.<br/>• **2.0 Ba Chức năng Cốt lõi:** Trung gian tài chính (Hicks 1939, NIM/Spread 70-80% LN, ưu thế trước P2P), Trung gian thanh toán (thủ quỹ kinh tế, CASA), Tạo tiền bút tệ ($S_n = \frac{U(1-q^n)}{1-q}$, $k = 1/d = 10$, $S_\infty = U/d$, rò rỉ thanh khoản).<br/>• **3.0 Hệ thống phân loại:** Sở hữu (Big 4 chiếm 70-80% thị phần, 31 NHTMCP, liên doanh, ngoại), Chiến lược (Bán buôn, Bán lẻ, Bản chất Ngân hàng số Cake/VCB Digibank là kênh phân phối), Lĩnh vực (NHTM Banking Book NII 83% vs IB Trading Book Mark-to-market).<br/>• **4.0 Cơ cấu & Quản trị:** Mạng lưới (Hội sở, Chi nhánh, PGD), Mô hình 3 sảnh (Front - Middle độc lập - Back), Thượng tầng (HĐQT, CEO, Ủy ban ALCO quyền lực nhất quản trị ALM/FTP/IRRBB, UB Chính sách tín dụng).<br/>• **5.0 Bốn hoạt động kinh doanh:** I. Huy động vốn (CASA ~0%, tiết kiệm, GTCG, liên ngân hàng), II. Cấp tín dụng (Cho vay, Bảo lãnh, Leasing, Factoring, Chiết khấu; 70% LN, rủi ro NPL & The Gap), III. Dịch vụ thanh toán & ngân quỹ (Séc, UNC, Thẻ, L/C, Thu/Chi hộ UEH, Fee income), IV. Hoạt động khác (Universal Banking & Bancassurance, Thị trường tiền tệ & Phái sinh, Ngân hàng giám sát Custodian Bank cho quỹ 5k-7k tỷ). | **HOÀN THÀNH**<br/>`CH02a.drawio`<br/>(60 cells, 29 vertices, 29 edges, 5 cột dọc cân đối, 0 va chạm) |
| **CH02b** | **Các hoạt động kinh doanh chủ yếu của Ngân hàng đầu tư** | `[E7]` *(Trục cốt lõi - Đào sâu)*, liên kết `[E5]`, `[E4]`, `[E3]`, `[E2]`, `[E1]` | **Đào sâu Phân khúc Phi tiền gửi & Ngân hàng Đầu tư [E7] (Investment Banking / CTCK):**<br/>• **1.0 Vị thế thể chế & Triết lý vận hành:** Định chế phi nhận tiền gửi, định nghĩa loại trừ của GS. Giuliano Iannotta, triết lý hàng "May đo" (Customized) vs "May sẵn" (Standardized), 4 đặc điểm cốt lõi, Danh tiếng (Reputation) là tài sản quý giá nhất.<br/>• **2.0 So sánh đối chuẩn toàn diện: NHTM vs. NHĐT:** Cơ chế luân chuyển dòng vốn gián tiếp vs trực tiếp; Phân bổ rủi ro tín dụng/thanh khoản vs rủi ro danh tiếng; Cơ cấu doanh thu Trading Book & Phí (~81%) vs Banking Book & NII (~83%); Khẩu vị rủi ro chấp nhận mạo hiểm cao.<br/>• **3.0 Bốn hoạt động kinh doanh chủ yếu:** I. Bảo lãnh phát hành (3 giá trị: Network, Pricing, Reputation; 3 hình thức: Firm Commitment, Best Effort, All or None), II. Dịch vụ Tư vấn tài chính (M&A và Tái cấu trúc doanh nghiệp), III. Môi giới & Tự doanh (Proprietary Trading trên Trading Book), IV. Dịch vụ Quản lý tài sản (Dòng tiền Quỹ đầu tư, giải quyết 3 rào cản NĐT nhỏ lẻ qua CCQ, Tiêu điểm Quỹ ETF).<br/>• **4.0 Định chế Bulge Bracket & Kiểm soát xung đột:** Top 9 Bulge Bracket toàn cầu (Goldman Sachs, JP Morgan, Morgan Stanley...), Lợi thế mạng lưới phân phối & rào cản danh tiếng, Cơ chế Bức tường Trung Hoa (Chinese Walls) ngăn ngừa giao dịch nội gián (Insider Trading).<br/>• **5.0 Chiến lược thực thi tại Việt Nam (Universal Banking):** Đánh giá 3 mô hình, Khuyến nghị tối ưu xây dựng Tập đoàn Ngân hàng Hỗn hợp 3 chân kiềng (NHTM vốn rẻ + CTCK/IB + CTQL Quỹ), Chiến lược bán chéo trọn vòng đời doanh nghiệp từ SME đến IPO/M&A, Thực tiễn Techcombank-TCBS và Vietcombank-VCBS. | **HOÀN THÀNH**<br/>`CH02b.drawio`<br/>(64 cells, 31 vertices, 31 edges, 5 cột dọc cân đối, 0 va chạm) |
| **CH03** | **Quản trị hoạt động kinh doanh ngân hàng** | `[E3]` *(Đào sâu Quản trị)*, liên kết `[E1]`, `[E6]` | **Đào sâu Năng lực Quản trị Chiến lược & Rủi ro tại [E3]:** Quản trị An toàn vốn Basel II/III (ICAAP), Quản trị Thanh khoản và Rủi ro thanh khoản (ILAAP), Quản trị Rủi ro Tín dụng, Rủi ro Thị trường, Rủi ro Hoạt động và tối ưu hóa hiệu quả kinh doanh qua chu kỳ. | **DỰ KIẾN KẾ TIẾP** |

---
*Ghi chú duy trì tính liên tục (Continuity Note):* File này là bộ nhớ dùng chung xuyên suốt toàn bộ học phần. Khi thực hiện các chương kế tiếp (`CH03`...), tuyệt đối không thay đổi mã số của các Entity đã được định danh (`E1` đến `E8`). Các chương sau chỉ bổ sung kiến thức chuyên sâu vào Entity tương ứng và cập nhật bảng Chapter Coverage.
