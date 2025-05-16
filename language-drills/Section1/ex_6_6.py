#6. send_generator

def echo():
    while True:
        x = yield
        print("Received:", x)

gen = echo()
next(gen)          # Start generator
gen.send("Hello")  # Output: Received: Hello
gen.send(42)       # Output: Received: 42
