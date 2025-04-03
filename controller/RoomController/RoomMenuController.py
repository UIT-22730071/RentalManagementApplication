from QLNHATRO.RentalManagementApplication.frontend.views.Rooms.RoomUpdateTenantPage import RoomUpdateTenantPage
from QLNHATRO.RentalManagementApplication.frontend.views.Rooms.RoomsHome import RoomsHome
from QLNHATRO.RentalManagementApplication.frontend.views.Rooms.RoomsInfor import RoomsInfor


class RoomMenuController:
    def __init__(self):
        pass  # Có thể khởi tạo DB connection tại đây nếu cần
    #TODO : Call hàm lấy thông tin phòng từ id_room ==> Dictionary hoặc List / Tuble
    def get_room_data_list(self):
        # Giả lập danh sách phòng, sau này sẽ lấy từ DB
        return [
            {'id': 1, 'ten_phong': 'Phòng 101', 'gia_phong': 2500000, 'chi_so_dien': 120, 'chi_so_nuoc': 45, 'dien_tich': 20},
            {'id': 2, 'ten_phong': 'Phòng 102', 'gia_phong': 2700000, 'chi_so_dien': 110, 'chi_so_nuoc': 50, 'dien_tich': 22}
        ]

    # TODO : Call hàm lấy thông tin người thuê từ CCCD ==> Dictionary hoặc List / Tuble
    def find_tenant_by_cccd(self, cccd):
        # Giả lập tìm người thuê, sau này dùng SQL
        if cccd == "123456789":
            return {
                'id': 5,
                'ho_ten': 'Nguyễn Văn A',
                'sdt': '0909090909',
                'cccd': '123456789',
                'email': 'a@gmail.com'
            }
        return None

    def update_tenant_for_room(self, room_id, tenant_id):
        print(f"✅ Cập nhật người thuê {tenant_id} vào phòng {room_id}")
        # TODO: Gọi query SQL để update `PhongTro.id_nguoithue = tenant_id` WHERE id = room_id

    def go_to_open_right_frame_room_menu(self, room_menu_instance, main_window, room_id):
        room_data_list = self.get_room_data_list()
        tenant_callback = self.find_tenant_by_cccd
        update_callback = self.update_tenant_for_room

        room_menu_instance.set_right_frame(
            RoomUpdateTenantPage,
            main_window,
            room_data_list,
            tenant_callback,
            update_callback,
            room_id
        )
    def go_to_open_right_frame_rooms_infor(self, room_menu_instance, main_window, room_id):
        room_menu_instance.set_right_frame(RoomsInfor, main_window, room_id)

    def go_to_open_right_frame_room_home(self, room_menu_instance, main_window, room_id):
        room_menu_instance.set_right_frame(RoomsHome, main_window, room_id)

