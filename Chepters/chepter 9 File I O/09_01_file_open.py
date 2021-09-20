
# f = open("sample.txt", "r")

# r = reading, w = writing, a = appending, + = updating
# rb = binary mode, rt = text mode

f = open("sample.txt")  # by default mode is = "r" means read

# data = f.read() #this will give all char
data = f.read(5)  # first 5 char of the file
print("\n")

print(data)

print("\n")
print("\n")

f.close()

# file have to be at folder you have choose to open it or it gives error.
