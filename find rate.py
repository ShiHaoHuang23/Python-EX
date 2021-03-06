import requests
from bs4 import BeautifulSoup

url = 'http://rate.bot.com.tw/xrt/all/day'
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')

dnames = soup.select('table tr td[data-table=幣別] div.visible-phone')
names = list()
for dname in dnames:
    names.append(dname.text.strip())

buyprice = soup.select('table tr td[data-table=本行即期買入]')
prices = list()
for price in buyprice:
    prices.append(price.text.strip())

rates = zip(names,prices)
for rate in rates:
    print(rate)