file = True
i = 1

with open("log.txt") as f:
    while file:
        file = f.readline().lower()

        if "python" in file:
            print(f"python is present in line no. = {i}")
        i += 1
