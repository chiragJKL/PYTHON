with open("log.txt") as f:
    a = f.read().lower()

if "python" in a:  # or a.lower()
    print("python is present")  # in the 10th line
else:
    print("python is not")
