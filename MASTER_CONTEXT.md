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
| **[E3]** | **Định chế nhận tiền gửi (NHTM cốt lõi)** | Depository Institutions | Vietcombank, BIDV, VietinBank, MB, Techcombank, ACB | Đặc quyền huy động tiền gửi từ công chúng; biến đổi kỳ hạn (Maturity Transformation); mạng lưới truyền dẫn thanh toán quốc gia. |
| **[E4]** | **Bên thừa vốn (Surplus Units)** | Chủ thể Cung ứng Vốn Tiết kiệm | Hộ gia đình, Cá nhân gửi tiền, Nhà đầu tư | Cung ứng nguồn vốn nhàn rỗi cho nền kinh tế; tìm kiếm lãi suất sinh lời, ưu tiên bảo toàn vốn gốc và đòi hỏi thanh khoản cao. |
| **[E5]** | **Bên thiếu vốn (Deficit Units)** | Chủ thể Cầu vốn Đầu tư & Chi tiêu | Doanh nghiệp sản xuất kinh doanh, Hộ tiêu dùng, Chính phủ | Hấp thụ vốn cho sản xuất, đầu tư hạ tầng, mua sắm tài sản; đòi hỏi kỳ hạn vay dài và chi phí vốn tối ưu; phát sinh nghĩa vụ hoàn trả. |
| **[E6]** | **Mạng lưới an toàn thể chế (Safety Net)** | Cơ chế Bảo vệ Niềm tin & Cứu trợ | Bảo hiểm Tiền gửi Việt Nam (DIV) & Cơ chế LoLR | Bảo vệ người gửi tiền nhỏ lẻ; ngăn chặn hiệu ứng rút tiền hàng loạt (Bank Run) theo mô hình Diamond & Dybvig (1983); dập tắt sụp đổ dây chuyền. |
| **[E7]** | **Định chế phi tiền gửi (Non-depository)** | Non-depository Institutions | CTCK (SSI, TCBS), Bảo hiểm (Bảo Việt, Manulife), Quỹ (Dragon Capital), CTTC (FE Credit) | Cung cấp dịch vụ đầu tư, bảo hiểm, thu xếp vốn chuyên sâu; tuyệt đối KHÔNG nhận tiền gửi cá nhân từ công chúng; khách hàng tự chịu rủi ro thị trường. |
| **[E8]** | **Định chế công nghệ & Nền tảng số (Fintech)** | Fintech Platforms & Super-Apps | Ví MoMo, ZaloPay, VNPay, Grab, Shopee (SPayLater) | Cầu nối hạ tầng kỹ thuật phân phối sản phẩm số; khai thác Big Data & AI; cung cấp thanh toán, BNPL; kênh liên kết huy động vốn cho NHTM. |

---

## 2. System Hierarchy

