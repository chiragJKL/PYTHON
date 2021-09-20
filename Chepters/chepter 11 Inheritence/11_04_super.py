# Super method is used to access the methods of a superclass in the derived class.

# super().__init__()  #Calls constructor of the base class

class person:
    company = "India"
    # religon = "Hindu"

    def personal_info(self):
        print("this is class person")
        # print(
        #     f"PERSONAL INFO : person is from {self.country} and from {self.religon} background\n")


class employee(person):
    company = "Google"
    # job = "Developer"

    def personal_info(self):
        super().personal_info()
        print("this is class employee")
        # print(
        #     f"JOB INFO : person is working at {self.company} as {self.job}\n")


class criminalRecord(employee):
    company = "CrimeMasterCCTV"
    # charges = "theft"
    # custody = "10 months"

    def personal_info(self):
        super().personal_info()

        # this is syntax of super method

        print("this is class criminal")
        # print(
        #     f"CRIMINAL INFO : person had charges of {self.charges} in past and was in custody for {self.custody}\n")


a = criminalRecord()
a.personal_info()
print(a.personal_info)  # every "super" will go one step above parent level.
