class math:
    def square(self, num):
        self.num = num
        print(f"square of {self.num} is = {self.num**2}")

    def cube(self, num):
        self.num = num
        print(f"cube of {self.num} is = {self.num**3}")

    def root(self, num):
        self.num = num
        print(f"root of {self.num} is = {self.num**0.5}")


a = math()
a.square(9)
a.cube(9)
a.root(9)

# or
print("\n")
# ********************************************************************


class math1:

    def __init__(self, num1):
        self.num1 = num1

    def square1(self, num1):
        # self.num1 = num1 #we already mention it in __init__
        print(f"square1 of {self.num1} is = {self.num1**2}")

    def cube1(self, num1):
        # self.num1 = num1
        print(f"cube1 of {self.num1} is = {self.num1**3}")

    def root1(self, num1):
        # self.num1 = num1
        print(f"root1 of {self.num1} is = {self.num1**0.5}")


a1 = math1(9)
a1.square1(9)
a1.cube1(9)
a1.root1(9)
