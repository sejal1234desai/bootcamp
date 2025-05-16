#5
# Operation: Create a temporary file and write content

import tempfile

with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
    temp.write("Temporary data")
    temp.seek(0)
    print(temp.read())
# Output: Temporary data
