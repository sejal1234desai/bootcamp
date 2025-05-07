#conditional_assignment_comprehension

nums = [1, -2, 3, -4]
fixed = [x if x > 0 else 0 for x in nums]
print(fixed)  # [1, 0, 3, 0]
