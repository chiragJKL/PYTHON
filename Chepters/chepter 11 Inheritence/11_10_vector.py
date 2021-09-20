class vector2D:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"


class vector3D(vector2D):

    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j +  {self.jcap}k"


a = vector2D(1, 5)
b = vector3D(6, 1, 9)

print(a)
print(b)
