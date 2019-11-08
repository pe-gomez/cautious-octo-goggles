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
import datetime  # for figuring out the part of day for greeting


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


print(
    "\n\n\x1b[4mHI, I hope you're having a Good {}, \x1b[0mWelcome to the Week 11 OOP programming assignment!!\n".format(
        mydaypart()))

x = locale.setlocale(locale.LC_ALL, '')  # setlocale


class CashRegister:

    def __init__(self):  # take no arguments on the instance creation
        self.itemcount = 0  # initialize on the instance cration
        self.itemtotal = 0  # initialize on the instance cration

    def addItem(self, price):
        self.itemcount += 1
        self.itemtotal += price

    # getter method for getCount
    def getCount(self):
        return self.itemcount

    # getter method for getTotal
    def getTotal(self):
        return self.itemtotal

def main():

    myCashRegister = CashRegister()  # create instance of CashRegister

    myinput = ''
    while myinput not in ['q', 'Q']:  # extract joke until user presses any other key than Y/y
        myinput = input("Please enter price for next item (q/Q to Quit): ")
        if myinput not in ['q', 'Q']:
            try:
                myprice = float(myinput)

            except ValueError:
                print("**** Value entered must be a valid quantity!!!")
                continue

            myCashRegister.addItem(myprice)  # add the price entered to cart

        else:
            continue

    # time to display the cart totals
    myGrandTotal = locale.currency(myCashRegister.getTotal(), grouping=True)  # total with local currency locale format

    myNote = "\nCount of items: {0:>" + str(len(myGrandTotal) - 3) + "}"  # message to print with format inst
    print(myNote.format(myCashRegister.getCount()))  # print count

    myNote = "         Total: {0:>" + str(len(myGrandTotal)) + "}"  # message to print with format inst
    print(myNote.format(myGrandTotal))  # print total

if __name__ == "__main__":
    main()
