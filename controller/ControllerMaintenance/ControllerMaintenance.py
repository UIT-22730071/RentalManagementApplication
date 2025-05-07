import os
import shutil
from PyQt5.QtGui import QPixmap
from QLNHATRO.RentalManagementApplication.services.MaintenanceService import MaintenanceService


class ControllerMaintenance:

    @staticmethod
    def save_uploaded_image(file_path):
        """
        Sao chép ảnh đã chọn vào thư mục nội bộ và trả về đường dẫn mới.
        """
        save_folder = "uploaded_images"
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        filename = os.path.basename(file_path)
        save_path = os.path.join(save_folder, filename)
        shutil.copy(file_path, save_path)

        return save_path

    @staticmethod
    def handle_maintenance_submission(request_data):
        """
        Gửi yêu cầu sửa chữa bằng Service.
        """
        try:
            MaintenanceService.create_request(
                room_id=request_data['room_id'],
                tenant_id=request_data['tenant_id'],
                description=request_data['description'],
                image_path=request_data['image_path']
            )
            return True, "Gửi yêu cầu thành công!"
        except Exception as e:
            return False, f"Lỗi khi gửi yêu cầu: {str(e)}"
