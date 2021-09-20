# (a+ci) + (b+di) = (a+b) + (c+d)i
# (a+bi) * (c+di) = ac + adi + bci + bdi2

class complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __sum__(self, c):
        return complex(self.real + c.real, self.imaginary + c.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i "


c1 = complex(1, 4)
c2 = complex(5, 8)
print(c1+c2)
