class students:
    team = "cricket"

    def __init__(self, name, age, height):
        # self will pass automatically but to pass others we need attributes

        self.name = name
        self.age = age
        self.height = height

        print("\n***student application for cricket team***\n")

    def student_details(self):
        print(f"student's name is {self.name}")
        print(f"student's age is {self.age}")
        print(f"student's height is {self.height}")


chirag = students("chirag", 25, 155)
# chirag = students() will show error cause we created self + 3 variables or arguments
chirag.student_details()
