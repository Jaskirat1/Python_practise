# Program to add two numbers in Python
#by using input from the user

from tkinter import Y


x = input("Enter the value of x:")
y = input("Enter the value of y:")

sum = int(x) + int(y)
sub = int(x) - int(y)
mul = int(x) * int(y)
mod = int(x) % int(y)
div = int(x) / int(y)


print("The addition of two numbers is:",sum)
print("The subtraction of x and y is:", sub)
print("The multiply value of x and y is:", mul)
print("THe division of x an dy is:", mod)
print("The division of x and y is:", div)