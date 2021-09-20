class employees:
    company = "Google"
    # CLASS = employees
    # CLASS ATTRIBUTE = company


chirag = employees()  # OBJECT initiation
hetu = employees()
print(chirag.company)
print(hetu.company)

employees.company = "YouTube"
# we can change it by calling class and class attribute (here --> company)
print(chirag.company)
print(hetu.company)
