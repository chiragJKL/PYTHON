myDict = {
    "pankha": "fan",
    "aam": "mango",
    "dabba": "box"
}

print("enter any word among : ", myDict.keys())

a = input("enter here = ")

print("translation =", myDict[a])

# use .get if wanna avoid error
