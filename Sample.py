def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("ENter a number: "))
if num<0:
    print("The factorial is not defined for negative number.")
else:
    result = factorial(num)
    print("The factorial is: ",result)