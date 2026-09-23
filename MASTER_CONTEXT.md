# MASTER_CONTEXT

> **Học phần:** Quản trị & Chiến lược Ngân hàng — Đại học Kinh tế TP. Hồ Chí Minh (UEH)  
> **Khung pháp lý & Chuẩn mực tham chiếu:** Luật Các Tổ chức Tín dụng số 32/2024/QH15, Hiệp ước An toàn Vốn Basel II / Basel III, Khung pháp lý BHC Act 1956 & Gramm-Leach-Bliley Act 1999.  
> **Nguyên tắc cốt lõi:** `DEFINE ONCE → EXPAND LATER → LINK WHEN NECESSARY` | `HIERARCHY FIRST → RELATIONSHIP SECOND → DETAIL LAST`

---

## 1. Entity Registry

| Entity ID | Tên Thực thể (Entity Name) | Nhóm Phân loại Thể chế | Định danh / Đại diện Tiêu biểu | Vai trò Cốt lõi trong Hệ thống |
| :---: | :--- | :--- | :--- | :--- |
| **[E1]** | **Ngân hàng Trung ương** (NHNN / SBV) | Quản lý Tiền tệ & Giám sát Hệ thống | Ngân hàng Nhà nước Việt Nam | Cơ quan ngang Bộ thuộc Chính phủ, điều hành CSTT, quản lý an toàn hệ thống TCTD, Người cho vay cuối cùng (LoLR). |
| **[E2]** | **Bộ Tài chính** (MoF) | Quản lý Tài chính công & Nợ công | Bộ Tài chính Việt Nam (UBCKNN, Cục QLGSBH) | Quản lý ngân sách, tài sản công, nợ quốc gia; điều hành chính sách tài khóa, phát hành TPCP; quản lý thị trường chứng khoán & bảo hiểm. |
| **[E3]** | **Định chế nhận tiền gửi (NHTM cốt lõi)** | Depository Institutions | Vietcombank, BIDV, VietinBank, MB, Techcombank, ACB | Đặc quyền huy động tiền gửi cá nhân; độc quyền cung ứng dịch vụ thanh toán qua tài khoản; biến đổi kỳ hạn (Maturity Transformation); cỗ máy nhân bản bút tệ. |
| **[E4]** | **Bên thừa vốn (Surplus Units)** | Chủ thể Cung ứng Vốn Tiết kiệm | Hộ gia đình, Cá nhân gửi tiền, Nhà đầu tư | Cung ứng nguồn vốn nhàn rỗi cho nền kinh tế; tìm kiếm lãi suất sinh lời, ưu tiên bảo toàn vốn gốc và đòi hỏi thanh khoản cao; cung cấp nguồn vốn CASA giá rẻ nhất. |
| **[E5]** | **Bên thiếu vốn (Deficit Units)** | Chủ thể Cầu vốn Đầu tư & Chi tiêu | Doanh nghiệp sản xuất kinh doanh, Hộ tiêu dùng, Chính phủ | Hấp thụ vốn cho sản xuất, đầu tư hạ tầng, mua sắm tài sản; đòi hỏi kỳ hạn vay dài và chi phí vốn tối ưu; phát sinh nghĩa vụ hoàn trả nợ gốc/lãi và nguy cơ nợ xấu (NPL). |
| **[E6]** | **Mạng lưới an toàn thể chế (Safety Net)** | Cơ chế Bảo vệ Niềm tin & Cứu trợ | Bảo hiểm Tiền gửi Việt Nam (DIV) & Cơ chế LoLR | Bảo vệ người gửi tiền nhỏ lẻ; ngăn chặn hiệu ứng rút tiền hàng loạt (Bank Run) theo mô hình Diamond & Dybvig (1983); dập tắt sụp đổ dây chuyền. |
| **[E7]** | **Định chế phi tiền gửi (Non-depository)** | Non-depository Institutions | CTCK (SSI, TCBS), Bảo hiểm (Bảo Việt, Manulife), Quỹ (Dragon Capital), CTTC (FE Credit) | Cung cấp dịch vụ đầu tư, bảo hiểm, thu xếp vốn chuyên sâu; tuyệt đối BỊ CẤM nhận tiền gửi cá nhân và BỊ CẤM cung ứng dịch vụ thanh toán qua tài khoản; khách hàng tự chịu rủi ro thị trường. |
| **[E8]** | **Định chế công nghệ & Nền tảng số (Fintech)** | Fintech Platforms & Super-Apps | Ví MoMo, ZaloPay, VNPay, Grab, Cake by VPBank, VCB Digibank | Cầu nối hạ tầng kỹ thuật phân phối sản phẩm số; khai thác Big Data & AI; cung cấp thanh toán, BNPL; kênh liên kết phân phối/chiến lược kinh doanh của NHTM. |

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
│   │   └── 1.4 Chức năng Người cho vay cuối cùng (LoLR cứu trợ thanh khoản Đ.192, 193)
│   └── [E2] Bộ Tài chính (MoF)
│       ├── 2.1 Quản lý Tài chính công, Ngân sách & Trần nợ công quốc gia
│       ├── 2.2 Chính sách Tài khóa & Cung ứng Trái phiếu Chính phủ (Tài sản chuẩn HQLA)
│       ├── 2.3 Cơ quan quản lý Nhà nước TTCK (UBCKNN) & Bảo hiểm (Cục QLGSBH)
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
│   │   ├── 4.3 Kênh phân bổ phi tiền gửi: Cổ phiếu, Trái phiếu DN, Chứng chỉ quỹ, Hợp đồng bảo hiểm
│   │   └── 4.4 Rủi ro tâm lý bầy đàn kích hoạt tháo chạy tập thể (Bank Run)
│   │
│   ├── [E3] Định chế nhận tiền gửi (NHTM cốt lõi) ── [TRỤC CHÍNH CỦA HỆ THỐNG - ĐÀO SÂU CH02a]
│   │   ├── 3.1 Vị thế pháp lý & Bản chất TCTD (Luật Các TCTD 2024)
│   │   │   ├── Quan hệ Cha - Con: TCTD là khái niệm rộng; NHTM là TCTD thực hiện đầy đủ toàn bộ HĐNH
│   │   │   ├── Mục tiêu lợi nhuận: Phân biệt NHTM với Ngân hàng Chính sách (VBSP, VDB - phi lợi nhuận)
│   │   │   ├── Bộ ba HĐNH cốt lõi: Nhận tiền gửi ➔ Cấp tín dụng ➔ Dịch vụ thanh toán (thường xuyên, liên tục)
│   │   │   ├── Hai thành trì độc quyền: Độc quyền nhận tiền gửi cá nhân & Độc quyền DV thanh toán qua tài khoản
│   │   │   └── So sánh pháp nhân TCTD: TCTD phi NH (cấm tiền gửi cá nhân/thanh toán), TC Vi mô, QTDND
│   │   ├── 3.2 Ba Chức năng Cốt lõi & Cơ chế Tạo tiền (Bộ gen sinh tồn)
│   │   │   ├── Trung gian tài chính: Hóa giải xung đột kỳ hạn Hicks (1939); Cỗ máy in tiền NIM/Spread (70-80% LN); Ưu thế cam kết hoàn trả 100% trước P2P Lending
│   │   │   ├── Trung gian thanh toán: Thủ quỹ của nền kinh tế; đảm bảo lưu thông không gián đoạn; tiền lương thực chất là CASA
│   │   │   └── Chức năng tạo tiền bút tệ: Công thức cấp số nhân $S_n = \frac{U(1-q^n)}{1-q}$; hệ số nhân $k = 1/d = 10$; $S_\infty = U/d$; yếu tố rò rỉ (dự trữ vượt mức, rút tiền mặt)
│   │   ├── 3.3 Hệ thống phân loại Ngân hàng Thương mại
│   │   │   ├── Hình thức sở hữu: Big 4 Nhà nước (70-80% thị phần; Agribank 100% vốn NN; VCB, CTG, BIDV CP chi phối), 31 NHTMCP, 2 Liên doanh, 9 100% vốn ngoại, 52 Chi nhánh NH ngoại
│   │   │   ├── Chiến lược kinh doanh: Bán buôn (Wholesale - tập đoàn, FDI), Bán lẻ (Retail - cá nhân, SME) & Hỗn hợp
│   │   │   ├── Bản chất Ngân hàng số (Cake by VPBank, VCB Digibank): Không phải pháp nhân độc lập; là chiến lược kinh doanh/kênh phân phối công nghệ
│   │   │   └── Lĩnh vực hoạt động: Chuyên doanh vs Universal Banking; NHTM Banking Book (NII ~83%) vs Investment Bank Trading Book (Phí ~49%, Tự doanh ~32%, Mark-to-market)
│   │   ├── 3.4 Cơ cấu tổ chức & Quản trị thượng tầng
│   │   │   ├── Mạng lưới không gian địa lý: Hội sở chính (Back & Middle Office), Chi nhánh (Front Office cấp cơ sở), Phòng giao dịch (vệ tinh dân cư)
│   │   │   ├── Mô hình vận hành 3 sảnh: Tiền sảnh (Front Office kinh doanh), Trung sảnh (Middle Office độc lập đo lường rủi ro/mô hình điểm tín dụng), Hậu sảnh (Back Office kế toán/IT)
│   │   │   └── Quản trị thượng tầng: HĐQT & UBQL Rủi ro, Ban Điều hành (CEO), Ủy ban Quản lý Tài sản Nợ - Có (ALCO - quyền lực nhất, CFO chủ tịch, quản trị LCR/NSFR/FTP/IRRBB), Ủy ban Chính sách Tín dụng
│   │   └── 3.5 Bốn Hoạt động kinh doanh chủ yếu của NHTM
│   │       ├── I. Hoạt động Huy động vốn (Liabilities): Nhận tiền gửi (CASA ~0%, tiết kiệm), Phát hành GTCG (CDs, trái phiếu), Vay liên ngân hàng & NHNN
│   │       ├── II. Hoạt động Cấp tín dụng (Assets): Cho vay (chiếm tỷ trọng lớn nhất), Bảo lãnh, Factoring, Chiết khấu, Cho thuê tài chính (Leasing); trụ cột thu nhập lãi (70% LN); đối mặt rủi ro NPL & The Gap
│   │       ├── III. Dịch vụ Thanh toán & Ngân quỹ: Séc, UNC, Thẻ, L/C, Thu/Chi hộ (học phí UEH); tạo Thu nhập phí thuần (Fee income); đối mặt rủi ro vận hành
│   │       └── IV. Hoạt động Kinh doanh khác: Góp vốn/mua CP công ty con (CTCK, Bảo hiểm, Quản lý quỹ, Leasing) phát triển Universal Banking & Bancassurance; Thị trường tiền tệ & Phái sinh (TPCP, IRS); Ngân hàng giám sát (Custodian Bank cho quỹ 5k-7k tỷ)
│   │
│   └── [E5] Bên thiếu vốn (Deficit Units)
│       ├── 5.1 Nhu cầu tài trợ dài hạn: Vốn lưu động, Máy móc thiết bị, Dự án hạ tầng, Mua nhà
│       ├── 5.2 Kênh tiếp cận vốn: Tín dụng NHTM, Cho vay hợp vốn (Syndicated Loans), Thị trường vốn (Trái phiếu, Cổ phiếu)
│       └── 5.3 Nghĩa vụ pháp lý & Nguy cơ phát sinh nợ xấu (NPL) đe dọa ngân hàng
│
└── 4. TẦNG ĐỊNH CHẾ CHUYÊN BIỆT & NỀN TẢNG SỐ MỞ RỘNG
    ├── [E7] Định chế phi tiền gửi (Non-depository Institutions)
    │   ├── 7.1 Ranh giới pháp lý tối thượng: TUYỆT ĐỐI KHÔNG nhận tiền gửi cá nhân từ công chúng & CẤM thanh toán qua TK
    │   ├── 7.2 Cơ chế rủi ro: Khách hàng tự chịu rủi ro thị trường (Không cam kết hoàn 100% gốc)
    │   ├── 7.3 Phân loại định chế chuyên biệt:
    │   │   ├── Công ty chứng khoán (CTCK): Môi giới, Margin, Tư vấn M&A, Bảo lãnh phát hành IPO
    │   │   ├── Công ty bảo hiểm: Thu phí định kỳ đầu tư tài sản an toàn dài hạn (TPCP, Cổ phiếu blue-chip)
    │   │   ├── Quỹ đầu tư & Quản lý quỹ: Phát hành CCQ quản lý danh mục đa tài sản (quỹ 5k-7k tỷ thuê NHTM làm Custodian Bank)
    │   │   └── Công ty tài chính (CTTC) & Cho thuê tài chính: Cho vay tiêu dùng tín chấp, cho thuê máy móc (TCTD phi ngân hàng)
    │   ├── 7.4 Tích hợp bán chéo (Cross-selling) & Bancassurance
    │   └── 7.5 Cơ chế "Bức tường lửa" (Firewalls) ngăn ngừa rủi ro lây lan (như vách ngăn tàu Titanic)
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

