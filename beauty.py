import requests
from bs4 import BeautifulSoup as BS

result = requests.get("http://midas.iiitd.com/")
src=result.content
soup = BS(src, 'lxml')

print(soup.text)
