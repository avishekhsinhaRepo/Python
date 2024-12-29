from database import Database


class Savable:

    def save(self):
        Database.insert(self.to_dict())

