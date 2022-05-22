#4.	Write a Python program to swap two variables?
x=int(input("Enter the no1 "))
y=int(input("Enter the no2"))
print("The Value of x is {}".format(x))
print("The Value of y is {}".format(y))

temp=x
x=y
y=temp
print(x,y)
print("The Value of x now is {}".format(x))
print("The Value of y now is {}".format(y))


