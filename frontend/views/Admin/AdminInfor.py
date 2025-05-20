import io
import os
import sys

import requests
import pymupdf  # hoặc: import fitz as pymupdf
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea,
                             QFrame, QSizePolicy, QPushButton, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtPrintSupport import QPrinter

from QLNHATRO.RentalManagementApplication.frontend.Style.GlobalStyle import GlobalStyle


class PageIndicator(QWidget):


    def __init__(self, total_pages=1):
        super().__init__()
        self.current_page = 1
        self.total_pages = total_pages

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)

        self.prev_btn = QPushButton()
        self.prev_btn.setIcon(QIcon("icons/prev.png"))
        self.prev_btn.setFixedSize(30, 30)
        self.prev_btn.clicked.connect(self.prev_page)

        self.page_label = QLabel(f"{self.current_page}/{self.total_pages}")
        self.page_label.setStyleSheet("color: white; font-size: 14px; font-family: Roboto; font-weight: 500;")

        self.next_btn = QPushButton()
        self.next_btn.setIcon(QIcon("icons/next.png"))
        self.next_btn.setFixedSize(30, 30)
        self.next_btn.clicked.connect(self.next_page)

        layout.addWidget(self.prev_btn)
        layout.addWidget(self.page_label)
        layout.addWidget(self.next_btn)

        self.update_buttons()

    def update_buttons(self):
        self.prev_btn.setEnabled(self.current_page > 1)
        self.next_btn.setEnabled(self.current_page < self.total_pages)
        self.page_label.setText(f"{self.current_page}/{self.total_pages}")

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_buttons()
            # Signal to parent widget to change content

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_buttons()
            # Signal to parent widget to change content


