# File: Week2-hw1-receipt.py
# Name: Pedro E Gomez
# Date: 2-sep-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
# Desc:
# Usage:

#
print ("Welcome to the Installation Cost Calculator.") # Display a welcome message for your user.

# Retrieve the company name from the user.
company_name = "ACME AAA" #input("Company Name: ")

# Retrieve the number of feet of fiber optic cable to be installed from the user. (convert to number)
number_of_feet = 20.1 #float(input("Feet of cable installed:"))

# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number
#   of feet times $0.87.
intallation_cost = number_of_feet * 0.87

# Print a receipt for the user including the company name, number of feet of fiber to be installed,
#   the calculated cost, and total cost in a legible format.
print ("\nReceipt for:" , company_name)
print ("\nFeed of cable to be installed:",number_of_feet)
print (" The installtion cost will be:",number_of_feet,"* 0.87 =",int(intallation_cost*100+.5)/100," dollars" )


#Include appropriate comments throughout the program.

