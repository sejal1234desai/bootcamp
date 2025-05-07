# Operation: Use partial to create nested defaultdict

from collections import defaultdict
from functools import partial

# Create a recursive nested defaultdict
nested_dict = partial(defaultdict, lambda: "default_value")

my_dict = defaultdict(nested_dict)
my_dict['user']['info'] = "Sejal"

print(my_dict['user']['info'])     # Output: Sejal
print(my_dict['missing']['value']) # Output: default_value
