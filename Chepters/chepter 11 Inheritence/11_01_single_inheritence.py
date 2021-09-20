# INHERITANCE --> is a way of creating a new class from an existing class.

# We can use the methods and attributes of Employee in Programmer object.

# Also, we can overwrite or add new attributes and methods in the Programmer class. means it will check..
# first] --> object if its not there..
# second] --> class if its not there
# third] --> 'will show error'

# *******************************************************************

# Single Inheritance

# *******************************************************************

# Single inheritance occurs when a child class inherits only a single parent class.

# Base (Parent) -> Derived (Child)


class Collage:  # parent/ base class
    clg = "Marwadi"

    def clg_details(self):
        print("\nthese are details of class collage")

    def check_inheritence(self):
        print("\nthe inheritence example : this line is in clg but inherited by dept!\n")


class Department (Collage):  # child/ derived class
    # This is the syntax for INHERITENCE
    dept = "Mechanical"

    def dept_details(self):
        print("\nthese are details of class Department")


student1 = Collage()
student1.clg_details()

student1 = Department()
student1.dept_details()
student1.check_inheritence()
