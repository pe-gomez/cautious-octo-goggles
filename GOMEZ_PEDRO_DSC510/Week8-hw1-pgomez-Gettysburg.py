#   File: Week8-hw1-pgomez-lists.py
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

from collections import OrderedDict  # for later use in storing the sorting dict by value


def add_word(mydictionary, mykey):
    mydictionary.update({mykey: 1})


def Process_line(line, mydictionary):
    for myreplace in ['.', ',', '-']:
        line = line.replace(myreplace, '').lower()  # clean the line; set to lower case

        #alternate method
        #import string
        #line = line.translate( line.maketrans('', '', string.punctuation))

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


def main():
    #
    word_count = dict()
    mypath = 'C:\\Users\\peg_o\\Desktop\\Bellevue\\DSC510-T303 Introduction to Programming\\week8program\\gettysburg.txt'
    try:
        gba_file = open(mypath, 'r')
    except:
        print(" File cannot be opened: ", mypath)
        exit()

    for line in gba_file:  # read file, line by line
        Process_line(line, word_count)

    Pretty_print(word_count)


if __name__ == "__main__":
    main()
