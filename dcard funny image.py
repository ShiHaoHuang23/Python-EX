import json,time,os,requests,random
import urllib.request

api_url = "http://www.dcard.tw/_api/forums/funny/posts?limit=100"
res = requests.get(api_url).text
data = json.loads(res)

for post in data:
    if len(post["media"])>0:
        for image in post["media"]:
            imgurl = image["url"]
            print(imgurl)
            if ".jpg" in imgurl or ".png" in imgurl:
                urllib.request.urlretrieve(imgurl,os.path.join("mypics",os.path.basename(imgurl)))
                time.sleep(random.randint(3,5))