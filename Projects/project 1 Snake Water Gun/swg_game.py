import random

# we can use "None = 0","True = 1", "False = -1"


def gameWin(comp, you):
    if comp == you:
        return None

    elif comp == 's':
        if you == 'w':
            return False
        if you == 'g':
            return True

    elif comp == 'w':
        if you == 'g':
            return False
        if you == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        if you == 'w':
            return True


you = input("choose snake, water or gun = ")

random_num = random.randint(1, 3)

if random_num == 1:
    comp = 's'

elif random_num == 2:
    comp = 'w'

elif random_num == 3:
    comp = 'g'

print(f"computer = {comp}")
print(f"you = {you}")

a = gameWin(comp, you)

if a == None:
    print("draw!!!")

if a == True:
    print("congrats you won!!!")

if a == False:
    print("oops! computer won!")
