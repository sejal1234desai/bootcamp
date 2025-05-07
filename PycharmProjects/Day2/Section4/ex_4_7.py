#7
# Operation: Group dicts by key using itertools.groupby()

from itertools import groupby
from operator import itemgetter

records = [
    {"dept": "IT", "name": "Sejal"},
    {"dept": "HR", "name": "Amit"},
    {"dept": "IT", "name": "Priya"},
    {"dept": "HR", "name": "Ravi"},
]

# Grouping needs to be sorted by key first
records.sort(key=itemgetter("dept"))

grouped = groupby(records, key=itemgetter("dept"))

for dept, group in grouped:
    print(dept, list(group))
# Output:
# HR [{'dept': 'HR', 'name': 'Amit'}, {'dept': 'HR', 'name': 'Ravi'}]
# IT [{'dept': 'IT', 'name': 'Sejal'}, {'dept': 'IT', 'name': 'Priya'}]
