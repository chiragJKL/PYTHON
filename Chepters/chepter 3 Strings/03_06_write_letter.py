letter = '''Hello Mr. <NAME>
Your exam date is <DATE>
and exam centre is in <LOCATION>

Thanks!!!'''

name = input("enter name = \n")
date = input("enter date = \n")
location = input("enter location = \n")

letter = letter.replace("<NAME>", name)
letter = letter.replace("<DATE>", date)
letter = letter.replace("<LOCATION>", location)

print(letter)
