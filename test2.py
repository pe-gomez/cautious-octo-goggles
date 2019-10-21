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
'''
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print (odd_square)

# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x ** 2)
print (odd_square)

# below list contains power of 2 from 1 to 8
power_of_2 = [2 ** x for x in range(1, 9)]
print(power_of_2)

my_letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
print(my_letters)

mystring="my zip code is 90210 and I like in California"
myzip=[x for x in mystring.split(' ') if x.isnumeric()]
print (myzip)

# mylist = [[i, j, i * j] for i in [5, 10] for j in range(1, 11)]
mylist = [[str(i) + " * " + str(j), i * j] for i in [5, 10] for j in range(1, 11)]
for x in mylist:
    print(x)

'''
import json
with open('states.jsom') as f:
    data = jsom.load(f)
for state in data['states']:
    del state['area_codes']

with open("myfile.txt","w") as f:
    json.dump(data,f,indent=2)

'''