### [E2] Bộ Tài chính (MoF)
- **Bản chất & Vai trò:** Cơ quan thuộc Chính phủ quản lý nền tài chính quốc gia, ngân sách nhà nước, thuế, hải quan, tài sản công, nợ công và dự trữ tài chính nhà nước. Quản lý vĩ mô hướng tới phân bổ nguồn lực công và ổn định phát triển kinh tế - xã hội.
- **Công cụ & Cơ chế điều hành:**
  - Chính sách tài khóa: Thu thuế, phân bổ chi thường xuyên và giải ngân đầu tư công.
  - Phát hành Trái phiếu Chính phủ (TPCP) bù đắp bội chi ngân sách và tài trợ dự án quốc gia.
  - Cung ứng Tài sản thanh khoản chất lượng cao (HQLA) cho hệ thống ngân hàng; định hình đường cong lợi suất phi rủi ro (Risk-free Benchmark Yield Curve) làm căn cứ định giá toàn bộ thị trường tài chính.
- **Phạm vi quản lý chuyên ngành:**
  - Trực tiếp quản lý Nhà nước đối với Thị trường Chứng khoán thông qua Ủy ban Chứng khoán Nhà nước (UBCKNN).
  - Trực tiếp quản lý Thị trường Bảo hiểm thông qua Cục Quản lý, Giám sát Bảo hiểm (QLGSBH).
  - Đại diện chủ sở hữu phần vốn Nhà nước tại các doanh nghiệp và TCTD có vốn nhà nước (SCIC, Agribank...).
  - *Lưu ý pháp lý cốt lõi:* Bộ Tài chính tuyệt đối KHÔNG quản lý Công ty Tài chính tiêu dùng hay Cho thuê tài chính (các định chế này là TCTD phi ngân hàng, thuộc thẩm quyền quản lý của NHNN).
