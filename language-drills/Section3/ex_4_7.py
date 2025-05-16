#7. field_rename

from collections import namedtuple

Person = namedtuple("Person", ["name", "class"], rename=True)
p = Person("Sejal", "X")
print(p)

# Output:
# Person(name='Sejal', _1='X')
