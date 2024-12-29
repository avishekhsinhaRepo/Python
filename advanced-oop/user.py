from save import Savable


class User(Savable):
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
