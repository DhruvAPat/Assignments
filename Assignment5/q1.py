#1.	Write a Python Program to Find the Factorial of a Number?
def fact(n):
    fact=1
    if n==0:
        print("Invalid")
    else:
        for i in range(2,n+1):
            fact=fact*i
        return fact

n=int(input("Enter the Number"))
print(fact(n))
