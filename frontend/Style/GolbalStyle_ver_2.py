# enhanced_global_style.py

import json
import os
from typing import Dict, Any, Optional, List, Callable
import platform

from enum import Enum

class EnhancedGlobalStyle:
    """
    Lớp quản lý style toàn cục cho ứng dụng với nhiều tính năng nâng cao:
    - Hỗ trợ nhiều theme (light, dark, high contrast)
    - Responsive design
    - Hiệu ứng và animation
    - Cấu hình linh hoạt từ file JSON
    - Hỗ trợ accessibility
    """

    # ===== LIGHT THEME =====
    # Color palette for light theme
    MAIN_BG = "#FFFFFF"  # trắng nền
    PRIMARY_COLOR = "#2158B6"  # xanh dương đậm cho header và button
    SECONDARY_COLOR = "#4F7DE0"  # xanh dương nhạt hơn cho các thành phần phụ
    ACCENT_COLOR = "#F5A623"  # màu nhấn
    TEXT_COLOR = "#202E66"  # màu chữ chính
    LABEL_TEXT_COLOR = "#FFFFFF"  # màu chữ trên header label
    TABLE_HEADER_BG = "#F5F5FA"
    TABLE_TEXT_COLOR = "#27272A"
    BORDER_COLOR = "#E0E0E0"
    SUCCESS_COLOR = "#00C853"
    ERROR_COLOR = "#F44336"
    WARNING_COLOR = "#FFC107"
    INFO_COLOR = "#2196F3"

    # Gradient colors
    PRIMARY_GRADIENT_START = "#2158B6"
    PRIMARY_GRADIENT_END = "#4F7DE0"

    # ===== DARK THEME =====
    DARK_BG = "#121212"
    DARK_PRIMARY_COLOR = "#4C7BD9"
    DARK_SECONDARY_COLOR = "#3D6BC9"
    DARK_ACCENT_COLOR = "#FFB74D"
    DARK_TEXT_COLOR = "#E0E0E0"
    DARK_LABEL_TEXT_COLOR = "#FFFFFF"
    DARK_TABLE_HEADER_BG = "#2D2D2D"
    DARK_TABLE_TEXT_COLOR = "#CCCCCC"
    DARK_BORDER_COLOR = "#444444"
    DARK_SUCCESS_COLOR = "#4CAF50"
    DARK_ERROR_COLOR = "#F44336"
    DARK_WARNING_COLOR = "#FFC107"
    DARK_INFO_COLOR = "#2196F3"

    # ===== HIGH CONTRAST =====
    HC_BG = "#FFFFFF"
    HC_PRIMARY_COLOR = "#000080"  # Navy
    HC_SECONDARY_COLOR = "#000000"
    HC_ACCENT_COLOR = "#FFFF00"  # Yellow
    HC_TEXT_COLOR = "#000000"
    HC_LABEL_TEXT_COLOR = "#FFFFFF"
    HC_TABLE_HEADER_BG = "#000000"
    HC_TABLE_TEXT_COLOR = "#FFFFFF"
    HC_BORDER_COLOR = "#000000"
    HC_SUCCESS_COLOR = "#008000"
    HC_ERROR_COLOR = "#FF0000"
    HC_WARNING_COLOR = "#FF8000"
    HC_INFO_COLOR = "#0000FF"

    # Font
    FONT_FAMILY = "'Be Vietnam Pro', 'Inter', Arial, sans-serif"
    TITLE_FONT_SIZE = "24px"
    LABEL_FONT_SIZE = "14px"
    BUTTON_FONT_SIZE = "14px"
    BODY_FONT_SIZE = "14px"
    SMALL_FONT_SIZE = "12px"

    # Accessibility
    LARGE_FONT_SIZE = "18px"
    LARGE_LABEL_FONT_SIZE = "16px"
    LARGE_TITLE_FONT_SIZE = "30px"

    # Animation & Effects
    TRANSITION_DURATION = "0.3s"
    HOVER_EFFECT = "brightness(1.1)"
    SHADOW = "0 2px 5px rgba(0, 0, 0, 0.1)"
    STRONG_SHADOW = "0 4px 8px rgba(0, 0, 0, 0.2)"

    # Responsive breakpoints
    SMALL_SCREEN_WIDTH = 800
    MEDIUM_SCREEN_WIDTH = 1200

    # Window size
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 600

    # Spacing
    PADDING_SMALL = "8px"
    PADDING_MEDIUM = "12px"
    PADDING_LARGE = "16px"
    MARGIN_SMALL = "8px"
    MARGIN_MEDIUM = "12px"
    MARGIN_LARGE = "16px"

    # Border radius
    BORDER_RADIUS_SMALL = "4px"
    BORDER_RADIUS_MEDIUM = "8px"
    BORDER_RADIUS_LARGE = "12px"

    @classmethod
    def load_from_json(cls, filename: str) -> None:
        """Tải style từ file JSON"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                config = json.load(file)
                for key, value in config.items():
                    if hasattr(cls, key):
                        setattr(cls, key, value)
        except Exception as e:
            print(f"Không thể tải cấu hình style: {e}")

    @classmethod
    def save_to_json(cls, filename: str) -> None:
        """Lưu style hiện tại vào file JSON"""
        try:
            # Lấy tất cả thuộc tính không phải là method và không bắt đầu bằng dấu _
            config = {
                name: value for name, value in vars(cls).items()
                if not callable(value) and not name.startswith("_")
            }

            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(config, file, indent=4)
        except Exception as e:
            print(f"Không thể lưu cấu hình style: {e}")

    @classmethod
    def get_base_stylesheet(cls, theme: str = "light") -> str:
        """
        Tạo stylesheet cơ bản dựa trên theme

        Args:
            theme: Tên theme ("light", "dark", "high_contrast")

        Returns:
            Stylesheet cơ bản cho theme đã chọn
        """
        if theme == "dark":
            bg = cls.DARK_BG
            primary = cls.DARK_PRIMARY_COLOR
            secondary = cls.DARK_SECONDARY_COLOR
            accent = cls.DARK_ACCENT_COLOR
            text = cls.DARK_TEXT_COLOR
            label_text = cls.DARK_LABEL_TEXT_COLOR
            table_header = cls.DARK_TABLE_HEADER_BG
            table_text = cls.DARK_TABLE_TEXT_COLOR
            border = cls.DARK_BORDER_COLOR
            success = cls.DARK_SUCCESS_COLOR
            error = cls.DARK_ERROR_COLOR
            warning = cls.DARK_WARNING_COLOR
            info = cls.DARK_INFO_COLOR
        elif theme == "high_contrast":
            bg = cls.HC_BG
            primary = cls.HC_PRIMARY_COLOR
            secondary = cls.HC_SECONDARY_COLOR
            accent = cls.HC_ACCENT_COLOR
            text = cls.HC_TEXT_COLOR
            label_text = cls.HC_LABEL_TEXT_COLOR
            table_header = cls.HC_TABLE_HEADER_BG
            table_text = cls.HC_TABLE_TEXT_COLOR
            border = cls.HC_BORDER_COLOR
            success = cls.HC_SUCCESS_COLOR
            error = cls.HC_ERROR_COLOR
            warning = cls.HC_WARNING_COLOR
            info = cls.HC_INFO_COLOR
        else:  # light theme default
            bg = cls.MAIN_BG
            primary = cls.PRIMARY_COLOR
            secondary = cls.SECONDARY_COLOR
            accent = cls.ACCENT_COLOR
            text = cls.TEXT_COLOR
            label_text = cls.LABEL_TEXT_COLOR
            table_header = cls.TABLE_HEADER_BG
            table_text = cls.TABLE_TEXT_COLOR
            border = cls.BORDER_COLOR
            success = cls.SUCCESS_COLOR
            error = cls.ERROR_COLOR
            warning = cls.WARNING_COLOR
            info = cls.INFO_COLOR

        return f"""
        /* Định nghĩa biến CSS để dễ tham chiếu */
        * {{
            --bg-color: {bg};
            --primary-color: {primary};
            --secondary-color: {secondary};
            --accent-color: {accent};
            --text-color: {text};
            --label-text-color: {label_text};
            --table-header-bg: {table_header};
            --table-text-color: {table_text};
            --border-color: {border};
            --success-color: {success};
            --error-color: {error};
            --warning-color: {warning};
            --info-color: {info};

            --font-family: {cls.FONT_FAMILY};
            --title-font-size: {cls.TITLE_FONT_SIZE};
            --label-font-size: {cls.LABEL_FONT_SIZE};
            --button-font-size: {cls.BUTTON_FONT_SIZE};
            --body-font-size: {cls.BODY_FONT_SIZE};
            --small-font-size: {cls.SMALL_FONT_SIZE};

            --transition-duration: {cls.TRANSITION_DURATION};
            --hover-effect: {cls.HOVER_EFFECT};
            --shadow: {cls.SHADOW};
            --strong-shadow: {cls.STRONG_SHADOW};

            --border-radius-small: {cls.BORDER_RADIUS_SMALL};
            --border-radius-medium: {cls.BORDER_RADIUS_MEDIUM};
            --border-radius-large: {cls.BORDER_RADIUS_LARGE};

            --padding-small: {cls.PADDING_SMALL};
            --padding-medium: {cls.PADDING_MEDIUM};
            --padding-large: {cls.PADDING_LARGE};
            --margin-small: {cls.MARGIN_SMALL};
            --margin-medium: {cls.MARGIN_MEDIUM};
            --margin-large: {cls.MARGIN_LARGE};
        }}
        """

    @classmethod
    def get_widget_style(cls) -> str:
        """
        Style cho QWidget
        """
        return """
        QWidget {
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: var(--font-family);
            font-size: var(--body-font-size);
        }
        """

    @classmethod
    def get_label_style(cls) -> str:
        """
        Style cho QLabel
        """
        return """
        QLabel {
            color: var(--text-color);
            font-family: var(--font-family);
            font-size: var(--label-font-size);
        }

        QLabel#Title {
            color: var(--label-text-color);
            font-size: var(--title-font-size);
            font-weight: 600;
            background-color: var(--primary-color);
            border-radius: var(--border-radius-large);
            padding: var(--padding-medium);
            text-align: center;
        }

        QLabel#SubTitle {
            color: var(--text-color);
            font-size: calc(var(--title-font-size) * 0.8);
            font-weight: 500;
            padding: var(--padding-small);
        }

        QLabel#Success {
            color: var(--success-color);
        }

        QLabel#Error {
            color: var(--error-color);
        }

        QLabel#Warning {
            color: var(--warning-color);
        }

        QLabel#Info {
            color: var(--info-color);
        }
        """

    @classmethod
    def get_button_style(cls) -> str:
        """
        Style cho QPushButton
        """
        return """
        QPushButton {
            background-color: var(--primary-color);
            color: white;
            font-size: var(--button-font-size);
            font-weight: 400;
            font-family: var(--font-family);
            border-radius: var(--border-radius-medium);
            padding: var(--padding-medium) calc(var(--padding-large) * 2);
            transition: background-color var(--transition-duration) ease;
        }

        QPushButton:hover {
            background-color: var(--secondary-color);
            filter: var(--hover-effect);
        }

        QPushButton:pressed {
            background-color: var(--secondary-color);
            padding-top: calc(var(--padding-medium) + 1px);
        }

        QPushButton:disabled {
            background-color: #CCCCCC;
            color: #666666;
        }

        QPushButton#Secondary {
            background-color: white;
            color: var(--primary-color);
            border: 1px solid var(--primary-color);
        }

        QPushButton#Secondary:hover {
            background-color: #F5F5F5;
        }

        QPushButton#Danger {
            background-color: var(--error-color);
        }

        QPushButton#Success {
            background-color: var(--success-color);
        }

        QPushButton#Warning {
            background-color: var(--warning-color);
        }

        QPushButton#GradientButton {
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:0, 
                stop:0 var(--primary-color), 
                stop:1 var(--secondary-color)
            );
        }
        """

    @classmethod
    def get_table_style(cls) -> str:
        """
        Style cho QTableWidget
        """
        return """
        QTableWidget {
            background-color: var(--bg-color);
            alternate-background-color: rgba(128, 128, 128, 0.05);
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-small);
            gridline-color: var(--border-color);
        }

        QTableWidget::item {
            padding: 4px;
            border-bottom: 1px solid var(--border-color);
        }

        QTableWidget::item:selected {
            background-color: rgba(var(--primary-color), 0.2);
            color: var(--text-color);
        }

        QTableWidget QHeaderView::section {
            background-color: var(--table-header-bg);
            color: var(--table-text-color);
            font-size: var(--label-font-size);
            font-weight: 500;
            font-family: var(--font-family);
            padding: 8px;
            border: none;
            border-bottom: 1px solid var(--border-color);
            border-right: 1px solid var(--border-color);
            border-top-left-radius: var(--border-radius-small);
            border-top-right-radius: var(--border-radius-small);
        }

        QTableWidget QHeaderView::section:first {
            border-top-left-radius: var(--border-radius-small);
        }

        QTableWidget QHeaderView::section:last {
            border-top-right-radius: var(--border-radius-small);
            border-right: none;
        }

        QTableWidget QTableCornerButton::section {
            background: var(--table-header-bg);
            border: none;
            border-bottom: 1px solid var(--border-color);
            border-right: 1px solid var(--border-color);
        }
        """

    @classmethod
    def get_input_style(cls) -> str:
        """
        Style cho QLineEdit, QTextEdit, QComboBox
        """
        return """
        QLineEdit, QTextEdit, QComboBox {
            font-size: var(--body-font-size);
            font-family: var(--font-family);
            padding: 8px;
            border-radius: var(--border-radius-medium);
            border: 1px solid var(--border-color);
            background: var(--bg-color);
            color: var(--text-color);
        }

        QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
            border: 1px solid var(--primary-color);
        }

        QLineEdit:disabled, QTextEdit:disabled, QComboBox:disabled {
            background-color: #F0F0F0;
            color: #A0A0A0;
        }

        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: center right;
            width: 20px;
            border-left: 1px solid var(--border-color);
        }

        QComboBox::down-arrow {
            image: url(:/icons/dropdown.png);
            width: 12px;
            height: 12px;
        }

        QComboBox QAbstractItemView {
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-small);
            background-color: var(--bg-color);
            selection-background-color: var(--primary-color);
            selection-color: white;
        }
        """

    @classmethod
    def get_scroll_area_style(cls) -> str:
        """
        Style cho QScrollArea và scrollbars
        """
        return """
        QScrollArea {
            background-color: transparent;
            border: none;
        }

        QScrollBar:vertical {
            background: transparent;
            width: 12px;
            margin: 0px;
        }

        QScrollBar::handle:vertical {
            background: #CCCCCC;
            min-height: 20px;
            border-radius: 6px;
        }

        QScrollBar::handle:vertical:hover {
            background: #AAAAAA;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
        }

        QScrollBar:horizontal {
            background: transparent;
            height: 12px;
            margin: 0px;
        }

        QScrollBar::handle:horizontal {
            background: #CCCCCC;
            min-width: 20px;
            border-radius: 6px;
        }

        QScrollBar::handle:horizontal:hover {
            background: #AAAAAA;
        }

        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
            width: 0px;
        }
        """

    @classmethod
    def get_menu_style(cls) -> str:
        """
        Style cho QMenu và QMenuBar
        """
        return """
        QMenuBar {
            background-color: var(--bg-color);
            color: var(--text-color);
            border-bottom: 1px solid var(--border-color);
        }

        QMenuBar::item {
            background-color: transparent;
            padding: 8px 12px;
        }

        QMenuBar::item:selected {
            background-color: var(--table-header-bg);
            border-radius: var(--border-radius-small);
        }

        QMenu {
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-small);
        }

        QMenu::item {
            padding: 8px 30px 8px 20px;
        }

        QMenu::item:selected {
            background-color: var(--table-header-bg);
        }

        QMenu::separator {
            height: 1px;
            background-color: var(--border-color);
            margin: 4px 0px;
        }
        """

    @classmethod
    def get_tab_style(cls) -> str:
        """
        Style cho QTabWidget và QTabBar
        """
        return """
        QTabWidget::pane {
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-small);
            top: -1px;
        }

        QTabBar::tab {
            background-color: transparent;
            color: var(--text-color);
            padding: 10px 20px;
            border-top-left-radius: var(--border-radius-small);
            border-top-right-radius: var(--border-radius-small);
            border: 1px solid transparent;
            border-bottom: none;
        }

        QTabBar::tab:selected {
            background-color: var(--bg-color);
            border-color: var(--border-color);
            border-bottom-color: var(--bg-color);
        }

        QTabBar::tab:!selected {
            margin-top: 2px;
        }

        QTabBar::tab:hover:!selected {
            background-color: var(--table-header-bg);
        }
        """

    @classmethod
    def get_groupbox_style(cls) -> str:
        """
        Style cho QGroupBox
        """
        return """
        QGroupBox {
            font-weight: bold;
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-medium);
            margin-top: 20px;
            padding-top: 10px;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 5px;
            left: 10px;
        }
        """

    @classmethod
    def get_progressbar_style(cls) -> str:
        """
        Style cho QProgressBar
        """
        return """
        QProgressBar {
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-small);
            text-align: center;
            background-color: var(--bg-color);
            height: 20px;
        }

        QProgressBar::chunk {
            background-color: var(--primary-color);
            border-radius: var(--border-radius-small);
        }
        """

    @classmethod
    def get_checkbox_style(cls) -> str:
        """
        Style cho QCheckBox và QRadioButton
        """
        return """
        QCheckBox, QRadioButton {
            spacing: 8px;
        }

        QCheckBox::indicator, QRadioButton::indicator {
            width: 18px;
            height: 18px;
        }

        QCheckBox::indicator:unchecked, QRadioButton::indicator:unchecked {
            border: 1px solid var(--border-color);
        }

        QCheckBox::indicator:checked {
            background-color: var(--primary-color);
            border: 1px solid var(--primary-color);
            image: url(:/icons/checkbox_checked.png);
        }

        QRadioButton::indicator {
            border-radius: 9px;
        }

        QRadioButton::indicator:checked {
            background-color: var(--primary-color);
            border: 1px solid var(--primary-color);
            width: 12px;
            height: 12px;
            border-radius: 6px;
        }
        """

    @classmethod
    def get_slider_style(cls) -> str:
        """
        Style cho QSlider
        """
        return """
        QSlider::groove:horizontal {
            border: 1px solid var(--border-color);
            height: 6px;
            background: #E0E0E0;
            border-radius: 3px;
        }

        QSlider::handle:horizontal {
            background: var(--primary-color);
            border: none;
            width: 16px;
            height: 16px;
            margin: -5px 0;
            border-radius: 8px;
        }

        QSlider::handle:horizontal:hover {
            background: var(--primary-color);
            filter: var(--hover-effect);
        }
        """

    @classmethod
    def get_tooltip_style(cls) -> str:
        """
        Style cho QToolTip
        """
        return """
        QToolTip {
            background-color: var(--bg-color);
            color: var(--text-color);
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-small);
            padding: 4px;
            font-size: var(--small-font-size);
        }
        """

    @classmethod
    def get_advanced_components_style(cls) -> str:
        """
        Style cho các components nâng cao
        """
        return """
        /* Custom Card Widget */
        .CardWidget {
            background-color: var(--bg-color);
            border-radius: var(--border-radius-medium);
            border: 1px solid var(--border-color);
            padding: var(--padding-medium);
            box-shadow: var(--shadow);
        }

        .CardWidget:hover {
            box-shadow: var(--strong-shadow);
        }

        /* Custom Badge Label */
        .BadgeLabel {
            background-color: var(--secondary-color);
            color: white;
            border-radius: 10px;
            padding: 2px 8px;
            font-size: var(--small-font-size);
        }

        /* Status Indicator */
        .StatusIndicator {
            border-radius: 5px;
            min-width: 10px;
            min-height: 10px;
        }

        .StatusIndicator.Online {
            background-color: var(--success-color);
        }

        .StatusIndicator.Offline {
            background-color: var(--error-color);
        }

        .StatusIndicator.Away {
            background-color: var(--warning-color);
        }
        """

    @classmethod
    def get_stylesheet(cls, theme: str = "light", accessibility: bool = False) -> str:
        """
        Tạo stylesheet đầy đủ cho ứng dụng

        Args:
            theme: Theme được chọn ("light", "dark", "high_contrast")
            accessibility: Bật chế độ trợ năng với font lớn hơn

        Returns:
            Stylesheet đầy đủ cho ứng dụng
        """
        # Điều chỉnh kích thước font nếu bật chế độ trợ năng
        if accessibility:
            orig_title_size = cls.TITLE_FONT_SIZE
            orig_label_size = cls.LABEL_FONT_SIZE
            orig_body_size = cls.BODY_FONT_SIZE

            cls.TITLE_FONT_SIZE = cls.LARGE_TITLE_FONT_SIZE
            cls.LABEL_FONT_SIZE = cls.LARGE_LABEL_FONT_SIZE
            cls.BODY_FONT_SIZE = cls.LARGE_FONT_SIZE
            cls.BUTTON_FONT_SIZE = cls.LARGE_FONT_SIZE

        # Tạo stylesheet
        stylesheet = "\n".join([
            cls.get_base_stylesheet(theme),
            cls.get_widget_style(),
            cls.get_label_style(),
            cls.get_button_style(),
            cls.get_table_style(),
            cls.get_input_style(),
            cls.get_scroll_area_style(),
            cls.get_menu_style(),
            cls.get_tab_style(),
            cls.get_groupbox_style(),
            cls.get_progressbar_style(),
            cls.get_checkbox_style(),
            cls.get_slider_style(),
            cls.get_tooltip_style(),
            cls.get_advanced_components_style()
        ])

        # Khôi phục kích thước font nếu đã thay đổi
        if accessibility:
            cls.TITLE_FONT_SIZE = orig_title_size
            cls.LABEL_FONT_SIZE = orig_label_size
            cls.BODY_FONT_SIZE = orig_body_size
            cls.BUTTON_FONT_SIZE = cls.BODY_FONT_SIZE

        return stylesheet

    @classmethod
    def get_responsive_stylesheet(cls, screen_width: int) -> str:
        """
        Tạo stylesheet đáp ứng theo kích thước màn hình

        Args:
            screen_width: Chiều rộng màn hình

        Returns:
            Stylesheet đáp ứng cho kích thước màn hình hiện tại
        """
        # Lưu giá trị hiện tại
        orig_padding_medium = cls.PADDING_MEDIUM
        orig_padding_large = cls.PADDING_LARGE
        orig_margin_medium = cls.MARGIN_MEDIUM
        orig_button_font_size = cls.BUTTON_FONT_SIZE

        # Điều chỉnh giá trị dựa trên kích thước màn hình
        if screen_width < cls.SMALL_SCREEN_WIDTH:
            cls.PADDING_MEDIUM = "8px"
            cls.PADDING_LARGE = "12px"
            cls.MARGIN_MEDIUM = "8px"
            cls.BUTTON_FONT_SIZE = "12px"
        elif screen_width < cls.MEDIUM_SCREEN_WIDTH:
            cls.PADDING_MEDIUM = "10px"
            cls.PADDING_LARGE = "14px"
            cls.MARGIN_MEDIUM = "10px"
            cls.BUTTON_FONT_SIZE = "13px"

        # Tạo stylesheet
        stylesheet = cls.get_stylesheet()

        # Khôi phục giá trị
        cls.PADDING_MEDIUM = orig_padding_medium
        cls.PADDING_LARGE = orig_padding_large
        cls.MARGIN_MEDIUM = orig_margin_medium
        cls.BUTTON_FONT_SIZE = orig_button_font_size

        return stylesheet


class ThemeType(Enum):
    """Định nghĩa các loại theme hỗ trợ"""
    LIGHT = "light"
    DARK = "dark"
    HIGH_CONTRAST = "high_contrast"
    CUSTOM = "custom"


class ThemeEngine:
    """
    Class quản lý theme cho ứng dụng, cung cấp các phương thức để áp dụng và chuyển đổi theme
    """
    _current_theme: str = "light"
    _accessibility_mode: bool = False
    _custom_themes: Dict[str, Dict[str, Any]] = {}
    _theme_listeners: List[Callable[[str, bool], None]] = []

    @classmethod
    def initialize(cls) -> None:
        """Khởi tạo ThemeEngine và tải các theme từ cấu hình"""
        # Tạo thư mục cấu hình nếu chưa tồn tại
        config_dir = cls._get_config_directory()
        os.makedirs(config_dir, exist_ok=True)

        # Tải các theme tùy chỉnh
        theme_file = os.path.join(config_dir, "custom_themes.json")
        if os.path.exists(theme_file):
            try:
                with open(theme_file, 'r', encoding='utf-8') as f:
                    cls._custom_themes = json.load(f)
            except Exception as e:
                print(f"Không thể tải theme tùy chỉnh: {e}")

        # Tải cấu hình người dùng
        settings_file = os.path.join(config_dir, "theme_settings.json")
        if os.path.exists(settings_file):
            try:
                with open(settings_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    cls._current_theme = settings.get("current_theme", "light")
                    cls._accessibility_mode = settings.get("accessibility_mode", False)
            except Exception as e:
                print(f"Không thể tải cấu hình theme: {e}")

    @classmethod
    def _get_config_directory(cls) -> str:
        """Trả về đường dẫn thư mục cấu hình phù hợp với hệ điều hành"""
        system = platform.system()
        if system == "Windows":
            return os.path.join(os.environ.get("APPDATA", ""), "GlobalStyleApp")
        elif system == "Darwin":  # macOS
            return os.path.join(os.path.expanduser("~"), "Library", "Application Support", "GlobalStyleApp")
        else:  # Linux và các hệ điều hành khác
            return os.path.join(os.path.expanduser("~"), ".config", "GlobalStyleApp")

    @classmethod
    def save_settings(cls) -> None:
        """Lưu cấu hình theme hiện tại"""
        config_dir = cls._get_config_directory()
        os.makedirs(config_dir, exist_ok=True)

        settings_file = os.path.join(config_dir, "theme_settings.json")
        try:
            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "current_theme": cls._current_theme,
                    "accessibility_mode": cls._accessibility_mode
                }, f, indent=4)
        except Exception as e:
            print(f"Không thể lưu cấu hình theme: {e}")

    @classmethod
    def save_custom_themes(cls) -> None:
        """Lưu các theme tùy chỉnh"""
        config_dir = cls._get_config_directory()
        os.makedirs(config_dir, exist_ok=True)

        theme_file = os.path.join(config_dir, "custom_themes.json")
        try:
            with open(theme_file, 'w', encoding='utf-8') as f:
                json.dump(cls._custom_themes, f, indent=4)
        except Exception as e:
            print(f"Không thể lưu theme tùy chỉnh: {e}")

    @classmethod
    def get_current_theme(cls) -> str:
        """Trả về tên theme hiện tại"""
        return cls._current_theme

    @classmethod
    def is_accessibility_mode(cls) -> bool:
        """Kiểm tra xem chế độ trợ năng có đang bật hay không"""
        return cls._accessibility_mode

    @classmethod
    def set_theme(cls, theme_name: str) -> bool:
        """
        Thiết lập theme hiện tại

        Args:
            theme_name: Tên của theme ('light', 'dark', 'high_contrast', hoặc tên theme tùy chỉnh)

        Returns:
            True nếu thay đổi thành công, False nếu theme không tồn tại
        """
        if theme_name in [t.value for t in ThemeType] or theme_name in cls._custom_themes:
            if cls._current_theme != theme_name:
                cls._current_theme = theme_name
                cls._notify_theme_changed()
                cls.save_settings()
            return True
        return False

    @classmethod
    def toggle_accessibility_mode(cls) -> None:
        """Bật/tắt chế độ trợ năng"""
        cls._accessibility_mode = not cls._accessibility_mode
        cls._notify_theme_changed()
        cls.save_settings()

    @classmethod
    def set_accessibility_mode(cls, enabled: bool) -> None:
        """
        Thiết lập chế độ trợ năng

        Args:
            enabled: True để bật, False để tắt
        """
        if cls._accessibility_mode != enabled:
            cls._accessibility_mode = enabled
            cls._notify_theme_changed()
            cls.save_settings()

    @classmethod
    def create_custom_theme(cls, name: str, theme_data: Dict[str, Any]) -> bool:
        """
        Tạo một theme tùy chỉnh mới

        Args:
            name: Tên cho theme mới
            theme_data: Dictionary chứa dữ liệu theme (màu sắc, font, etc.)

        Returns:
            True nếu tạo thành công, False nếu tên đã tồn tại
        """
        if name in [t.value for t in ThemeType]:
            return False  # Không thể ghi đè theme mặc định

        cls._custom_themes[name] = theme_data
        cls.save_custom_themes()
        return True

    @classmethod
    def update_custom_theme(cls, name: str, theme_data: Dict[str, Any]) -> bool:
        """
        Cập nhật một theme tùy chỉnh

        Args:
            name: Tên theme cần cập nhật
            theme_data: Dữ liệu theme mới

        Returns:
            True nếu cập nhật thành công, False nếu theme không tồn tại hoặc là theme mặc định
        """
        if name in [t.value for t in ThemeType]:
            return False  # Không thể cập nhật theme mặc định

        if name not in cls._custom_themes:
            return False

        cls._custom_themes[name] = theme_data
        cls.save_custom_themes()

        # Nếu đang sử dụng theme này, thông báo thay đổi
        if cls._current_theme == name:
            cls._notify_theme_changed()

        return True

    @classmethod
    def delete_custom_theme(cls, name: str) -> bool:
        """
        Xóa một theme tùy chỉnh

        Args:
            name: Tên theme cần xóa

        Returns:
            True nếu xóa thành công, False nếu theme không tồn tại hoặc là theme mặc định
        """
        if name in [t.value for t in ThemeType]:
            return False  # Không thể xóa theme mặc định

        if name not in cls._custom_themes:
            return False

        # Nếu đang sử dụng theme này, chuyển về light theme
        if cls._current_theme == name:
            cls._current_theme = ThemeType.LIGHT.value
            cls._notify_theme_changed()

        del cls._custom_themes[name]
        cls.save_custom_themes()
        return True

    @classmethod
    def get_custom_theme(cls, name: str) -> Optional[Dict[str, Any]]:
        """
        Lấy dữ liệu của một theme tùy chỉnh

        Args:
            name: Tên theme

        Returns:
            Dictionary chứa dữ liệu theme hoặc None nếu không tìm thấy
        """
        return cls._custom_themes.get(name)

    @classmethod
    def get_all_theme_names(cls) -> List[str]:
        """
        Lấy danh sách tên tất cả các theme có sẵn

        Returns:
            Danh sách tên theme
        """
        return [t.value for t in ThemeType if t != ThemeType.CUSTOM] + list(cls._custom_themes.keys())

    @classmethod
    def add_theme_listener(cls, listener: Callable[[str, bool], None]) -> None:
        """
        Thêm một listener để nhận thông báo khi theme thay đổi

        Args:
            listener: Hàm callback nhận tham số (theme_name, accessibility_mode)
        """
        if listener not in cls._theme_listeners:
            cls._theme_listeners.append(listener)

    @classmethod
    def remove_theme_listener(cls, listener: Callable[[str, bool], None]) -> None:
        """
        Xóa một listener

        Args:
            listener: Hàm callback đã đăng ký
        """
        if listener in cls._theme_listeners:
            cls._theme_listeners.remove(listener)

    @classmethod
    def _notify_theme_changed(cls) -> None:
        """Thông báo cho tất cả listeners khi theme thay đổi"""
        for listener in cls._theme_listeners:
            try:
                listener(cls._current_theme, cls._accessibility_mode)
            except Exception as e:
                print(f"Lỗi khi thông báo theme thay đổi: {e}")

    @classmethod
    def apply_theme_to_application(cls, app) -> None:
        """
        Áp dụng theme hiện tại cho toàn bộ ứng dụng

        Args:
            app: Đối tượng QApplication
        """
        stylesheet = EnhancedGlobalStyle.get_stylesheet(
            theme=cls._current_theme,
            accessibility=cls._accessibility_mode
        )
        app.setStyleSheet(stylesheet)

        # Áp dụng theme tùy chỉnh nếu có
        if cls._current_theme in cls._custom_themes:
            custom_data = cls._custom_themes[cls._current_theme]
            for key, value in custom_data.items():
                if hasattr(EnhancedGlobalStyle, key):
                    setattr(EnhancedGlobalStyle, key, value)


class ColorSetPresets:
    """
    Cung cấp các bộ màu định sẵn cho theme
    """

    @staticmethod
    def get_blue_preset() -> Dict[str, str]:
        """Bộ màu xanh dương chuyên nghiệp"""
        return {
            "PRIMARY_COLOR": "#1976D2",
            "SECONDARY_COLOR": "#2196F3",
            "ACCENT_COLOR": "#FFC107",
            "MAIN_BG": "#FFFFFF",
            "TEXT_COLOR": "#263238",
            "LABEL_TEXT_COLOR": "#FFFFFF",
            "TABLE_HEADER_BG": "#ECEFF1",
            "TABLE_TEXT_COLOR": "#212121",
            "BORDER_COLOR": "#CFD8DC",
            "SUCCESS_COLOR": "#4CAF50",
            "ERROR_COLOR": "#F44336",
            "WARNING_COLOR": "#FF9800",
            "INFO_COLOR": "#03A9F4",
        }

    @staticmethod
    def get_dark_blue_preset() -> Dict[str, str]:
        """Bộ màu xanh dương tối"""
        return {
            "DARK_BG": "#0D1117",
            "DARK_PRIMARY_COLOR": "#58A6FF",
            "DARK_SECONDARY_COLOR": "#1F6FEB",
            "DARK_ACCENT_COLOR": "#F0883E",
            "DARK_TEXT_COLOR": "#C9D1D9",
            "DARK_LABEL_TEXT_COLOR": "#FFFFFF",
            "DARK_TABLE_HEADER_BG": "#161B22",
            "DARK_TABLE_TEXT_COLOR": "#C9D1D9",
            "DARK_BORDER_COLOR": "#30363D",
            "DARK_SUCCESS_COLOR": "#3FB950",
            "DARK_ERROR_COLOR": "#F85149",
            "DARK_WARNING_COLOR": "#F0883E",
            "DARK_INFO_COLOR": "#58A6FF",
        }

    @staticmethod
    def get_green_preset() -> Dict[str, str]:
        """Bộ màu xanh lá"""
        return {
            "PRIMARY_COLOR": "#2E7D32",
            "SECONDARY_COLOR": "#4CAF50",
            "ACCENT_COLOR": "#FF9800",
            "MAIN_BG": "#FFFFFF",
            "TEXT_COLOR": "#212121",
            "LABEL_TEXT_COLOR": "#FFFFFF",
            "TABLE_HEADER_BG": "#E8F5E9",
            "TABLE_TEXT_COLOR": "#212121",
            "BORDER_COLOR": "#C8E6C9",
            "SUCCESS_COLOR": "#00C853",
            "ERROR_COLOR": "#D50000",
            "WARNING_COLOR": "#FF6D00",
            "INFO_COLOR": "#00B0FF",
        }

    @staticmethod
    def get_purple_preset() -> Dict[str, str]:
        """Bộ màu tím"""
        return {
            "PRIMARY_COLOR": "#6A1B9A",
            "SECONDARY_COLOR": "#9C27B0",
            "ACCENT_COLOR": "#FFC107",
            "MAIN_BG": "#FFFFFF",
            "TEXT_COLOR": "#212121",
            "LABEL_TEXT_COLOR": "#FFFFFF",
            "TABLE_HEADER_BG": "#F3E5F5",
            "TABLE_TEXT_COLOR": "#212121",
            "BORDER_COLOR": "#E1BEE7",
            "SUCCESS_COLOR": "#4CAF50",
            "ERROR_COLOR": "#F44336",
            "WARNING_COLOR": "#FF9800",
            "INFO_COLOR": "#2196F3",
        }

    @staticmethod
    def get_red_preset() -> Dict[str, str]:
        """Bộ màu đỏ"""
        return {
            "PRIMARY_COLOR": "#C62828",
            "SECONDARY_COLOR": "#F44336",
            "ACCENT_COLOR": "#FFC107",
            "MAIN_BG": "#FFFFFF",
            "TEXT_COLOR": "#212121",
            "LABEL_TEXT_COLOR": "#FFFFFF",
            "TABLE_HEADER_BG": "#FFEBEE",
            "TABLE_TEXT_COLOR": "#212121",
            "BORDER_COLOR": "#FFCDD2",
            "SUCCESS_COLOR": "#4CAF50",
            "ERROR_COLOR": "#D50000",
            "WARNING_COLOR": "#FF9800",
            "INFO_COLOR": "#2196F3",
        }

    @staticmethod
    def get_all_presets() -> Dict[str, Dict[str, str]]:
        """Lấy tất cả các bộ màu định sẵn"""
        return {
            "blue": ColorSetPresets.get_blue_preset(),
            "dark_blue": ColorSetPresets.get_dark_blue_preset(),
            "green": ColorSetPresets.get_green_preset(),
            "purple": ColorSetPresets.get_purple_preset(),
            "red": ColorSetPresets.get_red_preset(),
        }


class FontPresets:
    """
    Cung cấp các bộ font định sẵn
    """

    @staticmethod
    def get_system_default() -> Dict[str, str]:
        """Font mặc định của hệ thống"""
        system = platform.system()
        if system == "Windows":
            return {
                "FONT_FAMILY": "Segoe UI, Arial, sans-serif",
                "TITLE_FONT_SIZE": "24px",
                "LABEL_FONT_SIZE": "14px",
                "BUTTON_FONT_SIZE": "14px",
                "BODY_FONT_SIZE": "14px",
                "SMALL_FONT_SIZE": "12px",
            }
        elif system == "Darwin":  # macOS
            return {
                "FONT_FAMILY": "-apple-system, BlinkMacSystemFont, San Francisco, Helvetica Neue, sans-serif",
                "TITLE_FONT_SIZE": "24px",
                "LABEL_FONT_SIZE": "14px",
                "BUTTON_FONT_SIZE": "14px",
                "BODY_FONT_SIZE": "14px",
                "SMALL_FONT_SIZE": "12px",
            }
        else:  # Linux
            return {
                "FONT_FAMILY": "Ubuntu, Noto Sans, Droid Sans, sans-serif",
                "TITLE_FONT_SIZE": "24px",
                "LABEL_FONT_SIZE": "14px",
                "BUTTON_FONT_SIZE": "14px",
                "BODY_FONT_SIZE": "14px",
                "SMALL_FONT_SIZE": "12px",
            }

    @staticmethod
    def get_modern() -> Dict[str, str]:
        """Font hiện đại"""
        return {
            "FONT_FAMILY": "Roboto, 'Open Sans', Arial, sans-serif",
            "TITLE_FONT_SIZE": "28px",
            "LABEL_FONT_SIZE": "15px",
            "BUTTON_FONT_SIZE": "15px",
            "BODY_FONT_SIZE": "15px",
            "SMALL_FONT_SIZE": "13px",
        }

    @staticmethod
    def get_traditional() -> Dict[str, str]:
        """Font truyền thống"""
        return {
            "FONT_FAMILY": "'Times New Roman', Georgia, serif",
            "TITLE_FONT_SIZE": "26px",
            "LABEL_FONT_SIZE": "16px",
            "BUTTON_FONT_SIZE": "16px",
            "BODY_FONT_SIZE": "16px",
            "SMALL_FONT_SIZE": "14px",
        }

    @staticmethod
    def get_monospace() -> Dict[str, str]:
        """Font monospace"""
        return {
            "FONT_FAMILY": "'Courier New', Courier, monospace",
            "TITLE_FONT_SIZE": "24px",
            "LABEL_FONT_SIZE": "14px",
            "BUTTON_FONT_SIZE": "14px",
            "BODY_FONT_SIZE": "14px",
            "SMALL_FONT_SIZE": "12px",
        }

    @staticmethod
    def get_all_presets() -> Dict[str, Dict[str, str]]:
        """Lấy tất cả các bộ font định sẵn"""
        return {
            "system_default": FontPresets.get_system_default(),
            "modern": FontPresets.get_modern(),
            "traditional": FontPresets.get_traditional(),
            "monospace": FontPresets.get_monospace(),
        }


class AnimationPresets:
    """
    Cung cấp các bộ animation định sẵn
    """

    @staticmethod
    def get_subtle() -> Dict[str, str]:
        """Animation tinh tế"""
        return {
            "TRANSITION_DURATION": "0.2s",
            "HOVER_EFFECT": "brightness(1.05)",
            "SHADOW": "0 1px 3px rgba(0, 0, 0, 0.1)",
            "STRONG_SHADOW": "0 2px 5px rgba(0, 0, 0, 0.15)",
        }

    @staticmethod
    def get_medium() -> Dict[str, str]:
        """Animation trung bình"""
        return {
            "TRANSITION_DURATION": "0.3s",
            "HOVER_EFFECT": "brightness(1.1)",
            "SHADOW": "0 2px 5px rgba(0, 0, 0, 0.1)",
            "STRONG_SHADOW": "0 4px 8px rgba(0, 0, 0, 0.2)",
        }

    @staticmethod
    def get_pronounced() -> Dict[str, str]:
        """Animation mạnh mẽ"""
        return {
            "TRANSITION_DURATION": "0.4s",
            "HOVER_EFFECT": "brightness(1.15)",
            "SHADOW": "0 3px 7px rgba(0, 0, 0, 0.15)",
            "STRONG_SHADOW": "0 6px 12px rgba(0, 0, 0, 0.25)",
        }

    @staticmethod
    def get_no_animation() -> Dict[str, str]:
        """Không có animation"""
        return {
            "TRANSITION_DURATION": "0s",
            "HOVER_EFFECT": "none",
            "SHADOW": "none",
            "STRONG_SHADOW": "none",
        }

    @staticmethod
    def get_all_presets() -> Dict[str, Dict[str, str]]:
        """Lấy tất cả các bộ animation định sẵn"""
        return {
            "subtle": AnimationPresets.get_subtle(),
            "medium": AnimationPresets.get_medium(),
            "pronounced": AnimationPresets.get_pronounced(),
            "none": AnimationPresets.get_no_animation(),
        }


class StyleManager:
    """
    Quản lý và tạo các style tùy chỉnh từ các presets
    """

    @staticmethod
    def create_theme_from_presets(
            name: str,
            color_preset: str = "blue",
            font_preset: str = "system_default",
            animation_preset: str = "medium",
            dark_mode: bool = False
    ) -> Dict[str, Any]:
        """
        Tạo theme mới từ các preset

        Args:
            name: Tên theme
            color_preset: Tên bộ màu (blue, green, purple, red)
            font_preset: Tên bộ font (system_default, modern, traditional, monospace)
            animation_preset: Tên bộ animation (subtle, medium, pronounced, none)
            dark_mode: True để tạo theme tối, False cho theme sáng

        Returns:
            Dictionary chứa dữ liệu theme
        """
        # Lấy các preset
        all_colors = ColorSetPresets.get_all_presets()
        all_fonts = FontPresets.get_all_presets()
        all_animations = AnimationPresets.get_all_presets()

        color_data = all_colors.get(color_preset, all_colors["blue"])
        font_data = all_fonts.get(font_preset, all_fonts["system_default"])
        animation_data = all_animations.get(animation_preset, all_animations["medium"])

        # Tạo theme mới
        theme_data = {}

        # Áp dụng màu sắc cho theme tối hoặc sáng
        if dark_mode:
            dark_color_data = all_colors.get("dark_blue", all_colors["dark_blue"])
            for key, value in dark_color_data.items():
                theme_data[key] = value
        else:
            for key, value in color_data.items():
                if not key.startswith("DARK_"):
                    theme_data[key] = value

        # Áp dụng font và animation
        for key, value in font_data.items():
            theme_data[key] = value

        for key, value in animation_data.items():
            theme_data[key] = value

        return theme_data

    @staticmethod
    def apply_theme_to_global_style(theme_data: Dict[str, Any]) -> None:
        """
        Áp dụng dữ liệu theme vào EnhancedGlobalStyle

        Args:
            theme_data: Dictionary chứa dữ liệu theme
        """
        for key, value in theme_data.items():
            if hasattr(EnhancedGlobalStyle, key):
                setattr(EnhancedGlobalStyle, key, value)


class StyleExporter:
    """
    Xuất style ra các định dạng khác nhau (CSS, QSS, JSON)
    """

    @staticmethod
    def export_to_css(filename: str, theme: str = "light") -> bool:
        """
        Xuất style hiện tại ra file CSS

        Args:
            filename: Đường dẫn file CSS đầu ra
            theme: Theme cần xuất (light, dark, high_contrast hoặc tên theme tùy chỉnh)

        Returns:
            True nếu xuất thành công, False nếu có lỗi
        """
        try:
            # Lấy stylesheet
            stylesheet = EnhancedGlobalStyle.get_stylesheet(theme=theme)

            # Xử lý và chuyển đổi QSS sang CSS thuần túy
            # Loại bỏ các selector và thuộc tính đặc biệt của Qt
            css = stylesheet.replace("QWidget", "body")
            css = css.replace("QLabel", "label")
            css = css.replace("QPushButton", "button")
            css = css.replace("QLineEdit", "input[type='text']")
            css = css.replace("QTextEdit", "textarea")
            css = css.replace("QComboBox", "select")
            css = css.replace("QCheckBox", "input[type='checkbox']")
            css = css.replace("QRadioButton", "input[type='radio']")

            # Ghi ra file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(css)

            return True
        except Exception as e:
            print(f"Không thể xuất file CSS: {e}")
            return False

    @staticmethod
    def export_to_qss(filename: str, theme: str = "light") -> bool:
        """
        Xuất style hiện tại ra file QSS

        Args:
            filename: Đường dẫn file QSS đầu ra
            theme: Theme cần xuất

        Returns:
            True nếu xuất thành công, False nếu có lỗi
        """
        try:
            # Lấy stylesheet
            stylesheet = EnhancedGlobalStyle.get_stylesheet(theme=theme)

            # Ghi ra file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(stylesheet)

            return True
        except Exception as e:
            print(f"Không thể xuất file QSS: {e}")
            return False

    @staticmethod
    def export_theme_to_json(filename: str, theme_name: str = None) -> bool:
        """
        Xuất thông tin về một theme ra file JSON

        Args:
            filename: Đường dẫn file JSON đầu ra
            theme_name: Tên theme cần xuất, nếu None sẽ xuất theme hiện tại

        Returns:
            True nếu xuất thành công, False nếu có lỗi
        """
        try:
            if theme_name is None:
                theme_name = ThemeEngine.get_current_theme()

            # Nếu là theme tùy chỉnh, lấy dữ liệu từ ThemeEngine
            if theme_name in ThemeEngine._custom_themes:
                theme_data = ThemeEngine.get_custom_theme(theme_name)

                # Ghi ra file
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(theme_data, f, indent=4)

                return True

            # Nếu là theme mặc định, tạo dictionary từ EnhancedGlobalStyle
            else:
                # Lấy tất cả thuộc tính không phải là method và không bắt đầu bằng dấu _
                theme_data = {
                    name: value for name, value in vars(EnhancedGlobalStyle).items()
                    if not callable(value) and not name.startswith("_")
                }

                # Ghi ra file
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(theme_data, f, indent=4)

                return True
        except Exception as e:
            print(f"Không thể xuất file JSON: {e}")
            return False