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

import sys
import requests  # calling the world
import re  # call the regular expression module (for pattern matching)
from datetime import datetime, \
    timedelta  # for UNIX time transformations (https://www.programiz.com/python-programming/datetime/strftime)
import pycountry  # fuzzy resolution of country code (https://pypi.org/project/pycountry/)
import json  # json parsing


def isunixdt(inval):
    # return true if inval is numeric of 10 digits (validating unix dt)
    # this method will stop working properly on year 2038 because of signed 32 bit unix utc time issue
    # (so don't use after then ... :-) )
    return re.match("^\d{10}$", str(inval)) != None


def is5zip(inval):
    # return true if inval appears to be a valid 5 digit US zip code (i.e. at most 3 leading 0s, with 5 total digits)
    # method does not work for other countries
    return re.match("^(?!0{3})[0-9]{3,5}$", str(inval)) != None

def getURLq():   # builds city,country query switch (e.g.  &zip=90210  or &q=beverly hills,US)

    myinput=""
    while myinput =="":
        myinput = input("Please enter a US 5 digit Zip Code or World city : ")
        if myinput.isnumeric() and is5zip(myinput)==False:
            print('\x1b[31m ERROR! Numeric entry does not match US 5 digit zip format, Please try again!.\x1b[0m')
            myinput=""

    if is5zip(myinput):
        myURLq = "&zip=" + myinput.strip()
        # print(myURLq)
    else:
        mycity = myinput.strip()
        myinput = ""
        while myinput not in ['Y', 'y']:
            myinput = input("In what country is {0} in? (simply hit ENTER for US, or enter country) : ".format(mycity))
            if myinput == "":
                myURLq = "&q=" + mycity + ",US"
                myinput = "Y"
            else:
                try:
                    mycountrycode = pycountry.countries.search_fuzzy(myinput)[0].name  # do a fuzzy match to the country entere

                #throw an error if mycountrycode failed on any lookup
                except:
                    print('\x1b[31m ERROR! Unable to resolve country, please try again.\x1b[0m')
                    myinput = ""
                    continue

                myinput = input("Did you mean '{}' ? (Y/y for YES, anything else for NO) ".format(mycountrycode))
                if myinput in ['Y', 'y']:
                    mycountrycode = pycountry.countries.get(name=mycountrycode).alpha_2 # find country code for the country
                    myURLq = "&q=" + mycity + "," + mycountrycode

    # print(myURLq)
    return myURLq

def     get5fromjson(loaded_json,my5day ,my5max ,my5min ,my5maxw ,my5minw):  # populated dictonaries from JSON

    my5day.update({'timezone': loaded_json['city']['timezone']})

    # parce the city from json, storing wanted parameters in our forecast dictionary
    for key, value in loaded_json['city'].items():
        if key in ['name', 'country', 'sunrise', 'sunset','timezone']:
            if key not in my5day.keys():
                if key in ['sunrise', 'sunset'] and isunixdt(value):
                    mydate = str(datetime.utcfromtimestamp(value+my5day['timezone']))  # convert the unix date
                    my5day.update({key: mydate})
                else:
                    my5day.update({key: value})

    # get full name of the country (change ISO code to full common name)
    mycountrycode = my5day['country']
    my5day.update({'country': pycountry.countries.get(alpha_2=mycountrycode).name})

    for x in loaded_json['list']:
        # print (x)
        #myday = datetime.fromisoformat(x['dt_txt']).strftime('%Y-%m-%d')  # strip time from stamp, just keep date
        myday = datetime.utcfromtimestamp(x['dt']+my5day['timezone']).strftime('%Y-%m-%d')  # strip time from stamp, just keep date

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

