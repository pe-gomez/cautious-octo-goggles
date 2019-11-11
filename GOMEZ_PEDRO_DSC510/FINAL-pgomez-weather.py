#   File: FINAL-pgomez-weather
#   Name: Pedro E Gomez
#   Date: 11-nov-2019
# Course: DSC510-T303 Introduction to Programming (2201-1)
#   Desc: City Weather Forecast Reporting Program

# user proves either US 5 digit zip code or world city (and country).
# weather forecast data from OpenWeatherMap
#   * free 5-day forecast API is used
#   * since forecast data is provided for future timeframes in 3-hr increments, that data is
#     analyzed and transformed into a daily forecast.
#
# User has the ability to re-run new reports for other cities (one city at a time)
#
# Program makes us of the following modules:
#      requests (HTTP for Humans), for data extraction of remote API data through HTTP.
#      re (Regular Expressions), for input and data validation based on patters.
#      datetime (Encapsulation of date/time values.), for manipulation of UNIX, UTC, and ISO timestamps
#      pycountry (ISO databases for country standards), for fuzzy logic resolution of country/country code information (PACKAGE INSTALLATION REQUIRED)
#      json (JavaScript Object Notation package), for parsing of json data into lists/dictionaries
#      locale (Cultural Localization), for deriving defaults based on user’s locale information

import requests  # calling the world
import re  # call the regular expression module (for pattern matching)

# for UNIX time transformations (https://www.programiz.com/python-programming/datetime/strftime)
from datetime import datetime
import pycountry  # fuzzy resolution of country code (https://pypi.org/project/pycountry/)
import json  # json parsing
import locale  # localizing defaults and formatting (https://pymotw.com/3/locale/)

class clsWeather:

    def __init__(self):
        # All times are stored in UNIX format, adjusted for timezone

        self.varCityName = ""
        self.varCountryName = ""
        self.varunits = "Fahrenheit"
        self.varTimezone = 0
        self.varSunrise = 0
        self.varSunset = 0

        self.cntNextIndex = 0  # next available index to use in lists (for appends)
        self.dicDay2IndexXF = dict()  # day key to index location in lists (cross-reference)

        # Captured daily parameters lists
        #       x-referenced to the day via the dicDay2IndexXF dictionary
        # MaxT - Hith Temp
        # MinT - Min Temp
        # LastWD - First Weather description of day
        # FirstWD - Last Weather description of day
        self.lstMaxT = []
        self.lstMinT = []
        self.lstLastWD = []
        self.lstFirstWD = []

        # Corresponding Timestanps of the Captured daily parameters (in UNIX format, adjusted for timezone)
        #       also x-referenced to the day via the dicDay2IndexXF dictionary
        #       Timestamps are not necessary if JSON info is always presented in sequential order
        #           since API doc did not state sequential presentation, a sequential order cannot be assumed.
        self.lstMaxTUtime = []
        self.lstMinTUtime = []
        self.lstLastWDUtime = []
        self.lstFirstWDUtime = []

    def putrow(self, myOriginalDT, mytemp_max, mytemp_min, mydescription):
        # add/update daily data into data lists

        mydt = myOriginalDT + self.varTimezone  # adjust time for city timezone
        mydtkey = datetime.utcfromtimestamp(mydt).strftime('%Y-%m-%d')  # strip time from stamp, just keep date

        # new daily entry (judged by the cross-ref)
        if mydtkey not in self.dicDay2IndexXF.keys():
            # new entry on the cross-reference dictionary (key to list indexes)
            self.dicDay2IndexXF.update({mydtkey: self.cntNextIndex})

            # weather attributes for the day
            self.lstMaxT.insert(self.cntNextIndex, mytemp_max)
            self.lstMinT.insert(self.cntNextIndex, mytemp_min)
            self.lstLastWD.insert(self.cntNextIndex, mydescription)
            self.lstFirstWD.insert(self.cntNextIndex, mydescription)

            # Unix time stamps for each of those attributes
            self.lstMaxTUtime.insert(self.cntNextIndex, mydt)
            self.lstMinTUtime.insert(self.cntNextIndex, mydt)
            self.lstLastWDUtime.insert(self.cntNextIndex, mydt)
            self.lstFirstWDUtime.insert(self.cntNextIndex, mydt)

            self.cntNextIndex += 1

        # updade of current daily entry
        else:
            mylst_index = self.dicDay2IndexXF[mydtkey]  # get the index in lists for the key being processed

            # update self temp max if lower than new for the day
            if self.lstMaxT[mylst_index] < mytemp_max:
                self.lstMaxT[mylst_index] = mytemp_max
                self.lstMaxTUtime[mylst_index] = mydt

            # update self temp min if higher than new for the day
            if self.lstMinT[mylst_index] > mytemp_min:
                self.lstMinT[mylst_index] = mytemp_min
                self.lstMinTUtime[mylst_index] = mydt

            # update self weather description if not first for the day
            if self.lstFirstWDUtime[mylst_index] > mydt:
                self.lstFirstWD[mylst_index] = mydescription
                self.lstFirstWDUtime[mylst_index] = mydt

            # update self weather description if not last for the day
            if self.lstLastWDUtime[mylst_index] < mydt:
                self.lstLastWD[mylst_index] = mydescription
                self.lstLastWDUtime[mylst_index] = mydt
        return

    def getrow_report(self, mydtkey):
        # Returns a list of 4 formatted data elements (in list form) for report from the given date key
        # [Abreviated day for data, Rounded Max Temp, Rounded Min Temp, built described weather]
        # for example: ["Thu",44,37,"overcast clouds"]

        if mydtkey not in self.dicDay2IndexXF.keys():
            return ["", 0, 0, "ERROR date not found: " + mydtkey]

        else:
            if self.lstFirstWD[self.dicDay2IndexXF[mydtkey]] == self.lstLastWD[self.dicDay2IndexXF[mydtkey]]:
                myweather = self.lstFirstWD[self.dicDay2IndexXF[mydtkey]]
            else:
                myweather = self.lstFirstWD[self.dicDay2IndexXF[mydtkey]] + " to " + self.lstLastWD[
                    self.dicDay2IndexXF[mydtkey]]

            return [datetime.fromisoformat(mydtkey).strftime('%a'), round(self.lstMaxT[self.dicDay2IndexXF[mydtkey]]),
                    round(self.lstMinT[self.dicDay2IndexXF[mydtkey]]), myweather]
        return


