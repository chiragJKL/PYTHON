class employee:
    salary = 1000
    increament = 2

    @property
    def salary_plus(self):
        return self.salary * self.increament

    @salary_plus.setter
    def salary_plus(self, value):
        self.increament = value/self.salary


a = employee()
print(a.salary_plus)

print(a.increament)
a.salary_plus = 1500
print(a.increament)
