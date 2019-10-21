
import json
from urllib.request import urlopen

#with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
with urlopen("http://citibikenyc.com/stations/json") as response:
    source=response.read()

data=json.loads(source)
#print(json.dumps(data,indent=2))
print(len(data["stationBeanList"]))
#print (data)
for item in data["stationBeanList"]:
    print(item)
