from os import replace


with open("sample4.txt", "r") as f:
    a = f.read()
    # d = "donkey"
    # d.upper() = d.lower() #convert all upper and lower

a = a.replace("donkey", "######")

with open("sample4.txt", "w") as f:
    f.write(a)
