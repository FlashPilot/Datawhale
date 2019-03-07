import requests
url = 'https://www.baidu.com'
reponse = request.get(url)
print(reponse)

from urllib.request import urlopen
import re

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

res1 = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)
print("\nPage paragraph is: ", res1[0])

# Find all links.
res2 = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res2)
