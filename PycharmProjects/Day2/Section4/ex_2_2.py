#2 prefix_printer

def prefix_printer(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@prefix_printer(">>> Running:")
def say_hi():
    print("Hi!")

say_hi()
