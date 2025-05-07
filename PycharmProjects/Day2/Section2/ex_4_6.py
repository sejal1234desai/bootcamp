#6. tempfile_usage

import tempfile

with tempfile.TemporaryFile(mode="w+") as tf:
    tf.write("Temporary data")
    tf.seek(0)
    print("Read from tempfile:", tf.read())

# Output:
# Read from tempfile: Temporary data
