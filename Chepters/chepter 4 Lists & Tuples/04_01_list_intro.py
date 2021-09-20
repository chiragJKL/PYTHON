# list = array of c!

# if..
# [] = list
# () = tuples ; in that change won't happen
# {} = sets ; in that values won't repeat

a = [25, 5, 21, 20]
print("\n")
print(type(a))
print(a)

print(a[2])  # it starts from zero

# we can CHANGE value
print("before = ", a)
print("before = ", a[0])
a[0] = 50
print("after = ", a)

# we can create list containing different types

b = [35, "chirag", False, 6.9]
print(b)
print(b[0:3])  # means print 0 to 2
print(b[-4:])  # meansn print LAST to first
