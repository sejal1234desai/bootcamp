#8
# Operation: Read CSV rows as namedtuples

import csv
from collections import namedtuple

with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    headers = next(reader)
    Row = namedtuple("Row", headers)
    for line in reader:
        row = Row(*line)
        print(row.name, row.age)
# Output: Alice 30, Bob 25
