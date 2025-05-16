#mixed_args

def mix_args(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

mix_args(1, 2, 3, a="x", b="y")
