#3
# Operation: Read a CSV file using csv.DictReader

import csv

with open("data.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
# Output:
# {'name': 'Alice', 'age': '30'}
# {'name': 'Bob', 'age': '25'}
