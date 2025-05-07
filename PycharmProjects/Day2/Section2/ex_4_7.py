#7. db_style_lock

class DBConnection:
    def __enter__(self):
        print("DB connected")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("DB disconnected")

with DBConnection():
    print("Running query...")

# Output:
# DB connected
# Running query...
# DB disconnected
