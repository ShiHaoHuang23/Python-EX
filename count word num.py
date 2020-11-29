import requests
url = 'https://news.google.com/topstories?tab=wn&hl=zh-TW&gl=TW&ceid=TW:zh-Hant'

resp = requests.get(url)
html = resp.text
print(resp.status_code)
q = input("plz input word:")
while q != "":
    print(html.count(q))
    q = input("plz input word:")