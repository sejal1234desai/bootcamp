#variable_positional_args

def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # 10
