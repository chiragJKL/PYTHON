# by this we can change only instance attriutes not class attribute

# *********************************************************************

# class employee:
#     company = "google"
#     location = "rajkot"
#     salary = 100


#     def changeSalary(self, new_sal):
#         self.salary = new_sal


# a = employee()
# print(a.salary)
# a.changeSalary(255)
# print(a.salary)
# print(employee.salary)

# *********************************************************************

# to change all kinda attributes...

class employee:
    company = "google"
    location = "rajkot"
    salary = 100

    # def changeSalary(self, new_sal):
    #     self.__class__.salary = new_sal

    @classmethod
    def changeSalary(self, new_sal):
        self.salary = new_sal


a = employee()
print(a.salary)
a.changeSalary(255)
print(a.salary)
print(employee.salary)
