#
# Operation: Pretty-print JSON with sorted keys and indentation

import json

person = {"age": 25, "name": "Sejal", "skills": ["Python", "Django"]}
pretty = json.dumps(person, indent=4, sort_keys=True)
print("Pretty JSON:\n", pretty)
# Output:
# {
#     "age": 25,
#     "name": "Sejal",
#     "skills": [
#         "Python",
#         "Django"
#     ]
# }
