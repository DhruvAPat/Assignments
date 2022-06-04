#3.	Write a Python Program for array rotation?
def rotate(summ):
    
    s=summ[::-1]
    return s


summ=[]
choice=int(input("Enter the amount of numbers to be inserted"))
n=1
while(n<=choice):
    a=int(input("enter the number"))
    summ.append(a)
    n+=1
print(summ)
print(rotate(summ))