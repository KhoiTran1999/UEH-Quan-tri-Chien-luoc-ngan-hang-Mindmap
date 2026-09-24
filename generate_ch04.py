import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def create_ch04_xml():
    # Root element
    mxfile = ET.Element('mxfile', host='Electron')
    diagram = ET.SubElement(mxfile, 'diagram', name='Quản trị và Chiến lược Ngân hàng - Chương 4', id='Chapter4-BankStrategyPlanning-Mindmap')
    mxGraphModel = ET.SubElement(diagram, 'mxGraphModel',
                                dx='1628', dy='-1422', grid='0', gridSize='10',
                                guides='1', tooltips='1', connect='1', arrows='1',
                                fold='1', page='0', pageScale='1', pageWidth='850',
                                pageHeight='1100', math='0', shadow='0')
    root = ET.SubElement(mxGraphModel, 'root')

    # Base cells
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')

    def add_vertex(cell_id, value, style, x, y, width, height, parent='1'):
        cell = ET.SubElement(root, 'mxCell', id=cell_id, parent=parent, style=style, value=value, vertex='1')
        ET.SubElement(cell, 'mxGeometry', x=str(x), y=str(y), width=str(width), height=str(height), **{'as': 'geometry'})
        return cell

    def add_edge(edge_id, source, target, style, value='', parent='1', points=None, exit_xy=None, entry_xy=None):
        edge_style = style
        if exit_xy:
            edge_style += f"exitX={exit_xy[0]};exitY={exit_xy[1]};"
        if entry_xy:
            edge_style += f"entryX={entry_xy[0]};entryY={entry_xy[1]};"

        edge = ET.SubElement(root, 'mxCell', id=edge_id, parent=parent, style=edge_style, value=value, edge='1', source=source, target=target)
        geom = ET.SubElement(edge, 'mxGeometry', relative='1', **{'as': 'geometry'})
        if points:
            arr = ET.SubElement(geom, 'Array', **{'as': 'points'})
            for pt in points:
                ET.SubElement(arr, 'mxPoint', x=str(pt[0]), y=str(pt[1]))
        return edge

    # Title Banner
    add_vertex('TITLE_BANNER', '',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#1e293b;strokeColor=#0f172a;strokeWidth=2;fontColor=#ffffff;align=center;verticalAlign=middle;shadow=1;fontFamily=Helvetica;',
               1600, 3215, 2350, 95)

    add_vertex('TITLE_TEXT',
               'CHƯƠNG 4: HOẠCH ĐỊNH CHIẾN LƯỢC KINH DOANH NGÂN HÀNG<br/><span style="font-size: 13px; font-weight: normal; opacity: 0.85; color: #94a3b8;">Entity-based Hierarchical Mindmap | Đào sâu Chiến lược [E3] NHTM | Quy trình 11 Bước | Ma trận 3x3 Danh mục Thị trường &amp; Kiểm tra Chiến lược</span>',
               'text;html=1;whiteSpace=wrap;fillColor=none;strokeColor=none;align=center;verticalAlign=middle;fontFamily=Helvetica;fontColor=#ffffff;fontSize=24;fontStyle=1;',
               1620, 3225, 2310, 75)

    # Core Entity Root Node
    add_vertex('E3_ROOT',
               '🏛️ [E3] TRỤC CỐT LÕI: HOẠCH ĐỊNH CHIẾN LƯỢC KINH DOANH NGÂN HÀNG THƯƠNG MẠI<br/><span style="opacity: 0.9; font-size: 11px; font-weight: normal;">Định vị Tương lai | Quy trình Hoạch định 11 Bước | Ma trận Danh mục Thị trường (GE/McKinsey) &amp; Kiểm soát Chiến lược</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#0D47A1;strokeColor=#1565C0;fontColor=#ffffff;fontStyle=1;fontSize=14;shadow=1;fontFamily=Helvetica;',
               2480, 3365, 620, 65)

    # External Entities - Left Side
    add_vertex('EXT_E1_NHNN',
               '🏛️ [E1] NGÂN HÀNG TRUNG ƯƠNG (NHNN)<br/><span style="opacity: 0.85; font-size: 10px; font-weight: normal;">Định hướng CSTT vĩ mô, khống chế trần Room tín dụng,<br/>ban hành chuẩn an toàn vốn &amp; định hướng ngành ưu tiên; NHTM phải tuân thủ</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#263238;strokeColor=#37474F;fontColor=#ffffff;fontStyle=1;fontSize=11;shadow=1;fontFamily=Helvetica;align=center;',
               960, 3520, 360, 90)

    add_vertex('EXT_E8_FINTECH',
               '📱 [E8] CÔNG NGHỆ TÀI CHÍNH &amp; NỀN TẢNG SỐ (FINTECH &amp; AI)<br/><span style="opacity: 0.85; font-size: 10px; font-weight: normal;">Yếu tố công nghệ vĩ mô, Big Data, Open Banking, AI phân tích hành vi;<br/>vừa là đối thủ cạnh tranh loại bỏ trung gian, vừa là đối tác liên kết số</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#880E4F;strokeColor=#AD1457;fontColor=#ffffff;fontStyle=1;fontSize=11;shadow=1;fontFamily=Helvetica;align=center;',
               960, 3730, 360, 95)

    # External Entities - Right Side
    add_vertex('EXT_E4_SURPLUS',
               '💰 [E4] BÊN THỪA VỐN (KHÁCH HÀNG CÁ NHÂN - RETAIL)<br/><span style="opacity: 0.85; font-size: 10px; font-weight: normal;">Phân khúc Khách hàng Ưu tiên (Priority/VIP) vs Phổ thông (Mass);<br/>cung cấp tiền gửi CASA giá rẻ và tiêu dùng sản phẩm ngân hàng số</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#1B5E20;strokeColor=#2E7D32;fontColor=#ffffff;fontStyle=1;fontSize=11;shadow=1;fontFamily=Helvetica;align=center;',
               3690, 3520, 360, 90)

    add_vertex('EXT_E5_DEFICIT',
               '🏭 [E5] BÊN THIẾU VỐN (KHÁCH HÀNG DOANH NGHIỆP - CORPORATE)<br/><span style="opacity: 0.85; font-size: 10px; font-weight: normal;">Phân khúc Doanh nghiệp lớn (Account Plan may đo) vs SME (chuẩn hóa);<br/>hấp thụ tín dụng, tài trợ thương mại và dịch vụ thanh toán thương mại</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#BF360C;strokeColor=#E65100;fontColor=#ffffff;fontStyle=1;fontSize=11;shadow=1;fontFamily=Helvetica;align=center;',
               3690, 3710, 360, 90)

    add_vertex('EXT_E7_NONDEP',
               '🏢 [E7] ĐỊNH CHẾ PHI TIỀN GỬI (NHĐT, CTCK &amp; BẢO HIỂM)<br/><span style="opacity: 0.85; font-size: 10px; font-weight: normal;">Đối tác phân phối sản phẩm thị trường vốn, Bancassurance;<br/>hoàn thiện mô hình Universal Banking trong chiến lược đa dạng hóa thu nhập</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#4A148C;strokeColor=#6A1B9A;fontColor=#ffffff;fontStyle=1;fontSize=11;shadow=1;fontFamily=Helvetica;align=center;',
               3690, 3900, 360, 90)

    # ========================== GROUP 1 ==========================
    # Column 1: G1 (x=1400, w=380)
    add_vertex('G1_HEADER',
               '1.0 🧭 TỔNG QUAN HOẠCH ĐỊNH &amp; THỂ CHẾ VĨ MÔ<br/><span style="font-size:10px;font-weight:normal;opacity:0.9;">Khái niệm, 3 Câu hỏi Xương sống &amp; Mối liên hệ NHTM - NHTW</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=10;fontColor=#ffffff;fontStyle=1;fontSize=12;shadow=1;fontFamily=Helvetica;align=center;fillColor=#1A237E;strokeColor=#283593;',
               1400, 3490, 380, 55)

    add_vertex('G1_CARD_1',
               '1.1 🎯 KHÁI NIỆM CHIẾN LƯỢC &amp; 3 CÂU HỎI "XƯƠNG SỐNG":<br/>'
               '• <b>Chiến lược kinh doanh ngân hàng:</b> Chương trình hành động dài hạn nhằm tối ưu hóa các mục tiêu cốt lõi: tối đa hóa lợi nhuận, kiểm soát rủi ro, tăng trưởng thị phần và nâng cao giá trị ngân hàng<br/>'
               '• <b>Hoạch định chiến lược:</b> Quá trình thiết lập mục tiêu, xây dựng giải pháp và phân bổ nguồn lực; đòi hỏi sự phối hợp đa chiều và cập nhật liên tục<br/>'
               '• <b>Ba câu hỏi chiến lược nền tảng:</b><br/>'
               '  1. <i>Ngân hàng đang ở đâu?</i> ➔ Đánh giá vị thế hiện tại qua phân tích SWOT<br/>'
               '  2. <i>Ngân hàng muốn đến đâu?</i> ➔ Xác định tầm nhìn, sứ mệnh và mục tiêu<br/>'
               '  3. <i>Đạt đến đó bằng cách nào?</i> ➔ Lập chương trình hành động và điều phối nguồn lực',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#EDE7F6;strokeColor=#5C6BC0;fontColor=#1A237E;',
               1400, 3575, 380, 130)

    add_vertex('G1_CARD_2',
               '1.2 🏆 BỐN TÁC DỤNG CỐT LÕI CỦA HOẠCH ĐỊNH CHIẾN LƯỢC:<br/>'
               '• <b>Cầu nối hình thành &amp; thực thi:</b> Chuyển hóa tầm nhìn chiến lược trên giấy thành kết quả kinh doanh mong muốn; tối ưu hóa phân bổ nguồn lực thực tế<br/>'
               '• <b>Nhận dạng cơ hội &amp; Thích nghi môi trường:</b> Chủ động đón đầu biến động lãi suất, tỷ giá, công nghệ số và sự thay đổi hành vi tiêu dùng tài chính<br/>'
               '• <b>Định hướng hoạt động thống nhất:</b> Tạo sự tập trung toàn hệ thống từ Hội đồng quản trị, Ban điều hành đến toàn bộ mạng lưới chi nhánh/phòng giao dịch<br/>'
               '• <b>Công cụ kiểm tra &amp; Đánh giá quản trị:</b> Cung cấp hệ thống mục tiêu chuẩn mực làm thước đo đánh giá hiệu năng điều hành của từng cấp quản trị',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#EDE7F6;strokeColor=#5C6BC0;fontColor=#1A237E;',
               1400, 3720, 380, 135)

    add_vertex('G1_CARD_3',
               '1.3 ⚖️ PHÂN LOẠI HOẠCH ĐỊNH: CHIẾN LƯỢC VS. TÁC NGHIỆP:<br/>'
               '• <b>Hoạch định Chiến lược (Strategic Planning):</b> Tầm nhìn dài hạn (3–5 năm hoặc hơn); phạm vi toàn bộ hệ thống ngân hàng; do HĐQT và Ban TGĐ đảm trách; tập trung vào sứ mệnh, mục tiêu dài hạn, thị trường mục tiêu và mô hình kinh doanh<br/>'
               '• <b>Hoạch định Tác nghiệp (Operational Planning):</b> Tầm nhìn ngắn hạn (năm, quý, tháng); phạm vi từng phòng ban/chi nhánh; do cấp cơ sở thực thi; cụ thể hóa thành kế hoạch huy động vốn, cấp tín dụng, ngân sách chi phí và chỉ tiêu KPI cụ thể<br/>'
               '• <b>Mối quan hệ hữu cơ:</b> Hoạch định chiến lược là "kim chỉ nam" dẫn dắt; hoạch định tác nghiệp là "phương tiện" thực thi; tác nghiệp sai lệch sẽ phá vỡ chiến lược',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#EDE7F6;strokeColor=#5C6BC0;fontColor=#1A237E;',
               1400, 3870, 380, 130)

    add_vertex('G1_CARD_4',
               '1.4 🏛️ MỐI LIÊN HỆ GIỮA CHIẾN LƯỢC NHTM [E3] VÀ CHIẾN LƯỢC NHTW [E1]:<br/>'
               '• <b>Đặc điểm Chiến lược NHTW [E1]:</b> Mang tính vĩ mo, định hướng toàn bộ nền kinh tế; mục tiêu kiểm soát lạm phát, ổn định giá trị đồng tiền và an toàn hệ thống (phi lợi nhuận)<br/>'
               '• <b>Chiến lược NHTM [E3] - Bộ phận thực thi vĩ mô:</b> NHTM là một mắt xích trong hệ thống; chiến lược kinh doanh của NHTM không được đi ngược lại chính sách tiền tệ và định hướng tín dụng của NHTW<br/>'
               '• <b>Minh họa điều hành tín dụng:</b> Khi NHNN thắt chặt tăng trưởng tín dụng (áp trần Room tín dụng) hoặc định hướng vốn vào sản xuất kinh doanh/nông nghiệp, NHTM bắt buộc phải tái cấu trúc danh mục cho vay để thích ứng',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#EDE7F6;strokeColor=#5C6BC0;fontColor=#1A237E;',
               1400, 4015, 380, 135)

    # ========================== GROUP 2 ==========================
    # Column 2: G2 (x=1840, w=390)
    add_vertex('G2_HEADER',
               '2.0 🧱 ĐIỀU KIỆN CẦN &amp; PHÂN CẤP HOẠCH ĐỊNH<br/><span style="font-size:10px;font-weight:normal;opacity:0.9;">Yêu cầu cốt lõi, 6 Cơ sở Nền tảng &amp; 3 Cấp Quản trị</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=10;fontColor=#ffffff;fontStyle=1;fontSize=12;shadow=1;fontFamily=Helvetica;align=center;fillColor=#880E4F;strokeColor=#AD1457;',
               1840, 3490, 390, 55)

    add_vertex('G2_CARD_1',
               '2.1 🎯 HAI YÊU CẦU CỐT LÕI ĐỐI VỚI CHIẾN LƯỢC KINH DOANH:<br/>'
               '• <b>Sự tham gia đa chiều và liên cấp:</b> Chiến lược không thể là "sản phẩm tháp ngà" độc đoán từ cấp cao mà đòi hỏi sự thấu hiểu, đồng thuận và đóng góp từ cấp cơ sở; đảm bảo tính khả thi thực tế<br/>'
               '• <b>Tính linh hoạt và thích ứng liên tục:</b> Cân bằng giữa kiên định mục tiêu dài hạn và linh hoạt điều chỉnh giải pháp ngắn hạn trước các cú sốc vĩ mô (lãi suất, lạm phát, dịch bệnh, xung đột địa chính trị)<br/>'
               '• <b>Công thức thành công:</b> <i>Chiến lược hiệu quả = Sự thấu hiểu &amp; Đồng thuận mọi cấp + Tính linh hoạt điều chỉnh trước biến động thị trường</i>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#FCE4EC;strokeColor=#C2185B;fontColor=#880E4F;',
               1840, 3575, 390, 130)

    add_vertex('G2_CARD_2',
               '2.2 🏛️ SÁU CƠ SỞ NỀN TẢNG ĐỂ XÂY DỰNG CHIẾN LƯỢC:<br/>'
               '• <b>1. Đội ngũ nhân viên (Yếu tố con người - Quan trọng nhất):</b> Trình độ chuyên môn, đạo đức nghề nghiệp, văn hóa dịch vụ; nhân sự quyết định thành bại<br/>'
               '• <b>2. Nguồn vốn ngân hàng:</b> Quy mô vốn điều lệ, vốn tự có (CAR) và năng lực huy động; vốn là "bệ phóng" giới hạn quy mô mở rộng tài sản sinh lời<br/>'
               '• <b>3. Cơ sở vật chất &amp; Công nghệ:</b> Mạng lưới chi nhánh, Core Banking, hạ tầng số, bảo mật dữ liệu; chìa khóa giảm chi phí vận hành (CIR)<br/>'
               '• <b>4. Tài sản vô hình (Uy tín &amp; Thương hiệu):</b> Niềm tin của khách hàng là tài sản quý giá nhất, đặc biệt trong việc duy trì nguồn tiền gửi CASA giá rẻ<br/>'
               '• <b>5. Vị thế hiện tại &amp; Mục tiêu tương lai:</b> Đánh giá đúng năng lực thực chất<br/>'
               '• <b>6. Môi trường kinh doanh:</b> Phân tích nội bộ (SWOT) &amp; môi trường vĩ mô',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#FCE4EC;strokeColor=#C2185B;fontColor=#880E4F;',
               1840, 3720, 390, 140)

    add_vertex('G2_CARD_3',
               '2.3 👥 PHÂN CẤP 3 TẦNG HOẠCH ĐỊNH TRONG NGÂN HÀNG THƯƠNG MẠI:<br/>'
               '• <b>Quản trị viên Cấp cao (HĐQT):</b> Quyền lực quản trị cao nhất; kiến tạo tầm nhìn, đường lối dài hạn (3–5 năm); phân bổ nguồn lực lớn; cấp ngân sách; bổ nhiệm Tổng giám đốc; xác định mô hình (Bán lẻ, Bán buôn hay Đa năng)<br/>'
               '• <b>Quản trị viên Cấp trung (Ban điều hành - Ban TGĐ):</b> Cầu nối chiến lược; chuyển hóa tầm nhìn HĐQT thành chương trình hành động cụ thể; phân bổ chỉ tiêu cho các khối/chi nhánh; giám sát và điều chỉnh tác nghiệp<br/>'
               '• <b>Quản trị viên Cấp cơ sở (Giám đốc Chi nhánh/PGD):</b> Lực lượng trực tiếp thực thi; trực tiếp tiếp xúc khách hàng [E4], [E5]; triển khai bán hàng, quản trị rủi ro tại chỗ; thu thập dữ liệu thị trường phản hồi lên cấp trên<br/>'
               '• <b>Ẩn dụ quản trị:</b> <i>HĐQT vẽ bản đồ &amp; cấp kinh phí — Ban điều hành vạch lộ trình &amp; điều phối — Cấp cơ sở trực tiếp lái xe về đích</i>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#FCE4EC;strokeColor=#C2185B;fontColor=#880E4F;',
               1840, 3875, 390, 135)

    add_vertex('G2_CARD_4',
               '2.4 🔄 BA HÌNH THỨC QUAN HỆ VẬN HÀNH GIỮA CÁC CẤP HOẠCH ĐỊNH:<br/>'
               '• <b>Quan hệ chuyển giao nhiệm vụ &amp; quyền hạn (Top-Down):</b> HĐQT giao mục tiêu và ngân sách cho Ban điều hành; Ban điều hành phân bổ chỉ tiêu KPI và quyền hạn tác nghiệp xuống các chi nhánh/phòng ban<br/>'
               '• <b>Quan hệ phê duyệt và kiểm soát (Quản trị &amp; Giám sát):</b> Cấp trên thẩm định, phê duyệt kế hoạch triển khai của cấp dưới; kiểm soát việc tuân thủ hạn mức rủi ro, chính sách tín dụng và tiến độ thực hiện<br/>'
               '• <b>Quan hệ báo cáo &amp; Cho ý kiến điều chỉnh (Bottom-Up):</b> Cấp cơ sở gửi báo cáo định kỳ về kết quả thực tế, những vướng mắc phát sinh từ thị trường để cấp trên kịp thời điều chỉnh kế hoạch kinh doanh<br/>'
               '• <b>Chu trình khép kín:</b> <i>Giao nhiệm vụ ➔ Phê duyệt &amp; Kiểm soát ➔ Báo cáo &amp; Phản hồi</i>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#FCE4EC;strokeColor=#C2185B;fontColor=#880E4F;',
               1840, 4025, 390, 135)

    # ========================== GROUP 3 ==========================
    # Column 3: G3 (x=2290, w=400)
    add_vertex('G3_HEADER',
               '3.0 🎯 MỤC TIÊU &amp; PHÂN KHÚC THỊ TRƯỜNG<br/><span style="font-size:10px;font-weight:normal;opacity:0.9;">Quy trình Bước 1–5: Sứ mệnh, Thị trường mục tiêu, Phân khúc KH &amp; Cấu trúc ngành</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=10;fontColor=#ffffff;fontStyle=1;fontSize=12;shadow=1;fontFamily=Helvetica;align=center;fillColor=#004D40;strokeColor=#00695C;',
               2290, 3490, 400, 55)

    add_vertex('G3_CARD_1',
               '3.1 🧭 THIẾT LẬP MỤC TIÊU, TUYÊN BỐ SỨ MỆNH &amp; CHÍNH SÁCH:<br/>'
               '• <b>Nguyên tắc thiết lập mục tiêu (Objectives):</b> Rõ ràng, đo lường được, có thời hạn; bao gồm mục tiêu tài chính (ROE, ROA, NIM, CIR, NPL) và phi tài chính (thị phần, sự hài lòng của khách hàng, chuyển đổi số)<br/>'
               '• <b>Tuyên bố Sứ mệnh (Mission Statement):</b> Xác định "sân chơi" của ngân hàng; tuyên bố lý do tồn tại, giá trị cốt lõi mang lại cho khách hàng, cổ đông và cộng đồng xã hội<br/>'
               '• <b>Hoạch định Chính sách (Policies):</b> Là "quy tắc của trò chơi"; các chuẩn mực định hướng hành vi (chính sách tín dụng, khẩu vị rủi ro, chính sách lãi suất)<br/>'
               '• <b>Phân tích tình hình (Situation Analysis):</b> Nhận diện rào cản nội tại cản trở việc đạt mục tiêu',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#E0F2F1;strokeColor=#26A69A;fontColor=#004D40;',
               2290, 3575, 400, 130)

    add_vertex('G3_CARD_2',
               '3.2 🌐 XÁC ĐỊNH THỊ TRƯỜNG MỤC TIÊU (SERVED MARKET) &amp; MA TRẬN NHU CẦU:<br/>'
               '• <b>Thách thức cốt lõi:</b> Không ngân hàng nào đủ nguồn lực phục vụ toàn bộ thị trường cào bằng; bắt buộc phải xác định chính xác "sân chơi thực tế"<br/>'
               '• <b>Ba yếu tố giao thoa cấu thành Thị trường mục tiêu:</b><br/>'
               '  1. <i>Nhóm khách hàng (Customer Groups):</i> Khách hàng là ai? (Doanh nghiệp lớn, SME, cá nhân, giới trẻ)<br/>'
               '  2. <i>Nhu cầu khách hàng (Customer Needs):</i> Cần giải pháp gì? (Tiết kiệm, vay mua nhà, thanh toán)<br/>'
               '  3. <i>Công nghệ / Sản phẩm (Technologies/Products):</i> Bằng phương tiện nào? (Ứng dụng số, thẻ, quầy)<br/>'
               '• <b>Ma trận Nhu cầu Khách hàng / Sản phẩm:</b> Công cụ định lượng đối chiếu dòng sản phẩm với từng nhu cầu để tìm khoảng trống thị trường tiềm năng',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#E0F2F1;strokeColor=#26A69A;fontColor=#004D40;',
               2290, 3720, 400, 130)

    add_vertex('G3_CARD_3',
               '3.3 🏭 PHÂN KHÚC THỊ TRƯỜNG KHÁCH HÀNG DOANH NGHIỆP [E5]:<br/>'
               '• <b>Tiếp cận theo Quy mô Doanh nghiệp:</b><br/>'
               '  + <i>Doanh nghiệp lớn (Large Corporates / Big Accounts):</i> Số lượng ít nhưng chiếm tỷ trọng dư nợ/doanh thu khổng lồ; đòi hỏi chiến lược riêng biệt (Account Plan may đo), giám đốc quan hệ khách hàng (RM) chuyên trách, giải pháp tài chính tổng thể (Syndicated Loan, bảo lãnh, FX)<br/>'
               '  + <i>Doanh nghiệp vừa và nhỏ (SME):</i> Số lượng áp đảo; phân khúc theo ngành nghề (sản xuất, thương mại, logistics), vùng địa lý; sản phẩm đóng gói chuẩn hóa, tinh gọn quy trình thẩm định<br/>'
               '• <b>Biến số phân khúc:</b> Quy mô doanh thu/tài sản, ngành nghề kinh doanh, vị trí địa lý, cơ cấu sở hữu (FDI, Nhà nước, Tư nhân), xếp hạng tín nhiệm nội bộ',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#E0F2F1;strokeColor=#26A69A;fontColor=#004D40;',
               2290, 3865, 400, 135)

    add_vertex('G3_CARD_4',
               '3.4 👤 PHÂN KHÚC KHÁCH HÀNG CÁ NHÂN [E4] &amp; ĐẶC ĐIỂM NGÀNH:<br/>'
               '• <b>Mô hình Phân khúc Bán lẻ Nhị phân:</b><br/>'
               '  + <i>Khách hàng Ưu tiên (Priority / VIP Customer):</i> Thu nhập cao, tài sản tích lũy lớn, số dư tiền gửi cao; ưu tiên bảo toàn vốn, dịch vụ chuyên biệt (Private Lounge, RM riêng), sản phẩm quản lý tài sản, thẻ kim loại cao cấp<br/>'
               '  + <i>Khách hàng Phổ thông (Standard / Mass):</i> Thu nhập trung bình; ưu tiên tiện lợi, phí thấp, giao dịch online 24/7; sản phẩm chuẩn hóa (eKYC, vay tiêu dùng, thẻ tín dụng)<br/>'
               '• <b>Ứng dụng Big Data &amp; AI [E8]:</b> Chấm điểm tín dụng tự động, cá nhân hóa trải nghiệm theo thời gian thực (Hyper-personalization)<br/>'
               '• <b>Đặc điểm Cấu trúc Ngành:</b> Đánh giá Đặc điểm Cầu (quy mô, mùa vụ, độ co giãn lãi suất) vs Đặc điểm Cung/Chi phí (rào cản gia nhập, Core Banking)',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#E0F2F1;strokeColor=#26A69A;fontColor=#004D40;',
               2290, 4015, 400, 145)

    # ========================== GROUP 4 ==========================
    # Column 4: G4 (x=2750, w=390)
    add_vertex('G4_HEADER',
               '4.0 🔍 NỘI TẠI, CẠNH TRANH &amp; MÔI TRƯỜNG<br/><span style="font-size:10px;font-weight:normal;opacity:0.9;">Quy trình Bước 6–9: Phân tích SWOT, Vị thế Cạnh tranh, Tính hấp dẫn &amp; PESTLE</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=10;fontColor=#ffffff;fontStyle=1;fontSize=12;shadow=1;fontFamily=Helvetica;align=center;fillColor=#006064;strokeColor=#00838F;',
               2750, 3490, 390, 55)

    add_vertex('G4_CARD_1',
               '4.1 🔎 ĐÁNH GIÁ VỊ TRÍ HIỆN TẠI QUA SWOT &amp; 4 CÂU HỎI RÀ SOÁT:<br/>'
               '• <b>Phân tích SWOT toàn diện:</b><br/>'
               '  + <i>Điểm mạnh (S) &amp; Điểm yếu (W):</i> Năng lực nội bộ (vốn tự có CAR, nguồn CASA giá rẻ, mạng lưới, hạ tầng Core Banking, chất lượng nhân sự, nợ xấu NPL)<br/>'
               '  + <i>Cơ hội (O) &amp; Thách thức (T):</i> Môi trường bên ngoài (tăng trưởng GDP, Luật Các TCTD 2024, chuyển dịch số, cạnh tranh gay gắt từ Fintech)<br/>'
               '• <b>Bốn Câu hỏi Rà soát Kế hoạch Chiến lược Hiện tại:</b><br/>'
               '  1. Kế hoạch hiện tại có giải quyết thỏa đáng tất cả vấn đề chiến lược đã xác định?<br/>'
               '  2. Kết quả phân tích có gợi ý bất kỳ thay đổi nào trong mục tiêu ngắn/dài hạn?<br/>'
               '  3. Cần dùng kênh truyền thông nào để nhân viên toàn hệ thống hiểu rõ chiến lược?<br/>'
               '  4. Nguồn nhân lực hiện tại có đủ năng lực và cam kết để thực thi thành công?',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#E0F7FA;strokeColor=#00ACC1;fontColor=#006064;',
               2750, 3575, 390, 135)

    add_vertex('G4_CARD_2',
               '4.2 🏆 BA TRỤ CỘT ĐO LƯỜNG SỨC MẠNH VỊ THẾ CẠNH TRANH (TRỤC X):<br/>'
               '• <b>Trụ cột 1 - Các Thước đo Vị thế Cạnh tranh:</b> Thị phần huy động và cho vay; Tốc độ tăng trưởng thị phần so với toàn ngành; Năng lực sinh lời (ROA, ROE, NIM); Hiệu quả chi phí (CIR); Mức độ nhận diện thương hiệu và lòng trung thành của khách hàng<br/>'
               '• <b>Trụ cột 2 - Đối chuẩn Top 3 Đối thủ Cạnh tranh Lớn nhất:</b> So sánh trực tiếp từng chỉ tiêu cụ thể với 3 ngân hàng đối thủ mạnh nhất trong cùng phân khúc để nhận diện lợi thế vượt trội hoặc lỗ hổng tụt hậu<br/>'
               '• <b>Trụ cột 3 - Năng lực Định vị Chiến lược:</b> Khả năng khác biệt hóa dịch vụ, độc quyền mạng lưới phân phối, hoặc ưu thế chi phí vốn rẻ (CASA) tạo thành hào lũy phòng thủ cạnh tranh (Competitive Moat)',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#E0F7FA;strokeColor=#00ACC1;fontColor=#006064;',
               2750, 3725, 390, 130)

    add_vertex('G4_CARD_3',
               '4.3 📈 ĐO LƯỜNG TÍNH HẤP DẪN CỦA THỊ TRƯỜNG: 10 THƯỚC ĐO CỐT LÕI (TRỤC Y):<br/>'
               '• <b>Hệ thống 10 Chỉ tiêu Định lượng &amp; Định tính:</b><br/>'
               '  1. Quy mô thị trường (Market Size) | 2. Tốc độ tăng trưởng quá khứ | 3. Tốc độ tăng trưởng dự kiến | 4. Số lượng đối thủ cạnh tranh | 5. Mức độ tập trung của đối thủ | 6. Khả năng sinh lời bình quân thị trường | 7. Mức độ khác biệt hóa sản phẩm | 8. Quyền lực thương lượng của khách hàng | 9. Xu hướng biên lợi nhuận | 10. Mức độ phù hợp với năng lực ngân hàng (Market Fit)<br/>'
               '• <b>Phương pháp Chấm điểm Tổng hợp:</b> Quy đổi 10 tiêu chí theo trọng số và thang điểm chuẩn (1-5 hoặc 1-10) để tính ra Điểm số Hấp dẫn Thị trường ➔ Thiết lập tọa độ trục Y trên Ma trận Danh mục Chiến lược',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#E0F7FA;strokeColor=#00ACC1;fontColor=#006064;',
               2750, 3870, 390, 140)

    add_vertex('G4_CARD_4',
               '4.4 🌐 PHÂN TÍCH 5 NHÓM YẾU TỐ MÔI TRƯỜNG VĨ MÔ &amp; ĐỘ NHẠY:<br/>'
               '• <b>Năm Nhóm Yếu tố Vĩ mô Cốt lõi (PESTLE):</b><br/>'
               '  + <i>Kinh tế (Economic):</i> Tăng trưởng GDP, lạm phát, lãi suất điều hành NHNN, tỷ giá<br/>'
               '  + <i>Nhân khẩu học (Demographic):</i> Tháp dân số trẻ, tốc độ đô thị hóa, tầng lớp trung lưu<br/>'
               '  + <i>Văn hóa - Xã hội (Socio-cultural):</i> Thói quen thanh toán không tiền mặt, niềm tin hệ thống<br/>'
               '  + <i>Công nghệ (Technological):</i> AI, Open Banking, sinh trắc học, cạnh tranh Fintech [E8]<br/>'
               '  + <i>Chính trị - Pháp lý (Political/Legal):</i> Luật Các TCTD 2024, Thông tư 14/2025/TT-NHNN<br/>'
               '• <b>Nguyên tắc Quản trị Môi trường:</b> Đưa ra Giả định rõ ràng (Clear Assumptions) và Phân tích Độ nhạy (Sensitivity Analysis) để xây dựng kịch bản ứng phó biến động',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#E0F7FA;strokeColor=#00ACC1;fontColor=#006064;',
               2750, 4025, 390, 135)

    # ========================== GROUP 5 ==========================
    # Column 5: G5 (x=3200, w=410)
    add_vertex('G5_HEADER',
               '5.0 📊 MA TRẬN CHIẾN LƯỢC &amp; KIỂM TRA<br/><span style="font-size:10px;font-weight:normal;opacity:0.9;">Quy trình Bước 10–11 &amp; Kiểm tra Chiến lược: 9 Ô Định hướng, Kế hoạch 4Ps &amp; Audit</span>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=10;fontColor=#ffffff;fontStyle=1;fontSize=12;shadow=1;fontFamily=Helvetica;align=center;fillColor=#BF360C;strokeColor=#D84315;',
               3200, 3490, 410, 55)

    add_vertex('G5_CARD_1',
               '5.1 🗺️ MA TRẬN DANH MỤC THỊ TRƯỜNG CHIẾN LƯỢC (MA TRẬN 3x3):<br/>'
               '• <b>Khung lý thuyết:</b> Mô hình GE/McKinsey được điều chỉnh cho quản trị NHTM; kết hợp đồng thời hai trục tọa độ chiến lược:<br/>'
               '  + <i>Trục hoành (X):</i> Vị thế Cạnh tranh của Ngân hàng (Mạnh - Trung bình - Yếu)<br/>'
               '  + <i>Trục tung (Y):</i> Tính Hấp dẫn của Thị trường Mục tiêu (Cao - Trung bình - Thấp)<br/>'
               '• <b>Phân bổ ma trận 9 ô:</b> Mỗi phân khúc kinh doanh (vay mua nhà, SME xuất khẩu, thẻ tín dụng, ngân hàng số) được định vị vào một ô cụ thể dựa trên tọa độ (X, Y)<br/>'
               '• <b>Nguyên lý Cân đối Dòng tiền:</b> Sử dụng lợi nhuận tích lũy (thu hoạch) từ các ô vị thế mạnh/thị trường bão hòa để tái đầu tư vào các ô thị trường hấp dẫn cao nhằm chiếm lĩnh vị thế dẫn đầu tương lai',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#FBE9E7;strokeColor=#FF7043;fontColor=#BF360C;',
               3200, 3575, 410, 130)

    add_vertex('G5_CARD_2',
               '5.2 🧭 CHI TIẾT ĐỊNH HƯỚNG CHIẾN LƯỢC TRONG 9 Ô MA TRẬN:<br/>'
               '• <b>Nhóm Thị trường Hấp dẫn CAO:</b><br/>'
               '  + <i>Ô 1 (Mạnh + Cao): Tăng trưởng / Cân bằng (Grow/Balanced)</i> ➔ Ưu tiên nguồn lực lớn nhất, duy trì vị thế dẫn đầu<br/>'
               '  + <i>Ô 2 (TB + Cao): Tăng trưởng / Thâm nhập (Grow/Penetrate)</i> ➔ Tăng đầu tư, đẩy mạnh thâm nhập nâng lên Mạnh<br/>'
               '  + <i>Ô 3 (Yếu + Cao): Thu hoạch / Tái cấu trúc (Harvest/Rebuild)</i> ➔ Tái cơ cấu toàn diện hoặc rút vốn cắt lỗ<br/>'
               '• <b>Nhóm Thị trường Hấp dẫn TRUNG BÌNH:</b><br/>'
               '  + <i>Ô 4 (Mạnh + TB): Phòng thủ / Đầu tư</i> ➔ Duy trì vị thế hiện có, dựng rào cản ngăn đối thủ<br/>'
               '  + <i>Ô 5 (TB + TB): Đầu tư có chọn lọc</i> ➔ Tập trung vào tiểu phân khúc biên lợi nhuận cao<br/>'
               '  + <i>Ô 6 (Yếu + TB): Rút lui êm đẹp / Tìm ngách</i> ➔ Thu hẹp có trật tự hoặc chuyển sang thị trường ngách<br/>'
               '• <b>Nhóm Thị trường Hấp dẫn THẤP:</b><br/>'
               '  + <i>Ô 7 (Mạnh + Thấp): Thu hoạch</i> | <i>Ô 8 (TB + Thấp): Rút lui êm đẹp</i> | <i>Ô 9 (Yếu + Thấp): Rút lui nhanh / Tấn công</i>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#FBE9E7;strokeColor=#FF7043;fontColor=#BF360C;',
               3200, 3720, 410, 145)

    add_vertex('G5_CARD_3',
               '5.3 📋 PHÁT TRIỂN KẾ HOẠCH PHÂN KHÚC &amp; VÒNG LẶP PHẢN HỒI:<br/>'
               '• <b>Nội dung điều chỉnh trong Kế hoạch Phân khúc:</b> Cụ thể hóa Marketing-mix (4Ps) sau khi định vị trên ma trận 9 ô:<br/>'
               '  + <i>Product:</i> Thiết kế, may đo hoặc đóng gói lại sản phẩm phù hợp phân khúc<br/>'
               '  + <i>Price:</i> Điều chỉnh chính sách lãi suất, phí dịch vụ cạnh tranh<br/>'
               '  + <i>Place:</i> Tối ưu kênh phân phối (phòng giao dịch vật lý vs App ngân hàng số)<br/>'
               '  + <i>Promotion:</i> Chiến dịch tiếp thị, quảng bá và bán chéo (Cross-selling)<br/>'
               '• <b>Vòng lặp Quy trình Hoạch định (Feedback Loop):</b> Quy trình 11 bước (4.3.1 – 4.3.11) là chu trình lặp tuần hoàn: <i>Mục tiêu ➔ Phân khúc ➔ SWOT &amp; Vị thế ➔ Ma trận 9 ô ➔ Kế hoạch hành động ➔ Phản hồi điều chỉnh</i>',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#FBE9E7;strokeColor=#FF7043;fontColor=#BF360C;',
               3200, 3880, 410, 130)

    add_vertex('G5_CARD_4',
               '5.4 🛡️ KIỂM TRA CHIẾN LƯỢC (STRATEGIC CONTROL &amp; AUDIT):<br/>'
               '• <b>Bản chất &amp; 3 Mục đích Cốt lõi:</b> Kiểm tra là thành tố khép kín chu trình quản trị; nhằm: (1) Đánh giá sự phù hợp với từng phân khúc; (2) Đo lường mức độ hoàn thành chỉ tiêu KPI; (3) Nhận diện sớm sai lệch và rủi ro trồi hiện<br/>'
               '• <b>Ba Chức năng Điều chỉnh:</b> Phát hiện mâu thuẫn/xung đột nội tại; Cơ sở đánh giá lại và cập nhật liên tục; Thiết lập dòng thông tin phản hồi (Feedback)<br/>'
               '• <b>Ba Nguyên tắc &amp; Tư tưởng Kiểm tra Chiến lược:</b><br/>'
               '  1. <i>Tư tưởng tích cực (Positive Philosophy):</i> Kiểm tra là cơ hội học hỏi, cải tiến năng lực<br/>'
               '  2. <i>Nguyên tắc "Không trừng phạt - Không áp đặt":</i> Khuyến khích sự trung thực, đối thoại cởi mở thay vì che giấu sai sót do sợ phạt<br/>'
               '  3. <i>Nguyên tắc linh hoạt &amp; Cải tiến liên tục:</i> Chiến lược luôn sẵn sàng điều chỉnh thích nghi',
               'rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=11;align=left;spacingLeft=8;spacingRight=8;fontFamily=Helvetica;fillColor=#FBE9E7;strokeColor=#FF7043;fontColor=#BF360C;',
               3200, 4025, 410, 140)

    # ========================== CONNECTORS ==========================
    # Edges from ROOT to Group Headers
    add_edge('EDGE_ROOT_G1', 'E3_ROOT', 'G1_HEADER',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;curved=0;strokeColor=#1A237E;',
             value='1.0 Tổng quan & Thể chế', exit_xy=(0.1, 1), entry_xy=(0.5, 0))

    add_edge('EDGE_ROOT_G2', 'E3_ROOT', 'G2_HEADER',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;curved=0;strokeColor=#880E4F;',
             value='2.0 Điều kiện cần & Phân cấp', exit_xy=(0.3, 1), entry_xy=(0.5, 0))

    add_edge('EDGE_ROOT_G3', 'E3_ROOT', 'G3_HEADER',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;curved=0;strokeColor=#004D40;',
             value='3.0 Mục tiêu & Phân khúc', exit_xy=(0.5, 1), entry_xy=(0.5, 0))

    add_edge('EDGE_ROOT_G4', 'E3_ROOT', 'G4_HEADER',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;curved=0;strokeColor=#006064;',
             value='4.0 Nội tại, Cạnh tranh & Môi trường', exit_xy=(0.7, 1), entry_xy=(0.5, 0))

    add_edge('EDGE_ROOT_G5', 'E3_ROOT', 'G5_HEADER',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;curved=0;strokeColor=#BF360C;',
             value='5.0 Ma trận 3x3 & Kiểm tra', exit_xy=(0.9, 1), entry_xy=(0.5, 0))

    # Internal group bus connectors (Header to Cards)
    # G1 Bus
    add_edge('EDGE_G1_C1', 'G1_HEADER', 'G1_CARD_1',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#1A237E;',
             value='')
    add_edge('EDGE_G1_C2', 'G1_HEADER', 'G1_CARD_2',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#1A237E;',
             value='', points=[(1400, 3560), (1370, 3560), (1370, 3787), (1400, 3787)])
    add_edge('EDGE_G1_C3', 'G1_HEADER', 'G1_CARD_3',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#1A237E;',
             value='', points=[(1400, 3560), (1370, 3560), (1370, 3935), (1400, 3935)])
    add_edge('EDGE_G1_C4', 'G1_HEADER', 'G1_CARD_4',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#1A237E;',
             value='', points=[(1400, 3560), (1370, 3560), (1370, 4082), (1400, 4082)])

    # G2 Bus
    add_edge('EDGE_G2_C1', 'G2_HEADER', 'G2_CARD_1',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#880E4F;',
             value='')
    add_edge('EDGE_G2_C2', 'G2_HEADER', 'G2_CARD_2',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#880E4F;',
             value='', points=[(1840, 3560), (1810, 3560), (1810, 3790), (1840, 3790)])
    add_edge('EDGE_G2_C3', 'G2_HEADER', 'G2_CARD_3',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#880E4F;',
             value='', points=[(1840, 3560), (1810, 3560), (1810, 3942), (1840, 3942)])
    add_edge('EDGE_G2_C4', 'G2_HEADER', 'G2_CARD_4',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#880E4F;',
             value='', points=[(1840, 3560), (1810, 3560), (1810, 4092), (1840, 4092)])

    # G3 Bus
    add_edge('EDGE_G3_C1', 'G3_HEADER', 'G3_CARD_1',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#004D40;',
             value='')
    add_edge('EDGE_G3_C2', 'G3_HEADER', 'G3_CARD_2',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#004D40;',
             value='', points=[(2290, 3560), (2260, 3560), (2260, 3785), (2290, 3785)])
    add_edge('EDGE_G3_C3', 'G3_HEADER', 'G3_CARD_3',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#004D40;',
             value='', points=[(2290, 3560), (2260, 3560), (2260, 3932), (2290, 3932)])
    add_edge('EDGE_G3_C4', 'G3_HEADER', 'G3_CARD_4',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#004D40;',
             value='', points=[(2290, 3560), (2260, 3560), (2260, 4087), (2290, 4087)])

    # G4 Bus
    add_edge('EDGE_G4_C1', 'G4_HEADER', 'G4_CARD_1',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#006064;',
             value='')
    add_edge('EDGE_G4_C2', 'G4_HEADER', 'G4_CARD_2',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#006064;',
             value='', points=[(2750, 3560), (2720, 3560), (2720, 3790), (2750, 3790)])
    add_edge('EDGE_G4_C3', 'G4_HEADER', 'G4_CARD_3',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#006064;',
             value='', points=[(2750, 3560), (2720, 3560), (2720, 3940), (2750, 3940)])
    add_edge('EDGE_G4_C4', 'G4_HEADER', 'G4_CARD_4',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#006064;',
             value='', points=[(2750, 3560), (2720, 3560), (2720, 4092), (2750, 4092)])

    # G5 Bus
    add_edge('EDGE_G5_C1', 'G5_HEADER', 'G5_CARD_1',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#BF360C;',
             value='')
    add_edge('EDGE_G5_C2', 'G5_HEADER', 'G5_CARD_2',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#BF360C;',
             value='', points=[(3200, 3560), (3170, 3560), (3170, 3792), (3200, 3792)])
    add_edge('EDGE_G5_C3', 'G5_HEADER', 'G5_CARD_3',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#BF360C;',
             value='', points=[(3200, 3560), (3170, 3560), (3170, 3945), (3200, 3945)])
    add_edge('EDGE_G5_C4', 'G5_HEADER', 'G5_CARD_4',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#BF360C;',
             value='', points=[(3200, 3560), (3170, 3560), (3170, 4095), (3200, 4095)])

    # ========================== CROSS-ENTITY RELATIONSHIPS ==========================
    # [E1] NHNN -> [E3] ROOT
    add_edge('EDGE_E1_E3', 'EXT_E1_NHNN', 'E3_ROOT',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#37474F;dashed=1;',
             value='Định hướng CSTT, áp trần room tín dụng & giám sát an toàn vĩ mô',
             exit_xy=(1, 0.5), entry_xy=(0, 0.5))

    # [E1] NHNN -> G1_CARD_4 (Chiến lược NHTM tuân thủ NHTW)
    add_edge('EDGE_E1_G1', 'EXT_E1_NHNN', 'G1_CARD_4',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#37474F;dashed=1;',
             value='Chiến lược NHTM là bộ phận thực thi chiến lược vĩ mô của NHTW',
             points=[(1140, 3610), (1140, 4082), (1400, 4082)])

    # [E8] FINTECH -> G3_CARD_4 (Big Data & AI phân khúc bán lẻ)
    add_edge('EDGE_E8_G3', 'EXT_E8_FINTECH', 'G3_CARD_4',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#880E4F;dashed=1;',
             value='Ứng dụng Big Data & AI phân khúc khách hàng bán lẻ',
             points=[(1320, 3777), (1350, 3777), (1350, 4190), (2240, 4190), (2240, 4087), (2290, 4087)])

    # [E8] FINTECH -> G4_CARD_4 (Môi trường công nghệ PESTLE)
    add_edge('EDGE_E8_G4', 'EXT_E8_FINTECH', 'G4_CARD_4',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#880E4F;dashed=1;',
             value='Tác nhân công nghệ vĩ mô thúc đẩy chuyển đổi số ngân hàng',
             points=[(1140, 3825), (1140, 4210), (2700, 4210), (2700, 4092), (2750, 4092)])

    # [E4] SURPLUS -> G3_CARD_4 (Khách hàng cá nhân Mass vs VIP)
    add_edge('EDGE_E4_G3', 'EXT_E4_SURPLUS', 'G3_CARD_4',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#1B5E20;dashed=1;',
             value='Khách hàng cá nhân: Nhu cầu Mass vs Priority VIP',
             points=[(3690, 3565), (3140, 3565), (3140, 4087), (2690, 4087)])

    # [E5] DEFICIT -> G3_CARD_3 (Khách hàng doanh nghiệp Big Accounts vs SME)
    add_edge('EDGE_E5_G3', 'EXT_E5_DEFICIT', 'G3_CARD_3',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#BF360C;dashed=1;',
             value='Phân khúc Doanh nghiệp lớn (Account Plan) vs SME',
             points=[(3690, 3755), (3130, 3755), (3130, 3932), (2690, 3932)])

    # [E7] NONDEP -> G5_CARD_1 (Universal Banking & Bán chéo danh mục đầu tư)
    add_edge('EDGE_E7_G5', 'EXT_E7_NONDEP', 'G5_CARD_1',
             'edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=1.5;curved=0;strokeColor=#4A148C;dashed=1;',
             value='Mô hình Universal Banking & Bán chéo đa dạng hóa danh mục',
             points=[(3690, 3945), (3640, 3945), (3640, 3640), (3610, 3640)])

    # Format XML nicely
    xml_str = ET.tostring(mxfile, encoding='utf-8')
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent='  ', encoding='utf-8')

    with open('CH04.drawio', 'wb') as f:
        f.write(pretty_xml)

    print("CH04.drawio successfully generated!")

if __name__ == '__main__':
    create_ch04_xml()
