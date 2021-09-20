maths = int(input("enter marks of maths = "))
physics = int(input("enter marks of physics = "))
chemistry = int(input("enter marks of chemistry = "))

percentage = (maths + physics + chemistry) / 3
print(percentage)

if (maths <= 33 and physics <= 33 and chemistry <= 33):
    print("failed due to less then 33% in one of the subjects")

if (percentage >= 40):
    print("failed due to less then 40% total marks")

else:
    print("congrats! you are pass!!")