def    display5(my5day ,my5max ,my5min ,my5maxw ,my5minw):  # print the forecast report
    # Day High Temp Low Temp   Wather thought the day
    # --- --------- ---------- -----------------------------------------------
    # \x1b[34m for blue
    # \x1b[4m for underline
    # \x1b[0m for no-color

    # Headings
    print("\x1b[34m\nForecast for \x1b[4m{0} ({1})\x1b[0m\x1b[34m - Temperature in Fahrenheit, Using Local {0} time.".format(
        my5day['name'],
        my5day['country']))
    print(
        "Sunrise: {0}  Sunset: {1} for {2} \x1b[0m\n".format(
            datetime.fromisoformat(my5day['sunrise']).strftime('%I:%M %p'),
            datetime.fromisoformat(my5day['sunset']).strftime('%I:%M %p'),
            datetime.fromisoformat(my5day['sunrise']).strftime(
                '%A %B %d, %Y')))

    print("{0:4} {1:^9} {2:^9} {3}".format("Day", "High Temp", "Low Temp", "Weather throughout the day"))
    print("-" * 4 + " " + "-" * 9 + " " + "-" * 9 + " " + "-" * 50)

    # data
    for key, value in my5max.items():
        # if key != datetime.fromisoformat(my5day['sunrise']).strftime('%Y--%m-%d'):
        myweather=my5maxw[key] + " to " + my5minw[key]
        if my5maxw[key] == my5minw[key]:
            myweather = my5maxw[key]

        print("{0:4} {1:^9} {2:^9} {3}".format((datetime.fromisoformat(key).strftime('%a')), round(my5max[key]),
                                               round(my5min[key]), myweather))


def main():
    my5day = dict()  # the dictionary for heading info (timezone,name,country,sunrise,sunset)
    my5max = dict()  # the dictionary for max day temp (dates are key)
    my5min = dict()  # the dictionary for min day temp (dates are key)
    my5maxw = dict()  # the dictionary for max day weather description (dates are key)
    my5minw = dict()  # the dictionary for min day weather description (dates are key)

    myinput="Y"
    while myinput  in ['y', 'Y']:  # add to cart until user presses q/Q

        myURLq=getURLq() # fetch location from user

        try:
            response = requests.get(
                "http://api.openweathermap.org/data/2.5/forecast?APPID=1d6396e456b004718aba6387a0e99fc7&mode=json&units=imperial" + myURLq)
        except requests.exceptions.RequestException as myerror:  # print any exception errors posted by the requests
            print(myerror)

        if response:
            myerror = json.loads(response.text)['message']
            print('\x1b[32m SUCCESS! API able to connect. {0} \x1b[0m'.format(myerror))
        else:
            myerror = json.loads(response.text)['message']
            print('\x1b[31m ERROR! API Response error: {0} \x1b[0m'.format(myerror))
            myinput="Y"
            continue

        # with open(
        #         "C:\\Users\\peg_o\\Desktop\\Bellevue\\DSC510-T303 Introduction to Programming\\finalProject\\78717jsonIMPERIAL.txt",
        #         "r") as response:
        #     source = response.read()

        # loaded_json = json.loads(source)
        # source = None
        loaded_json = response.json()
        response.close()
        response= None

        # print(json.dumps(data, indent=2, sort_keys=True))
        # print(json.dumps(loaded_json, indent=2))

        # for x in loaded_json:
        # 	print("%s: %s" % (x, loaded_json[x]))

        # for key,value in loaded_json['list'].items():
        #     print(key,value)

        # x=loaded_json['list'][0]

        # extract the dictionaries from json
        my5day.clear()
        my5max.clear()
        my5min.clear()
        my5maxw.clear()
        my5minw.clear()
        get5fromjson(loaded_json,my5day ,my5max ,my5min ,my5maxw ,my5minw)

        # print(my5day)
        # print(my5max)
        # print(my5min)
        # print(my5maxw)
        # print(my5minw)

        # print the weather forecast
        display5(my5day ,my5max ,my5min ,my5maxw ,my5minw)

        myinput = input("\nExtract another forecast? (y/Y for YES, any other to QUIT): ")


if __name__ == "__main__":
    main()