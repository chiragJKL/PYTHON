

cusswords = ["donkey", "is", "has"]

with open("sample4.txt", "r") as f:
    a = f.read()
    # d = "donkey"
    # d.upper() = d.lower() #convert all upper and lower

for word in cusswords:
    a = a.replace(word, "######")
    with open("sample4.txt", "w") as f:
        f.write(a)
