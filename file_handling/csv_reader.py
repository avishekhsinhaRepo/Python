import csv

data = open("example.csv","r", encoding="utf-8")
data_csv = csv.reader(data)


data_lines = list(data_csv)

for data_line in data_lines[1:]:
    print(data_line)