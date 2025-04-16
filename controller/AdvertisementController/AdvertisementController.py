from QLNHATRO.RentalManagementApplication.backend.services.AdvertisementService import AdvertisementService

class AdvertisementController:
    @staticmethod
    def handle_submit_ad(room_name, description, image_path, preferences, view):
        if not room_name or not description:
            view.show_error("Phòng và mô tả không được để trống!")
            return

        AdvertisementService.create_advertisement(room_name, description, image_path, preferences)
        view.show_success("🎉 Quảng cáo phòng trọ đã được đăng!")
