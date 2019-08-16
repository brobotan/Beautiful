import requests
from bs4 import BeautifulSoup as BS
url=["http://midas.iiitd.com/"]
for u in url:

    result = requests.get(u)
    src=result.content
    soup = BS(src, 'lxml')

    for a in soup.find_all('a', href=True):
        url.append(a['href'])
        print ("URL:", a['href'])
