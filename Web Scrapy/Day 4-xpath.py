import  requests
from lxml import etree
url='http://www.dxy.cn/bbs/thread/626626#626626'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
x= requests.get(url, headers=headers, timeout=3)
x.encoding=x.apparent_encoding
wb_data=x.text
html = etree.HTML(wb_data)#源码分析
data=[]
new_data=[]
result_txt = html.xpath('//td[@class="postbody"]/text()')#找到所需要的数据
print(result_txt)
result_name=html.xpath('//div[@class="auth"]/a/text()')
print(result_name)
for i in range(0,4):
    data.append(result_name[i]+"###"+result_txt[i])
for i in data:
    x=i.replace("\n","").replace("\t","").replace(" ","")
    new_data.append(x)
print(new_data)

import urllib.request
from lxml import etree
def main():
    data = []
    s1 = '//div[@class="auth"]/a/text()'
    s2 = '//div/table/tbody/tr/td[@class="postbody"]/text()'
    url = 'http://www.dxy.cn/bbs/thread/626626'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    request = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(request).read().decode("utf-8")
    # 解析HTML文件为HTML DOM模型
    content = etree.HTML(html)
    userNames = content.xpath(s1)
    cons = content.xpath(s2)
    for user, con in userNames, cons:
        data.append((userNames, con))
    print(data)

if __name__ == '__main__':
    main()
