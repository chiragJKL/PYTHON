

# ****STRING FUNCTIONS****

story = "once upon a time we tried to learn python py"


print(len(story))  # give lenght in int

print(story.endswith("python"))  # checks in true or false

print(story.count("a"))
print(story.count("py"))

print(story.capitalize())  # capitalise first word

# starts from 0 hence output = 5 also it shows FIRST OCURRENCE only
print(story.find("up"))

# it will work in saperate programme here all function ar creating issue. refer "replace_fun.py". also this will replace ALL WORDS
print(story.replace("pyhton", "java"))
