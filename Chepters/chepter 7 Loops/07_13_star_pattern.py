print("\n")
# n = 4

for i in range(3):
    print("*" * (i+1))


n = 3

print("\n")
print("*************************************************")
print("\n")

for j in range(3):
    # ..*..
    # .***.
    # *****
    # n j
    # 3 0 -1 . 3 1 -1 . 3 2 -1  === n-j-1 (obvious)
    # 3 0 -2 . 3 1 -1 . 3 2  0  === 2*j+1 (we need 1,3,5 so odd equation)
    # 3 0 -1 . 3 1 -1 . 3 2 -1  === n-j-1

    # print(" " * (2))
    # print("*" * (1))
    # print(" " * (2))

    # print(" " * (1))
    # print("*" * (3))
    # print(" " * (1))

    # print(" " * (0))
    # print("*" * (5))
    # print(" " * (0))

    # end --> to give space at the end; see 08_05.py
    print(" "*(n-j-1), end=" ")
    print("*"*(2*j+1), end=" ")
    print(" "*(n-j-1))

print("\n")
print("*************************************************")
print("\n")

# ***
# **
# *


a = 3

for a1 in range(a):
    print("*" * (a-a1))


print("\n")
print("*************************************************")
print("\n")

# * * *
# *   *
# * * *

# m = 3
# for k in range(3):
#     print("*" * (m))


# print("\n")
# WRONG PROGRAM
