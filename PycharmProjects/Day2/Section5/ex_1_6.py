## Operation: Preserve insertion order using OrderedDict

from collections import OrderedDict

od = OrderedDict()
od["name"] = "Sejal"
od["age"] = 24
od["role"] = "Developer"

for key, value in od.items():
    print(key, value)
# Output:
# name Sejal
# age 24
# role Developer
