## Operation: Print detailed error trace using traceback.format_exc()

import traceback

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print("An error occurred:", traceback.format_exc())

# Example usage:
divide(5, 0)

# Output:
# An error occurred: Traceback (most recent call last):
#   File "use_traceback_module.py", line 10, in <module>
#     divide(5, 0)
#   File "use_traceback_module.py", line 7, in divide
#     return a / b
# ZeroDivisionError: division by zero