class ContentSection(QFrame):
    """Reusable content section with title and content"""

    def __init__(self, title, content_widget=None):
        super().__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet("""
            QFrame {
                background-color: #F9F9F9;
                border-radius: 10px;
                border: 1px solid #E0E0E0;
            }
        """)
        #self.setMinimumHeight(420)

        layout = QVBoxLayout(self)

        # Section title
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            color: #F6645A; 
            font-size: 18px; 
            font-family: 'Source Serif Pro'; 
            font-weight: 600;
            padding: 5px;
            border-bottom: 1px solid #E0E0E0;
        """)

        layout.addWidget(title_label)

        # Content
        if content_widget:
            layout.addWidget(content_widget)

        # Allow for expanding vertically
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


class ImageGallery(QWidget):
    """Widget for displaying and managing images"""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Image display area
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(200, 280)
        self.image_label.setStyleSheet("""
            border: 2px dashed #CCCCCC;
            background-color: white;
            border-radius: 5px;
        """)
        self.image_label.setText("Chưa có hình ảnh")

        # Caption for image
        self.image_caption = QLabel("Hình ảnh demo giao diện")
        self.image_caption.setStyleSheet("""
            color: #3A3A3A; 
            font-size: 12px; 
            font-family: Roboto; 
            font-weight: 400;
            font-style: italic;
        """)
        self.image_caption.setAlignment(Qt.AlignCenter)

        # Image controls
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(10)
        controls_layout.setContentsMargins(0, 8, 0, 0)

        self.prev_image_btn = QPushButton("Trước")
        self.add_image_btn = QPushButton("Thêm ảnh")
        self.next_image_btn = QPushButton("Tiếp")

        for btn in [self.prev_image_btn, self.add_image_btn, self.next_image_btn]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    padding: 6px 12px;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)

        controls_layout.addWidget(self.prev_image_btn)
        controls_layout.addWidget(self.add_image_btn)
        controls_layout.addWidget(self.next_image_btn)

        # Thứ tự thêm các thành phần vào layout chính
        layout.addWidget(self.image_label)
        layout.addWidget(self.image_caption)
        layout.addLayout(controls_layout)  # Thêm controls_layout vào layout chính
        layout.addStretch()

        # Set sample image if available
        try:
            pixmap = QPixmap("resources/demo_image.png")
            if not pixmap.isNull():
                self.set_image(pixmap)
        except:
            pass

    def set_image(self, pixmap):
        """Set image while maintaining aspect ratio"""
        if pixmap:
            scaled_pixmap = pixmap.scaled(
                self.image_label.width(),
                self.image_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)
            self.image_label.setText("")


class EditableInfoField(QWidget):
    """Editable text field with dynamic number of default values"""

    def __init__(self, label_text=None, *default_values):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Label
        label = QLabel(label_text)
        label.setStyleSheet("""
            color: #3A3A3A; 
            font-size: 12px; 
            font-family: Roboto; 
            font-weight: 600;
        """)

        # Value text
        joined_text = "\n".join([str(val) for val in default_values if val])
        self.value_label = QLabel(joined_text)
        self.value_label.setStyleSheet("""
            color: #3A3A3A; 
            font-size: 14px; 
            font-family: Roboto; 
            font-weight: 400;
            padding: 5px;
            background-color: white;
            border: 1px solid #E0E0E0;
            border-radius: 3px;
        """)
        self.value_label.setWordWrap(True)
        self.value_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Edit button
        edit_layout = QHBoxLayout()
        edit_layout.setAlignment(Qt.AlignRight)
        self.edit_btn = QPushButton("Chỉnh sửa")
        self.edit_btn.setFixedWidth(80)
        edit_layout.addWidget(self.edit_btn)

        layout.addWidget(label)
        layout.addWidget(self.value_label)
        layout.addLayout(edit_layout)


class PDFViewer(QWidget):
    def __init__(self, url):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.setMinimumHeight(600)
        self.setMinimumWidth(800)

        response = requests.get(url)
        if response.status_code == 200:
            pdf_data = response.content
            pdf_stream = io.BytesIO(pdf_data)
            self.doc = pymupdf.open(stream=pdf_stream, filetype="pdf")  # ✅ Gán cho self.doc
            print(f"[DEBUG] Tải PDF thành công. Số trang: {len(self.doc)}")


        else:
            print("❌ Không thể tải file PDF.")
            self.doc = None
            return

        self.current_page = 0
        self.layout = QVBoxLayout(self)

        # PDF page display
        self.image_label = QLabel("Đang tải trang...")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        # Navigation buttons
        button_layout = QHBoxLayout()
        self.prev_btn = QPushButton("← Trước")
        self.next_btn = QPushButton("Tiếp →")
        self.prev_btn.clicked.connect(self.show_prev_page)
        self.next_btn.clicked.connect(self.show_next_page)
        button_layout.addWidget(self.prev_btn)
        button_layout.addWidget(self.next_btn)
        self.layout.addLayout(button_layout)

        self.show_page(self.current_page)

    def show_page(self, page_number):
        if self.doc is None or page_number >= len(self.doc):
            return

        page = self.doc.load_page(page_number)
        pix = page.get_pixmap()
        qimage = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap.scaledToWidth(600, Qt.SmoothTransformation))
        self.setMinimumHeight(700)

    def show_next_page(self):
        if self.doc and self.current_page < len(self.doc) - 1:
            self.current_page += 1
            self.show_page(self.current_page)

    def show_prev_page(self):
        if self.doc and self.current_page > 0:
            self.current_page -= 1
            self.show_page(self.current_page)


class AdminInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet(GlobalStyle.global_stylesheet())
        self.setMinimumSize(GlobalStyle.WINDOW_WIDTH, GlobalStyle.WINDOW_HEIGHT)
        self.setMaximumSize(GlobalStyle.WINDOW_WIDTH, GlobalStyle.WINDOW_HEIGHT)

    def initUI(self):
        # A4 portrait dimensions (approximately 210mm x 297mm @ 72dpi)
        self.setMinimumSize(595, 842)  # Size in pixels for A4 at 72dpi

        # Main layout with proper margins for A4 format
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 50, 50, 30)  # Decent margins for A4
        main_layout.setSpacing(20)

        # Header Section
        header_section = QFrame()
        header_section.setStyleSheet("background-color: white;")
        header_layout = QVBoxLayout(header_section)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(5)

        # Title with improved styling
        title_line1 = QLabel("QUẢN LÝ NHÀ TRỌ")
        title_line1.setStyleSheet("""
            color: black; 
            font-size: 40px; 
            font-family: Roboto; 
            font-weight: 700;
        """)
        title_line1.setAlignment(Qt.AlignCenter)

        title_line2 = QLabel("Đồ án tốt nghiệp Đại học")
        title_line2.setStyleSheet("""
            color: #F6645A; 
            font-size: 24px; 
            font-family: 'Source Serif Pro'; 
            font-weight: 600;
        """)
        title_line2.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(title_line1)
        header_layout.addWidget(title_line2)

        # Horizontal rule separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("background-color: #E0E0E0;")
        separator.setFixedHeight(2)

        main_layout.addWidget(header_section)
        main_layout.addWidget(separator)

        # Scrollable content area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: white; }")

        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: white;")
        scroll.setWidget(content_widget)

        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)

        # Content sections
        # Project Info Section
        project_info_text = QLabel(
            "Ứng dụng quản lý nhà trọ giúp các chủ trọ quản lý người thuê, phòng trọ và hóa đơn một cách minh bạch và hiệu quả. "
            "Hệ thống chia theo quyền: admin, chủ trọ, người thuê; mỗi quyền có dashboard và chức năng riêng. "
            "Dự án sử dụng Python + SQL Server, kiến trúc MVC, giao diện bằng PyQt5."
        )
        project_info_text.setWordWrap(True)
        project_info_text.setStyleSheet("""
            color: #3A3A3A; 
            font-size: 14px; 
            font-family: Roboto; 
            line-height: 1.5;
        """)

        # Features list with bullet points
        features_text = QLabel(
            "<ul>"
            "<li>Đăng ký / đăng nhập</li>"
            "<li>Quản lý phòng, hóa đơn, người thuê</li>"
            "<li>Tự động tính tiền điện, nước và xuất hóa đơn</li>"
            "<li>Quản trị tài khoản người dùng (Admin)</li>"
            "<li>Giao diện đẹp, dễ sử dụng và trực quan</li>"
            "</ul>"
        )
        features_text.setTextFormat(Qt.RichText)
        features_text.setStyleSheet("""
            color: #3A3A3A; 
            font-size: 14px; 
            font-family: Roboto; 
            line-height: 1.5;
        """)

        # Combine into a widget
        project_info_widget = QWidget()
        project_info_layout = QVBoxLayout(project_info_widget)
        project_info_layout.addWidget(project_info_text)
        project_info_layout.addWidget(features_text)

        project_section = ContentSection("THÔNG TIN DỰ ÁN", project_info_widget)

        # Student Info Section - Now using editable fields

        student_1 = EditableInfoField("Người thực hiện: ", "Trần Hoàng Phúc", "MSSV: 22730091",
                                      "Vai trò: Frontend - PyQt, OOP")
        student_2 = EditableInfoField("Người thực hiện: ", "Trần Đoàn Quang Hiếu", "MSSV: 22730071",
                                      "Vai trò: Backend - SQL Lite, OOP")

        student_info_widget = QWidget()
        student_info_layout = QVBoxLayout(student_info_widget)
        student_info_layout.setSpacing(4)
        student_info_layout.setContentsMargins(0, 0, 0, 0)

        student_info_layout.addWidget(student_1)
        student_info_layout.addWidget(student_2)

        #student_info_layout.addWidget(student_role)

        student_section = ContentSection("THÔNG TIN SINH VIÊN", student_info_widget)
        #student_section.setMaximumHeight(400)

        # Content layout - Two columns with responsive sizing
        two_col_layout = QHBoxLayout()

        # Giới hạn chiều rộng cột trái
        left_container = QWidget()
        left_container.setFixedWidth(500)
        left_layout = QVBoxLayout(left_container)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(20)

        left_layout.addWidget(project_section)
        left_layout.addWidget(student_section)
        left_layout.addStretch(1)

        right_container = QWidget()
        right_container.setMinimumWidth(600)  # hoặc điều chỉnh theo bố cục
        right_container.setMinimumHeight(700)
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(20)

        gallery = ImageGallery()
        gallery_section = ContentSection("HÌNH ẢNH DEMO", gallery)

        right_layout.addWidget(gallery_section)
        right_layout.addStretch(1)

        # Add columns to layout with proportional sizing
        two_col_layout.addWidget(left_container, alignment=Qt.AlignTop)
        two_col_layout.addWidget(right_container, alignment=Qt.AlignTop)

        content_layout.addLayout(two_col_layout)

        # Space for additional content
        # Space for additional content
        additional_content = ContentSection("NỘI DUNG MỞ RỘNG")

        # Tự động tìm đường dẫn tương đối
        base_dir = os.path.dirname(os.path.abspath(__file__))
        url = "https://drive.google.com/uc?export=download&id=1qT1hUiCRdNECckQShze3cRPb7s6-EYyD"
        pdf_viewer = PDFViewer(url)
        additional_content_layout = QVBoxLayout()
        additional_content_layout.addWidget(pdf_viewer)
        additional_content.setLayout(additional_content_layout)

        # Add spacer at the bottom to push content up
        content_layout.addWidget(additional_content)
        content_layout.addStretch(1)


        main_layout.addWidget(scroll)

        # Footer with page indicator
        footer = QFrame()
        footer.setFixedHeight(40)
        footer.setStyleSheet("background-color: #F6645A; border-radius: 5px;")
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(10, 0, 10, 0)

        # Page indicators
        page_indicator = PageIndicator(3)  # Total 3 pages

        footer_layout.addWidget(page_indicator)

        main_layout.addWidget(footer)

    def resizeEvent(self, event):
        """Handle resize events to maintain A4 proportions"""
        # This keeps the aspect ratio close to A4 when resizing
        super().resizeEvent(event)

    def save_as_pdf(self, filename):
        """Save current view as PDF (A4 format)"""
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        printer.setPageSize(QPrinter.A4)
        printer.setPageMargins(20, 20, 20, 20, QPrinter.Millimeter)

        # Render widget to PDF
        # Implementation would depend on specific requirements

import sys # Import sys for sys.argv and sys.exit

# ... (all your existing class definitions: PageIndicator, ContentSection, ImageGallery, EditableInfoField, AdminInfo) ...

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create a QApplication instance

    # Apply global styles if you want them for this standalone test
    # app.setStyleSheet(GlobalStyle.global_stylesheet()) # Optional: if GlobalStyle is self-contained or you mock it

    window = AdminInfo()
    window.show()
    window.activateWindow()  # Brings the window to the front

    sys.exit(app.exec_())  # Start the application's event loop
