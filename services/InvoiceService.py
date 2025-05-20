from QLNHATRO.RentalManagementApplication.Repository.InvoiceRepository import InvoiceRepository
from QLNHATRO.RentalManagementApplication.Repository.LandlordRepository import LanlordRepository
from QLNHATRO.RentalManagementApplication.Repository.RoomRepository import RoomRepository
from QLNHATRO.RentalManagementApplication.Repository.TenantRepository import TenantRepository


class InvoiceService:
    @staticmethod
    def create_invoice(invoice_data):
        """Tạo hóa đơn mới"""
        # TODO: tạo truy vấn SQL lấy invoice
        # Xử lý logic tạo hóa đơn
        room = invoice_data['room']

        # Tạo ID hóa đơn
        invoice_id = f"INV-{room['id']}-{invoice_data['chi_so_dien_moi']}"

        # Chuẩn bị dữ liệu hóa đơn
        invoice = {
            'invoice_id': invoice_id,
            'room': room,
            'tenant': invoice_data['tenant'],
            'chi_so_dien_cu': room['chi_so_dien'],
            'chi_so_dien_moi': invoice_data['chi_so_dien_moi'],
            'chi_so_nuoc_cu': room['chi_so_nuoc'],
            'chi_so_nuoc_moi': invoice_data['chi_so_nuoc_moi'],
            'so_nguoi': invoice_data['so_nguoi'],
            'phi_khac': invoice_data['phi_khac'],
            'ngay_tao': 'Ngày tạo: 06/04/2025'
        }

        # Lưu hóa đơn vào database
        InvoiceRepository.save_invoice(invoice)

        return invoice

    @staticmethod
    def calculate_total(self):
        so_dien = self.new_electricity - self.old_electricity
        so_nuoc = self.new_water - self.old_water
        tong = (
                self.rent_price +
                so_dien * self.electricity_price +
                so_nuoc * self.water_price +
                self.internet_price +
                self.other_fees
        )
        return tong



    @staticmethod
    def handle_data_for_invoice_list_page(id_lanlord):
        raw_data = InvoiceRepository.get_data_invoice_by_lanlord_id(id_lanlord)
        number_data = []
        '''
                   'room_name': 'Phòng 101',
                   'cost_rent': 3500000,
                   'electricity_cost': 3800,
                   'water_cost': 100000,
                   'internet_cost': 100000,
                   'other_cost': 20000,
                   'created_date': '2025-04-06',
                   'id_invoice': '01'
        '''
        for idx, item in enumerate(raw_data, start=1):
            total_cost = (
                    item['cost_rent'] +
                    item['electricity_cost'] +
                    item['water_cost'] +
                    item['internet_cost'] +
                    item['other_cost']
            )
            item_with_extra = {
                "STT": idx,
                "Tên Phòng": item["room_name"],
                "Tiền nhà": f"{item['cost_rent']:,} VNĐ",
                "Tiền điện": f"{item['electricity_cost']:,} VNĐ",
                "Tiền nước": f"{item['water_cost']:,} VNĐ",
                "Tiền rác": f"{item['other_cost']:,} VNĐ",
                "Tổng chi phí": f"{total_cost:,} VNĐ",
                "Ngày xuất hóa đơn": item["created_date"],  # format lại nếu cần
                "Chi tiết hóa đơn": "Chi tiết",
                "id_invoice":item["id_invoice"]
            }

            number_data.append(item_with_extra)

        return InvoiceService.map_keys_for_table(number_data)

    @staticmethod
    def map_keys_for_table(data):
        """Chuyển đổi key từ dữ liệu gốc sang key UI cần (nếu cần thiết)"""
        mapped = []
        for item in data:
            try:
                mapped.append({
                    'STT': item['STT'],
                    'Tên Phòng': item['Tên Phòng'],
                    'Tiền nhà': item['Tiền nhà'],
                    'Tiền điện': item['Tiền điện'],
                    'Tiền nước': item['Tiền nước'],
                    'Tiền rác': item['Tiền rác'],
                    'Tổng chi phí': item['Tổng chi phí'],
                    'Ngày xuất hóa đơn': item['Ngày xuất hóa đơn'],
                    'Chi tiết hóa đơn': item['Chi tiết hóa đơn'],
                    'id_invoice':item['id_invoice']
                })
            except KeyError as e:
                print(f"[ERROR] Key không tồn tại trong dữ liệu hóa đơn: {e}")
        return mapped

    @staticmethod
    def get_full_invoice_data(invoice_id):
        return InvoiceRepository.get_invoice_data(invoice_id)

    @staticmethod
    def get_invoice_data_for_invoice_view(invoice_id):
        """Lấy dữ liệu hóa đơn đầy đủ để truyền vào giao diện InvoiceView"""
        id_lanlord = InvoiceRepository.get_id_lanlord_from_id_invoice(invoice_id)
        id_room = InvoiceRepository.get_id_room_from_id_invoice(invoice_id)
        id_tenant = InvoiceRepository.get_id_tenant_from_id_invoice(invoice_id)

        invoice_data = InvoiceRepository.get_invoice_data_for_invoice_view(invoice_id)
        landlord_data = LanlordRepository.get_landlord_data_for_invoice_view(id_lanlord)
        tenant_data = TenantRepository.get_tenant_data_for_invoice_view(id_tenant)
        room_data = RoomRepository.get_room_data_for_invoice_view(id_room)
        total_data_invoice_view = {'invoice_data': invoice_data, 'landlord_data': landlord_data, 'tenant_data': tenant_data, 'room_data': room_data}

        # chuẩn hóa hoặc xử lý thêm nếu cần
        return total_data_invoice_view

    @staticmethod
    def calculate_totals(invoice_data: dict, room_data: dict) -> dict:
        electric_used = invoice_data['curr_electric'] - invoice_data['prev_electric']
        water_used = invoice_data['curr_water'] - invoice_data['prev_water']

        room_fee_base = room_data['room_price']
        electric_fee_base = electric_used * room_data['electric_price']
        water_fee_base = water_used * room_data['water_price']
        garbage_fee_base = room_data['garbage_fee']
        internet_fee_base = room_data.get('internet_fee', 0)
        another_fee_base = room_data.get('another_fee', 0)

        room_fee_tax = room_fee_base * 0.1
        electric_fee_tax = electric_fee_base * 0.1
        water_fee_tax = water_fee_base * 0.1
        garbage_fee_tax = garbage_fee_base * 0.1
        internet_fee_tax = 0
        another_fee_tax = another_fee_base * 0.1

        total_base = (room_fee_base + electric_fee_base + water_fee_base +
                      garbage_fee_base + internet_fee_base + another_fee_base)
        total_tax = (room_fee_tax + electric_fee_tax + water_fee_tax +
                     garbage_fee_tax + internet_fee_tax + another_fee_tax)

        discount = invoice_data.get('discount', 0)
        total_amount = total_base + total_tax - discount

        return {
            'total_base': total_base,
            'total_tax': total_tax,
            'total_amount': total_amount
        }

    @staticmethod
    def number_to_words(number: int) -> str:
        if number == 0:
            return "Không đồng"

        units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
        teens = ["", "mười một", "mười hai", "mười ba", "mười bốn", "mười lăm", "mười sáu", "mười bảy", "mười tám",
                 "mười chín"]
        tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi",
                "chín mươi"]

        def read_group(num):
            result = ""
            hundred = num // 100
            remainder = num % 100

            if hundred > 0:
                result += units[hundred] + " trăm "

            if remainder > 0:
                if remainder < 10:
                    if hundred > 0:
                        result += "lẻ "
                    result += units[remainder]
                elif remainder < 20:
                    result += teens[remainder - 10]
                else:
                    ten = remainder // 10
                    unit = remainder % 10
                    result += tens[ten]
                    if unit > 0:
                        if unit == 1:
                            result += " mốt"
                        elif unit == 5:
                            result += " lăm"
                        else:
                            result += " " + units[unit]

            return result.strip()

        result = ""
        billion = number // 1000000000
        million = (number % 1000000000) // 1000000
        thousand = (number % 1000000) // 1000
        remainder = number % 1000

        if billion > 0:
            result += read_group(billion) + " tỷ "
        if million > 0:
            result += read_group(million) + " triệu "
        if thousand > 0:
            result += read_group(thousand) + " nghìn "
        if remainder > 0:
            result += read_group(remainder)

        return result.strip() + " đồng"


    @staticmethod
    def map_room_tenant_info(room: dict, tenant: dict) -> dict:
        """Trả về mapping dữ liệu giữa phòng và người thuê để hiển thị lên view"""
        return {
            "Tên phòng": room['ten_phong'],
            "Mã phòng": room['id'],
            "Người thuê": tenant['ho_ten'],
            "CCCD": tenant['cccd'],
            "Địa chỉ": room.get('dia_chi', '---'),
            "Giá phòng": f"{room['gia_phong']} VNĐ",
            "Giá điện": f"{room['gia_dien']} VNĐ/kWh",
            "Giá nước": f"{room['gia_nuoc']} VNĐ/người",
            "Internet": f"{room.get('internet', '100000')} VNĐ",
            "Phí khác": f"{room.get('phi_khac', '20000')} VNĐ",
            "Số điện cũ": f"{room.get('chi_so_dien', '---')} KWH",
            "Số nước cũ": f"{room.get('chi_so_nuoc', '---')} m3",
        }
