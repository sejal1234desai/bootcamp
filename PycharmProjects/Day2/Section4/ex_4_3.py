#3
# Operation: Use repeat to generate a list of Nones

import itertools

none_list = list(itertools.repeat(None, 10))

print(none_list)  # Output: [None, None, None, None, None, None, None, None, None, None]
