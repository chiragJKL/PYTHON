

# Why Class?? : to use it as we talk in real world.

# its kinda similer to "STRUCTURE (struct)" in C language but have some differences.

# Many MODULES are simply Class!

# by using Class and Object we can keep track of long programmes easily


class RailwayForm:
    def print_data(self):  # have to write "self"
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


chiragApplication = RailwayForm()
# Here :
# RailwayForm --> CLASS
# chiragApplication --> OBJECT
chiragApplication.name = "Harry"
chiragApplication.train = "Rajdhani"
chiragApplication.print_data()
