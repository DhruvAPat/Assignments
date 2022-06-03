#2.	Write a Python Program to Find Factorial of Number Using Recursion?
def fact(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(n*fact(n-1))

n=int(input("enter the number"))
print(fact(n))