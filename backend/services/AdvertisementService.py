
from QLNHATRO.RentalManagementApplication.backend.Repository.AdvertisementRepository import AdvertisementRepository
from QLNHATRO.RentalManagementApplication.backend.model.Advertisement import Advertisement


class AdvertisementService:
    @staticmethod
    def create_advertisement(room_name, description, image_path, preferences):
        ad = Advertisement(room_name, description, image_path, preferences)
        AdvertisementRepository.save_advertisement(ad)
        return ad
