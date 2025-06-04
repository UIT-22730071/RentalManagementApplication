
class User:
    def __init__(self, username, password, role, user_id=None, is_active=0):
        self.username = username
        self.password = password
        self.role = role
        self.user_id = user_id
        self.is_active = is_active

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "user_id": self.user_id,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data.get("username"),
            password=data.get("password"),
            role=data.get("role"),
            user_id=data.get("user_id"),
            is_active=data.get("is_active", 0)
        )

