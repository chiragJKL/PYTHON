# tuples : it described by () "small brackets" ; unlike list []
# diff btw "list" and "tuples" is tuples can't be change once defined

tuples = (1, 3, 5, 10)

print(type(tuples))  # to just check class
print(tuples[0])

tuples[0] = 111
print(tuples[0])
# OUTPUT = TypeError: 'tuple' object does not support item assignment
# because we tried to change values
