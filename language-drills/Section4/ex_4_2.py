#
# Operation: Cycle through colors using itertools.cycle()

import itertools

colors = itertools.cycle(["red", "green", "blue"])

for _ in range(6):
    print(next(colors))  # Output: red, green, blue, red, green, blue
