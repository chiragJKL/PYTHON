a1 = int(input("enter 1st num : "))
a2 = int(input("enter 2nd num : "))
a3 = int(input("enter 3rd num : "))
a4 = int(input("enter 4th num : "))

if(a1 > a2 and a1 > a3 and a1 > a4):
    print(a1, " is greatest")
elif(a2 > a1 and a2 > a3 and a2 > a4):
    print(a2, " is greatest")
elif(a3 > a2 and a3 > a1 and a3 > a4):
    print(a3, " is greatest")
elif(a4 > a2 and a4 > a3 and a4 > a1):
    print(a4, " is greatest")

# OR

# **********************************************************

b1 = int(input("enter 1st num : "))
b2 = int(input("enter 2nd num : "))
b3 = int(input("enter 3rd num : "))
b4 = int(input("enter 4th num : "))

if (b1 > b4):
    x1 = b1
else:
    x1 = b4

if (b2 > b3):
    x2 = b2
else:
    x2 = b3

if (x1 > x2):
    print(str(x1) + " is the greatest")

else:
    print(str(x2) + " is the greatest")
