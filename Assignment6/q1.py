#1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
def fib(n):
    if n==0 or n==1:
        return n
    elif n<0:
        print("Invalid Number")
    else:
        return(fib(n-1)+fib(n-2))
            
        
        
n=int(input("Enter the  number"))
for i in range(n):
    print(fib(i))
