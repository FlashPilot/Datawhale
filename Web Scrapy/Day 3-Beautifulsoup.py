import re, requests
from bs4 import BeautifulSoup
url = 'http://www.dxy.cn/bbs/thread/626626#626626'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome
r = requests.get(url, headers = headers)

soup = BeautifulSoup(r.text, 'lxml')
soup.link, soup.link.name, soup.link['media'], soup.link.attrs
soup.title.string, soup.title.string.replace_with
soup.name

replies = {}
ids = []
for reply_id in soup.find_all("div", "auth'):
    ids.append(reply_id.a.contents[0])
    
reply_conts = []
for rid, reply_cont in enumerate(soup.find_all("td", "post"):
    temp = ""
    for content in reply_cont.contents:
        if content.name != 'br' and content.name != 'a':
            temp += content.strip()
        elif content.name == 'a':
            temp += content['href']
     
    replies[ids[rid]] = temp
print(replies)
