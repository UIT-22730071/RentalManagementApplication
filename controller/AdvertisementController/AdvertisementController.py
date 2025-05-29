from QLNHATRO.RentalManagementApplication.services.AdvertisementService import AdvertisementService

class AdvertisementController:
    @staticmethod
    def handle_submit_ad(room_name, description, image_path, preferences, view,RoomID):
        if not room_name or not description:
            view.show_error("Phòng và mô tả không được để trống!")
            return

        AdvertisementService.create_advertisement(room_name, description, image_path, preferences,RoomID)
        view.show_success("🎉 Quảng cáo phòng trọ đã được đăng!")
