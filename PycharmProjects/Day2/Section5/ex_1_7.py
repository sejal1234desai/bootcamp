## Operation: Defaultdict with lambda fallback value

from collections import defaultdict

d = defaultdict(lambda: "N/A")
d["name"] = "Sejal"

print(d["name"])   # Output: Sejal
print(d["email"])  # Output: N/A
