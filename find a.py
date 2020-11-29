import requests
from bs4 import BeautifulSoup

url = 'https://news.google.com/topstories?tab=wn&hl=zh-TW&gl=TW&ceid=TW:zh-Hant'
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')

links = soup.find_all('a')
for link in links:
    print(link)