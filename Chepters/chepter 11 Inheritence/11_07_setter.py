class employee:
    salary = 8000
    bonus = 500

    @property  # its also called "getter method"
    def totalSalary(self):  # MISTAKES : YOU ARE FORGETTING "SELF"!!!!
        return self.salary+self.bonus

    # setter will set a value and change other value in corruspondance to it.
    @totalSalary.setter
    def totalSalary(self, value):
        self.bonus = value - self.salary


a = employee()

print(a.totalSalary)
a.totalSalary = 8300
print(a.totalSalary)
print(a.salary)
print(a.bonus)
