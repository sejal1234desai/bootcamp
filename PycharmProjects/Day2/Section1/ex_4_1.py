#LEGB Rule

x = 10  # Global

def show():
    x = 20  # Local
    print("Inside function:", x)

show()
print("Outside function:", x)
