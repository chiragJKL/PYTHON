
# n! = 1 * 2 * 3 *... *(n-1) * n
# n! = [1 - (n-1)] * n
# n! = (n-1)! * n

def factorial(n):

    if n == 0 or n == 1:
        return n
    else:
        # here function is calling itself = recurssion
        return factorial(n-1) * n


num = int(input("enter num = "))
print(factorial(num))
