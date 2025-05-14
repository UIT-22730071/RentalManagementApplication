'''

# global_styles.py

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


    @staticmethod
    def global_stylesheet():
        return f"""
        QWidget {{
            background-color: {GlobalStyle.MAIN_BG};
            color: {GlobalStyle.TEXT_COLOR};
            font-family: {GlobalStyle.FONT_FAMILY};
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
        """



'''