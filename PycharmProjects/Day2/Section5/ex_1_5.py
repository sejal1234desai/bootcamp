## Operation: Rotate a deque

from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)

print(dq)
# Output: deque([4, 5, 1, 2, 3])
