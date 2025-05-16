#list_vs_generator

import sys

lst = [x for x in range(1000000)]
gen = (x for x in range(1000000))

print("List size:", sys.getsizeof(lst))
print("Generator size:", sys.getsizeof(gen))
