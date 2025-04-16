from QLNHATRO.RentalManagementApplication.backend.Repository import InvoiceRepository


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

