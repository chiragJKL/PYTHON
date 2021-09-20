

# @STATICMETHOD : here above we needed "self" to pass as self.company BUT if write something where its not required then we can use @staticmethod


class employees:
    company = "Google"

    @staticmethod
    def greet():
        print("GOOD MORNING SIR!")


yash = employees()
yash.greet()
