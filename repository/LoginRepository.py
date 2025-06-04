from QLNHATRO.RentalManagementApplication.Repository.UserRepository import UserRepository
from QLNHATRO.RentalManagementApplication.backend.database.Database import Database


db = Database()
class LoginRepository:


    @staticmethod
    def get_user(username):
        return UserRepository.get_user_by_username(username)

    @staticmethod
    def get_role_from_username(username):
        # TODO: Thay thế bằng truy ván SQL thực tế
        # giả lập truy vấn cho ra kết quả

        role = 'landlord'
        return role

    @staticmethod
    def get_role_from_user_id(user_id):
        # TODO: Thay thế bằng truy ván SQL thực tế
        role = 'landlord'
        return role

    @staticmethod
    def create_new_user_name(user):
        # user = [username, password, role]
        #TODO: Tạo truy vấn dữ liêu tạo mới user name theo role

        return True

    @staticmethod
    def update_user_info(user_id, data):
        # TODO: Thực hiện truy vấn UPDATE SQL
        print(f"[DB] Đã cập nhật user_id={user_id} với data={data}")

    @staticmethod
    def get_user_id_from_username(username):
        # TODO: Tạo truy vấn SQL để get user_id
        user_id = "01"
        return user_id
    @staticmethod
    def change_password_into_database(username,password):
        #TODO: Tạo truy vấn upate cho table user để cập nhật CSDL thay đoi9r mật khẩu
        print("mật khẩu đã được thay đổi")


    @staticmethod
    def get_sdt_from_username(username):
        #TODO: trả về sdt user
        sdt = '0325575333'
        return sdt

    @staticmethod
    def get_email_from_username(username):
        #TODO: trả về email sử dụng cảu username
        email = 'khonglamthi0diemr@gmail.com'
        return email

    @staticmethod
    def is_username_exists(username: str) -> bool:
        #TODOL Tạo try vấn trả về sự tồn tại cúa username
        # Trả về True nếu username tồn tại trong bảng Users
        is_exist = True
        return is_exist
