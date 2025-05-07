#List Comprehension with Condition

nums = [1, 2, 3, 4]
result = [n**2 for n in nums if n % 2 == 0]  #[4,16]
print(result)
# [4, 16]
