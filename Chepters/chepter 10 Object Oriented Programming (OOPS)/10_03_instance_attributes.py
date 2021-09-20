class employees:
    company = "Google"
    salary = 50  # Class Attribute

    # CLASS = employees
    # CLASS ATTRIBUTE = company, salary


chirag = employees()  # OBJECT initiation
hetu = employees()

chirag.salary = 100  # Instance Attribute
# It will
# first] check Instance Attribute
# second] Class Attribute
# third] if both of them are not there it will show error

# thats why value of salary of chirag, hetu will be different.

print(chirag.salary)
print(hetu.salary)
# print(hetu.address) will show error.
