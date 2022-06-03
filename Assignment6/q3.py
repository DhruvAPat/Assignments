#3.	Write a Python Program to calculate your Body Mass Index?
height=float(input("Enter the Height in inches"))
weight=int(input("Enter the Weight"))
bmi=round((weight)*(height**2),2)
print("The BMI Calculated is {}".format(bmi))