from PyQt5.QtGui import QFont


class ButtonUI:
    """Lớp quản lý thiết kế UI cho các Button trong PyQt6"""

    def __init__(self, background="#FF6B6B", text_color="white", border="2px solid black",
                 border_radius="10px", font_size="16px", padding="10px",
                 margin="5px", hover_bg="#FF9999", hover_text="black"):
        self.background = background
        self.text_color = text_color
        self.border = border
        self.border_radius = border_radius
        self.font_size = font_size
        self.padding = padding
        self.margin = margin
        self.hover_bg = hover_bg
        self.hover_text = hover_text

    def apply_style(self, widget):
        """Áp dụng style cho một QPushButton"""
        style = f"""
            QPushButton {{
                background-color: {self.background};
                color: {self.text_color};
                border: {self.border};
                border-radius: {self.border_radius};
                font-size: {self.font_size};
                padding: {self.padding};
                margin: {self.margin};
                text-align: left;
            }}
            QPushButton::hover {{
                background-color: {self.hover_bg};
                color: {self.hover_text};
            }}
        """

        if self.hover_bg or self.hover_text:
            hover_style = "QPushButton:hover {"
            if self.hover_bg:
                hover_style += f"background-color: {self.hover_bg}; "
            if self.hover_text:
                hover_style += f"color: {self.hover_text}; "
            hover_style += "}"
            style += hover_style

        widget.setStyleSheet(style)

    @staticmethod
    def primary_button():
        """Tạo kiểu button chính"""
        return ButtonUI(background="#FF6B6B", hover_bg="#FF9999")

    @staticmethod
    def secondary_button():
        """Tạo kiểu button phụ"""
        return ButtonUI(background="#4A90E2", hover_bg="#72B6F9")

    @staticmethod
    def success_button():
        """Tạo kiểu button xác nhận"""
        return ButtonUI(background="#28A745", hover_bg="#5BC85B")

    @staticmethod
    def danger_button():
        """Tạo kiểu button cảnh báo"""
        return ButtonUI(background="#DC3545", hover_bg="#FF6B6B")

    @staticmethod
    def login_register_button():
         #""" background-color: #FF6B6B; color: white; font-weight: bold;  border-radius: 20px;""")
        return ButtonUI(background="#FF6B6B", hover_bg="#FF9999", border_radius="20px", font_size="14px")

    @staticmethod
    def landlord_dashboard_button():
        """Button chính cho dashboard chủ trọ: đều, căn trái, đổ bóng, bo góc"""
        return ButtonUI(
            background="#0E3958",
            text_color="white",
            border="none",
            border_radius="10px",
            font_size="16px",
            padding="12px",
            margin="8px",
            hover_bg="#38ACFE",
            hover_text="white"
        )
    @staticmethod
    def tenant_dashboard_button():
        """
        Create a style configuration for tenant dashboard buttons
        Similar to landlord_dashboard_button() but with a different color scheme
        """
        return ButtonUI(
            background="#0192F4",  # Deep blue background
            text_color="white",
            border="none",
            border_radius="10px",
            font_size="16px",
            padding="12px",
            margin="8px",
            hover_bg="#38ACFE",  # Lighter blue on hover
            hover_text="white"
        )

