class User:
    def __init__(self, username, password, role, user_id=None):
        self.__username = username
        self.__password = password
        #self.__role = Role(role)
        self.__user_id = user_id  # Lưu UserID sau khi tạo tài khoản


    # hàm này Staticmethod vì nó check 2 giá trị có gióng nhau hay không thoi chứ không updata

def check_password_not_equal(password_input, confirm_password_input):
    if password_input == confirm_password_input:
        return True
    else:
        return False


