from QLNHATRO.RentalManagementApplication.backend.model.Advertisement import Advertisement


class AdvertisementRepository:
    @staticmethod
    def save_advertisement(ad: Advertisement,RoomID):
        # TODO: Replace with actual SQL insert

        print("[DEBUG] Lưu quảng cáo vào DB:")
        print("Phòng:", ad.room_name)
        print("Mô tả:", ad.description)
        print("Hình ảnh:", ad.image_path)
        print("Ưu tiên:", ad.preferences)

        # Ví dụ: dùng SQLAlchemy / sqlite3 để lưu vào bảng Advertisements
    @staticmethod
    def get_all_advertisements():
        all_data_ad ={}

        return all_data_ad

    @staticmethod
    def get_all_advertised_rooms():
        data = [
            {
                "id": 1,
                "room_name": "Phòng 101",
                "address": "123 Đường ABC, Q.1, TP.HCM",
                "price": "3.000.000 VNĐ",
                "description": "Phòng rộng rãi, thoáng mát, gần trung tâm.",
                "preferences": ["Sinh viên nữ", "Không hút thuốc"]
            },
            {
                "id": 2,
                "room_name": "Phòng 202",
                "address": "456 Đường XYZ, Q.Bình Thạnh",
                "price": "2.500.000 VNĐ",
                "description": "Gần chợ, trường học, an ninh tốt.",
                "preferences": ["Nam độc thân", "Ưu tiên ở lâu dài"]
            },
            {
                "id": 3,
                "room_name": "Phòng 303",
                "address": "789 Đường DEF, Q.Thủ Đức",
                "price": "2.800.000 VNĐ",
                "description": "Có máy lạnh, wifi, chỗ để xe miễn phí.",
                "preferences": []
            }
        ]
        return data

