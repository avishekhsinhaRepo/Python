import csv

# Open the file
data = open('C:\\Users\\asinha37\\AviRepo\\Python\\python-exercises\\python-exercies\\resources\\example.csv',
            encoding='utf-8')

# Call csv.reader
data_csv = csv.reader(data)

# reformat it to python object i.e list of list
data_lines = list(data_csv)


list_of_full_name=[];
for data_line in data_lines[1:]:
    list_of_full_name.append(data_line[1]+" "+ data_line[2])

# Writing to file in csv format
file_to_output = open('C:\\Users\\asinha37\\AviRepo\\Python\\python-exercises\\python-exercies\\resources\\full_name.csv', mode="w", newline= '')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['Full Name'])
for full_name in list_of_full_name:
    csv_writer.writerow([full_name])
