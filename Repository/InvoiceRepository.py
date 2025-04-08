from QLNHATRO.RentalManagementApplication.Repository.RoomRepository import RoomRepository
# Thực hiên CRUD

class InvoiceRepository:
    @staticmethod
    def save_invoice(invoice_data):
        """Lưu hóa đơn vào database"""
        # TODO: Thay thế bằng truy vấn SQL INSERT
        print(f"✅ Đã lưu hóa đơn: {invoice_data['invoice_id']}")

        # Cập nhật chỉ số điện nước mới cho phòng
        RoomRepository.update_room_metrics(
            invoice_data['room']['id'],
            invoice_data['chi_so_dien_moi'],
            invoice_data['chi_so_nuoc_moi']
        )

        return True

    @staticmethod
    def update_invoice_to_database(invoice_data_update_database):
        # TODO: Thay thế bằng truy vấn SQL UPDATE
        '''
        invoice_data_update_database = {
            'id_room': self.selected_room['id'],
            'id_tenant': self.selected_tenant['id'],
            'chi_so_dien': chi_so_dien,
            'chi_so_nuoc': chi_so_nuoc
        }
        '''

        print(f"✅ Đã cập nhật hóa đơn:")

        return True
    @staticmethod
    #TODO: tạo truy vấn SQL lấy id hóa đơn mới nhất của phòng
    def get_new_id_invoice(room_id, tenant_id):
        # blabla
        invoice_id = '02'
        return invoice_id
    @staticmethod
    def get_invoice_data(invoice_id):
        """
        Lấy thông tin chi tiết của một hóa đơn dựa trên invoice_id.
        TODO: Thay thế bằng truy vấn SQL thực tế từ cơ sở dữ liệu.
        """
        # Giả lập dữ liệu hóa đơn từ database
        invoice_data = {
            "invoice_id": invoice_id,
            "room": {
                "room_id": "P101",
                "room_name": "Phòng 101"
            },
            "tenant": {
                "tenant_id": "TNT001",
                "full_name": "Nguyễn Văn A"
            },
            "rent_price": 3500000,
            "electricity_price": 3800,
            "water_price": 100000,
            "internet_price": 100000,
            "old_electricity": 245,
            "new_electricity": 260,
            "old_water": 32,
            "new_water": 36,
            "other_fees": 20000,
            "created_date": "2025-04-06"
        }

        return invoice_data


    @staticmethod
    def  get_data_invoice_by_lanlord_id(id_lanlord):
        # TODO: tạo truy vấn SQL lấy danh sách tất cả hóa đơn theo id phòng from INVOICE
        data_invoice = [{
        'room_name': 'Phòng 101',
        'cost_rent': 3500000,
        'electricity_cost': 3800,
        'water_cost': 100000,
        'internet_cost': 100000,
        'other_cost': 20000,
        'created_date': '2025-04-06',
        'id_invoice': '01'
        },
        {
            'room_name': 'Phòng 102',
            'cost_rent': 3500000,
            'electricity_cost': 4800,
            'water_cost': 102000,
            'internet_cost': 102000,
            'other_cost': 22000,
            'created_date': '2025-05-06',
            'id_invoice': '02'
        }
        ]
        return data_invoice



    @staticmethod
    def get_invoice_data_for_view_bill(invoice_id):
        ''' Chuẩn bị dữ liệu cho hóa đơn trong view hóa đơn'''
        pass

    @staticmethod
    def get_invoice_data_from_invoice_id(invoice_id):
        pass
    @staticmethod
    def get_old_number_electricity_water(invoice_id):
        pass
