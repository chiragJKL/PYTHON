num = int(input("enter num = "))

factorial = 1  # 1 because it makes sense in fact*1 loop condition
for i in range(1, num+1):  # num+1 --> 1 to num
    factorial = factorial*i

print(f"value of the factorial of {num} is = {factorial}")
