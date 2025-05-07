#
# Operation: Generate IDs using itertools.count()

import itertools

id_gen = itertools.count(start=1001)

for _ in range(5):
    print(next(id_gen))  # Output: 1001, 1002, 1003, 1004, 1005
