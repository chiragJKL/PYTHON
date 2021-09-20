# # sets : {} is used,  in which values won't repeat

# ***Properties of Sets

# Sets are unordered
# Elements order doesn’t matter
# Sets are unindexed
# Cannot access elements by index
# There is no way to change items in sets (even if we try to put list inside sets it will throw an error)
# Sets cannot contain duplicate values

a = {1, 2, 5, 2}

print(type(a))  # class -> set
print(a)  # 2 won't repeat


print("\n")
# ***********************************************

# EMPTY SETS

# b = {}
# #is empty DICTIONARY !!!!!!!!!!!!!!

b = set()  # is an empty set.
print(b)

print("\n")


# ***********************************************

s = {18, "18"}
# it will print both as python see one as int and other str
print(s)

s1 = {20, 20.0, "20"}
print(s1)
print(len(s1))  # will be 2
