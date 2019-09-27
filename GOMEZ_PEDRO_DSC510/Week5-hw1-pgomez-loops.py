#   File: Week5-hw1-pgomez-loops.py
#   Name: Pedro E Gomez
#   Date: 24-sep-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
#   Desc: This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation)
# This program will contain a variety of loops and functions.
# The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
#
# Usage: The main program should prompt the user for the operation they wish to perform.
#       The main program should evaluate the entered data using if statements.
#       The main program should call the necessary function to perform the calculation.
##

def performCalculation(myop):
    ''' parameter will be the operation being performed (+, -, *, /).  '''
    print(f"performing {myop} of two numbers")
    fnum = float(input(" Enter First number: "))
    snum = float(input("Enter Second number: "))
    if myop == '+': myres = fnum + snum
    if myop == '-': myres = fnum - snum
    if myop == '*': myres = fnum * snum
    if myop == '/': myres = fnum / snum
    print(f"\n{fnum} {myop} {snum} = {myres}\n")


def calculateAverage():
    n = 0
    i=1
    mytot=0
    myentry=0
    while n == 0:
        try:
            n = float(input("how many numbers to input: "))
        except ValueError:
            print("**** Value entered must be a valid quantity!!!")
            n = 0
        if n != int(n) or n < 1:
            print("**** Value entered must be a positive whole number!!!")
            n = 0
    for i in range(1,int(n)+1):
        myentry=0
        while myentry == 0:
            try:
                myentry = float(input("entry #"+str(i)+": "))
            except ValueError:
                print("**** Value entered must be a valid quantity!!!")
                myentry = 0
        mytot=mytot+myentry
    print (f"Avarage of the {n} numbers is: {mytot/n}")


import sys

myop = ''

while myop not in ['e', 'E']:
    while myop not in ['+', '-', '*', '/', 'a', 'A', 'e', 'E']:
        print("\n    (+ to add, - to subtract, * to multiply, / to divide, A to Average, E to EXIT)\n")
        myop = input("Please select operation to perform  : ")

    #perform math calcs
    if myop in ['+', '-', '*', '/']: performCalculation(myop)

    #perform average
    if myop in ['a', 'A']: calculateAverage()

    #reset to go back and ask again
    myop = ''

print("\n\nHave a nice day!!!)")

'''
print("Welcome to the Installation Cost Calculator.")  # Display a welcome message for your user.

# Retrieve the company name from the user.
company_name = input("Company Name: ")

# Retrieve the number of feet of fiber optic cable to be installed from the user. (convert to number)

# exception handling
try:
    number_of_feet = float(input("Feet of FO cable to be installed: "))
except IndexError:
    print("**** Quantity of cable must be supplied!!!")
    sys.exit(1)
except ValueError:
    print("**** Value entered must be a valid quantity!!!")
    sys.exit(1)

# input validation
if number_of_feet <= 0:
    print("**** Value entered must be a positive number!!!")
    sys.exit(1)

# is there a bulk discount
if number_of_feet > 500:
    inst_rate = 0.5
elif number_of_feet > 250:
    inst_rate = 0.7
elif number_of_feet > 100:
    inst_rate = 0.8
else:
    inst_rate = 0.87

# Calculate the installation cost of fiber optic
# intallation_cost = number_of_feet * inst_rate
intallation_cost = inst_calc(number_of_feet, inst_rate)


# Print a receipt for the user including the company name, number of feet of fiber to be installed,
#   the calculated cost, and total cost in a legible format.
print("==============================================")
print("\nReceipt for:", company_name)
print("\nFeet of cable to be installed:", number_of_feet)
print(f"\n    Undiscounted cost would have been: {number_of_feet} * 0.87 = {round(number_of_feet * 0.87, 2)} dollars\n")
print(f"Your actual installation cost will be: {number_of_feet} * {inst_rate} = {round(intallation_cost, 2)} dollars")
'''