# File: Week2-hw1-receipt.py
# Name: Pedro E Gomez
# Date: 2-sep-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
# Desc: Week 2 homework; program to calculate installation cost per foot of FO cable.
#
# Usage: User enters company name and amount of FO cable installed, program presents
#        receipt with the anticipated cost

import sys
print("Welcome to the Installation Cost Calculator.")  # Display a welcome message for your user.

# Retrieve the company name from the user.
company_name = input("Company Name: ")

# Retrieve the number of feet of fiber optic cable to be installed from the user. (convert to number)

# exception handling
try:
    number_of_feet = float(input("Feet of FO cable to be installed: "))
except IndexError:
    print("**** Quantity of cable must be supplied!!!")
    sys.exit(1)  # abort execution
except ValueError:
    print("**** Value entered must be a valid quantity!!!")
    sys.exit(1)

# input validation
if number_of_feet <= 0:
    print("**** Value entered must be a positive number!!!")
    sys.exit(1)

# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number
#   of feet times $0.87.
intallation_cost = number_of_feet * 0.87

# Print a receipt for the user including the company name, number of feet of fiber to be installed,
#   the calculated cost, and total cost in a legible format.
print("==============================================")
print("\nReceipt for:", company_name)
print("\nFeet of cable to be installed:", number_of_feet)
print(
    f" The installation cost will be: {number_of_feet} * 0.87 = {round(intallation_cost,2)} dollars")
