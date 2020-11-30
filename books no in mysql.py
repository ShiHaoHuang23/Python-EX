import requests
import mysql.connector
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
           'AppleWebKit/537.36 (KHTML, like Gecko)'
           'Chrome/86.0.4240.198 Safari/537.36'}

html = requests.get("https://www.books.com.tw/web/sys_tdrntb/books/?loc=menu_th_1_001",headers=headers).text

conn = mysql.connector.connect(host='localhost',database='books',user='root',password='19910203')
cursor = conn.cursor()
sql = """
      insert into `ranking30` (`rank`,`title`,`author`,`price`)
      values({},'{}','{}','{}');
      """

soup = BeautifulSoup(html,"html.parser")
sel = 'li.item'
ranking = soup.select(sel)

for rank,book in enumerate(ranking,1):
    title = book.h4.a.text
    detail = book.find_all("li")
    author = detail[0].text
    price = detail[1].text
    print(rank,title,author,price)
    
    try:
        cursor.execute(sql.format(rank,title,author,price))
    except mysql.connector.Error as error:
        print("Error:{}",format(error))
        pass
    
    conn.commit()
conn.close()
print("Done")