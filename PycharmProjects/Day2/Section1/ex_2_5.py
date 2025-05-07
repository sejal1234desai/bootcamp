#generator_expression

gen = (n * n for n in range(5))
for val in gen:
    print(val)


#output : 0 1 4 9 16