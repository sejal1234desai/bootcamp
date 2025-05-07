# Operation: Use lru_cache to memoize recursive Fibonacci

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    # Simple recursive fib with caching
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))  # Output: 832040
