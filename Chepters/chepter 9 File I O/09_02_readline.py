print("\n")

f = open("sample.txt", "r")
data = f.readline()  # every readline will print a line
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)

print("\n")

f.close()