- **Phối hợp vĩ mô Tài khóa - Tiền tệ:** Phối hợp nhịp nhàng với NHNN để duy trì thanh khoản hệ thống, tránh hiện tượng phát hành nợ công quá mức gây hiệu ứng chèn lấn nguồn vốn tín dụng của khu vực tư nhân (Crowding-out effect).

### [E3] Định chế nhận tiền gửi (NHTM cốt lõi) — [ĐÀO SÂU TOÀN DIỆN TỪ CH02a]
- **Vị thế pháp lý & Bản chất TCTD (Luật Các TCTD 2024):**
  - *Quan hệ Cha - Con:* TCTD là khái niệm mẹ/rộng (doanh nghiệp thực hiện 1 hoặc một số hoạt động ngân hàng); NHTM là loại hình TCTD đặc thù được thực hiện đầy đủ toàn bộ hoạt động ngân hàng.
  - *Mục tiêu lợi nhuận:* NHTM hoạt động hoàn toàn vì mục tiêu lợi nhuận, phân biệt rạch ròi với Ngân hàng Chính sách (VBSP, VDB - hoạt động phi lợi nhuận, thực thi chính sách an sinh xã hội của Nhà nước).
  - *Bộ ba HĐNH cốt lõi:* Nhận tiền gửi ➔ Cấp tín dụng ➔ Cung ứng dịch vụ thanh toán qua tài khoản (phải mang tính chất thường xuyên, liên tục).
  - *Hai thành trì độc quyền tối thượng:*
    1. Độc quyền nhận tiền gửi từ cá nhân: Bảo vệ đối tượng công chúng yếu thế, thiếu thông tin; đem lại nguồn vốn khổng lồ với chi phí rẻ nhất (đặc biệt là tiền gửi thanh toán CASA với lãi suất ~0%).
    2. Độc quyền cung ứng dịch vụ thanh toán qua tài khoản: Đòi hỏi quy mô vốn điều lệ cực lớn (vốn pháp định tối thiểu 3.000 tỷ; thực tế Big 4 và NHTMCP lớn từ 40.000 đến hơn 80.000 tỷ); đủ tiềm lực và uy tín xử lý các giao dịch quy mô hàng tỷ USD (như thương vụ ThaiBev mua Sabeco 5 tỷ USD chuyển qua Vietcombank).
  - *Phân định rạch ròi các định chế khác:* TCTD phi ngân hàng (CTTC, Leasing) bị CẤM nhận tiền gửi cá nhân và CẤM mở tài khoản thanh toán; Tổ chức tài chính vi mô (CEP, TYM) chỉ cho vay hộ nghèo/DN siêu nhỏ bằng VND; Quỹ tín dụng nhân dân hoạt động theo nguyên tắc tương trợ xã viên nội bộ địa phương.
- **Ba Chức năng Cốt lõi (Bộ gen sinh tồn của NHTM):**
  - *1. Chức năng Trung gian Tài chính:*
    - Hóa giải mâu thuẫn kỳ hạn theo lý thuyết John Hicks (1939) ("Constitutional Weakness"): Vay ngắn hạn (tiền gửi thanh khoản cao) để Cho vay dài hạn (dự án, nhà ở 25 năm).
    - Phân tán rủi ro (Pooling & Spreading): Bể vốn tập trung từ hàng triệu khách hàng giúp triệt tiêu rủi ro thanh khoản cá biệt.
    - Cỗ máy tạo thu nhập NIM (Spread): Chênh lệch giữa lãi suất cho vay và lãi suất huy động tạo ra Thu nhập lãi thuần (NII), đóng góp 70% - 80% tổng lợi nhuận của NHTM Việt Nam.
    - Ưu thế vượt trội trước P2P Lending: NHTM cam kết trả nợ 100% vô điều kiện kể cả khi bên vay vỡ nợ; trong khi P2P đẩy toàn bộ rủi ro bùng nợ/sập nền tảng cho người cho vay tự gánh chịu.
  - *2. Chức năng Trung gian Thanh toán:*
    - Đóng vai trò là "Thủ quỹ của toàn bộ nền kinh tế", quản lý tài khoản thanh toán, cung ứng công cụ séc, thẻ, ủy nhiệm chi (UNC) và hệ thống bù trừ điện tử liên ngân hàng.
    - Đảm bảo huyết mạch lưu thông hàng hóa không bị ngưng trệ; nếu hệ thống thanh toán sụp đổ, toàn bộ giao dịch kinh tế xã hội đóng băng.
    - Bản chất tiền lương: Nhận lương qua tài khoản ngân hàng thực chất là hành vi gửi tiền không kỳ hạn (CASA giá rẻ) vào NHTM.
  - *3. Chức năng Tạo tiền bút tệ (Money Creation):*
    - Cơ chế tạo tiền qua hệ thống ngân hàng: Tiền gửi ban đầu $U$ ➔ trích Dự trữ bắt buộc ($d = 10\%$) ➔ cho vay số còn lại ($q = 90\%$) ➔ tiền giải ngân được nộp vào ngân hàng thứ hai ➔ tiếp tục cho vay.
    - Công thức cấp số nhân lùi vô hạn:
      $$S_n = \frac{U(1 - q^n)}{1 - q} = \frac{U(1 - (1-d)^n)}{d}$$
      Với $n = 10$, từ $U = 5.000$ tỷ VND tạo ra lượng tiền gửi mới tích lũy $S_{10} = 32.566,1$ tỷ VND.
    - Hệ số nhân tiền cực đại: $k = \frac{1}{d} = 10$. Khối tiền tệ mở rộng tối đa: $S_\infty = \frac{U}{d} = 50.000$ tỷ VND (gấp 10 lần tiền gửi gốc).
    - Các yếu tố rò rỉ (Leakage) làm suy giảm hệ số tạo tiền: Ngân hàng giữ dự trữ vượt mức (Excess Reserves) để phòng thủ thanh khoản; Người dân rút tiền mặt chi tiêu ra khỏi hệ thống ngân hàng.
