# Operation: Compare recursive Fibonacci with and without lru_cache

import time
from functools import lru_cache

def plain_fib(n):
    if n < 2:
        return n
    return plain_fib(n-1) + plain_fib(n-2)

@lru_cache(maxsize=None)
def cached_fib(n):
    if n < 2:
        return n
    return cached_fib(n-1) + cached_fib(n-2)

start = time.time()
plain_fib(30)
print(f"Without cache: {time.time() - start:.2f}s")  # ~0.3s+

start = time.time()
cached_fib(30)
print(f"With cache: {time.time() - start:.6f}s")     # ~0.00001s
