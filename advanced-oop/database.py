class Database:
    content = {'users': []}

    @classmethod
    def insert(cls, user):
        cls.content["users"].append(user)

    @classmethod
    def remove(cls, finder):
        cls.content["users"] = [usr for usr in cls.content["users"] if not finder(usr)]

    @classmethod
    def find(cls, finder):
        found_users = [usr for usr in cls.content["users"] if finder(usr)]
        if found_users:
            return found_users[0]
        return None
