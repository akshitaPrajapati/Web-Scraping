import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter url: ')
uh = urllib.request.urlopen(url, None)
sum=0
data = uh.read()
tree = ET.fromstring(data)
count_tags = tree.findall('comments/comment')
for tag in count_tags:    
    y=tag.find('count')
    sum+=int(y.text)
print(sum)    
   