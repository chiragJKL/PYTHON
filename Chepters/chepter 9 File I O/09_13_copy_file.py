with open("original.txt") as f:
    file = f.read()

with open("copy.txt", "w") as f:
    f.write(file)
