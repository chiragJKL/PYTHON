# username length have less than 10 char or not

name = input("enter username : ")

if (len(name) > 10):
    print("username is INVALID because it have", len(name), "characters!!")
else:
    print("correct!!")
