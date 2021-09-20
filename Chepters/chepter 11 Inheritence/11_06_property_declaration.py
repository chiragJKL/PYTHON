# @property --> we can write function as property!!

# its called "getter method" too.

# ************************************************************

class employee:
    salary = 8000
    bonus = 500
    # totalSalary = 8500

    @property
    def totalSalary(self):  # MISTAKES : YOU ARE FORGETTING "SELF"!!!!
        return self.salary+self.bonus


a = employee()

# we can write function as property!!
print(a.totalSalary)

# if we don't use @property we can write it as function as per given below
# print(a.totalSalary())
