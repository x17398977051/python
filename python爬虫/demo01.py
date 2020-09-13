
import requests; #导入爬虫包
from bs4 import BeautifulSoup
link = 'http://santostang.com' #定义需要爬取的网址
headers = {
    'User-Agent':'Mozilla/5.0 (windows; U; Windows NT6.1; en-US; rv:1.9.1.6) GECKO/20091201 fIREFOX/3.5.6'
}
r = requests.get(link,headers=headers)
soup = BeautifulSoup(r.text,'html.parser')#使用 BeautifulSoup解析html文件
title = soup.find('h1',class_="post-title").a.text.strip()
print(title)

with open('title_test.txt','a+') as f:
    f.write(title)