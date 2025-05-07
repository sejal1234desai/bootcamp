#3. stop_iteration

def limited():
    yield 1
    raise StopIteration("End of generator")

gen = limited()
try:
    print(next(gen))  # Output: 1
    print(next(gen))
except StopIteration as e:
    print("Caught StopIteration:", e)

# Output:
# 1
# Caught StopIteration: End of generator
