#6. namedtuple_basics

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)

# Output:
# 1 2
