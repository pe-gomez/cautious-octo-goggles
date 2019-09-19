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

'''


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
