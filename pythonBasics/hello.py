# functions - a block of code that performs specific task
list1 = [1,2,3]
list2 = [4,5,6]

def calculate_total(exp):
    total = 0
    for item in exp: 
        total = total + item  
    return total

def sum(a, b):

    """
    DOCUMENTATION STRINGS
    this function takes two arguments which are integers or numbers 
    and returns sum of both numbers
    """
    print("a is:", a)
    print("b is:", b)
    total = a + b
    return total

# print(total) this is not visible here.
# print(sum(5,6))

# total = 0
# for item in list1: 
#     total = total + item  
# print("Total list1" , total)

# total = 0
# for item in list2: 
#     total = total + item  
# print("Total list2" , total)

list1Total = calculate_total(list1)
list2Total = calculate_total(list2)

# print("Total list1" , list1Total)
# print("Total list2" , list2Total)


############################################################33
# DICTIONARIES
# Used to store key value pairs (like contacts)
# order does not matter, only thing is to get values from keys
d = {
    "yash": 123,
    "raghav": 456,
}
# print(d["yash"])

# del(d["yash"]) # to delete
# print(d)

# for key in d: 
#     print("Key: ", key, "value: " ,d[key])

# for k, v in d.items():
#     print("Key: ", k, "value: " ,v)


# print("yash" in d) # to check if key is present in dicttionary
# d.clear() # to clear all items in dictionary

###################################33
# Tuples
# list of values grouped together
# in list - all have similar meaning (homogenous)
# list example - a list of expense

# in tuples - all values have different meaning (heterogenous)
# tupeles example - a point, coordinate, an address
# tuples are immutable

point = (5,6) # here 5 is x-co, 6 is y-co
print(point[0])
address = ("1 purple street", "new york", 1011)
# address[2] = 34 # shows error

#########################################################
# pip install matplotlib
# list of all packag
# packeges can be found on "pypi.python.org/pypi"
# to uninstall - pip uninstall matplotlib

##################################################33
# Modules
# the whole idea of reusing something also applies to programming as well
# module is a way to reuse a code written by someone else
# you can use it for free
import math
print(math.sqrt(16))
print(math.pow(2,5))
# to see all , "dir(math)" or 
# you can google to know about all of them according to use
# docs.python.org
# pi, log10(100), 
print(math.floor(2.3))
print(math.ceil(2.3))

import calendar
cal = calendar.month(2016, 1)
print(cal)

print(calendar.isleap(2016))

### how make your own module
import functions as f
# import functions 
print(f.sum(4,5))
