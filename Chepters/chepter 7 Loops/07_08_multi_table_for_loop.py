a = int(input("enter number ="))

i = 0
for i in range(1, 11):

    # print(a, "x", i, "=", i*a)
    # or
    # print(str(a) + "x" + str(i) + "=" + str(i*a))
    # or

    print(f"{a} X  {i} = {a*i}")  # f string; f"" no space
    i = i+1
