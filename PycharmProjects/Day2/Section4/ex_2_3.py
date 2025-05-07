#3  timer_decorator

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_add(x, y):
    time.sleep(1)
    return x + y

slow_add(5, 10)
