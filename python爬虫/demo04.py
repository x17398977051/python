#设置爬虫超市时间
import requests
link = 'http://www.santostang.com/'
r = requests.get(link,timeout=0.001)