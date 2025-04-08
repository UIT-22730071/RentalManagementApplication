from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

from QLNHATRO.RentalManagementApplication.controller.RoomController.RoomMenuController import RoomMenuController
from QLNHATRO.RentalManagementApplication.frontend.Component.ButtonUI import ButtonUI


class RoomMenu(QWidget):
    def __init__(self, main_window, room_id):
        super().__init__()
        self.controller = RoomMenuController()
        self.main_window = main_window
        self.room_id = room_id
        self.current_page = None

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        # ------------ LEFT MENU FRAME ------------
        self.left_frame = QWidget()
        self.left_frame.setFixedWidth(250)
        self.left_frame.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FF6B6B, stop:1 #FFA07A);
            border-radius: 15px;
        """)

        left_layout = QVBoxLayout(self.left_frame)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.label_landlord = QLabel(f"👋 Phòng: {room_id}")
        self.label_landlord.setStyleSheet("color: white; font-weight: bold; padding: 10px;")

        # Nút menu
        button_ui = ButtonUI.room_menu_button()

        self.home_btn = QPushButton("Trang chính")
        button_ui.apply_style(self.home_btn)
        self.home_btn.clicked.connect(lambda: self.controller.go_to_open_right_frame_room_home(self, self.main_window, self.room_id))

        self.room_infor_btn = QPushButton("Thông tin phòng")
        button_ui.apply_style(self.room_infor_btn)
        self.room_infor_btn.clicked.connect(lambda: self.controller.go_to_open_right_frame_rooms_infor(self, self.main_window, self.room_id))

        self.add_new_tenant_btn = QPushButton("Cập nhật người thuê")
        button_ui.apply_style(self.add_new_tenant_btn)
        self.add_new_tenant_btn.clicked.connect(
            lambda: self.controller.go_to_open_right_frame_room_menu(self, self.main_window, self.room_id)
        )
        self.create_invoice_btn = QPushButton("Tạo hóa đơn")
        button_ui.apply_style(self.create_invoice_btn)
        self.create_invoice_btn.clicked.connect(lambda: self.controller.go_to_open_right_frame_ManagerInvoicePage(self, self.main_window, self.room_id))

        self.delete_room_btn = QPushButton("Xóa phòng")
        button_ui.apply_style(self.delete_room_btn)
        self.delete_room_btn.clicked.connect(lambda: print("Clicled Xóa phòng"))


        self.back_button = QPushButton("Quay lại")
        button_ui.apply_style(self.back_button)
        self.back_button.clicked.connect(lambda: self.main_window.go_to_exs())

        # Thêm vào layout trái
        left_layout.addWidget(self.label_landlord)
        left_layout.addWidget(self.home_btn)
        left_layout.addWidget(self.room_infor_btn)
        left_layout.addWidget(self.add_new_tenant_btn)
        left_layout.addWidget(self.create_invoice_btn)
        left_layout.addWidget(self.delete_room_btn)
        left_layout.addWidget(self.back_button)

        # ------------ RIGHT CONTENT FRAME ------------
        self.right_frame = QWidget()
        self.right_layout = QVBoxLayout(self.right_frame)
        self.right_layout.setContentsMargins(0, 0, 0, 0)

        # Khởi tạo page mặc định
        self.controller.go_to_open_right_frame_room_home(self, self.main_window, self.room_id)

        self.main_layout.addWidget(self.left_frame)
        self.main_layout.addWidget(self.right_frame, 1)

    def set_right_frame(self, PageClass, *args):
        """Thay đổi nội dung frame bên phải với khả năng truyền nhiều tham số khác nhau"""
        if self.current_page:
            self.right_layout.removeWidget(self.current_page)
            self.current_page.deleteLater()
            self.current_page = None

        self.current_page = PageClass(*args)
        self.right_layout.addWidget(self.current_page)

