class number:
    def __init__(self, num):
        self.num = num

# __XYZ__ its called "DUNDER"

# __add__, mul, truediv, sub etc are python provides for perticuler operation overloading. GOOGLE IT FOR MORE

    def __add__(self, num2):
        return self.num + num2.num
        # take care: its not (self.num + self.num2)

    def __mul__(self, num2):
        return self.num * num2.num


n1 = number(4)
n2 = number(6)

sum = n1+n2
mul = n1*n2

print(sum)
print(mul)
