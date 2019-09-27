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
    n = 0       #holder for number of entries
    i = 1       #generic counter (starting from 1)
    mytot = 0   #holder for total
    myentry = 0 #holder for individual entry

    # ask for the number of entries to average
    while n == 0:
        try:
            n = float(input("how many numbers to input: "))
        except ValueError:
            print("**** Value entered must be a valid quantity!!!")
            n = 0
        if n != int(n) or n < 1:
            print("**** Value entered must be a positive whole number!!!")
            n = 0

    n = int(n)

    # ask for all entries to average
    for i in range(1, n + 1):
        myentry = 0
        while myentry == 0:
            try:
                myentry = float(input("entry #" + str(i) + ": "))
            except ValueError:
                print("**** Value entered must be a valid quantity!!!")
                myentry = 0
        mytot = mytot + myentry

    print(f"\nAvarage of the {n} numbers is: {mytot / n}")

import sys

myop = ''  # holder for action to take (initialize to blank)

while myop not in ['e', 'E']:

    myop = ''  # always initialize to force the question

    print("\n    (+ to add, - to subtract, * to multiply, / to divide, A to Average, E to EXIT)\n")

    while myop not in ['+', '-', '*', '/', 'a', 'A', 'e', 'E']:
        myop = input("Please select operation to perform  : ")

    # perform math calcs
    if myop in ['+', '-', '*', '/']:
        performCalculation(myop)

    # perform average
    if myop in ['a', 'A']:
        calculateAverage()

print("\n\nHave a nice day!!!)")
