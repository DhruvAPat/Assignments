#2.	Write a Python Program to Display the multiplication Table?
def mul(m,n):
    for i in range(1,n+1):
        print(m,'*', i, 'is',(m*i))
m=int(input("Enter the lower limit"))
n=int(input("enter the upper limit"))
s=mul(m,n)