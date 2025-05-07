#4
# Operation: Flatten nested lists using itertools.chain()

import itertools

nested = [[1, 2], [3, 4], [5]]
flat = list(itertools.chain(*nested))

print(flat)  # Output: [1, 2, 3, 4, 5]
