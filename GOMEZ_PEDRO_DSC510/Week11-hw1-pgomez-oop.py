#   File: Week11-hw1-pgomez-oop.py
#   Name: Pedro E Gomez
#   Date: 2-nov-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
#   Desc: a simple cash register program

# one class called CashRegister.  an instance of the CashRegister class is used as the "cash register"
# addItem  one parameter for price; also keep track of the number of items in  cart.
# getTotal getter methods – returns totalPrice
# getCount getter methods – returns the itemCount of the cart

#  program loop add items to the cart until user responts with q or Q to quit.
#  program  prints the total number of items in the cart.
#  program prints the total $ amount of the cart (formatted as currency, per  locale class)


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


class CashRegister:

    def __init__(self):  # take no arguments on the instance creation
        self.itemcount = 0  # initialize to 0 on the instance creation
        self.itemtotal = 0  # initialize to 0 on the instance creation

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
    print(
        "\n\n\x1b[4mHI, I hope you're having a Good {}, \x1b[0mWelcome to the Week 11 OOP programming assignment!!\n".format(
            mydaypart()))

    x = locale.setlocale(locale.LC_ALL, '')  # setlocale

    myCashRegister = CashRegister()  # create instance of CashRegister

    myinput = ''
    while myinput not in ['q', 'Q']:  # add to cart until user presses q/Q
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

    # total with local currency locale format
    myGrandTotal = locale.currency(myCashRegister.getTotal(), grouping=True)

    # print the item count (right justified, depending on max lenght)
    myNote = "\nCount of items: {0:>" + str(len(myGrandTotal) - 3) + "}"
    print(myNote.format(myCashRegister.getCount()))

    # print the total (right justified, depending on max lenght)
    myNote = "         Total: {0:>" + str(len(myGrandTotal)) + "}"
    print(myNote.format(myGrandTotal))


if __name__ == "__main__":
    main()
