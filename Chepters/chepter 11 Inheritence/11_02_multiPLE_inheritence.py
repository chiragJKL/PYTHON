
# ************************************************************

# Multiple Inheritance

# ************************************************************

# Multiple inheritances occurs when the child class inherits from more than one parent class.

class employee:
    company = "Google"
    eCode = 120


class freelancer:
    company = "Fiverrr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level+1


class programmer(employee, freelancer):
    # here order is important. preference will be given that way.
    name = "rohit"


a = programmer()
a.upgradeLevel()
# by using programmer we can use attributes of employee and freelancer both in that order
print(a.level)
print(a.company)  # here it will take "Google" cause preference!
