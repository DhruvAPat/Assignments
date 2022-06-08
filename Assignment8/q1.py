#1.	Write a Python Program to Add Two Matrices?
def add(l1,l2):
    l3=[]
    n=len(l1)
    for i in range(n):
        l3.append(l1[i]+l2[i])
    return l3

l1=[1,2,3,4]
l2=[4,5,6,7]
print(add(l1,l2))
