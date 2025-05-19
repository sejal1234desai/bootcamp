# 08_skip_attributes_serialize_user.py

import pickle

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password  # Sensitive data
        self.email = email

    def __getstate__(self):
        # Custom serialization: Exclude the password attribute
        state = self.__dict__.copy()
        del state['password']  # Remove sensitive data
        return state

    def __setstate__(self, state):
        # Rebuild the user object from the saved state
        self.__dict__.update(state)

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"

# Create a User instance
user = User(
    username="sejal_desai",
    password="supersecretpassword",
    email="sejal.desai@example.com"
)

# Serialize the User object
with open("user_data.pkl", "wb") as f:
    pickle.dump(user, f)

print("User object serialized successfully without password.")
