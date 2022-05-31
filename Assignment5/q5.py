#5.	Write a Python Program to Find Armstrong Number in an Interval?
upper=int(input("Enter the upper limit"))
lower=int(input("enter the lower limit"))
for i in range(lower,upper+1):
    
    order=len(str(i))
    sum=0
    temp=i
    while(temp>0):
        digit=temp%10
        sum+=(digit**(order))
        temp//=10
    if sum==i:
        print("The armstrong numbers are as follows",sum)
        
    else:
        continue
