#5. lbyl_race_condition

import os

filename = "temp.txt"
if os.path.exists(filename):
    # Another process might delete the file now
    with open(filename) as f:
        print(f.read())
else:
    print("File does not exist.")

# This illustrates potential race conditions in LBYL.
