"""There are four different literal Collections in python
that are:= List , tuple, dict, set"""


#List in python
""" First item in the list will represent with the index 0 and second with the index 1"""

from xml.dom.minidom import Element


fruits =['apple', 'banana', 'mango', 'orange', 'dates']

"""There are set of built-in methods in python
     
    1. append(): Adds an element at the end of the list

"""
fruits.append("fig")
print(fruits)

"""
 2. clear(): Removes all; the elemnts from the list.
"""
#fruits.clear()
#print(fruits)

""" 
3. copy(): returns a copy of the list 
"""
fruits.copy()
print(fruits)

"""
4. count(): counts that how many times one item is placed in a list and return the specific value of list of items
"""
x = fruits.count("apple")
print(x)

"""
5. extend(): you can say to add two lists example add other list at the end of current list
"""

cars=['bmw','volvo','nissan','mercedes','jeep']
fruits.extend(cars)
print(fruits)

"""
6. index() : this will return the index of the item
"""
y = fruits.index("bmw")
print(y)


"""
7. pop() : removes the element from a specific position
just put the index of that particular item

"""

z= fruits.pop(5)
print(z)

"""
8. remove() : This will remove the item with the specific value."""

fruits.remove("apple")
print(fruits)


"""
9. reverse() : This will reverses the order of the list"""

fruits.reverse()
print(fruits)

""" 10. sort(): It will sort the list
here we can use (reverse)and (key) attribute to sort accordingly.
"""

fruits.sort(reverse=True)
print(fruits)



def myfunc(y):
    return y['year']
    
students =[
    {'name': 'aman', 'year':2000 },
    {'name': 'jasman', 'year':2004},
    {'name': 'kiran', 'year': 2006},
    {'name' : 'taran', 'year': 2007},
    {'name' : 'sahil', 'year': 2001}
            ]
students.sort(key=myfunc)
print(students)

students.sort(reverse=True, key=myfunc)
print(students)


""" 
11. len() : this will print the length of the list.
"""

print(len(students))

""" List constructor : to create a new list 
list() constructor will be used"""


mycars= list(('volvo', 'jaguar','lamborgini','thar'))
print(mycars)