from QLNHATRO.RentalManagementApplication.backend.model.Advertisement import Advertisement


class AdvertisementRepository:
    @staticmethod
    def save_advertisement(ad: Advertisement):
        # TODO: Replace with actual SQL insert
        print("[DEBUG] Lưu quảng cáo vào DB:")
        print("Phòng:", ad.room_name)
        print("Mô tả:", ad.description)
        print("Hình ảnh:", ad.image_path)
        print("Ưu tiên:", ad.preferences)

        # Ví dụ: dùng SQLAlchemy / sqlite3 để lưu vào bảng Advertisements
