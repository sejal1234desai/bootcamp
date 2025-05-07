#nested_try

try:
    print("Outer try")
    try:
        print("Inner try")
        x = 1 / 0
    except ZeroDivisionError:
        print("Handled ZeroDivisionError in inner block")
except Exception as e:
    print("Outer Exception:", e)

# Output:
# Outer try
# Inner try
# Handled ZeroDivisionError in inner block
