#   File: Week10-hw1-pgomez-web.py
#   Name: Pedro E Gomez
#   Date: 27-oct-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
#   Desc: perform GET request of https://api.chucknorris.io/jokes/random and present joke in pretty format

# parse the JSON data to obtain the “value” key.(i.e., the joke).
# continue extracting jokes until user selects any other key than Y/y

import json  # the JSONinator
import requests  # calling the world
import textwrap  # create a list of wrapped text (for pretty printing)
import datetime  # find the time of day (for welcome greeting)


# function returns part of the day according to the hour of the day
def mydaypart(x):
    if (x > 0) and (x <= 12):
        return 'Morning'
    elif (x > 12) and (x <= 16):
        return 'Afternoon'
    elif (x > 16) and (x <= 20):
        return 'Evening'
    elif (x > 20) and (x <= 24):
        return 'Night'


# print to standard console using some ANSI escape sequences for emphasis
# \x1b[37m for grey
# \x1b[31m for red
# \x1b[32m for green
# \x1b[33m for yellow
# \x1b[34m for blue
# \x1b[0m for no-color
# \x1b[4m for underline
print("\n\n\x1b[4mHI, I hope you're having a Good {}, \x1b[0mWelcome to the Week 10 programming assignment!!\n".format(
    mydaypart(datetime.datetime.now().hour)))

myinput = 'Y'
while myinput in ['y', 'Y']:  #extract joke until user presses any other key than Y/y
    myinput = input("Would you like a Chuck Norris Joke? (y/Y for yes)")
    if myinput in ['y', 'Y']:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        if response:
            myjoke = response.json()['value']  #grab the joke from the response
            mywrap = textwrap.wrap(myjoke, 50) #create wrapped form of joke (for pretty printing)
            print("\nHere is your Chuck Norris Joke:\x1b[34m")
            for cc in mywrap:
                print(cc)
            print("\n\x1b[0m")  # no more color
        else:
            print('\x1b[31m ERROR! unable to fetch joke. \x1b[0m')

    else:
        print("\x1b[32m Have a Nice Day!!! \x1b[0m")
    continue
