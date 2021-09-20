file1 = "copy.txt"
file2 = "original.txt"

with open("copy.txt") as f:
    file1 = f.read()
with open("original.txt") as f:
    file2 = f.read()

if file1 == file2:
    print("files are same")
else:
    print("files are NOT same")
