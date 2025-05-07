#dict_access


user = {"name": "Alice"}
print(user.get("age"))  # None
print(user.setdefault("age", 25))  # Adds 'age': 25
print(user)
