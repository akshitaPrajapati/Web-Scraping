import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key=False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?key=42&'
else :
    serviceurl='https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address=input('Enter location: ')
    if len(address)<1: break

    parms = {"address": address, "key":api_key}
    url= serviceurl + urllib.parse.urlencode(parms)
    uh=urllib.request.urlopen(url, context=ctx)
    data=uh.read().decode()

    try:
        js=json.loads(data)
#       print(json.dumps(js, indent=4)) 
    except:
        js=None


    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    pid=js['results'][0]['place_id']
    print(pid)
    break
