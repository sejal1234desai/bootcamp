#7. and_guarded_expression

is_admin = True

def delete_user(uid):
    print(f"User {uid} deleted.")

user_id = 42
is_admin and delete_user(user_id)

# Output:
# User 42 deleted.
