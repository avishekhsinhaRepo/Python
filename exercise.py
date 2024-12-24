import csv

with open('C:\\Users\\asinha37\\AviRepo\\Python\\python-exercises\\python-exercies\\resources\\find_the_link.csv',
            encoding='utf-8') as find_the_link:
    data_csv = csv.reader(find_the_link)
    data_lines = list(data_csv)
    link_str = ''
    for index,data in enumerate(data_lines):
        link_str+=data[index]
    print(link_str)