- **Hệ thống Phân loại Ngân hàng Thương mại:**
  - *Theo hình thức sở hữu:*
    - NHTM Nhà nước (Big 4): Nắm giữ 70% - 80% thị phần tín dụng và tiền gửi toàn quốc; Agribank là 100% vốn Nhà nước; Vietcombank, VietinBank, BIDV do Nhà nước nắm cổ phần chi phối tuyệt đối.
    - 31 NHTM Cổ phần: Quản trị theo mô hình ĐHĐCĐ, HĐQT, Ban Kiểm soát; chiếm 23% - 24% thị phần (ACB, Techcombank, MB, VPBank...).
    - 2 Ngân hàng Liên doanh (IVB, VRB) & 9 Ngân hàng 100% vốn nước ngoài (HSBC, Standard Chartered, Shinhan...): Thành lập dưới hình thức Công ty TNHH tại Việt Nam, là pháp nhân độc lập.
    - 52 Chi nhánh Ngân hàng nước ngoài (Citibank, SMBC, Mizuho...): Đơn vị phụ thuộc của ngân hàng mẹ ở nước ngoài, KHÔNG được phép góp vốn, mua cổ phần tại Việt Nam.
  - *Theo chiến lược kinh doanh:*
    - Bán buôn (Wholesale Banking): Tập trung phục vụ tập đoàn lớn, đa quốc gia, FDI, tài trợ dự án nghìn tỷ; mạng lưới vật lý tinh gọn.
    - Bán lẻ (Retail Banking): Phục vụ cá nhân, hộ kinh doanh, SME, vay mua nhà, thẻ tín dụng; mạng lưới chi nhánh rộng khắp.
    - Mô hình hỗn hợp: Hầu hết NHTMCP Việt Nam áp dụng mô hình hỗn hợp để tối ưu hóa nguồn thu.
    - *Bản chất Ngân hàng số (Cake by VPBank, VCB Digibank):* Không phải là một pháp nhân ngân hàng độc lập; thực chất là chiến lược kinh doanh/kênh phân phối công nghệ số được bảo trợ pháp lý bởi ngân hàng mẹ.
  - *Theo phạm vi/lĩnh vực hoạt động:*
    - Chuyên doanh vs. Đa năng (Universal Banking): Xu hướng thành lập/thâu tóm công ty con chứng khoán, bảo hiểm, leasing để bán chéo trọn gói.
    - NHTM truyền thống: Nguồn vốn phụ thuộc tiền gửi cá nhân rẻ nhất; Doanh thu phụ thuộc Thu nhập lãi thuần (NII chiếm ~83%); Tài sản hạch toán trên **Banking Book** (nắm giữ đến ngày đáo hạn, giá trị ổn định).
    - Investment Bank (IB): Không nhận tiền gửi nhỏ lẻ; Doanh thu từ Phí dịch vụ (~49%) và Tự doanh (~32%); Tài sản hạch toán trên **Trading Book** (đánh giá lại theo giá thị trường hàng ngày - Mark-to-Market).
- **Cơ cấu Tổ chức & Quản trị Thượng tầng:**
  - *Mạng lưới vật lý không gian:*
    - Hội sở chính (Head Office): Trung tâm đầu não quản trị toàn hệ thống; đảm nhận vai trò Back & Middle Office, hoạch định chiến lược, quản lý rủi ro tập trung, CNTT, kiểm toán nội bộ, Khối số.
    - Chi nhánh (Branch): Đơn vị tiền sảnh (Front Office) trực tiếp kinh doanh; có thẩm quyền phán quyết tín dụng theo hạn mức phân cấp ủy quyền từ Hội sở.
    - Phòng giao dịch (Transaction Office): Điểm vệ tinh trực thuộc Chi nhánh đặt tại các khu dân cư/trường học; nhân sự tinh gọn (5-10 người) cung cấp dịch vụ giao dịch cơ bản.
  - *Mô hình vận hành 3 sảnh chuyên môn hóa:*
    - Tiền sảnh (Front Office): Trực tiếp tiếp xúc và bán sản phẩm cho khách hàng (Khối Bán lẻ, Khối KHDN, Khối Bán buôn, Khối IB, Khối Khách hàng Ưu tiên - Wealth).
    - Trung sảnh (Middle Office): Hoạt động ĐỘC LẬP với kinh doanh; chịu trách nhiệm đo lường rủi ro danh mục, phát triển mô hình chấm điểm tín dụng (Credit Scoring), giám sát tuân thủ, quản lý tài sản bảo đảm và xử lý nợ.
    - Hậu sảnh (Back Office): Xử lý dữ liệu tập trung, hạch toán kế toán, giải ngân tín dụng, quản lý ngân quỹ, đối chiếu bù trừ, hạ tầng CNTT và nhân sự.
  - *Quản trị thượng tầng & Ủy ban ALCO:*
    - HĐQT & Ủy ban Quản lý Rủi ro: Thiết lập khẩu vị rủi ro, phê duyệt các chính sách và hạn mức lớn; giám sát độc lập ban điều hành.
    - Tổng Giám đốc (CEO): Điều hành toàn bộ hoạt động kinh doanh hàng ngày theo chiến lược đã duyệt.
    - **Ủy ban Quản lý Tài sản Nợ - Có (ALCO - Asset-Liability Committee):** Ủy ban quyền lực nhất trong ngân hàng; thường do Giám đốc Tài chính (CFO) làm Chủ tịch; chịu trách nhiệm cân đối kỳ hạn Bảng cân đối kế toán, quản trị tỷ lệ thanh khoản LCR/NSFR, phòng ngừa rủi ro lãi suất trên sổ ngân hàng (IRRBB) và xác định cơ chế định giá vốn điều chuyển nội bộ (FTP).
    - Ủy ban Chính sách Tín dụng: Do CEO làm Chủ tịch; thẩm định và phê duyệt các hồ sơ tín dụng lớn vượt thẩm quyền của chi nhánh.
