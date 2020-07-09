import urllib.request, urllib.parse, urllib.error
import json
while True:
    url=input('Enter url: ')
    if len(url)<1 : break
    sum=0
    uh=urllib.request.urlopen(url).read()
    data=uh.decode()
    info=json.loads(data)
    dict=info['comments']
    for item in dict:
        num=item['count']
        sum+=int(num)
    print(sum)   