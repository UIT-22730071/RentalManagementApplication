from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout,
    QPushButton, QGroupBox, QMessageBox
)
from typing import List, Dict, Any

from QLNHATRO.RentalManagementApplication.frontend.Component.LabelUI import LabelUI
from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle
from QLNHATRO.RentalManagementApplication.frontend.Component.InforUpdater import InfoUpdater


class FormInforUI(QWidget):

    info_updated = pyqtSignal(dict)

    def __init__(self,
                 title: str,
                 initial_data: Dict[str, Any] = None,
                 field_configs: List[Dict[str, str]] = None,
                 custom_styles: Dict[str, str] = None):
        """
        Initialize the FormInforUI

        :param title: Title of the form
        :param initial_data: Initial data dictionary
        :param field_configs: List of field configurations
        :param custom_styles: Optional custom styling dictionary
        """
        super().__init__()

        # Default color palette
        self.MENU_COLOR = "#2196F3"
        self.BACKGROUND_COLOR = "#F5F5F5"
        self.TEXT_COLOR = "#333333"
        self.ACCENT_COLOR = "#1976D2"
        self.BORDER_COLOR = "#E0E0E0"

        # Override default colors if custom styles provided
        if custom_styles:
            # Lưu custom_styles gốc để kiểm tra
            bg_color = custom_styles.get("BACKGROUND_COLOR", self.BACKGROUND_COLOR)

            for key, value in custom_styles.items():
                # Kiểm tra đặc biệt cho TEXT_COLOR
                if key == "TEXT_COLOR":
                    # Nếu màu chữ và màu nền giống nhau, sử dụng màu chữ tương phản
                    if value.lower() == bg_color.lower() or self._similar_colors(value, bg_color):
                        print(
                            f"⚠️ TEXT_COLOR ({value}) quá giống với BACKGROUND_COLOR ({bg_color}), sử dụng màu tương phản.")
                        # Chọn màu chữ tương phản với nền
                        value = self._get_contrasting_color(bg_color)
                setattr(self, key, value)

        # Initialize data and configurations
        self.initial_data = initial_data or {}
        self.field_configs = field_configs or []
        self.label_fields = {}

        self.setup_ui(title)

    def _similar_colors(self, color1: str, color2: str) -> bool:
        """
        Kiểm tra xem hai màu có tương tự nhau không
        """
        try:
            # Chuyển mã màu hex thành RGB
            def hex_to_rgb(hex_color):
                hex_color = hex_color.lstrip('#')
                return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

            rgb1 = hex_to_rgb(color1)
            rgb2 = hex_to_rgb(color2)

            # Tính khoảng cách màu đơn giản
            distance = sum(abs(c1 - c2) for c1, c2 in zip(rgb1, rgb2))

            # Nếu độ chênh lệch quá thấp, coi là tương tự
            return distance < 125
        except Exception:
            return False

    def _get_contrasting_color(self, color: str) -> str:
        """
        Trả về màu tương phản với màu đã cho
        """
        try:
            # Chuyển hex sang RGB
            color = color.lstrip('#')
            r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)

            # Tính độ sáng
            brightness = (r * 299 + g * 587 + b * 114) / 1000

            # Đối với màu tối, trả về màu sáng và ngược lại
            return "#FFFFFF" if brightness < 128 else "#000000"
        except Exception:
            return "#333333"  # Màu chữ mặc định an toàn

    def setup_ui(self, title: str):
        """
        Set up the user interface

        :param title: Title of the form
        """
        self.setStyleSheet(GlobalStyle.global_stylesheet() + f"""
            QLabel {{
                color: {self.TEXT_COLOR};
                font-weight: 500;
            }}
            QPushButton {{
                background-color: {self.ACCENT_COLOR};
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 4px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #1565C0;
            }}
            QGroupBox {{
                border: 1px solid {self.BORDER_COLOR};
                border-radius: 5px;
                background-color: white;
                color: {self.TEXT_COLOR};
                margin-top: 10px;
            }}
        """)

        main_layout = QVBoxLayout()

        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            font-size: 24px; 
            font-weight: bold; 
            color: {self.TEXT_COLOR}; 
            padding: 15px;
            background-color: white;
            border-bottom: 2px solid {self.BORDER_COLOR};
        """)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setSpacing(10)

        # Create fields dynamically
        for config in self.field_configs:
            group = QGroupBox()
            hbox = QHBoxLayout()

            # Label with icon
            label = QLabel(f"{config.get('icon', '')} {config['name']}:")
            label.setStyleSheet(f"font-size: 16px; min-width: 160px; color: {self.TEXT_COLOR};")

            # LabelUI for displaying value - không thay đổi cách tạo

            label_ui = LabelUI(str(self.initial_data.get(config['key'], '')), color="#333")

            # Đảm bảo LabelUI có màu chữ rõ ràng nhưng không can thiệp quá nhiều
            self._ensure_label_visibility(label_ui)

            self.label_fields[config['key']] = label_ui

            # Update button
            update_btn = QPushButton("Cập nhật")
            update_btn.clicked.connect(lambda _, cfg=config: self.update_field(cfg))

            hbox.addWidget(label)
            hbox.addWidget(label_ui, stretch=1)
            hbox.addWidget(update_btn)
            group.setLayout(hbox)
            content_layout.addWidget(group)

        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

    def _ensure_label_visibility(self, label_ui):
        """
        Đảm bảo LabelUI có thể nhìn thấy được bằng cách ghi đè màu chữ
        """
        # Luôn đặt màu chữ tối trên nền trắng
        current_style = label_ui.styleSheet()
        # Loại bỏ các thuộc tính color cũ nếu có
        if "color:" in current_style:
            parts = current_style.split(';')
            filtered_parts = [p for p in parts if not p.strip().startswith("color:")]
            current_style = ';'.join(filtered_parts)

        # Thêm thuộc tính color mới với !important
        label_ui.setStyleSheet(f"{current_style}; color: #333333 !important;")

    def load_data(self, data: Dict[str, Any] = None):
        """
        Load or update data in the form

        :param data: Dictionary of data to load
        """
        if data:
            self.initial_data.update(data)

        for key, label_ui in self.label_fields.items():
            label_ui.setText(str(self.initial_data.get(key, '')))
            # Đảm bảo màu chữ luôn là tối, bất kể style hiện tại
            label_ui.setStyleSheet("* { color: #333333 !important; }")

    def update_field(self, config: Dict[str, str]):
        """
        Open update dialog for a specific field

        :param config: Field configuration dictionary
        """
        label = self.label_fields[config['key']]

        dialog = InfoUpdater(
            title=config['name'],
            current_value=label.text(),
            on_update_callback=lambda new_val: self.apply_update(config['key'], new_val)
        )
        dialog.exec_()

    def apply_update(self, key: str, new_value: str):
        """
        Apply update to a specific field

        :param key: Field key
        :param new_value: New value for the field
        """
        try:
            # Optional custom validation can be added here
            if key == 'phone_number' and not new_value.isdigit():
                raise ValueError("Số điện thoại phải là chữ số")

            self.label_fields[key].setText(new_value)
            # Đảm bảo màu vẫn đúng sau khi cập nhật
            self._ensure_label_visibility(self.label_fields[key])

            self.initial_data[key] = new_value

            self.info_updated.emit({
                "updated_key": key,
                "new_value": new_value,
                "full_data": self.initial_data
            })

            QMessageBox.information(
                self,
                "Cập Nhật Thành Công",
                f"Đã cập nhật {key} thành {new_value}"
            )

        except ValueError as e:
            QMessageBox.warning(self, "Lỗi Cập Nhật", str(e))

        print(f"✅ Đã cập nhật {key}: {new_value}")