- **Bốn Hoạt động Kinh doanh Chủ yếu:**
  - *I. Hoạt động Huy động vốn (Capital Mobilization - Bên Nợ):*
    - Nhận tiền gửi: Tiền gửi thanh toán không kỳ hạn (CASA giá rẻ ~0%), Tiền gửi tiết kiệm có kỳ hạn theo đường cong lợi suất dương, Tiền gửi thanh toán của các TCTD khác.
    - Phát hành Giấy tờ có giá (GTCG): Chứng chỉ tiền gửi (CDs), kỳ phiếu, tín phiếu, trái phiếu chuyển đổi/thứ cấp trung dài hạn bổ sung vốn cấp 2.
    - Vay vốn trên thị trường liên ngân hàng & Vay NHNN: Vay qua đêm/ngắn hạn hỗ trợ thanh khoản tạm thời; vay tái cấp vốn NHNN.
    - Bản chất tài chính: Nguồn vốn đầu vào làm phát sinh chi phí trả lãi; tiềm ẩn rủi ro thanh khoản nếu khách hàng rút tiền đồng loạt.
  - *II. Hoạt động Cấp tín dụng (Credit Extension - Bên Có):*
    - Đa dạng phương thức: Cho vay (ngắn/trung/dài hạn - chiếm tỷ trọng áp đảo); Bảo lãnh ngân hàng (cam kết tài chính); Bao thanh toán (Factoring - tài trợ khoản phải thu); Chiết khấu GTCG; Cho thuê tài chính (Leasing - tối ưu thuế và TSĐB).
    - Trụ cột tạo thu nhập: Đem lại Thu nhập lãi thuần (NII), đóng góp ~70% tổng lợi nhuận ngân hàng (ví dụ VietinBank lãi 30.000 tỷ thì 21.000 tỷ đến từ hoạt động cấp tín dụng).
    - Rủi ro sống còn: Rủi ro tín dụng khách hàng vỡ nợ (NPL) và Rủi ro chênh lệch kỳ hạn (The Gap) do dùng tiền gửi ngắn hạn cho vay dài hạn.
  - *III. Dịch vụ Thanh toán và Ngân quỹ (Payment & Cash Services):*
    - Cung ứng phương tiện: Séc, ủy nhiệm chi (UNC), ủy nhiệm thu, thẻ ghi nợ (Debit) và thẻ tín dụng (Credit).
    - Dịch vụ thanh toán trong nước & quốc tế: Chuyển tiền điện tử, thanh toán hóa đơn tự động, phát hành L/C (Thư tín dụng), nhờ thu tài liệu (D/P, D/A).
    - Thu hộ và chi hộ: Dịch vụ thu hộ học phí, chi trả lương cho doanh nghiệp và trường đại học (như Agribank thu hộ học phí và trả lương cho UEH).
    - Lợi ích: Mang lại Thu nhập phí thuần (Net Fee Income - nguồn thu bền vững, không chịu rủi ro tín dụng); đối mặt rủi ro vận hành (lỗi hệ thống, gian lận công nghệ).
  - *IV. Hoạt động Kinh doanh khác (Other Business Activities):*
    - Góp vốn, mua cổ phần: Thành lập hoặc mua lại công ty con bảo hiểm, chứng khoán, quản lý quỹ, leasing để phát triển Universal Banking và phân phối bảo hiểm qua ngân hàng (Bancassurance).
    - Thị trường tiền tệ & Phái sinh: Đấu thầu tín phiếu Kho bạc, mua bán TPCP; Kinh doanh ngoại hối (FX Spot, Forward, Swap); Giao dịch phái sinh lãi suất (IRS, CCS) phòng ngừa rủi ro tỷ giá và lãi suất.
    - Ngân hàng Giám sát (Custodian Bank): Cung cấp dịch vụ lưu ký chứng khoán, định giá NAV và giám sát dòng tiền cho các quỹ đầu tư quy mô 5.000 - 7.000 tỷ VND, đem lại nguồn thu phí ủy thác béo bở.
    - Phân định hạch toán: Phân định rạch ròi danh mục nắm giữ đến hạn (Banking Book) và danh mục kinh doanh ngắn hạn (Trading Book - Mark-to-Market).

### [E4] Bên thừa vốn (Surplus Units)
- **Bản chất:** Các cá nhân, hộ gia đình, tổ chức kinh tế sở hữu nguồn vốn tiết kiệm thặng dư.
- **Đặc trưng hành vi & Kỳ vọng:**
  - Có tâm lý ngại rủi ro (Risk-averse), đòi hỏi cam kết hoàn trả 100% vốn gốc kèm lãi suất sinh lời.
  - Ưu tiên tính thanh khoản cao (kỳ hạn gửi ngắn, khả năng rút tiền tức thời khi có nhu cầu chi tiêu đột xuất).
  - Cung ứng nguồn vốn CASA với lãi suất danh nghĩa xấp xỉ 0% cho ngân hàng thông qua tài khoản thanh toán nhận lương.
- **Các kênh phân bổ tài sản:**
  - Kênh tiền gửi tại NHTM: Tiền gửi thanh toán không kỳ hạn (CASA), Tiết kiệm kỳ hạn 1-12 tháng, Chứng chỉ tiền gửi (CDs).
  - Kênh phi tiền gửi: Cổ phiếu niêm yết, Trái phiếu doanh nghiệp, Chứng chỉ quỹ mở/đóng, Hợp đồng bảo hiểm nhân thọ, Tài khoản hợp tác đầu tư Fintech.
- **Rủi ro hệ thống:**
  - Tâm lý bầy đàn (Herd behavior): Dễ bị kích động bởi tin đồn, tháo chạy tập thể tạo nên Bank Run.
  - Mất vốn ở kênh phi tiền gửi do không được bảo hiểm tiền gửi bảo vệ.

