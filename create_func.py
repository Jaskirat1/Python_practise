#create simple function in python


def myfunc(x):
    return list(dict.fromkeys(x))


list1 = myfunc(["a","b","c","d","x","b","c","a"])
print(list1)