"""
Numeric Literals : Integer, Float, Complex

#Integer 

Binary Literal, 
Decimal Literal,
Octal Literal,
Hexadecimal Literal

#Float Literal

#Complex Literal

#Boolean Literal

#Special Literal
"""


from codecs import charmap_build


a = 0b1111
b = 10000
c = 0o4
d = 0X3

print(a,b,c,d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))



e = 2.5
f = 1.5e2
g = 2E2

print(e,f,g)
print(type(e))
print(type(f))
print(type(g))


string ="This is String Literals"
char = "C"
multiline_str ="""This is multiline string"""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"



print(string)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


print(type(string))
print(type(char))
print(type(multiline_str))
print(type(unicode))
print(type(raw_str))


x = (1== True)
y = (1 == False)
s = True + 4
t = False - 2
print(x, y)
print("s:", s)
print("t:", t)


""" Python Contains One Special Literal i.e. None 
we use it to specify that the field is not been created."""


drink =  "Chocolate shake"
food = None

def menu(x):
    if x == drink:
        print( drink ," is availabe here")

    else:
        print("This item is not currently available")

menu(drink)
menu(food)