### [E5] Bên thiếu vốn (Deficit Units)
- **Bản chất:** Các doanh nghiệp sản xuất kinh doanh, thương mại, hộ gia đình vay tiêu dùng và các đơn vị công cần vốn đầu tư hạ tầng.
- **Đặc trưng nhu cầu:**
  - Nhu cầu tài trợ kỳ hạn trung và dài hạn (3 năm đến 25 năm) để xây dựng nhà máy, đầu tư thiết bị, mua bất động sản hoặc làm dự án PPP.
  - Mong muốn tối thiểu hóa chi phí lãi vay và kéo dài thời gian ân hạn trả nợ.
- **Kênh tiếp cận nguồn vốn:**
  - Vay vốn tín dụng từ NHTM: Vốn lưu động ngắn hạn, Vay trung dài hạn dự án, Cho vay hợp vốn (Syndicated Loans) cho các đại dự án nghìn tỷ, Bao thanh toán (Factoring), Thuê mua tài chính (Leasing).
  - Huy động qua thị trường vốn: Phát hành Trái phiếu Doanh nghiệp (riêng lẻ/ra công chúng), Chào bán cổ phiếu lần đầu ra công chúng (IPO).
  - Vay tiêu dùng tín chấp từ CTTC hoặc ứng dụng Mua trước trả sau (BNPL).
- **Rủi ro & Tác động hệ thống:** Chịu áp lực tăng chi phí tài chính khi lãi suất thả nổi điều chỉnh tăng; kinh doanh thua lỗ dẫn đến vỡ nợ, trực tiếp chuyển hóa thành nợ xấu (NPL) trên bảng cân đối của ngân hàng.

### [E6] Mạng lưới an toàn thể chế (Safety Net)
- **Bản chất & Sứ mệnh:** Được thiết kế để triệt tiêu trạng thái cân bằng xấu trong mô hình kinh tế toán học Diamond & Dybvig (1983). Nếu người gửi tiền tin rằng ngân hàng có thể mất thanh khoản, tất cả sẽ đồng loạt đi rút tiền và biến nỗi sợ thành hiện thực (Self-fulfilling Prophecy). Safety Net dựng lên để bảo vệ niềm tin công chúng.
- **Hai chốt chặn rường cột:**
  - *Bảo hiểm tiền gửi (Deposit Insurance):* Cơ chế bảo vệ tài chính công khai, cam kết chi trả hạn mức tối đa (hiện tại là 125 triệu đồng tại Việt Nam) cho người gửi tiền cá nhân khi TCTD phá sản.
  - *Người cho vay cuối cùng (LoLR):* Ngân hàng Trung ương can thiệp cung cấp nguồn thanh khoản cứu trợ khẩn cấp (qua tái cấp vốn, cho vay đặc biệt Đ.192, 193 Luật TCTD 2024) khi ngân hàng mất khả năng thanh toán tạm thời nhưng còn đủ tài sản bảo đảm.
- **Hạn chế & Rủi ro đạo đức (Moral Hazard):**
  - Chỉ bảo vệ người gửi tiền nhỏ lẻ, không bảo hiểm cho tiền gửi doanh nghiệp hay nhà đầu tư lớn.
  - Ngân hàng thương mại có thể ỷ lại vào sự cứu trợ của nhà nước để chấp nhận rủi ro quá mức (Moral Hazard). Do đó, Safety Net bắt buộc phải đi kèm chế độ giám sát và thanh tra an toàn nghiêm ngặt từ NHNN.

### [E7] Định chế phi tiền gửi (Non-depository Institutions)
- **Ranh giới pháp lý cốt lõi:**
  - TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP nhận tiền gửi cá nhân từ công chúng và TUYỆT ĐỐI BỊ CẤM cung ứng dịch vụ thanh toán qua tài khoản của khách hàng.
  - Dòng tiền huy động không phải là "nợ tiền gửi cam kết hoàn trả 100% gốc", mà là phí dịch vụ, tiền mua chứng chỉ quỹ, trái phiếu hoặc vốn góp ủy thác đầu tư. Khách hàng tự chịu rủi ro theo thị trường.
- **Cấu trúc phân loại theo phân ngành:**
  - *Công ty chứng khoán (CTCK):* Hoạt động môi giới, cho vay ký quỹ (Margin), tự doanh, tư vấn tài chính doanh nghiệp M&A, bảo lãnh phát hành chứng khoán (SSI, TCBS, VPS, Vietcap).
  - *Công ty bảo hiểm (Nhân thọ & Phi nhân thọ):* Thu phí bảo hiểm định kỳ (Premiums); thực hiện tái đầu tư an toàn dài hạn vào Trái phiếu Chính phủ, tiền gửi ngân hàng kỳ hạn dài và cổ phiếu blue-chip (Bảo Việt, Prudential, Manulife, MIC).
  - *Quỹ đầu tư & Công ty Quản lý quỹ:* Phát hành chứng chỉ quỹ (CCQ) huy động vốn từ nhà đầu tư cá nhân/tổ chức; quản lý danh mục đa tài sản (Dragon Capital, VinaCapital, SSIAM, Techcom Capital); thuê NHTM làm Ngân hàng Giám sát (Custodian Bank) bảo đảm an toàn dòng tiền.
  - *Công ty tài chính (CTTC) & Cho thuê tài chính:* Thuộc nhóm TCTD phi ngân hàng (do NHNN cấp phép và quản lý); huy động vốn từ vốn CSH, phát hành trái phiếu, vay liên ngân hàng, và tiền gửi có kỳ hạn từ tổ chức; cấp tín dụng tiêu dùng tín chấp, cho thuê tài chính máy móc thiết bị (FE Credit, HD SAISON, VietinBank Leasing).
  - *Tổ chức cầm đồ & Cho vay thay thế:* Cho vay cầm cố ngắn hạn giải ngân nhanh (F88, Vietmoney).
- **Mô hình FHC & Chiến lược Bán chéo (Cross-selling):**
  - Tích hợp "Ngân hàng - Chứng khoán - Bảo hiểm - Leasing" phục vụ trọn vòng đời tài chính của khách hàng (Bancassurance).
  - *Yêu cầu Bức tường lửa (Firewalls):* Các công ty con phải hoàn toàn độc lập về pháp lý, vốn và hạch toán; hoạt động như các vách ngăn chống chìm của tàu Titanic nhằm cô lập rủi ro thua lỗ từ mảng đầu tư, bảo vệ an toàn cho Ngân hàng mẹ.

