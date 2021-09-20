b = set()  # is an empty set.
print(b)

print("\n")

# now to add values in it

b.add(15)
b.add(15)
b.add(15)  # sets dont repeat values hence show ONLY ONE TIME
b.add(4)
b.add(10)
b.add(55)
# b.add([5,6])  --> is not allowed nor DICTIONARY
# we cant add list in sets
b.add((550))  # ...BUT we can add tuples!

print(b)

# to find lenth
print(len(b))

# now to remove values in it

b.remove(10)
# b.remove(100) will show error as its not in the set

print(b)
