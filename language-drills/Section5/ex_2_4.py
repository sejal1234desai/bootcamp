#4
# Operation: Create and delete directory using os & shutil

import os
import shutil
import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    nested_dir = os.path.join(temp_dir, "subfolder")
    os.makedirs(nested_dir)
    print(os.path.exists(nested_dir))  # Output: True

    shutil.rmtree(nested_dir)
    print(os.path.exists(nested_dir))  # Output: False
