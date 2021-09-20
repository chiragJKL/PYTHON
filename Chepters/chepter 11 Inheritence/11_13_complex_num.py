# (a+ci) + (b+di) = (a+b) + (c+d)i
# (a+bi) * (c+di) = ac + adi + bci + bdi2; i2= -1 (real= ac-bd)

class complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return complex(self.real + c.real, self.imaginary + c.imaginary)
        # see without writing "complex" after return and see the difference

    def __mul__(self, c):
        mulreal = self.real*c.real - self.imaginary*c.imaginary
        mulimg = self.real*c.imaginary + self.imaginary*c.real
        return complex(mulreal, mulimg)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary} i "
            # otherwise output will be weird (ab + -cd i) kinda check it
        else:
            return f"{self.real} + {self.imaginary} i "


c1 = complex(1, -4)
c2 = complex(331, -37)
print(f"Sum = {c1 + c2}")
print(f'Multiplication = {c1 * c2}')
