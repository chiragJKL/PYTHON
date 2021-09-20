f = open("poem.txt", "r")
t = f.read()

if "twinkle" in t:
    print("twinkle word is here")
else:
    print("its not here")
