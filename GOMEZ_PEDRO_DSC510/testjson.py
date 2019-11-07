
import json
from urllib.request import urlopen

#with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
with urlopen("http://citibikenyc.com/stations/json") as response:
#with open("C:\\Users\\peg_o\\Desktop\\Bellevue\\DSC510-T303 Introduction to Programming\\finalProject\\78717json.txt","r") as response:
#with open("C:\\Users\\peg_o\\Desktop\\Bellevue\\DSC510-T303 Introduction to Programming\\finalProject\\78717json.txt","r") as response:

    source=response.read()
    ##source=json.load(response)


data=json.loads(source)
#print(json.dumps(data,indent=2))
#print(len(data["stationBeanList"]))
print (data)
for item in data:
    print(item)
#for item2 in data["city"]:
#    print (item2,type(item2))
#print (data["city"]["name"])

#json.dump(data,f,indent=2)

