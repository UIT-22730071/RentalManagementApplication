
class LoginRepository:


    @staticmethod
    def get_user(username):
        # TODO: Thay thế bằng truy ván SQL thực tế lấy đối tượng user
        print("getuser được gọi")
        # giả lập truy vấn cho ra kết quả

        user_landlord = {'username': 'lanlord', 'password':'lanlord' ,'role': 'landlord','user_id': 1}
        user_tenant = {'username': 'tenant', 'password':'tenant' ,'role': 'tenant','user_id': 2}
        admin_user = {'username': 'admin', 'password':'admin' ,'role': 'admin','user_id': 3}
        #print(" dã lấy được truy vấn" + user_landlord['username'] + user_landlord['password'] + user_landlord['role'])

        if username == 'lanlord':
            return user_landlord
        elif username == 'tenant':
            return user_tenant
        elif username =='admin':
            return admin_user
        else:
            return None


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