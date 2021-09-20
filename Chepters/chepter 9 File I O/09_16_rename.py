
# here google module to remove file

# ****** here programme is not directly renaming but delecting old file and created same with new name!!!

import os

oldname = "old.txt"
newname = "renamed_in_python.txt"

with open(oldname) as f:
    file = f.read()

with open(newname, "w") as f:
    f.write(file)

os.remove(oldname)
