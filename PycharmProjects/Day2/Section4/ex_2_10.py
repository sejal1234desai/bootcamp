#10. decorator_composition

from time import sleep

def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("[Logger] Start")
        result = func(*args, **kwargs)
        print("[Logger] End")
        return result
    return wrapper

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[Timer] Took {end - start:.2f}s")
        return result
    return wrapper

def debug_info(func):
    def wrapper(*args, **kwargs):
        print(f"[Debug] Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"[Debug] {func.__name__} returned {result}")
        return result
    return wrapper

@simple_logger
@timer
@debug_info
def process_data(x):
    sleep(1)
    return x * 2

process_data(10)
