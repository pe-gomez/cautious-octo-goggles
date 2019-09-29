#   File: Week6-hw1-pgomez-lists.py
#   Name: Pedro E Gomez
#   Date: 30-sep-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
#   Desc: Program will populate the list based upon user input. Your program will determine the number of temperatures in the program, determine the largest temperature, and the smallest temperature.
#
# Usage: Create an empty list called temperatures.
#   Allow the user to input a series of temperatures along with a sentinel value which
#     will stop the user input.
#   Evaluate the temperature list to determine the largest and smallest temperature.
#   Print the largest temperature.
#   Print the smallest temperature.
#   Print a message tells the user how many temperatures are in the list.
##

temperatures = []

my_input = ""

# read until user ends
while my_input == "":

    my_input = input("Please enter temperature, (e or E to END)  : ")

    # get out if the user is done
    if my_input in ['e', 'E']: break

    # check for number
    try:
        my_input = float(my_input)
    except ValueError:
        print("{my_input] is not a valid entry!!!")
        my_input = ""  # always initialize to force the question
        continue  # keep trying for a number

    # append the temperature
    temperatures.append(my_input)
    my_input = ""  # always initialize to force the question

#order the entries
temperatures.sort()

print(f"\n\n              largest temperature: {temperatures[len(temperatures)-1]}")
print(f"             smallest temperature: {temperatures[0]}")
print(f"number of temperatures in the list: {len(temperatures)+1}")
