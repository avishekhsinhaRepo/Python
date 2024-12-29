from user import User
from save import Savable


class Admin(User, Savable):
    def __init__(self, user_name, user_password, access_level):
        super().__init__(user_name, user_password)
        self.access_level = access_level

    def __repr__(self):
        return f'<Admin {self.user_name}, access level {self.access_level}>'

    def to_dict(self):
        return {
            'user_name': self.user_name,
            'user_password': self.user_password,
            'access_level': self.access_level
        }
