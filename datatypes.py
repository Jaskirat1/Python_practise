"""Different data types in Python 
int, str, float, set, tuple, dict, list, frozenset, memoryview, bool, bytes, bytearray, complex, range"""

#a ="My name is Python"
a=str("hi, Python")
print(type(a))
print(a)

#b =2
b= int(0.009)
print(b)
print(type(b))

c=float(5)
print(c)
print(type(c))

d= complex(1j)
print(d)
print(type(d))

e= list(("volvo","bmw","lambo"))
print(e)
print(type(e))

f=dict( apple=2, mango=35, name= "emily")
print(f)
print(type(f))

g=set(("Ammy","babbu","cat","Denver"))
print(g)
print(type(g))

h=range(9)
print(type(h))
print(h)

i=tuple(("Hello", "Welcome"))
print(i)
print(type(i))

j=bool(0)
print(j)
print(type(j))

k=b"Python"
p=bytes(5)
print(p)
print(type(k))
print(k)

l=bytearray(5)
print(type(l))
print(l)

m=frozenset({"apple","cheery"})
print(type(m))
print(m)

n= memoryview(bytes(2))
print(type(n))
print(n)

o = None
print(type(o))