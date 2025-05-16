## Operation: Use deque to simulate stack and queue

from collections import deque

dq = deque()

# Stack behavior
dq.append(10)
dq.append(20)
print(dq.pop())  # Output: 20

# Queue behavior
dq.appendleft(30)
print(dq.pop())  # Output: 10
