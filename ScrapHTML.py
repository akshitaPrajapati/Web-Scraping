from urllib.request import urlopen
from bs4 import BeautifulSoup 
url=input('Enter url: ')
html=urlopen(url).read()
Soup=BeautifulSoup(html,'html.parser')
tags=Soup('span')

sum=0
for tag in tags:
    x = tag.contents[0]
    sum+= int(x)
print(sum)       

    