#7. retry_decorator

def retry(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            print("All attempts failed.")
        return wrapper
    return decorator

@retry(3)
def unstable():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    print("Succeeded!")

unstable()
