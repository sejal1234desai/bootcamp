#8. boolean_check

class Response:
    def __init__(self, status):
        self.status = status

    def __bool__(self):
        return self.status == "success"

resp = Response("success")
if resp:
    print("It worked!")
else:
    print("It failed.")

# Output:
# It worked!
