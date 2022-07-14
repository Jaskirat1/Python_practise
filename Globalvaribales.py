""" Global Variables: 
These variables are created outside a function
these variables can be used by both inside and outside functions"""

#Create variable outside a function
x= "This is a very beautiful mountain in North-East"

def newfunc():
    print("Read about Mountains:" + x)

newfunc()

#Create variable inside the function

y ="Astonishing View!"
def thisfunc():
    y = "Awesome view!"
    print("Mountains are beautiful but this mountain has "+ y)

thisfunc()

print(y)

"""To create a global variable inside the function we can 
use global keyword for the same.
"""


def myfunc():
    global y
    y="Beautiful "
    print(y)
myfunc()
print("This is a " + y + "mountain")