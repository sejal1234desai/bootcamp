# 10_versioned_object_handling.py

import pickle

class PersonV1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"PersonV1: {self.name}, Age: {self.age}"

    def to_dict(self):
        return {'name': self.name, 'age': self.age}


class PersonV2:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email  # New field added in V2

    def __str__(self):
        return f"PersonV2: {self.name}, Age: {self.age}, Email: {self.email}"

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'email': self.email}


def save_person(person, filename):
    with open(filename, 'wb') as f:
        pickle.dump(person, f)
    print(f"{type(person).__name__} object serialized successfully.")


def load_person(filename):
    with open(filename, 'rb') as f:
        person = pickle.load(f)
        if isinstance(person, PersonV1):
            print("Deserialized PersonV1 object")
            # Assign your email when upgrading from PersonV1 to PersonV2
            return PersonV2(person.name, person.age, "sejaldesai2001@gmail.com")
        return person


# Create and serialize a PersonV1 object
person_v1 = PersonV1(name="Sejal Desai", age=25)
save_person(person_v1, "person_v1.pkl")

# Load the PersonV1 object, which will be upgraded to PersonV2
person_v2 = load_person("person_v1.pkl")
print(person_v2)
