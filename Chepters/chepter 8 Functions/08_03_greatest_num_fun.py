def greatest_num(x, y, z):

    if(x > y):
        if(x > z):
            return x
        else:
            return z
    else:
        if(y > z):
            return y
        else:
            return z


num1 = int(input("enter num 1= "))
num2 = int(input("enter num 2= "))
num3 = int(input("enter num 3= "))

print(greatest_num(num1, num2, num3))
