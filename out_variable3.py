#Output variables
x= "My name is Variable"
print(x)

l= "Hello"
m="Welcome to"
n ="Python3"
print(l,m,n)
print(n)
print(l+m+n)
print(l + m + n) # no difference if you add space in print statement

#Now see below instance
x = "Welcome "
y ="to the Python World! "
print(x+y)
print(x,y)

#Note if you will try to concatenate + string with int python enterpreter 
#will gives you an error as unsupported operand type(s) for +: 'int' and 'str'

#example:

"""
r = 90
s ="This is an amount to pay"
print(r+s)
"""
#instead of using concatenate we use comma for the results 
r = 90
s='This is an amount to pay'
print(r,s)
