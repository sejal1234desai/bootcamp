#6.role_required

def role_required(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("role") == required_role:
                return func(user, *args, **kwargs)
            else:
                print("Access denied.")
        return wrapper
    return decorator

@role_required("admin")
def delete_user(user, username):
    print(f"{username} deleted by {user['name']}")

admin_user = {"name": "Sejal", "role": "admin"}
guest_user = {"name": "Guest", "role": "viewer"}

delete_user(admin_user, "john")
delete_user(guest_user, "john")
