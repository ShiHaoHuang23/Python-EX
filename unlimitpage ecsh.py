import json,time
import urllib.parse
import requests

url_pattern = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=ipnone&page={}&sort=sale/dc"
alldata = list()

for page in range(1,11):
    url = url_pattern.format(page)
    html = requests.get(url).text
    data = json.loads(html)
    titles = data['prods']
    for title in titles:
        item = dict()
        print(title['name'])
        item['name'] = title['name']
        alldata.append(item)
    time.sleep(3)
with open("allnews.json","w") as fp:
    json.dump(alldata,fp)
print("over!")