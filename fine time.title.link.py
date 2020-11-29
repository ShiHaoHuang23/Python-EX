import requests
from bs4 import BeautifulSoup

url = 'https://tw.appledaily.com/realtime/new/'
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')

sel = '#maincontent>div.thoracis>div.abdominis.rlby.clearmen>ul>li.rtddt>a'
data = soup.select(sel)

for item in data:
    print(item.time.text)
    print(item.hl.text)
    print(item['href'])
    