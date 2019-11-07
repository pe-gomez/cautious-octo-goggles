#http://www.py4e.com/code3/json2.py
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]
'''

info = json.loads(data)
print (info)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

import urllib.request

#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#for line in fhand:
#    print(line.decode().strip())

with urllib.request.urlopen("http://data.pr4e.org/romeo.txt") as response:
    source=response.read().decode().strip()

print(source)

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()

req = urllib.request.Request('http://www.pretend_server.org')
try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)

