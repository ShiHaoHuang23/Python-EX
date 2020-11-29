import requests
from bs4 import BeautifulSoup

url = 'https://udn.com/news/breaknews/1'
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')

links = soup.find_all(class_='story-list_text')
for link in links:
    title = link.find('h2')
    try:
        print(title.a['title'])
        print(title.a['href'])
    except:
        pass