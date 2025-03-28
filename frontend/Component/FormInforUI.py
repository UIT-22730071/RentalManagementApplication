from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout,
    QPushButton, QGroupBox, QMessageBox
)
from typing import List, Dict, Any, Callable

from QLNHATRO.RentalManagementApplication.frontend.Component.LabelUI import LabelUI
from QLNHATRO.RentalManagementApplication.frontend.views.UpdateUI.InforUpdater import InfoUpdater


class FormInforUI(QWidget):
    """
    A reusable form information UI component that can be used across different classes.
    Supports dynamic field configuration and updates.
    """
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
            for key, value in custom_styles.items():
                setattr(self, key, value)

        # Initialize data and configurations
        self.initial_data = initial_data or {}
        self.field_configs = field_configs or []
        self.label_fields = {}

        self.setup_ui(title)

    def setup_ui(self, title: str):
        """
        Set up the user interface

        :param title: Title of the form
        """
        # Styling
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {self.BACKGROUND_COLOR};
                color: {self.TEXT_COLOR};
                font-family: 'Segoe UI', Arial, sans-serif;
            }}
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
                margin-top: 10px;
                background-color: white;
                color: {self.TEXT_COLOR};
            }}
            QScrollArea {{
                background-color: {self.BACKGROUND_COLOR};
                border: none;
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

            # LabelUI for displaying value
            label_ui = LabelUI(str(self.initial_data.get(config['key'], '')))
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

    def load_data(self, data: Dict[str, Any] = None):
        """
        Load or update data in the form

        :param data: Dictionary of data to load
        """
        if data:
            self.initial_data.update(data)

        for key, label_ui in self.label_fields.items():
            label_ui.setText(str(self.initial_data.get(key, '')))

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
            self.initial_data[key] = new_value

            self.info_updated.emit(self.initial_data)

            QMessageBox.information(
                self,
                "Cập Nhật Thành Công",
                f"Đã cập nhật {key} thành {new_value}"
            )

        except ValueError as e:
            QMessageBox.warning(self, "Lỗi Cập Nhật", str(e))

        print(f"✅ Đã cập nhật {key}: {new_value}")