```text
HỆ THỐNG TÀI CHÍNH & MÔ HÌNH HOẠT ĐỘNG KINH DOANH NGÂN HÀNG
│
├── 1. TẦNG QUẢN LÝ VĨ MÔ & ĐIỀU TIẾT THỂ CHẾ
│   ├── [E1] Ngân hàng Trung ương (NHNN Việt Nam)
│   │   ├── 1.1 Vị thế pháp lý & Mục tiêu phi lợi nhuận (Cơ quan ngang Bộ)
│   │   ├── 1.2 Công cụ điều tiết CSTT (OMO, Tái cấp vốn, Dự trữ bắt buộc)
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
│   │   ├── 4.2 Kênh phân bổ tiền gửi: CASA không kỳ hạn, Tiết kiệm có kỳ hạn, Chứng chỉ tiền gửi (CDs)
│   │   ├── 4.3 Kênh phân bổ phi tiền gửi: Cổ phiếu, Trái phiếu DN, Chứng chỉ quỹ, Hợp đồng bảo hiểm
│   │   └── 4.4 Rủi ro tâm lý bầy đàn kích hoạt tháo chạy tập thể (Bank Run)
│   │
│   ├── [E3] Định chế nhận tiền gửi (NHTM cốt lõi) ── [TRỤC CHÍNH CỦA HỆ THỐNG]
│   │   ├── 3.1 Đặc quyền pháp lý & Vị thế kinh tế
│   │   │   ├── Quyền năng độc quyền: Tiếp nhận tiền gửi từ công chúng (Cá nhân & Tổ chức)
│   │   │   ├── Hóa giải xung đột kỳ hạn hiến định Hicks (1939) ("Constitutional Weakness")
│   │   │   └── Cơ chế truyền dẫn thanh toán huyết mạch của toàn bộ nền kinh tế
│   │   ├── 3.2 Cơ chế vận hành ALM & Kỹ thuật quản trị Bảng cân đối
│   │   │   ├── Biến đổi kỳ hạn (Maturity Transformation): "Huy động ngắn hạn (Fund Short) - Cho vay dài hạn (Lend Long)"
│   │   │   ├── Đòn bẩy tài chính cực cao (Vốn chủ sở hữu tài trợ tài sản gấp 10 - 25 lần)
│   │   │   ├── Bể thanh khoản quy luật số lớn & Vốn tiền gửi lõi (Core Deposits / CASA)
│   │   │   ├── Kỹ thuật phòng vệ: Quản trị khe hở (The Gap), Lãi suất thả nổi, Phái sinh IRS
│   │   │   └── Chuẩn thanh khoản Basel III: Đệm LCR (chống chịu 30 ngày) & Tỷ lệ vốn ổn định NSFR
│   │   ├── 3.3 Mô hình cấu trúc tổ chức & Kinh doanh
│   │   │   ├── Mô hình BHC (Bank Holding Company Act 1956) vs FHC (Gramm-Leach-Bliley Act 1999)
│   │   │   ├── Universal Banking (Tích hợp Ngân hàng thương mại & Ngân hàng đầu tư)
│   │   │   ├── 6 Mô hình chuyên biệt: Narrow, Universal, Investment, Retail, Wholesale, Offshore Banks
│   │   │   └── Độc lập hóa Treasury Middle Office trực thuộc CEO
│   │   └── 3.4 Rủi ro sống còn & Dịch chuyển tư duy chiến lược
│   │       ├── Rủi ro thanh khoản (Liquidity Risk) & Rủi ro tín dụng vỡ nợ (Credit / Default Risk)
│   │       ├── Rủi ro lây lan (Contagion) trong mô hình tập đoàn FHC
│   │       ├── Chuyển dịch Pre-crash (Chạy theo ROE) ──► Post-crash (Lấy Bảng cân đối làm cốt lõi)
│   │       └── Áp lực chỉ số CIR & Thách thức Rút tiền Mili-giây qua Automated API Bots
│   │
│   └── [E5] Bên thiếu vốn (Deficit Units)
│       ├── 5.1 Nhu cầu tài trợ dài hạn: Vốn lưu động, Máy móc thiết bị, Dự án hạ tầng, Mua nhà
│       ├── 5.2 Kênh tiếp cận vốn: Tín dụng NHTM, Cho vay hợp vốn (Syndicated Loans), Thị trường vốn (Trái phiếu, Cổ phiếu)
│       └── 5.3 Nghĩa vụ pháp lý & Nguy cơ phát sinh nợ xấu (NPL) đe dọa ngân hàng
│
└── 4. TẦNG ĐỊNH CHẾ CHUYÊN BIỆT & NỀN TẢNG SỐ MỞ RỘNG
    ├── [E7] Định chế phi tiền gửi (Non-depository Institutions)
    │   ├── 7.1 Ranh giới pháp lý tối thượng: TUYỆT ĐỐI KHÔNG nhận tiền gửi cá nhân từ công chúng
    │   ├── 7.2 Cơ chế rủi ro: Khách hàng tự chịu rủi ro thị trường (Không cam kết hoàn 100% gốc)
    │   ├── 7.3 Phân loại định chế chuyên biệt:
    │   │   ├── Công ty chứng khoán (CTCK): Môi giới, Margin, Tư vấn M&A, Bảo lãnh phát hành IPO
    │   │   ├── Công ty bảo hiểm: Thu phí định kỳ đầu tư tài sản an toàn dài hạn (TPCP, Cổ phiếu blue-chip)
    │   │   ├── Quỹ đầu tư & Quản lý quỹ: Phát hành CCQ quản lý danh mục đa tài sản
    │   │   └── Công ty tài chính (CTTC) & Cho thuê tài chính: Cho vay tiêu dùng tín chấp, cho thuê máy móc
    │   ├── 7.4 Tích hợp bán chéo (Cross-selling) & Bancassurance
    │   └── 7.5 Cơ chế "Bức tường lửa" (Firewalls) ngăn ngừa rủi ro lây lan (như vách ngăn tàu Titanic)
    │
    └── [E8] Định chế công nghệ & Nền tảng số (Fintech & Super-Apps)
        ├── 8.1 Vị thế hệ sinh thái: Cầu nối hạ tầng kỹ thuật (Platform), Open API, Phân tích dữ liệu lớn (Big Data)
        ├── 8.2 Chiến lược Siêu ứng dụng (Super-App): Tích lũy hành vi khách hàng, giữ chân người dùng trọn đời
        ├── 8.3 Phân định bản chất sản phẩm:
        │   ├── Tiết kiệm Online liên kết: Vốn chuyển về NHTM đối tác (ĐƯỢC Bảo hiểm tiền gửi)
        │   ├── Túi hợp tác kinh doanh: Bản chất ủy thác đầu tư (KHÔNG ĐƯỢC Bảo hiểm tiền gửi)
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
  - Quy định tỷ lệ Dự trữ bắt buộc (RRR) kiểm soát hệ số tạo tiền.
  - Quản lý hạn mức tăng trưởng tín dụng (Room tín dụng) định hướng dòng vốn vào lĩnh vực ưu tiên.
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

### [E3] Định chế nhận tiền gửi (NHTM cốt lõi)
- **Đặc quyền tối thượng & Vị thế kinh tế:**
  - Là định chế duy nhất được phép huy động tiền gửi từ công chúng (cả cá nhân và tổ chức).
  - Hóa giải mâu thuẫn "yếu kém mang tính hiến định" (Constitutional Weakness) theo lý thuyết John Hicks (1939): Người gửi tiền muốn gửi ngắn hạn để linh hoạt thanh khoản; người đi vay cần vốn dài hạn để đầu tư sản xuất/nhà ở.
  - Đóng vai trò là mạng lưới truyền dẫn và thanh toán cốt lõi của nền kinh tế.
- **Cơ chế vận hành ALM & Bảng cân đối kế toán:**
  - *Biến đổi kỳ hạn (Maturity Transformation):* Huy động ngắn hạn (Fund Short) để Cho vay dài hạn (Lend Long).
  - *Đòn bẩy tài chính cực cao (Financial Leverage):* Nền tảng vốn chủ sở hữu nhỏ tài trợ quy mô tài sản lớn gấp 10 - 25 lần.
  - *Bể thanh khoản tập trung & Quy luật số lớn (Law of Large Numbers):* Dòng tiền nộp/rút của hàng triệu khách hàng triệt tiêu lẫn nhau; hình thành phần "Tiền gửi lõi" (Core Deposits / CASA) có tính chất nằm trơ dài hạn trong hệ thống.
  - *Quản trị rủi ro lãi suất (Interest Rate Risk):* Đo lường khe hở nhạy cảm lãi suất (The Gap); áp dụng cơ chế lãi suất cho vay thả nổi (Floating Rates) bằng lãi suất cơ sở cộng biên độ cố định; sử dụng công cụ phái sinh hoán đổi lãi suất (IRS).
  - *Chuẩn mực thanh khoản Basel III:* Duy trì tỷ lệ đảm bảo thanh khoản 30 ngày (LCR) bằng tài sản HQLA và tỷ lệ nguồn vốn ổn định ròng (NSFR).
- **Cấu trúc tập đoàn & 6 Mô hình kinh doanh ngân hàng:**
  - *Bank Holding Company (BHC):* Công ty mẹ sở hữu ngân hàng thương mại con và các công ty con phi ngân hàng có hoạt động gắn liền mật thiết với ngân hàng (Đạo luật BHC 1956).
  - *Financial Holding Company (FHC):* Tập đoàn tài chính toàn diện sở hữu cả ngân hàng, chứng khoán, bảo hiểm, bất động sản (Đạo luật Gramm-Leach-Bliley 1999 dỡ bỏ rào cản Glass-Steagall 1933).
  - *Narrow Banks (Ngân hàng hẹp):* Siêu truyền thống, chỉ nhận tiền gửi và đầu tư vào tài sản thanh khoản tuyệt đối an toàn (TPCP, gửi NHNN); đại diện tương đồng tại VN: NH Chính sách Xã hội (VBSP), Kho bạc Nhà nước.
  - *Universal Banks (Ngân hàng đa năng):* Tích hợp toàn diện NHTM và Ngân hàng đầu tư (VCB, BIDV, TCB, MB).
  - *Investment Banks (Ngân hàng đầu tư):* Không nhận tiền gửi công chúng; thu phí dịch vụ underwriting, tư vấn M&A, tự doanh (Vietcap, TCBS, SSI IB).
  - *Retail Banks (Ngân hàng bán lẻ):* Tập trung khách hàng cá nhân, vay mua nhà, thẻ tín dụng, ô tô (ACB, VIB, TPBank).
  - *Wholesale Banks (Ngân hàng bán buôn):* Phục vụ tập đoàn lớn, FDI, chính phủ, cho vay hợp vốn, tài trợ thương mại (Citibank, HSBC, Standard Chartered, khối KHDN lớn BIDV/VCB).
  - *Offshore Banks (Ngân hàng ngoại biên):* Đăng ký tại trung tâm tài chính hải ngoại phục vụ khách hàng không cư trú, ưu đãi thuế và bảo mật cao (Singapore, Cayman Islands, BVI).
- **Dịch chuyển tư duy chiến lược:**
  - *Pre-crash Paradigm:* Giả định vốn/thanh khoản vô hạn ──► Chạy theo chỉ tiêu ROE không điều chỉnh rủi ro ──► Hạ chuẩn cho vay, bơm phồng tài sản mạo hiểm.
  - *Post-crash Paradigm:* Thừa nhận vốn/thanh khoản hữu hạn ──► Sức mạnh Bảng cân đối làm trọng tâm (ICAAP/ILAAP) ──► Định hình danh mục tài sản an toàn, quản trị vốn kinh tế bền vững xuyên chu kỳ.
- **Thách thức trồi hiện:** Áp lực cải thiện chỉ số CIR; nguy cơ rút tiền hàng loạt trong vài giây (Millisecond Liquidity Run) kích hoạt bởi Automated API Bots kết nối tâm lý mạng xã hội, phá vỡ giả định đệm LCR 30 ngày.

### [E4] Bên thừa vốn (Surplus Units)
- **Bản chất:** Các cá nhân, hộ gia đình, tổ chức kinh tế sở hữu nguồn vốn tiết kiệm thặng dư.
- **Đặc trưng hành vi & Kỳ vọng:**
  - Có tâm lý ngại rủi ro (Risk-averse), đòi hỏi cam kết hoàn trả 100% vốn gốc kèm lãi suất sinh lời.
  - Ưu tiên tính thanh khoản cao (kỳ hạn gửi ngắn, khả năng rút tiền tức thời khi có nhu cầu chi tiêu đột xuất).
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
  - Vay vốn tín dụng từ NHTM: Vốn lưu động ngắn hạn, Vay trung dài hạn dự án, Cho vay hợp vốn (Syndicated Loans) cho các đại dự án nghìn tỷ.
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
  - TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP nhận tiền gửi cá nhân từ công chúng.
  - Dòng tiền huy động không phải là "nợ tiền gửi cam kết hoàn trả 100% gốc", mà là phí dịch vụ, tiền mua chứng chỉ quỹ, trái phiếu hoặc vốn góp ủy thác đầu tư. Khách hàng tự chịu rủi ro theo thị trường.
- **Cấu trúc phân loại theo phân ngành:**
  - *Công ty chứng khoán (CTCK):* Hoạt động môi giới, cho vay ký quỹ (Margin), tự doanh, tư vấn tài chính doanh nghiệp M&A, bảo lãnh phát hành chứng khoán (SSI, TCBS, VPS, Vietcap).
  - *Công ty bảo hiểm (Nhân thọ & Phi nhân thọ):* Thu phí bảo hiểm định kỳ (Premiums); thực hiện tái đầu tư an toàn dài hạn vào Trái phiếu Chính phủ, tiền gửi ngân hàng kỳ hạn dài và cổ phiếu blue-chip (Bảo Việt, Prudential, Manulife, MIC).
  - *Quỹ đầu tư & Công ty Quản lý quỹ:* Phát hành chứng chỉ quỹ (CCQ) huy động vốn từ nhà đầu tư cá nhân/tổ chức; quản lý danh mục đa tài sản (Dragon Capital, VinaCapital, SSIAM, Techcom Capital).
  - *Công ty tài chính (CTTC) & Cho thuê tài chính:* Thuộc nhóm TCTD phi ngân hàng (do NHNN cấp phép và quản lý); huy động vốn từ vốn CSH, phát hành trái phiếu, vay liên ngân hàng, và tiền gửi có kỳ hạn từ tổ chức; cấp tín dụng tiêu dùng tín chấp, cho thuê tài chính máy móc thiết bị (FE Credit, HD SAISON, VietinBank Leasing).
  - *Tổ chức cầm đồ & Cho vay thay thế:* Cho vay cầm cố ngắn hạn giải ngân nhanh (F88, Vietmoney).
- **Mô hình FHC & Chiến lược Bán chéo (Cross-selling):**
  - Tích hợp "Ngân hàng - Chứng khoán - Bảo hiểm" phục vụ trọn vòng đời tài chính của khách hàng (Bancassurance).
  - *Yêu cầu Bức tường lửa (Firewalls):* Các công ty con phải hoàn toàn độc lập về pháp lý, vốn và hạch toán; hoạt động như các vách ngăn chống chìm của tàu Titanic nhằm cô lập rủi ro thua lỗ từ mảng đầu tư, bảo vệ an toàn cho Ngân hàng mẹ.

### [E8] Định chế công nghệ & Nền tảng số (Fintech & Super-Apps)
- **Bản chất & Vị thế:** Các công ty công nghệ cung cấp giải pháp tài chính số hóa dựa trên nền tảng (Platform), Open API, Trí tuệ nhân tạo (AI) và Phân tích dữ liệu lớn (Big Data).
- **Chiến lược Siêu ứng dụng (Super-App):**
  - Mở rộng hệ sinh thái đa dịch vụ (gọi xe, giao đồ ăn, thương mại điện tử) để thu thập dữ liệu hành vi khổng lồ, sau đó tích hợp dịch vụ tài chính (Grab, Shopee) nhằm giữ chân khách hàng trọn đời.
- **Phân định bản chất sản phẩm trên Ví điện tử (Ví dụ: MoMo, ZaloPay):**
  - *Tiết kiệm Online:* Ví điện tử chỉ là kênh phân phối kỹ thuật (Platform); dòng tiền thực tế được chuyển về gửi tại NHTM đối tác (như MB, Bản Việt) và ĐƯỢC hưởng bảo hiểm tiền gửi.
  - *Túi Thần Tài / Đầu tư:* Bản chất là Hợp đồng hợp tác kinh doanh với tổ chức quản lý đầu tư bên thứ ba; khách hàng chấp nhận rủi ro đầu tư và KHÔNG ĐƯỢC hưởng bảo hiểm tiền gửi.
  - *Mua trước trả sau (BNPL: SPayLater):* Bản chất là một khoản vay tín dụng tiêu dùng tín chấp được cấp bởi ngân hàng/CTTC đối tác thông qua nền tảng số.
- **Rủi ro trồi hiện & Thách thức vĩ mô:**
  - Gặm nhấm thị phần thanh toán và làm xói mòn nguồn thu phí truyền thống của ngân hàng.
  - Đẩy tăng áp lực chi phí đầu tư CNTT và tỷ lệ CIR.
  - Nguy cơ Rút tiền Mili-giây (Millisecond Bank Run) qua mạng lưới API Bots kết nối dữ liệu mạng xã hội, có khả năng kích hoạt tháo chạy hàng nghìn tỷ trong vài giây, vô hiệu hóa đệm an toàn LCR 30 ngày của Basel III.

---

## 4. Relationship Registry

```text
[E1] NHNN ──(Phối hợp CSTK & CSTT)── [E2] MoF
[E1] NHNN ──(CSTT, Dự trữ BB, Basel CAR/LDR, Room tín dụng)──► [E3] NHTM
[E3] NHTM ──(Ký gửi Dự trữ BB, Báo cáo an toàn vĩ mô)──► [E1] NHNN
[E2] MoF ──(Phát hành TPCP cung ứng HQLA)──► [E3] NHTM
[E2] MoF ──(Quản lý Nhà nước TTCK & Bảo hiểm qua UBCKNN/QLGSBH)──► [E7] Định chế phi TG
[E4] Bên thừa vốn ──(Gửi tiền tiết kiệm & CASA)──► [E3] NHTM
[E3] NHTM ──(Chi trả lãi suất tiền gửi, Thanh toán yêu cầu)──► [E4] Bên thừa vốn
[E3] NHTM ──(Cấp tín dụng ngắn/trung/dài hạn, Biến đổi kỳ hạn)──► [E5] Bên thiếu vốn
[E5] Bên thiếu vốn ──(Hoàn trả nợ gốc & Lãi vay, Rủi ro nợ xấu NPL)──► [E3] NHTM
[E4] Bên thừa vốn ──(Mua CCQ, Cổ phiếu, Trái phiếu DN, Phí bảo hiểm)──► [E7] Định chế phi TG
[E5] Bên thiếu vốn ──(Thu xếp vốn M&A, Bảo lãnh Trái phiếu & IPO)──► [E7] Định chế phi TG
[E3] NHTM ──(Mô hình FHC, Đầu tư công ty con, Bán chéo Bancassurance)──► [E7] Định chế phi TG
[E1] NHNN ──(Dựng Bức tường lửa Firewalls ngăn lây lan rủi ro)──► [E7] Định chế phi TG
[E3] NHTM ──(Nộp phí Bảo hiểm tiền gửi định kỳ)──► [E6] Safety Net
[E6] Safety Net ──(Cam kết hạn mức chi trả 125tr triệt tiêu Bank Run)──► [E4] Bên thừa vốn
[E1] NHNN ──(Cho vay đặc biệt LoLR Đ.192, 193 bơm thanh khoản khẩn cấp)──► [E6] Safety Net
[E8] Fintech ──(Hạ tầng thanh toán, Open API, Rủi ro rút tiền mili-giây)──► [E3] NHTM
[E8] Fintech ──(Trải nghiệm Super-App, Ví điện tử, Dịch vụ BNPL)──► [E4] Bên thừa vốn
```

### Bảng Diễn giải Quan hệ Chi tiết

| Chiều Quan hệ (Flow) | Loại Liên kết (Type) | Căn cứ Nội dung & Cơ chế Vận hành Thực tế |
| :--- | :--- | :--- |
| **[E1] ↔ [E2]** | Phối hợp Vĩ mô | Phối hợp Chính sách Tiền tệ (NHNN) và Chính sách Tài khóa (Bộ Tài chính) nhằm giữ vững ổn định kinh tế vĩ mô, kiểm soát lạm phát và ngăn chặn hiệu ứng chèn lấn tín dụng (Crowding-out). |
| **[E1] → [E3]** | Giám sát & Điều tiết | NHNN điều tiết cung ứng tiền tệ qua OMO, Tái cấp vốn, Dự trữ bắt buộc; thiết lập chuẩn mực Basel (CAR ≥ 8%, siết LDR 85%); áp trần sở hữu cổ phần theo Luật Các TCTD 2024 để ngăn ngừa sở hữu chéo. |
| **[E3] → [E1]** | Tuân thủ & Ký gửi | NHTM mở tài khoản và ký gửi dự trữ bắt buộc tại NHNN; thực hiện nghĩa vụ báo cáo thống kê định kỳ phục vụ giám sát an toàn vĩ mô và vi mô. |
| **[E2] → [E3]** | Cung ứng Tài sản HQLA | Kho bạc Nhà nước (Bộ Tài chính) phát hành Trái phiếu Chính phủ; NHTM đầu tư nắm giữ TPCP để hình thành tài sản thanh khoản chất lượng cao (HQLA) đáp ứng chuẩn LCR Basel III. |
| **[E2] → [E7]** | Quản lý Chuyên ngành | Bộ Tài chính quản lý trực tiếp thị trường chứng khoán (thông qua UBCKNN) và thị trường bảo hiểm (thông qua Cục Quản lý, Giám sát Bảo hiểm). |
| **[E4] → [E3]** | Dẫn vốn Tiền gửi | Người gửi tiền cung ứng thặng dư nhàn rỗi thông qua tài khoản thanh toán (CASA giá rẻ) và sổ tiết kiệm có kỳ hạn; chấp nhận lãi suất thấp để đổi lấy an toàn và thanh khoản. |
| **[E3] → [E4]** | Dịch vụ & Hoàn trả | NHTM có nghĩa vụ pháp lý hoàn trả 100% tiền gửi vô điều kiện khi đến hạn hoặc khi khách hàng yêu cầu rút tiền; chi trả lãi suất tiền gửi; cung cấp dịch vụ thanh toán 24/7. |
| **[E3] → [E5]** | Cấp tín dụng & ALM | NHTM cung cấp vốn vay ngắn hạn, trung dài hạn và cho vay hợp vốn (Syndicated Loans) cho nền kinh tế; thực hiện chức năng biến đổi kỳ hạn (Maturity Transformation) lên tới 20-25 năm. |
| **[E5] → [E3]** | Trả nợ & Rủi ro Tín dụng | Bên vay hoàn trả gốc và lãi theo khế ước; sự suy giảm hiệu quả sản xuất kinh doanh của bên vay phát sinh rủi ro nợ xấu (NPL), trực tiếp bào mòn vốn chủ sở hữu ngân hàng. |
| **[E4] → [E7]** | Đầu tư Thị trường Vốn | Cá nhân/tổ chức ủy thác vốn mua chứng chỉ quỹ, cổ phiếu, trái phiếu doanh nghiệp hoặc tham gia bảo hiểm nhân thọ; tự gánh chịu rủi ro thị trường theo biến động giá trị tài sản ròng (NAV). |
| **[E5] → [E7]** | Thu xếp Tài chính Doanh nghiệp | Doanh nghiệp sử dụng dịch vụ tư vấn M&A, bảo lãnh phát hành cổ phiếu IPO và trái phiếu doanh nghiệp thông qua Khối Ngân hàng Đầu tư (IB) của các Công ty Chứng khoán. |
| **[E3] → [E7]** | Cấu trúc Tập đoàn & Bán chéo | NHTM mẹ thành lập/sở hữu công ty con chuyên biệt trong cấu trúc BHC/FHC hoặc hợp tác độc quyền phân phối chéo sản phẩm bảo hiểm (Bancassurance) nhằm tối ưu hóa thu nhập ngoài lãi. |
| **[E1] → [E7]** | Thiết lập Bức tường lửa | NHNN yêu cầu thiết lập ranh giới "Bức tường lửa" (Firewalls) độc lập về vốn, nhân sự và hạch toán; ngăn chặn rủi ro thua lỗ từ mảng đầu tư chứng khoán lây lan sang làm sụp đổ NHTM mẹ. |
| **[E3] → [E6]** | Nộp phí Bảo hiểm | NHTM nhận tiền gửi có nghĩa vụ trích nộp phí bảo hiểm tiền gửi định kỳ theo quy định của Luật Bảo hiểm Tiền gửi. |
| **[E6] → [E4]** | Bảo vệ Niềm tin Công chúng | Cơ quan Bảo hiểm Tiền gửi cam kết hạn mức chi trả bảo hiểm (125 triệu đồng) khi ngân hàng mất khả năng thanh toán, triệt tiêu động cơ rút tiền hoảng loạn hàng loạt (Bank Run). |
| **[E1] → [E6]** | Cứu trợ Thanh khoản Khẩn cấp | NHNN thực thi vai trò Người cho vay cuối cùng (LoLR) qua nghiệp vụ tái cấp vốn đặc biệt (Điều 192, 193 Luật Các TCTD 2024), hỗ trợ thanh khoản tối thượng cho Safety Net bảo vệ hệ thống. |
| **[E8] → [E3]** | Hạ tầng số & Nguy cơ Rút tiền | Fintech cung cấp giải pháp Open API kết nối thanh toán và phân phối sản phẩm số cho NHTM; đồng thời mạng lưới API Bots tự động hóa tạo nguy cơ rút tiền mili-giây đe dọa thanh khoản. |
| **[E8] → [E4]** | Trải nghiệm Siêu ứng dụng | Fintech cung cấp giao diện Super-App tiện ích, tích hợp thanh toán, chấm điểm tín dụng AI và giải pháp Mua trước trả sau (BNPL) cho người dùng cá nhân. |

---

## 5. Chapter Coverage

| Mã Chương | Tên Chương & Trọng tâm Học phần | Danh mục Entity Bao phủ | Mức độ Đào sâu & Vai trò trong Toàn bộ Học phần |
| :---: | :--- | :--- | :--- |
| **CH01** | **Mô hình hoạt động Kinh doanh ngân hàng & Các định chế tài chính** | `[E1]`, `[E2]`, `[E3]`, `[E4]`, `[E5]`, `[E6]`, `[E7]`, `[E8]` | **Chương Nền tảng Vĩ mô & Toàn cảnh Hệ thống (Baseline Macro System Map):** Thiết lập cấu trúc tổng thể 8 Entity; phân định rạch ròi Nhận tiền gửi vs Phi tiền gửi; cơ chế biến đổi kỳ hạn ALM; cấu trúc BHC/FHC; 6 mô hình kinh doanh ngân hàng; mạng lưới an toàn và dịch chuyển tư duy chiến lược sau khủng hoảng. |
| **CH02a** | **Các hoạt động kinh doanh chủ yếu của Ngân hàng thương mại** | `[E3]` *(Đào sâu)*, liên kết `[E4]`, `[E5]`, `[E1]` | **Đào sâu Nghiệp vụ Cốt lõi của [E3] NHTM:** Đi sâu vào 3 hoạt động trụ cột: Hoạt động Huy động vốn (Liabilities), Hoạt động Cấp tín dụng & Đầu tư (Assets), Hoạt động Dịch vụ thanh toán và Quản lý Bảng cân đối ALM chi tiết. |
| **CH02b** | **Các hoạt động kinh doanh chủ yếu của Ngân hàng đầu tư** | `[E7]` *(Đào sâu nhánh IB/CTCK)*, liên kết `[E5]`, `[E3]`, `[E2]` | **Đào sâu Phân khúc Phi tiền gửi [E7] (Trọng tâm Investment Banking):** Cấu trúc nghiệp vụ Bảo lãnh phát hành chứng khoán (Underwriting), Tư vấn M&A, Thu xếp vốn doanh nghiệp, Tự doanh, Môi giới và Quản lý tài sản. |
| **CH03** | **Quản trị hoạt động kinh doanh ngân hàng** | `[E3]` *(Đào sâu Quản trị)*, liên kết `[E1]`, `[E6]` | **Đào sâu Năng lực Quản trị Chiến lược & Rủi ro tại [E3]:** Quản trị An toàn vốn Basel II/III (ICAAP), Quản trị Thanh khoản và Rủi ro thanh khoản (ILAAP), Quản trị Rủi ro Tín dụng, Rủi ro Thị trường, Rủi ro Hoạt động và tối ưu hóa hiệu quả kinh doanh qua chu kỳ. |

---
*Ghi chú duy trì tính liên tục (Continuity Note):* File này là bộ nhớ dùng chung. Khi thực hiện các chương kế tiếp (`CH02a`, `CH02b`, `CH03`...), tuyệt đối không thay đổi mã số của các Entity đã được định danh (`E1` đến `E8`). Các chương sau chỉ bổ sung kiến thức chuyên sâu vào Entity tương ứng và cập nhật bảng Chapter Coverage.
