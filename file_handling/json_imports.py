import json

with open("friends.json", "r") as json_file:
    json_data = json.load(json_file)

print(type(json_data))
print("Json Data :\n", json_data)
# Extracting data from json
print("[friends][0][\"name\"]:", json_data["friends"][0]["name"])

#Looping
friend_list = json_data["friends"]
for friend in friend_list:
    print(f"Friend is {friend['name']} and age is {friend['age']}")

# cars dictionary
cars = [
    {"name": "Audi", "price": 10000},
    {"name": "BMW", "price": 20000},
    {"name": "Mercedes", "price": 30000}
]

with open("cars.json", "w") as file:
    file.write(json.dumps(cars))

json_str = '[{"name": "Audi", "price": 10000}, {"name": "BMW", "price": 20000}, {"name": "Mercedes", "price": 30000}]'
json_cars = json.loads(json_str)
print(type(json_cars))
print(type(json_cars[0]))
print("Car Name:",json_cars[0]["name"])
