
# this is "int"
a = 25
print(type(a))

# thia is "str"
a1 = "25"
print(type(a1))
# so if we do maths operation it won't work and programme will not give output of next lines.
a1 += 2

# we can change type with typecasting
a2 = "25"
a2 = int(a2)  # with is we changed int into str
print(type(a2))
a2 += 12
print(a2)
