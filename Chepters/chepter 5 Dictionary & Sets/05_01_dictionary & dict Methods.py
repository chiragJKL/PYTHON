
# ******Properties of Python Dictionaries

# It is unordered
# It is mutable
# It is indexed
# It cannot contain duplicate keys


myDict = {
    "a": "apple",  # MISTAKE : don't forget " , " after every term
    "b": "ball",
    "c": "chirag",
    "marks": [75, 88, 98],
    "nester": {"d": "dexter"},
    1: 100  # we can directly use this too
}

print(myDict["a"])  # note that here [" "] is used
print(myDict["b"])
print(myDict["c"])
print(myDict["marks"])
print(myDict["nester"])
print(myDict["nester"]["d"])  # we can give deeper meanings
print(myDict[1])

print("\n")


# *************************************************************
#   DICTIONARY METHODS


# [1]keys
# *************************************************************

# to print just KEYS means just left side of terms
print(myDict.keys())
# to covert it into simple list
print(list(myDict.keys()))  # take care its KEYS not key
print("\n")

# [2]values
# *************************************************************

# to print just VALUES means just right side of terms
print(myDict.values())
print(list(myDict.values()))
print("\n")

# [3]items : its not LISTS but similer to list though different
# it gets all (keys, values) of the dictionary
# *************************************************************

print(myDict.items())
print(list(myDict.items()))
print("\n")

# *************************************************************

# to UPDATE dictionary

updateDict = {
    "e": "eye",
    "c": "ccccccc"  # here it will update previous key. check output.
}

myDict.update(updateDict)
print(myDict)

print("\n")

# *************************************************************
# .get and simple

print(myDict.get("c"))
print(myDict["c"])  # both get() and [] print associate values from keys BUT...
print("\n")

# ...BUT

print(myDict.get("c2"))  # will show "NONE" in output
print(myDict["c2"])  # will show error in output


# *************************************************************


# LEARN MORE METHODS FROM GOOGLE AS PER THE NEED
