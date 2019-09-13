#   File: Week2-hw1-pgomez-receipt.py
#   Name: Pedro E Gomez
#   Date: 9-sep-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
#   Desc: Week 3 assignment; program to calculate installation cost per foot of FO cable and evaluate a bulk discount.
#
# Usage: User enters company name and amount of FO cable installed, program presents receipt with the anticipated cost. Calculate the cost of fiber optic cable installation by multiplying the number of feet needed by $0.87. If the user purchases more than 100 feet they are charged $0.80 per foot. If the user purchases more than 250 feet they will be charged $0.70 per foot. If they purchase more than 500 feet, they will be charged $0.50 per foot.
#

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
intallation_cost = number_of_feet * inst_rate

# Print a receipt for the user including the company name, number of feet of fiber to be installed,
#   the calculated cost, and total cost in a legible format.
print("==============================================")
print("\nReceipt for:", company_name)
print("\nFeet of cable to be installed:", number_of_feet)
print(f"\n    Undiscounted cost would have been: {number_of_feet} * 0.87 = {round(number_of_feet * 0.87, 2)} dollars\n")
print(f"Your actual installation cost will be: {number_of_feet} * {inst_rate} = {round(intallation_cost, 2)} dollars")