### [E8] Định chế công nghệ & Nền tảng số (Fintech & Super-Apps)
- **Bản chất & Vị thế:** Các công ty công nghệ cung cấp giải pháp tài chính số hóa dựa trên nền tảng (Platform), Open API, Trí tuệ nhân tạo (AI) và Phân tích dữ liệu lớn (Big Data).
- **Chiến lược Siêu ứng dụng (Super-App):**
  - Mở rộng hệ sinh thái đa dịch vụ (gọi xe, giao đồ ăn, thương mại điện tử) để thu thập dữ liệu hành vi khổng lồ, sau đó tích hợp dịch vụ tài chính (Grab, Shopee) nhằm giữ chân khách hàng trọn đời.
- **Phân định bản chất sản phẩm & Mô hình Ngân hàng số:**
  - *Ngân hàng số (Cake by VPBank, VCB Digibank):* Không phải là định chế độc lập mà là kênh phân phối kỹ thuật số và chiến lược mở rộng tệp khách hàng trẻ của các ngân hàng mẹ.
  - *Tiết kiệm Online:* Ví điện tử chỉ là kênh phân phối kỹ thuật (Platform); dòng tiền thực tế được chuyển về gửi tại NHTM đối tác (như MB, Bản Việt) và ĐƯỢC hưởng bảo hiểm tiền gửi.
  - *Túi Thần Tài / Đầu tư:* Bản chất là Hợp đồng hợp tác kinh doanh với tổ chức quản lý đầu tư bên thứ ba; khách hàng chấp nhận rủi ro đầu tư và KHÔNG ĐƯỢC hưởng bảo hiểm tiền gửi.
  - *P2P Lending:* Mô hình kết nối trực tiếp người cho vay và người đi vay; tiềm ẩn rủi ro vỡ nợ rất cao và người cho vay tự chịu mất vốn nếu người vay bùng nợ hoặc nền tảng sụp đổ.
  - *Mua trước trả sau (BNPL: SPayLater):* Bản chất là một khoản vay tín dụng tiêu dùng tín chấp được cấp bởi ngân hàng/CTTC đối tác thông qua nền tảng số.
- **Rủi ro trồi hiện & Thách thức vĩ mô:**
  - Gặm nhấm thị phần thanh toán và làm xói mòn nguồn thu phí truyền thống của ngân hàng.
  - Đẩy tăng áp lực chi phí đầu tư CNTT và tỷ lệ CIR.
  - Nguy cơ Rút tiền Mili-giây (Millisecond Bank Run) qua mạng lưới API Bots kết nối dữ liệu mạng xã hội, có khả năng kích hoạt tháo chạy hàng nghìn tỷ trong vài giây, vô hiệu hóa đệm an toàn LCR 30 ngày của Basel III.

---

## 4. Relationship Registry

```text
[E1] NHNN ──(Phối hợp CSTK & CSTT)── [E2] MoF
[E1] NHNN ──(CSTT, Dự trữ BB d=10%, Basel CAR/LDR, Room tín dụng)──► [E3] NHTM
[E3] NHTM ──(Ký gửi Dự trữ BB, Báo cáo an toàn vĩ mô)──► [E1] NHNN
[E2] MoF ──(Phát hành TPCP cung ứng HQLA)──► [E3] NHTM
[E2] MoF ──(Quản lý Nhà nước TTCK & Bảo hiểm qua UBCKNN/QLGSBH)──► [E7] Định chế phi TG
[E4] Bên thừa vốn ──(Gửi tiền tiết kiệm & CASA giá rẻ ~0%)──► [E3] NHTM (G5.1 Huy động vốn)
[E3] NHTM ──(Chi trả lãi suất tiền gửi, Thanh toán yêu cầu)──► [E4] Bên thừa vốn
[E3] NHTM (G5.2 Cấp tín dụng) ──(Cho vay, Bảo lãnh, Leasing, Chiết khấu)──► [E5] Bên thiếu vốn
[E5] Bên thiếu vốn ──(Hoàn trả nợ gốc & Lãi vay, Rủi ro nợ xấu NPL)──► [E3] NHTM (G5.2 Cấp tín dụng)
[E4] Bên thừa vốn ──(Mua CCQ, Cổ phiếu, Trái phiếu DN, Phí bảo hiểm)──► [E7] Định chế phi TG
[E5] Bên thiếu vốn ──(Thu xếp vốn M&A, Bảo lãnh Trái phiếu & IPO)──► [E7] Định chế phi TG
[E3] NHTM (G5.4 HĐ khác) ──(Góp vốn lập CT con CTCK, Bảo hiểm, Leasing - Bán chéo Bancassurance)──► [E7] Định chế phi TG
[E3] NHTM (G1.3 Ranh giới) ──(Ranh giới pháp lý cấm nhận tiền gửi cá nhân & thanh toán)──► [E7] Định chế phi TG
[E1] NHNN ──(Dựng Bức tường lửa Firewalls ngăn lây lan rủi ro)──► [E7] Định chế phi TG
[E3] NHTM ──(Nộp phí Bảo hiểm tiền gửi định kỳ)──► [E6] Safety Net
[E6] Safety Net ──(Cam kết hạn mức chi trả 125tr triệt tiêu Bank Run)──► [E4] Bên thừa vốn
[E1] NHNN ──(Cho vay đặc biệt LoLR Đ.192, 193 bơm thanh khoản khẩn cấp)──► [E6] Safety Net
[E8] Fintech ──(Cạnh tranh Disintermediation - P2P vs NHTM cam kết trả nợ 100%)──► [E3] NHTM (G2.1 Chức năng TGTC)
[E3] NHTM (G3.2 Chiến lược) ──(Bảo trợ pháp lý ngân hàng số Cake/VCB Digibank làm kênh phân phối)──► [E8] Fintech
[E8] Fintech ──(Hạ tầng thanh toán, Open API, Rủi ro rút tiền mili-giây)──► [E3] NHTM
[E8] Fintech ──(Trải nghiệm Super-App, Ví điện tử, Dịch vụ BNPL)──► [E4] Bên thừa vốn
```

### Bảng Diễn giải Quan hệ Chi tiết (Bao gồm các liên kết mở rộng từ CH02a)

