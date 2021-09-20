
# '''
# class person = grand parent
# class employee = parent
# class criminal record = child

# '''


print("\n************")


class person:
    country = "India"
    religon = "Hindu"

    def personal_info(self):
        print(
            f"PERSONAL INFO : person is from {self.country} and from {self.religon} background\n")


class employee(person):
    company = "Google"
    job = "Developer"

    def employee_info(self):
        print(
            f"JOB INFO : person is working at {self.company} as {self.job}\n")


class criminalRecord(employee):
    company = "CrimeMasterCCTV"
    charges = "theft"
    custody = "10 months"

    def criminal_info(self):
        print(
            f"CRIMINAL INFO : person had charges of {self.charges} in past and was in custody for {self.custody}\n")


per = person()
per.personal_info()
# print(per.company) will show error as it does not have that info and not linked with other class.

emp = employee()
emp.employee_info()
print(emp.company)

cr = criminalRecord()
cr.criminal_info()
print(cr.company)
print(cr.country)  # it will take country from "grand parent" class!

print("\n************\n")
