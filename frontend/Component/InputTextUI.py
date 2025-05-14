from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class InputTextUI:
    """Lớp lưu trữ giao diện QLineEdit tùy chỉnh"""

    def __init__(self, background="white", text_color="black", border="2px solid #ccc",
                 border_radius="8px", font_size="14px", padding="8px",
                 focus_border="2px solid #FF6B6B", focus_bg="white"):
        self.background = background
        self.text_color = text_color
        self.border = border
        self.border_radius = border_radius
        self.font_size = font_size
        self.padding = padding
        self.focus_border = focus_border
        self.focus_bg = focus_bg

    def apply_style(self, widget):
        """Áp dụng style cho ô nhập liệu (QLineEdit)"""
        base_style = GlobalStyle.global_stylesheet()
        custom_style = f"""
            QLineEdit {{
                background-color: {self.background};
                color: {self.text_color};
                border: {self.border};
                border-radius: {self.border_radius};
                font-size: {self.font_size};
                padding: {self.padding};
                transition: 0.3s;
            }}
            QLineEdit:focus {{
                border: {self.focus_border};
                background-color: {self.focus_bg};
            }}
        """
        widget.setStyleSheet(base_style + custom_style)

    @staticmethod
    def default_input():
        """Tạo ô nhập liệu với style mặc định"""
        return InputTextUI()

    @staticmethod
    def rounded_input():
        """Tạo ô nhập liệu bo tròn hơn"""
        return InputTextUI(border_radius="15px", border="2px solid #ddd", focus_border="2px solid #FF6B6B")

    @staticmethod
    def dark_input():
        """Tạo ô nhập liệu tối"""
        return InputTextUI(background="#333", text_color="white", border="2px solid #555", focus_border="2px solid #FF6B6B")

    @staticmethod
    def transparent_input():
        """Tạo ô nhập liệu trong suốt"""
        return InputTextUI(background="transparent", border="1px solid white", text_color="white", focus_border="2px solid #FF6B6B")
