# 11_serialize_custom_collection.py

import pickle

class MyCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"MyCollection contains: {self.items}"

    def to_dict(self):
        # Custom method to convert the collection to a dictionary representation
        return {'items': self.items}

    @classmethod
    def from_dict(cls, data):
        # Custom method to recreate the collection from the dictionary
        collection = cls()
        collection.items = data['items']
        return collection

# Create a custom collection and add items
collection = MyCollection()
collection.add_item("Sejal Desai")
collection.add_item("Rahul Patil")
collection.add_item("Amit Jadhav")

# Serialize the custom collection to a file
with open("my_collection.pkl", "wb") as f:
    pickle.dump(collection, f)

print("MyCollection object serialized successfully.")

# Deserialize the custom collection from the file
with open("my_collection.pkl", "rb") as f:
    loaded_collection = pickle.load(f)

print("\nDeserialized collection:")
print(loaded_collection)

