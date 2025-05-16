#finally_block

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide")
finally:
    print("Cleanup done")

# Output:
# Cannot divide
# Cleanup done
