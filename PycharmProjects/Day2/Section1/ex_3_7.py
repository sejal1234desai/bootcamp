#keyword_only_args

def configure(*, theme, layout):
    print(f"Theme: {theme}, Layout: {layout}")

configure(theme="dark", layout="grid")
# configure("dark", "grid")  # This will raise a TypeError
