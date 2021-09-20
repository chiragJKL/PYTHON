class number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"{self.num}"

    def __len__(self):
        return 1  # this can be use in other way. here wont make sense.


n = number(9)
print(n)
print(len(n))
