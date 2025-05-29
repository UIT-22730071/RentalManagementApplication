from QLNHATRO.RentalManagementApplication.Repository.AdvertisementRepository import AdvertisementRepository
from QLNHATRO.RentalManagementApplication.Repository.RoomRepository import RoomRepository
from QLNHATRO.RentalManagementApplication.backend.model.Advertisement import Advertisement


class AdvertisementService:
    @staticmethod
    def create_advertisement(room_name, description, image_path, preferences,RoomID):
        ad = Advertisement(room_name, description, image_path, preferences)
        AdvertisementRepository.save_advertisement(ad,RoomID)
        return ad

    @staticmethod
    def get_all_advertised_rooms_for_view():
        rooms = RoomRepository.get_all_rooms()
        ads = AdvertisementRepository.get_all_advertisements()

        data = []
        for idx, ad in enumerate(ads, 1):
            matched_room = next((r for r in rooms if r["ten_phong"] == ad.room_name), None)
            if matched_room:
                data.append({
                    "STT": idx,
                    "Tên chủ trọ": "Nguyễn Văn A",  # TODO: match từ `room['landlord_id']`
                    "Diện tích phòng": f"{matched_room['dien_tich']} m²",
                    "Giá phòng": f"{matched_room['gia_phong']:,} VNĐ",
                    "Ưu tiên": ", ".join(ad.preferences),
                    "id_room": matched_room["id"]
                })

        return data
