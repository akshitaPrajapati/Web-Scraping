from urllib.request import urlopen
from bs4 import BeautifulSoup 
url=input('Enter url: ')
pos=int(input('Enter position: '))
rep=int(input('Enter iterations: '))

for i in range(0,rep):
    html=urlopen(url).read()
    Soup=BeautifulSoup(html,'html.parser')
    tags=Soup('a')
    count=0
    for tag in tags:
        count+=1
        if count==pos:
           x=tag.get('href',None)
           print(x)
           url=x
           count=0
           break 
           
       
 