def isunixdt(inval):
    # return true if inval is numeric of 10 digits (validating unix dt)
    # this method will stop working properly on year 2038 because of signed 32 bit unix utc time issue
    # (so don't use after then ... :-) )

    return re.match("^\d{10}$", str(inval)) != None


def is5zip(inval):
    # return true if inval appears to be a valid 5 digit US zip code (i.e. at most 3 leading 0s, with 5 total digits)
    # method does not work for other countries

    return re.match("^(?!0{3})[0-9]{3,5}$", str(inval)) != None


def getURLq():
    # builds city,country query switch (e.g.  &zip=90210  or &q=beverly hills,US)

    myinput = ""
    while myinput == "":
        myinput = input("Please enter a US 5 digit Zip Code or World city : ")
        if myinput.isnumeric() and is5zip(myinput) == False:
            print('\x1b[31m ERROR! Numeric entry does not match US 5 digit zip format, Please try again!.\x1b[0m')
            myinput = ""

    if is5zip(myinput):  # user provided a US 5 digit zip (no country needed for API)
        myURLq = "&zip=" + myinput.strip()

    else:  # figure out the country belonging to the city
        mycity = myinput.strip().title()
        myinput = ""
        while myinput not in ['Y', 'y']:

            # set default country to use (based on guessed country from locale)
            mycountrycode = locale.getlocale()[0]  # first guess at country - from locale
            x = mycountrycode.find("_") + 1
            myinput = mycountrycode[x:]  # refined guess at country
            try:
                # attempt do a fuzzy match to the country in the locale (to serve as default country code)
                mycountrycode = pycountry.countries.search_fuzzy(myinput)[0].alpha_2
            # go with US if mycountrycode failed on fuzzy match
            except:
                mycountrycode = 'US'

            myinput = input("In what country is {0} in? (simply hit ENTER for {1}, or enter country) : ".format(mycity, mycountrycode))
            if myinput == "":
                myURLq = "&q=" + mycity + "," + mycountrycode  # build the zip query portion of URL (US is deault)
                myinput = "Y"
            else:
                try:
                    # attempt do a fuzzy match to the country entered (to better resolve country code)
                    mycountrycode = pycountry.countries.search_fuzzy(myinput)[0].name

                # throw an error if mycountrycode failed on fuzzy match
                except:
                    print('\x1b[31m ERROR! Unable to resolve country, please try again.\x1b[0m')
                    myinput = ""
                    continue

                myinput = input("Did you mean '{}' ? (Y/y for YES, anything else for NO) ".format(mycountrycode))
                if myinput in ['Y', 'y']:
                    # country confirmed, now resolve the 2-digit country code
                    mycountrycode = pycountry.countries.get(
                        name=mycountrycode).alpha_2  # find country code for the country
                    myURLq = "&q=" + mycity + "," + mycountrycode  # build the city query portion of URL

    return myURLq


