#4. custom_contextlib_timer

import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed time: {end - start:.4f}s")

with timer():
    sum(i for i in range(1000000))

# Output:
# Elapsed time: X.XXXXs
