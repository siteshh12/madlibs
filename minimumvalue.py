######## Read two numbers from the keyboard and print minimum value#######
x = int(input("enter your first number:"))
y = int(input("enter your second number"))
if (x<y):
  print('minimum value is' ,x)
else:
    print('minimum value is' ,y)
#########alternatively#######
x = int(input('enter first number'))
y = int(input('enter second number'))
min = x if x<y else y
print('minimum value is' , min)
#########alternatively#######
x = int(input("enter your first number:"))
y = int(input("enter your second number"))
print("minimum value is x" if x<y else "minimum value is y")

#########program for minimum of three numbers#######
x = int(input("enter your first number:"))
y = int(input("enter your second number"))
z = int(input("enter your third number"))
if x<y and x<z:
    print("minimum number is",x)
elif y<z and y<x:
    print("minimum number is", y)
else:
    print("minimum number is", z)
#########alternatively#######
x = int(input("enter your first number:"))
y = int(input("enter your second number"))
z = int(input("enter your third number"))
min = x if x<y and y<z else y if y<z and y<x else z
print("minimum value is:", min)
########alternatively############
x = int(input("enter your first number:"))
y = int(input("enter your second number"))
z = int(input("enter your third number"))
print("minimum value is x " if x<y and x<z else " minimum value is y" if y<z and y<x else"minimum value is z")
#########program for maximum of three numbers#######
x = int(input("enter your first number:"))
y = int(input("enter your second number"))
z = int(input("enter your third number"))
max = x if x>y and y>z else y if y>z and z>y else z
print("maximum value is, max")
########alternatively############
x = int(input("enter your first number:"))
y = int(input("enter your second number"))
print("both numbers are equal" if x==y else "first number is less than the second number" if x<y else "first number is greater than second number")







