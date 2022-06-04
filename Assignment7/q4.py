#4.	Write a Python Program to Split the array and add the first part to the end?
def cut(summ):
    k=int(input("Enter the splitting index"))
    m=len(summ)
    s1=summ
    s2=summ[k:m]
    print(s2)
    s3=s1+s2
 
    return s3


summ=[]
choice=int(input("Enter the amount of numbers to be inserted"))
n=1
while(n<=choice):
    a=int(input("enter the number"))
    summ.append(a)
    n+=1
print(summ)
print(cut(summ))