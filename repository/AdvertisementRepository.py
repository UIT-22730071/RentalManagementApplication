from QLNHATRO.RentalManagementApplication.backend.database.Database import Database
from QLNHATRO.RentalManagementApplication.backend.model.Advertisement import Advertisement


class AdvertisementRepository:
    @staticmethod
    def save_advertisement(ad: Advertisement, room_id):
        db = Database()
        db.connect()
        query = """
                INSERT INTO Advertisements (RoomID, Description, Priority, ImagePath, CreatedAt)
                VALUES (?, ?, ?, ?, ?) \
                """
        params = (room_id, ad.description, ad.priority, ad.image_path, ad.created_at)
        result = db.execute(query, params)
        db.close()
        return result is not None

        # Ví dụ: dùng SQLAlchemy / sqlite3 để lưu vào bảng Advertisements
    @staticmethod
    def get_all_advertisements():
        all_data_ad ={}

        return all_data_ad

    @staticmethod
    def get_all_advertised_rooms():
        db = Database()
        db.connect()
        query = "SELECT * FROM Advertisements"
        cursor = db.execute(query)
        ads = []
        if cursor:
            rows = db.fetchall()
            for row in rows:
                ad_data = {
                    'ad_id': row['AdID'],
                    'RoomID': row['RoomID'],
                    'description': row['Description'],
                    'priority': row['Priority'],
                    'image_path': row['ImagePath'],
                    'created_at': row['CreatedAt']
                }
                ads.append(Advertisement(ad_data))
        db.close()
        if ads is None:
            ads = [
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
        return ads


