# 12_serialize_cyclic_references.py

import pickle

class Person:
    def __init__(self, name):
        self.name = name
        self.friend = None  # Will reference another Person object

    def __str__(self):
        return f"Person({self.name})"

    def set_friend(self, friend):
        self.friend = friend

# Create two Person objects
person1 = Person("Sejal Desai")
person2 = Person("Rahul Patil")

# Create a cyclic reference
person1.set_friend(person2)
person2.set_friend(person1)

# Serialize the objects with cyclic references
with open("person_with_cycle.pkl", "wb") as f:
    pickle.dump(person1, f)

print("Objects with cyclic references serialized successfully.")

# Deserialize the objects back from the file
with open("person_with_cycle.pkl", "rb") as f:
    loaded_person1 = pickle.load(f)

print("\nDeserialized person with cyclic references:")
print(loaded_person1)
print(f"{loaded_person1.name}'s friend is: {loaded_person1.friend.name}")
