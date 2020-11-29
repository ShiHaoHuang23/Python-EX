import requests,re,urllib,os,time
from bs4 import BeautifulSoup

url = 'https://technews.tw/'
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')

regex = r'http.+jpg'
links = soup.find_all("a")
photos = list()

for link in links:
    try:
        if ".jpg" in link['herf']:
            target = link['href']
            for item in re.findall(regex,target):
                photos.append(item)
    except:pass

for link in photos:
    #存檔
    item = urllib.parse.urlparse(link)
    q = urllib.parse.parse_qs(item.query)
    target = urllib.parse.urlparse(q['u'][0])
    filename = os.path.basename(target.path)
    
    urllib.request.urlretrieve(link,os.path.join("images",filename))
    print("Storing"+filename)
    time.sleep(3)

print("goooooooood...")