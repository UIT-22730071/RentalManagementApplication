class LanlordRepository:
    @staticmethod
    def get_all_landlords():
        #TODO: Tao truy vấn SLQ select * from landlords
        landlords = [
            {
                'id': 'L001',
                'ho_ten': 'Nguyễn Văn A',
                'cccd': '012345678901',
                'sdt': '0901234567',
                'email': 'nguyenvana@email.com',
                'so_phong': 2
            },
            {
                'id': 'L002',
                'ho_ten': 'Trần Thị B',
                'cccd': '098765432109',
                'sdt': '0909876543',
                'email': 'tranthib@email.com',
                'so_phong': 1
            }
        ]
        return landlords

    @staticmethod
    def get_id_landlord_from_user_id(user_id):
        #TODO: Tao truy vấn SLQ select landlord_id from landlords where user_id = ?
        user_id = '2'
        return user_id
