from datetime import datetime

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
    def get_id_lanlord_from_id_invoice(invoice_id):
        #TODO: tạo truy vấn SQL lấy id lanlord
        pass
    @staticmethod
    def get_id_room_from_id_invoice(invoice_id):
        #TODO tạo truy vấn SQL lấy id phòng
        pass
    @staticmethod
    def get_id_tenant_from_id_invoice(invoice_id):
        #TODO: tạo truy vấn SQL lấy id người thuê
        pass
    @staticmethod
    def get_invoice_data_for_invoice_view(invoice_id):
        #TODO: tạo truy vấn SQL lấy dữ liệu hóa đơn
        # Lấy số điện cũ và nước cũ đòi hỏi phải truy vấn hóa đơn tháng trước
        invoice_data = {
            'invoice_id': 123,
            'invoice_code': '1C21TAA',
            'date': datetime.now().strftime('%d/%m/%Y'),
            'prev_electric': 0,
            'curr_electric': 0,
            'prev_water': 0,
            'curr_water': 0,
            'discount': 0  # Added default discount value
        }
        return invoice_data

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

    @staticmethod
    def get_date_new_invoice_of_room(tenant_id):
        #TODO: Tạo truy vấn trả về date mới nhất của cái hóa đơn mới nhất
        return "30-04-2025"

    @staticmethod
    def get_invoices_by_tenant_id(tenant_id):
        """
        Get all invoices for a tenant from the database

        Args:
            tenant_id: The ID of the tenant

        Returns:
            A list of invoice data dictionaries
        """
        # TODO: Replace with actual SQL query
        # SQL would be something like:
        # SELECT i.*, r.room_name
        # FROM invoices i
        # JOIN RoomAdvertisement r ON i.room_id = r.id
        # WHERE i.tenant_id = [tenant_id]
        # ORDER BY i.created_date DESC

        # Sample data for development
        invoices = [
            {
                'invoice_id': '12345',
                'created_date': '2025-04-15',
                'room': {
                    'room_id': 'P101',
                    'room_name': 'Phòng 101'
                },
                'rent_price': 3500000,
                'electricity_price': 3800,
                'water_price': 25000,
                'internet_price': 100000,
                'old_electricity': 1250,
                'new_electricity': 1420,
                'old_water': 45,
                'new_water': 52,
                'other_fees': 20000,
                'garbage_fee': 50000,
                'is_paid': True
            },
            {
                'invoice_id': '12346',
                'created_date': '2025-03-15',
                'room': {
                    'room_id': 'P101',
                    'room_name': 'Phòng 101'
                },
                'rent_price': 3500000,
                'electricity_price': 3800,
                'water_price': 25000,
                'internet_price': 100000,
                'old_electricity': 1100,
                'new_electricity': 1250,
                'old_water': 38,
                'new_water': 45,
                'other_fees': 20000,
                'garbage_fee': 50000,
                'is_paid': True
            },
            {
                'invoice_id': '12347',
                'created_date': '2025-02-15',
                'room': {
                    'room_id': 'P101',
                    'room_name': 'Phòng 101'
                },
                'rent_price': 3500000,
                'electricity_price': 3500,  # Notice price changed
                'water_price': 25000,
                'internet_price': 100000,
                'old_electricity': 950,
                'new_electricity': 1100,
                'old_water': 32,
                'new_water': 38,
                'other_fees': 20000,
                'garbage_fee': 50000,
                'is_paid': True
            }
        ]

        return invoices
    # TODO Admin
    ''' Phần này của Admin chưa cập nhật'''

    @staticmethod
    def count_paid_invoices_by_month(month, year):
        # TODO: Truy vấn SQL đếm hóa đơn thanh toán trong tháng
        return 2  # Giả lập

    @staticmethod
    def get_all_invoices():
        return [
            {
                "invoice_id": 1,
                "room_name": "Phòng A101",
                "rent_price": 1500000,
                "electric_fee": 300000,
                "water_fee": 100000,
                "garbage_fee": 50000,
                "internet_fee": 70000,
                "other_fee": 30000,
                "created_at": "2025-04-01",
                "landlord_name": "Nguyễn Văn A",
                "tenant_name": "Trần Thị B"
            },
            {
                "invoice_id": 2,
                "room_name": "Phòng B202",
                "rent_price": 2000000,
                "electric_fee": 250000,
                "water_fee": 90000,
                "garbage_fee": 40000,
                "internet_fee": 80000,
                "other_fee": 20000,
                "created_at": "2025-04-02",
                "landlord_name": "Lê Thị C",
                "tenant_name": "Phạm Văn D"
            },
            {
                "invoice_id": 3,
                "room_name": "Phòng C303",
                "rent_price": 1800000,
                "electric_fee": 320000,
                "water_fee": 95000,
                "garbage_fee": 55000,
                "internet_fee": 75000,
                "other_fee": 25000,
                "created_at": "2025-04-03",
                "landlord_name": "Trương Văn E",
                "tenant_name": "Ngô Thị F"
            }
        ]

