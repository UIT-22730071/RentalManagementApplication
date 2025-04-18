
class LoginRepository:


    @staticmethod
    def get_user(username):
        # TODO: Thay thế bằng truy ván SQL thực tế lấy đối tượng user
        print("getuser được gọi")
        # giả lập truy vấn cho ra kết quả
        username = 'admin'
        user = {'username': 'admin', 'password':'admin' ,'role': 'landlord','user_id': 1}
        print(" dã lấy được truy vấn" + user['username'] + user['password'] + user['role'])
        return user

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
