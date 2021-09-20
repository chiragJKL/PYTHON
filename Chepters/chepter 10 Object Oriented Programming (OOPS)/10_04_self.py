# SELF --> refers to the instance of the class.

# We can use any other term instead of "SELF" but just for universality programmers genarally use "SELF"

# It is automatically passed with a function call from an object.

# harry.getSalary()
# here, self is harry, and the above line of code is equivalent to Employee.getSalary(harry)

class employees:
    company = "Google"

    def getSalary(self, signature):
        # self because see below comment
        # self will be used by Class as well as Instance attributes

        print(
            f"\nsalary of this employee working in {self.company} is {self.salary}\n{signature}")

# @STATICMETHOD : here above we needed "self" to pass as self.company BUT if write something where its not required then we can use @staticmethod

    @staticmethod
    def greet():
        print("GOOD MORNING SIR!")


chirag = employees()
chirag.salary = 100
# chirag.getSalary()  # is same as [employees.getSalary(chirag)] but to pass it like normal function..
# here "thanks" is signature to pass it like normal function.
chirag.getSalary("thanks!!!")

chirag.greet()
