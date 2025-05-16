## Operation: Field with Default Factory

from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    age: int
    tags: List[str] = field(default_factory=list)

u = User("Sejal", 22)
print("Tags:", u.tags)
# Output: Tags: []
