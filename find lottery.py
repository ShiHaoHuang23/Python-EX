import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

datas = soup.find('table',class_='tableWin')
title = datas.find('td','L638DrawTerm_new').text
# <span id="SL638DrawTerm_new"> 109000096 </span>
print('威力彩期數:',title)

nums = datas.find_all('span',class_='even')

print('開出順序:', end='')
for i in range(0,6):
    print(nums[i].text, end='')

print('\n大小順序:', end='')
for i in range(6,12):
    print(nums[i].text, end='')

num = datas.find('span', class_='font_red14').text
 
print('\n第二區:', num)