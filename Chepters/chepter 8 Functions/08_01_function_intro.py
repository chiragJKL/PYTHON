def greeting(name):
    print(f"Hello! Mr. {name}")


greeting("chirag")
greeting("yash")
greeting("akshay")


# *****************************************************************


def greeting(name="STRENGER"):  # giving it a "default parameter value"
    print(f"Hello! Mr. {name}")


greeting("chirag")
greeting()  # here output will be default = STRENGER


# *****************************************************************


def MySumFunction(x, y):
    z = x+y
    print(z)


MySumFunction(5, 6)
MySumFunction(1, 1)
MySumFunction(4, 6)
