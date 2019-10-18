#   File: Week6-hw1-pgomez-lists.py
#   Name: Pedro E Gomez
#   Date: 12-oct-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
#   Desc: Open the file and process each line.
#
# Usage: Open the file and process each line.
# Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
# Nicely print the output, in this case from high to low frequency. You should use string formatting for this. (See discussion 8.3).
# We want to achieve each major goal with a function (one function, one action). We can find four functions that need to be created.
#
# add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.
#
# Process_line: There is some work to be done to process the line: strip off various characters,
# split out the words, and so on. Parameters are a line and the dictionary.
# It calls the function add word with each processed word. No return value.
#
# Pretty_print: Because formatted printing can be messy and often particular to each
# situation (meaning that we might need to modify it later), we separated out the
# printing function. The parameter is a dictionary. No return value.
#
# main: We will use a main function as the main program. As usual, it will open the file
# and call process_line on each line. When finished, it will call pretty_print to print
# the dictionary.
#
# In the main function, you will need to open the file. We will cover more regarding opening
# of files next week but I wanted to provide you with the block of code you will utilize to
# open the file, see below.

##
'''
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
        print(f"{my_input} is not a valid entry!!!")
        my_input = ""  # always initialize to force the question
        continue  # keep trying for a number

    # append the temperature
    temperatures.append(my_input)
    my_input = ""  # always initialize to force the question

# order the entries (evaluation done in the sort)
temperatures.sort()

print(f"\n\n               largest temperature: {temperatures[- 1]}")
print(f"              smallest temperature: {temperatures[0]}")
print(f"number of temperatures in the list: {len(temperatures)}")
'''

word_count = dict()
mypath = 'C:\\Users\\peg_o\\Desktop\\Bellevue\\DSC510-T303 Introduction to Programming\\week8program\\gettysburg.txt'
gba_file = open(mypath, 'r')
for line in gba_file:  # read file, line by line
    for myreplace in ['.', ',', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        line = line.replace(myreplace, '').lower()  # clean the line; set to lower case
    mywords = line.split()

    for myword in mywords:
        mykey = myword.rstrip()

        if mykey not in word_count.keys():
            word_count.update({mykey: 0})
        word_count.update({mykey : word_count.get(mykey) + 1})
        #print("{0}  {1}".format(mykey, word_count.get(mykey)))
print ("\n Lenght of the dictionary: {0}\n".format(len(word_count)))
print(" {0:<18} {1}".format("Word", "Count"))
print("{0:-<25}".format(" "))  #25 dashes
for (mykey, myvalue) in sorted(word_count.items()):  #print sorted dictionary
    print(" {0:<20} {1}".format(mykey, myvalue))
