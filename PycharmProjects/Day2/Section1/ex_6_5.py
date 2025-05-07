#5. generator_state

def running_total(lst):
    total = 0
    for num in lst:
        total += num
        yield total

for t in running_total([1, 2, 3]):
    print(t)

# Output:
# 1
# 3
# 6
