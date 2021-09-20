
def recurssive_sum(n):

    if n <= 1:
        return n
    else:
        # for i in range(n, 0, -1):
        return n + recurssive_sum(n-1)


x = 3
print(recurssive_sum(x))
