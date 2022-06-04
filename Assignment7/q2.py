#2.	Write a Python Program to find largest element in an array?
def largest(summ):
    max=summ[0]
    n=len(summ)
    for i in range(1,n):
        if max<summ[i]:
            max=summ[i]
    return max
       
summ=[]
choice=int(input("Enter the amount of numbers to be inserted"))
n=1
while(n<=choice):
    a=int(input("enter the number"))
    summ.append(a)
    n+=1
print(summ)
print("The Largest number in the array is {}".format(largest(summ)))


