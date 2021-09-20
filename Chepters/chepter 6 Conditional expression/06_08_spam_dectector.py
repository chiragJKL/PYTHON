
text = input("enter the text: \n\n")

# such a nice use of "in" and "true/false"

if("subcribe now" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("sale sale sale" in text):
    spam = True
else:
    spam = False

if (spam == True):  # MISTAKE : put "==" not "="
    print("SPAM SPAM SPAM. BEWARE!!!")
else:
    print("no spam in the text")
