#   File: Week11-hw1-pgomez-oop.py
#   Name: Pedro E Gomez
#   Date: 2-nov-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
#   Desc: demonstrate our knowledge of Python object oriented programming concepts by creating a simple cash register program

# Your program must have a header.
# Your program must have a welcome message for the user.
# Your program must have one class called CashRegister.
# Your program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
# Your program should have two getter methods.
# getTotal – returns totalPrice
# getCount – returns the itemCount of the cart
# Your program must create an instance of the CashRegister class.
# Your program should have a loop which allows the user to continue to add items to the cart until they request to quit.
# Your program should print the total number of items in the cart.
# Your program should print the total $ amount of the cart.
# The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.


import locale  # currency formatting
# from datetime import datetime
import datetime


# function returns part of the day according to the hour of the day
def mydaypart():
    x = datetime.datetime.now().hour
    if (x >= 0) and (x <= 12):
        return 'Morning'
    elif (x > 12) and (x <= 16):
        return 'Afternoon'
    elif (x > 16) and (x <= 20):
        return 'Evening'
    elif (x > 20) and (x <= 24):
        return 'Night'


# print to standard console using some ANSI escape sequences for emphasis
# \x1b[37m for grey
# \x1b[31m for red
# \x1b[32m for green
# \x1b[33m for yellow
# \x1b[34m for blue
# \x1b[0m for no-color
# \x1b[4m for underline
print(
    "\n\n\x1b[4mHI, I hope you're having a Good {}, \x1b[0mWelcome to the Week 11 OOP programming assignment!!\n".format(
        mydaypart()))

x = locale.setlocale(locale.LC_ALL, '')  # setlocale


# locale.currency(188518982.18, grouping=True)

# print(datetime.datetime.now())


class CashRegister:

    def __init__(self):
        self.itemcount = 0
        self.itemtotal = 0

    def addItem(self, price):
        self.itemcount += 1
        self.itemtotal += price

    def getCount(self):
        return self.itemcount

    def getTotal(self):
        return self.itemtotal


# def getCount():
#    pass

myCashRegister = CashRegister()
# print(CashRegister.itemcount)

myCashRegister.addItem(1)
myCashRegister.addItem(7.25)
myCashRegister.addItem(9.85)
myCashRegister.addItem(12.8)
myCashRegister.addItem(6.5)
myCashRegister.addItem(13)
myCashRegister.addItem(10)

print(myCashRegister.getCount())

# myobjs = list()
# myobjs.append(CashRegister(1))
# myobjs.append(CashRegister(2.55))
# myobjs.append(CashRegister(6.5))
# myobjs.append(CashRegister(14.5333))

# print(CashRegister.itemcount)
# print(len(myobjs))
# print(myobjs)

print(locale.currency(myCashRegister.getTotal(), grouping=True))  # print with local currency locale
