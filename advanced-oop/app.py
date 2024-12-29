from admin import Admin
from database import Database

admin1 = Admin(user_name='Alex', user_password='1234', access_level=1)
admin2 = Admin(user_name='Anna', user_password='5678', access_level=2)

admin1.save()
admin2.save()

find_user= lambda user:  user['user_name'] == 'Alex'
user = Database.find(find_user)
print(user)
Database.remove(find_user)
user = Database.find(find_user)
print(user)
