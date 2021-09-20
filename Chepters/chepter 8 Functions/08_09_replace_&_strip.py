def replace_and_strip(string, word):
    new_str = string.replace(word, "")
    return new_str.strip()


a1 = "      chirag   yoyo      lunagaria       "
n = replace_and_strip(a1, "chirag")
print(n)
