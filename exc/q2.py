#2.	Write a Python program to do arithmetical operations addition and division.?
def arth(a,b):
    choice=int(input("enter choice"))
    try:
        if choice==1:
            return a+b
        elif choice==2:
            return a-b
        elif choice==3:
            return a*b
        elif choice==4:
            return a/b
        else:
            print("invalid choice")
    except Exception as e:
        print(str(e))

a=int(input("enter no"))
b=int(input("enter no 2"))
print(arth(a,b))