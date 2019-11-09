#   File: FINAL-pgomez-weather
#   Name: Pedro E Gomez
#   Date: 8-nov-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
#   Desc: Weather Program

# #Create a Python Application which asks the user for their zip code or city.
# Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
# Display the weather forecast in a readable format to the user.
# Use comments within the application where appropriate in order to document what the program is doing.
# Use functions including a main function.
# Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
# Validate whether the user entered valid data. If valid data isn’t presented notify the user.
# Use the Requests library in order to request data from the webservice.
# Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.

# Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful

import re  # call the regular expression module (for pattern matching)
from datetime import datetime, timedelta  # for UNIX time transformations

import json


def isunixdt(inval):
    # return true if inval is numeric of 10 digits (validating unix dt)
    return re.match("^\d{10}$", str(inval)) != None


my5day = dict()  # the 5 day dictionary for heading info
my5max = dict()  # the 5 day dictionary for max day temp
my5min = dict()  # the 5 day dictionary for min day temp
my5maxw = dict()  # the 5 day dictionary for max day weather description
my5minw = dict()  # the 5 day dictionary for min day weather description


with open(
        "C:\\Users\\peg_o\\Desktop\\Bellevue\\DSC510-T303 Introduction to Programming\\finalProject\\78717jsonIMPERIAL.txt",
        "r") as response:
    source = response.read()

loaded_json = json.loads(source)
source = None

# print(json.dumps(data, indent=2, sort_keys=True))
# print(json.dumps(loaded_json, indent=2))

# for x in loaded_json:
# 	print("%s: %s" % (x, loaded_json[x]))

# for key,value in loaded_json['list'].items():
#     print(key,value)

# x=loaded_json['list'][0]

for x in loaded_json['list']:
    # print (x)
    myday = datetime.fromisoformat(x['dt_txt']).strftime('%Y-%m-%d')  # strip time from stamp, just keep date
    # print(myday)
    if myday not in my5max.keys():
        my5max.update({myday: float(x['main']['temp_max'])})

    if my5max[myday] < x['main']['temp_max']:
        my5max.update({myday: float(x['main']['temp_max'])})

    if myday not in my5min.keys():
        my5min.update({myday: float(x['main']['temp_min'])})

    if my5min[myday] > x['main']['temp_min']:
        my5min.update({myday: float(x['main']['temp_min'])})

    if myday not in my5maxw.keys():
        my5maxw.update({myday: x['weather'][0]['description']})

    my5minw.update({myday: x['weather'][0]['description']})
    # my5minw.update({myday: 'hello'})



    # for key, value in x['main'].items():
    #     print(key, value)

# parce the city from json, storing wanted parameters in our forecast dictionary
for key, value in loaded_json['city'].items():

    if key in ['name', 'country', 'sunrise', 'sunset']:
        if key not in my5day.keys():
            if key in ['sunrise', 'sunset'] and isunixdt(value):
                mydate = str(datetime.fromtimestamp(value))  # convert the unix date
                my5day.update({key: mydate})
            else:
                my5day.update({key: value})

print(my5day)
print(my5max)
print(my5min)
print(my5maxw)
print(my5minw)

# dt = (datetime.fromtimestamp(unix_ts) - timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S')
