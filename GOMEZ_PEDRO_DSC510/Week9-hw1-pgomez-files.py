#   File: Week9-hw1-pgomez-files.py
#   Name: Pedro E Gomez
#   Date: 20-oct-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
#   Desc: Open the file and process each line; open new file for output
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
# Create a new function called process_fie. This function will perform the same operations as pretty_print from week 8 however it will print to a file instead of to the screen.
# Modify your main method to print the length of the dictionary to the file as opposed to the screen.
# This will require that you open the file twice. Once in main and once in process_file.
# Prompt the user for the filename they wish to use to generate the report.
# Use the filename specified by the user to write the file.
# This will require you to pass the file as an additional parameter to your new process_file function.
#
#
# main: We will use a main function as the main program. As usual, it will open the file
# and call process_line on each line. When finished, it will call pretty_print to print
# the dictionary.
#
# In the main function, you will need to open the file. We will cover more regarding opening
# of files next week but I wanted to provide you with the block of code you will utilize to
# open the file, see below.

import os  # for testing existance of file and deleting them
from collections import OrderedDict  # for later use in storing the sorting dict by value

def add_word(mydictionary, mykey):
    mydictionary.update({mykey: 1})

def Process_line(line, mydictionary):

    #Remove unwanted characters and lower case the line
    line = line.lower().translate(line.maketrans('', '', "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"))

    mywords = line.split()

    for myword in mywords:
        mykey = myword.rstrip()

        if mykey not in mydictionary.keys():  # add word if not in dictionary
            add_word(mydictionary, mykey)
            continue

        mydictionary[mykey] = mydictionary[mykey] + 1


def Pretty_print(mydictionary):
    print("\n Lenght of the dictionary: {0}\n".format(len(mydictionary)))
    print(" {0:<18} {1}".format("Word", "Count"))
    print("{0:-<25}".format(" "))  # 24 dashes

    # create reverse sorted dictionary by value
    mydictionary_s = OrderedDict(sorted(mydictionary.items(), key=lambda x: x[1], reverse=True))

    for (mykey, myvalue) in (mydictionary_s.items()):  # print sorted dictionary
        print(" {0:<20} {1}".format(mykey, myvalue))


def process_file(mydictionary, out_path):
    with open(out_path, "a") as out_file:
        out_file.write(" {0:<18} {1}\n".format("Word", "Count"))  # headers for dictionary data
        out_file.write("{0:-<25}\n".format(" "))  # 24 dashes

        # create reverse sorted dictionary by value
        mydictionary_s = OrderedDict(sorted(mydictionary.items(), key=lambda x: x[1], reverse=True))

        for (mykey, myvalue) in (mydictionary_s.items()):  # print sorted dictionary
            out_file.write(" {0:<20} {1}\n".format(mykey, myvalue))

        out_file.close()


def main():
    #
    mydictionary = dict()
    in_path = 'gettysburg.txt'
    try:
        in_file = open(in_path, 'r')
    except:
        print(" File cannot be opened: ", in_path)
        exit()

    for line in in_file:  # read file, line by line
        Process_line(line, mydictionary)

    # out_path = "myout.txt"  # if outputfile exists, delete it
    out_path = ""
    while out_path == "":

        out_path = input("Please enter file name for output (hit ENTER for default: myout.txt) ")  # get file name
        if out_path == "":
            out_path = "myout.txt"

        if os.path.exists(out_path):
            myinput = input("{} exists, would you like to overwrite file? (y for yes)".format(out_path))
            if myinput in ['y', 'Y']:
                try:
                    os.remove(out_path)
                except:
                    print("Error while deleting file ", out_path)
            else:
                out_path = ""
                continue

    print("\n\nUsing '{}'".format(out_path))

    with open(out_path, "w") as out_file:
        out_file.write("\n Lenght of the dictionary: {0}\n\n".format(len(mydictionary)))
        out_file.close()

    # Pretty_print(mydictionary)
    process_file(mydictionary, out_path)


if __name__ == "__main__":
    main()
