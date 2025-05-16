#nonlocal_example

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print("Count:", count)

    inner()

outer()