def getfromjson(loaded_json, myweather):
    # populate the instance weather class from JSON data

    # parse the city header data from json
    for key, value in loaded_json['city'].items():
        if key == 'name': myweather.varCityName = value
        if key == 'country': myweather.varCountryName = value
        if key == 'sunrise': myweather.varSunrise = value
        if key == 'sunset': myweather.varSunset = value
        if key == 'timezone': myweather.varTimezone = value

    # adjust Unix times for timezone
    myweather.varSunrise += myweather.varTimezone
    myweather.varSunset += myweather.varTimezone

    # derive full name of the country (change ISO code to full common name)
    mycountrycode = myweather.varCountryName
    myweather.varCountryName = pycountry.countries.get(alpha_2=mycountrycode).name

    # parse the Entire list data from json
    for x in loaded_json['list']:
        myOriginalDT = x['dt']
        mytemp_max = x['main']['temp_max']
        mytemp_min = x['main']['temp_min']
        mydescription = x['weather'][0]['description']

        # send the info to the weather class to be further reviewed and stored into the day info
        myweather.putrow(myOriginalDT, mytemp_max, mytemp_min, mydescription)

    return


def reportforecast(myweather):
    # print the forecast report, in the following format
    # Day High Temp Low Temp   Weather thought the day
    # --- --------- ---------- -----------------------------------------------

    # \x1b[34m for blue
    # \x1b[4m for underline
    # \x1b[0m for no-color

    # Table intro Headings
    print(
        "\x1b[34m\nForecast for \x1b[4m{0} ({1})\x1b[0m\x1b[34m - Temperature in {2}, Using Local {0} time.".format(
            myweather.varCityName, myweather.varCountryName, myweather.varunits))
    print(
        "Sunrise: {0}  Sunset: {1} for {2} \x1b[0m\n".format(
            datetime.utcfromtimestamp(myweather.varSunrise).strftime('%I:%M %p'),
            datetime.utcfromtimestamp(myweather.varSunset).strftime('%I:%M %p'),
            datetime.utcfromtimestamp(myweather.varSunrise).strftime(
                '%A %B %d, %Y')))

    # Column Headings
    print("{0:4} {1:^9} {2:^9} {3}".format("Day", "High Temp", "Low Temp", "Weather throughout the day"))
    print("-" * 4 + " " + "-" * 9 + " " + "-" * 9 + " " + "-" * 50)

    # data expressed in sorted form (in case lson dates were not in order)
    #   clsWeather method getrow_report generates the row data information
    for key in sorted(myweather.dicDay2IndexXF.keys()):
        print("{0:4} {1:^9} {2:^9} {3}".format(*myweather.getrow_report(key)))

    return


def main():
    x = locale.setlocale(locale.LC_ALL, '')  # setlocale
    # is program being run in the US, used to set temperature units default
    myinUS = x.find("United States") > 0  # US locale identifier (True for US)

    # default the units for the runs (all forecasts)
    if myinUS:
        myURLunits = "&units=imperial"
        myinput = input("\nExtracting all forecasts in Fahrenheit. Switch to Celsius? (y/Y for YES, any other for NO): ")
        if myinput in ['y', 'Y']:
            myURLunits = "&units=metric"
    else:
        myURLunits = "&units=metric"
        myinput = input("\nExtracting all forecasts in Celsius. Switch to Fahrenheit? (y/Y for YES, any other for NO): ")
        if myinput in ['y', 'Y']:
            myURLunits = "&units=imperial"

    myinput = "Y"
    while myinput in ['y', 'Y']:  # add to cart until user presses something other than y/Y

        myURLq = getURLq()  # fetch location from user

        # make the URL connections
        try:
            response = requests.get(
                "http://api.openweathermap.org/data/2.5/forecast?APPID=1d6396e456b004718aba6387a0e99fc7&mode=json" + myURLunits + myURLq)
        except requests.exceptions.RequestException as myerror:  # print any exception errors posted by the requests
            print(myerror)

        myerror = json.loads(response.text)['message']
        if response:  # API reports no issues on response==True
            print('\x1b[32m SUCCESS! API able to connect. {0} \x1b[0m'.format(myerror))

        else:  # further catching of errors (from both requests and API)
            print('\x1b[31m ERROR! API Response error: {0} \x1b[0m'.format(myerror))
            myinput = "Y"  # return to the user input
            continue

        # grab json info
        loaded_json = response.json()
        response.close()
        response = None  # no longer need response object

        # create/delete clsWeather instance
        if 'myweather' in locals():
            del myweather
        myweather = clsWeather()
        if myURLunits == "&units=metric":  # register the temperature units in the class
            myweather.varunits = "Celsius"
        else:
            myweather.varunits = "Fahrenheit"

        # parse the weather data from json
        getfromjson(loaded_json, myweather)

        # print the weather forecast
        reportforecast(myweather)

        myinput = input("\nExtract another forecast? (y/Y for YES, any other to QUIT): ")

    return


if __name__ == "__main__":
    main()