| Chiều Quan hệ (Flow) | Loại Liên kết (Type) | Căn cứ Nội dung & Cơ chế Vận hành Thực tế |
| :--- | :--- | :--- |
| **[E1] ↔ [E2]** | Phối hợp Vĩ mô | Phối hợp Chính sách Tiền tệ (NHNN) và Chính sách Tài khóa (Bộ Tài chính) nhằm giữ vững ổn định kinh tế vĩ mô, kiểm soát lạm phát và ngăn chặn hiệu ứng chèn lấn tín dụng (Crowding-out). |
| **[E1] → [E3]** | Giám sát & Điều tiết | NHNN điều tiết cung ứng tiền tệ qua OMO, Tái cấp vốn, Dự trữ bắt buộc ($d = 10\%$); thiết lập chuẩn mực Basel (CAR ≥ 8%, siết LDR 85%); áp trần sở hữu cổ phần theo Luật Các TCTD 2024 để ngăn ngừa sở hữu chéo. |
| **[E3] → [E1]** | Tuân thủ & Ký gửi | NHTM mở tài khoản và ký gửi dự trữ bắt buộc tại NHNN; thực hiện nghĩa vụ báo cáo thống kê định kỳ phục vụ giám sát an toàn vĩ mô và vi mô. |
| **[E2] → [E3]** | Cung ứng Tài sản HQLA | Kho bạc Nhà nước (Bộ Tài chính) phát hành Trái phiếu Chính phủ; NHTM đầu tư nắm giữ TPCP để hình thành tài sản thanh khoản chất lượng cao (HQLA) đáp ứng chuẩn LCR Basel III. |
| **[E2] → [E7]** | Quản lý Chuyên ngành | Bộ Tài chính quản lý trực tiếp thị trường chứng khoán (thông qua UBCKNN) và thị trường bảo hiểm (thông qua Cục Quản lý, Giám sát Bảo hiểm). |
| **[E4] → [E3] (G5.1)** | Dẫn vốn Tiền gửi Rẻ nhất | Người gửi tiền cá nhân & tổ chức cung ứng thặng dư nhàn rỗi thông qua tài khoản CASA (lãi suất ~0%) và sổ tiết kiệm có kỳ hạn; chấp nhận lãi suất thấp để đổi lấy sự an toàn tuyệt đối và thanh khoản cao. |
| **[E3] → [E4]** | Dịch vụ & Hoàn trả | NHTM có nghĩa vụ pháp lý hoàn trả 100% tiền gửi vô điều kiện khi đến hạn hoặc khi khách hàng yêu cầu rút tiền; chi trả lãi suất tiền gửi; cung cấp dịch vụ thanh toán 24/7. |
| **[E3] (G5.2) → [E5]** | Cấp tín dụng Đa dạng | NHTM cung cấp vốn qua các hình thức: Cho vay ngắn/trung/dài hạn, Bảo lãnh ngân hàng, Bao thanh toán (Factoring), Chiết khấu GTCG, Cho thuê tài chính (Leasing); thực hiện biến đổi kỳ hạn (Maturity Transformation). |
| **[E5] → [E3] (G5.2)** | Trả nợ & Rủi ro Tín dụng | Bên vay hoàn trả nợ gốc và lãi vay định kỳ; tạo ra Thu nhập lãi thuần (NII chiếm ~70% lợi nhuận ngân hàng); nếu bên vay mất khả năng thanh toán sẽ trực tiếp kích hoạt rủi ro nợ xấu (NPL). |
| **[E4] → [E7]** | Đầu tư Thị trường Vốn | Cá nhân/tổ chức ủy thác vốn mua chứng chỉ quỹ, cổ phiếu, trái phiếu doanh nghiệp hoặc tham gia bảo hiểm nhân thọ; tự gánh chịu rủi ro thị trường theo biến động giá trị tài sản ròng (NAV). |
| **[E5] → [E7]** | Thu xếp Tài chính Doanh nghiệp | Doanh nghiệp sử dụng dịch vụ tư vấn M&A, bảo lãnh phát hành cổ phiếu IPO và trái phiếu doanh nghiệp thông qua Khối Ngân hàng Đầu tư (IB) của các Công ty Chứng khoán. |
| **[E3] (G5.4) → [E7]** | Universal Banking & Bán chéo | NHTM mẹ thành lập/mua lại công ty con bảo hiểm, chứng khoán, quản lý quỹ, leasing để hoàn thiện mô hình Universal Banking và đẩy mạnh bán chéo (Bancassurance) gia tăng thu nhập ngoài lãi. |
| **[E3] (G1.3) → [E7]** | Ranh giới Pháp lý Độc quyền | Luật Các TCTD 2024 quy định ranh giới nghiêm ngặt: TCTD phi ngân hàng (CTTC, Leasing) TUYỆT ĐỐI BỊ CẤM nhận tiền gửi từ cá nhân và BỊ CẤM cung ứng dịch vụ thanh toán qua tài khoản khách hàng. |
| **[E1] → [E7]** | Thiết lập Bức tường lửa | NHNN yêu cầu thiết lập ranh giới "Bức tường lửa" (Firewalls) độc lập về vốn, nhân sự và hạch toán; ngăn chặn rủi ro thua lỗ từ mảng đầu tư chứng khoán lây lan sang làm sụp đổ NHTM mẹ. |
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
| **CH02b** | **Các hoạt động kinh doanh chủ yếu của Ngân hàng đầu tư** | `[E7]` *(Đào sâu nhánh IB/CTCK)*, liên kết `[E5]`, `[E3]`, `[E2]` | **Đào sâu Phân khúc Phi tiền gửi [E7] (Trọng tâm Investment Banking):** Cấu trúc nghiệp vụ Bảo lãnh phát hành chứng khoán (Underwriting), Tư vấn M&A, Thu xếp vốn doanh nghiệp, Tự doanh, Môi giới và Quản lý tài sản. | **DỰ KIẾN KẾ TIẾP** |
| **CH03** | **Quản trị hoạt động kinh doanh ngân hàng** | `[E3]` *(Đào sâu Quản trị)*, liên kết `[E1]`, `[E6]` | **Đào sâu Năng lực Quản trị Chiến lược & Rủi ro tại [E3]:** Quản trị An toàn vốn Basel II/III (ICAAP), Quản trị Thanh khoản và Rủi ro thanh khoản (ILAAP), Quản trị Rủi ro Tín dụng, Rủi ro Thị trường, Rủi ro Hoạt động và tối ưu hóa hiệu quả kinh doanh qua chu kỳ. | **DỰ KIẾN KẾ TIẾP** |

---
*Ghi chú duy trì tính liên tục (Continuity Note):* File này là bộ nhớ dùng chung xuyên suốt toàn bộ học phần. Khi thực hiện các chương kế tiếp (`CH02b`, `CH03`...), tuyệt đối không thay đổi mã số của các Entity đã được định danh (`E1` đến `E8`). Các chương sau chỉ bổ sung kiến thức chuyên sâu vào Entity tương ứng và cập nhật bảng Chapter Coverage.
