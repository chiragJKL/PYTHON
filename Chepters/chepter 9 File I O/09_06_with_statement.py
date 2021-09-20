
# WITH STATEMENT : best way to open and close file automatically

with open("sample3.txt", "r") as f:
    a = f.read()
    print(a)

with open("sample3.txt", "w") as f:
    a = f.write("me")
