import csv
csv_columns = ['No','Name','Country']
dict_data = [
{'No': 1, 'Name': 'Abhilash', 'Country': 'India'},
{'No': 2, 'Name': 'Amjiyad', 'Country': 'USA'},
{'No': 3, 'Name': 'Nihal', 'Country': 'Newyork'},
{'No': 4, 'Name': 'Nithin Raj', 'Country': 'Canada'},
{'No': 5, 'Name': 'Shad', 'Country': 'Australia'},
]
csv_file = "names.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)


with open('names.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
