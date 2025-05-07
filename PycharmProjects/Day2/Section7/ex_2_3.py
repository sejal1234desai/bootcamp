#3
# Operation: Lazy filter for CSV rows based on a condition using a generator

import csv

def filter_csv_rows(file_path, condition):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if condition(row):
                yield row

# Example usage: Filter rows where age is greater than 30
for row in filter_csv_rows('data.csv', lambda x: int(x['age']) > 30):
    print(row)

# Output:
# Only rows meeting the condition (age > 30) will be processed lazily.
