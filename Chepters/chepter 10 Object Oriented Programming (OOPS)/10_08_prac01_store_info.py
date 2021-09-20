class database:
    company = "Mircosoft"

    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def details(self):
        print(self.name)
        print(self.designation)
        print(self.salary)


employee = database("chirag", "Developer", 25000)
employee.details()
