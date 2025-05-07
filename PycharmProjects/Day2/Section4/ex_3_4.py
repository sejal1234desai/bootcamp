# Operation: Create customized print function using chained partials

from functools import partial

# First partial to always print with sep=" - "
custom_print = partial(print, sep=" - ")

# Then, create another partial to add end="\n\n"
fancy_print = partial(custom_print, end="\n\n")

fancy_print("Hello", "Sejal", "Desai")
# Output:
# Hello - Sejal - Desai
#
