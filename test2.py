'''
colors = ["red", "blue", "yellow", "green"]

i = 0
while i < len(colors):
    print ("when i was %d, my favorite color was %s" % (i, colors[i]))
    i=i+1

import random

for i in range(10):
    x = random.random()
    print(x)


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses=['math','art']
info={'name':'John','age':22}

student_info(*courses,**info)




def student_info(myarg, **kwargs):
    print(myarg, kwargs)
    # print(args)


# courses=['math','art']
info = {'name': 'John', 'age': 22}

student_info('Student Info:', name='John', age=22)


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s==%s" % (key, value))


print(datetime.datetime.now())

import datetime


def student_info(*args):
    pass


print(student_info())


def my_func(fargs, *args, **kwargs)


import math


def area(radius):
    b = math.pi * float(radius) ** 2
    #return b


radius = input("What is the radius of the circle? ")

ourarea = area(radius)

print(ourarea)
print(type(area(5)))
print(ourarea == None)

https://www.datacamp.com/community/tutorials/functions-python-tutorial

def xbyy(x, y):
    return x * y
The filter() function
The map() function


xbyy = lambda x, y: x * y
print(xbyy(2,3))
'''

# empty dictionary
my_dict = {}
# dictionary with integer keys
my_dict = {1: "pencil", 2: "pen"}
# dictionary with mixed keys
my_dict = {"name": "Peter", 1: [2, 4, 3]}
# using dict()
my_dict = dict({1: "pencil", 2: "pen"})
# from sequence having each item as a pair
my_dict = dict([(1, "pencil"), (2, "pen")])

if 1 in myD.keys():
    print(myD[1])

for (key, value) in myD.items():
    print(key, " :: ", value)