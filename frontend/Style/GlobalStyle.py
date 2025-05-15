

# global_styles.py
'''
self.setStyleSheet(GlobalStyle.global_stylesheet())
title.setObjectName("Title")
title.setFixedHeight(60)

cancel_button.setObjectName("CancelBtn")

'''

class GlobalStyle:
    # Color palette
    MAIN_BG = "#FFFFFF"  # trắng nền
    PRIMARY_COLOR = "#2158B6"  # xanh dương đậm cho header và button
    TEXT_COLOR = "#202E66"  # màu chữ chính
    LABEL_TEXT_COLOR = "#FFFFFF"  # màu chữ trên header label
    TABLE_HEADER_BG = "#F5F5FA"
    TABLE_TEXT_COLOR = "#27272A"

    # Font
    FONT_FAMILY = "'Be Vietnam Pro', 'Inter', Arial, sans-serif"
    TITLE_FONT_SIZE = "24px"
    LABEL_FONT_SIZE = "14px"

    # Window size
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 600
    # Thêm các hằng số cho responsive design
    SMALL_SCREEN_WIDTH = 800
    MEDIUM_SCREEN_WIDTH = 1200
    #Button
    BUTTON_SPECIAL_COLOR = "#233FF3"

    @staticmethod
    def global_stylesheet():
        return f"""
        QWidget {{
            background-color: {GlobalStyle.MAIN_BG};
            color: {GlobalStyle.TEXT_COLOR};
            font-family: {GlobalStyle.FONT_FAMILY};
        }}
        
        
        QFrame#separator {{
            background-color: #E9FBFC;
            min-height: 2px;
            max-height: 2px;
            margin: 10px 0px;
                }}

        
        QLabel#Title {{
            color: {GlobalStyle.LABEL_TEXT_COLOR};
            font-size: {GlobalStyle.TITLE_FONT_SIZE};
            font-weight: 600;
            background-color: {GlobalStyle.PRIMARY_COLOR};
            border-radius: 12px;
            padding: 10px;
            text-align: center;
        }}

        QPushButton {{
            background-color: {GlobalStyle.PRIMARY_COLOR};
            color: white;
            font-size: 14px;
            font-weight: 400;
            font-family: 'Be Vietnam', sans-serif;
            border-radius: 9px;
            padding: 12px 38px;
        }}

        QPushButton:hover {{
            background-color: #1D4DA5;
        }}
        
        QPushButton#CancelBtn {{
            background-color: #F44336 ;  /* Màu xám nhạt */
            color: #202E66;
            font-size: 14px;
            font-weight: 400;
            font-family: 'Be Vietnam', sans-serif;
            border-radius: 9px;
            padding: 12px 38px;
        }}
        
        QPushButton#CancelBtn:hover {{
            background-color: #B0B0B0;
        }}

        
        QTableWidget QHeaderView::section {{
            background-color: {GlobalStyle.TABLE_HEADER_BG};
            color: {GlobalStyle.TABLE_TEXT_COLOR};
            font-size: 14px;
            font-weight: 400;
            font-family: 'Inter', sans-serif;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            padding: 8px;
        }}

        QTableWidget QTableCornerButton::section {{
            background: {GlobalStyle.TABLE_HEADER_BG};
        }}

        QTableWidget QTableView {{
            background: white;
            color: {GlobalStyle.TABLE_TEXT_COLOR};
            font-size: 14px;
            font-family: 'Inter';
        }}

        QLineEdit, QTextEdit, QComboBox {{
            font-size: 14px;
            font-family: 'Be Vietnam';
            padding: 8px;
            border-radius: 8px;
            border: 1px solid #ccc;
            background: white;
        }}

        QScrollArea {{
            background-color: transparent;
        }}
        QComboBox {{
            font-size: 14px;
            font-family: 'Be Vietnam';
            padding: 8px;
            border-radius: 8px;
            border: 1px solid #ccc;
            background-color: white;
        }}
        QComboBox QAbstractItemView {{
            background-color: white;
            selection-background-color: #EAF2FF;
            selection-color: {GlobalStyle.TEXT_COLOR};
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 6px;
        }}
        
        QComboBox::drop-down {{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 28px;
            border-left: 1px solid #ccc;
        }}
        
        QComboBox::down-arrow {{
            image: url(icons/arrow-down.svg); /* nếu có icon riêng */
            width: 12px;
            height: 12px;
        }}
        QCheckBox {{
            font-size: 14px;
            color: #202E66;
            padding: 6px 8px;
            border-radius: 6px;
            background-color: #f5f5f5;
        }}
        
        QCheckBox:hover {{
            background-color: #EAF2FF;
        }}
        
        QCheckBox::indicator {{
            width: 16px;
            height: 16px;
            border-radius: 4px;
            background-color: white;
            border: 2px solid #2158B6;
        }}
        
        QCheckBox::indicator:checked {{
            background-color: #2158B6;
        }}
        
        QCheckBox::indicator:unchecked {{
            background-color: white;
        }}
        QFrame#tableCard {{
            background-color: white;
            border-radius: 12px;
            border: 1px solid #dcdcdc;
            padding: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }}
        QRadioButton::indicator {{
            width: 22px;
            height: 22px;
        }}
        QRadioButton::indicator:checked {{
            background-color: #2158B6;
            border: 2px solid #2158B6;
            border-radius: 11px;
        }}
        QRadioButton::indicator:unchecked {{
            background-color: white;
            border: 2px solid #ccc;
            border-radius: 11px;
        }}

        QLabel#infoLabel {{
            color: #7f8c8d;
            font-style: italic;
        }}
        
        QLabel#sectionLabel {{
            font-weight: bold;
            color: #202E66;
            font-size: 14px;
        }}
        
        QLabel#imagePreview {{
            border: 1px dashed #bdc3c7;
            border-radius: 8px;
            background-color: #FAFAFA;
            min-height: 120px;
            min-width: 120px;
        }}
        
        QLabel#keyLabel {{
            font-size: 14px;
            color: #2c3e50;
            font-weight: bold;
        }}
        
        QLabel#valueLabel {{
            font-size: 16px;
            font-weight: bold;
            color: white;
            background-color: #2158B6;
            border-radius: 5px;
            padding: 8px;
            margin: 2px;
        }}


        QLabel#valueLabel[highlight] {{
            background-color: #e74c3c;
        }}


        
        QGroupBox {{
            border: 1px solid #ddd;
            border-radius: 8px;
            background-color: #fafafa;
            margin-top: 10px;
            padding: 8px;
        }}
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 6px;
            font-weight: bold;
            background-color: transparent;
        }}

        QGroupBox[theme="blue"] {{
            font-weight: bold;
            border: 1px solid #333333;   
            border-radius: 10px;
            margin-top: 15px;
            padding-top: 15px;
            background-color: white;
            color: #2c3e50;
        }}
        
        QGroupBox[theme="blue"]::title {{
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 10px;
            color: #2c3e50;
            font-size: 16px;
            background-color: white;
            border-radius: 5px;
        }}

        """






#TODO: Sau khi apply toàn bộ gobalStyle sẽ tiín hành áp dụng gobalTyle_ver2

'''
from QLNHATRO.RentalManagementApplication.frontend.styles.GolbalStyle_ver_2 import EnhancedGlobalStyle

class GlobalStyle:
    """
    Lớp bridge giữ nguyên API `GlobalStyle.global_stylesheet()` cũ,
    nhưng nội dung sẽ lấy từ `EnhancedGlobalStyle.get_stylesheet(theme='light')`
    """
    @staticmethod
    def global_stylesheet():
        return EnhancedGlobalStyle.get_stylesheet(theme="light", accessibility=False)

'''