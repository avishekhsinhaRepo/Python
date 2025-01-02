import json
import csv

csv_file = open("csv_file.txt", 'r')
csv_reader = csv.reader(csv_file)
csv_data = list(csv_reader)
csv_file.close()

# print(csv_data)

club = []
for data in csv_data:
    club.append({"club": data[0], "city": data[1], "country": data[2]})

print(club)

json_file = open("json_file.txt", 'w')
json_file.write(json.dumps(club))
json_file.close()
