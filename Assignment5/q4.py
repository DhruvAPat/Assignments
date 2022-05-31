#4.	Write a Python Program to Check Armstrong Number?
n=int(input("Enter the number"))
sum=0
temp=n
order=len(str(n))
while temp>0:
    digit=temp%10
    sum+=(digit**(order))
    temp//=10

if n==sum:
    print(n," is a armstrong number")
else:
    print( n,"Not and armstrong number")
