## Operation: Nested defaultdict for hierarchical data

from collections import defaultdict

nested = defaultdict(lambda: defaultdict(int))
nested["user1"]["likes"] += 1
nested["user1"]["comments"] += 3
nested["user2"]["likes"] += 2

print(dict(nested))
# Output: {'user1': {'likes': 1, 'comments': 3}, 'user2': {'likes': 2}}
