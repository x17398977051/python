import requests
import json

titles = []
abstracts = []
images = []

headers = {
    'Referer': 'https://www.toutiao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
link = 'https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A175DFE52D1E1CD&cp=5F5D1E316CDDBE1&_signature=_02B4Z6wo00f01W7lXWAAAIBCd7u7VkdKTBFu5VnAAATl8e'
r = requests.get(link, headers=headers, timeout=5)
json_string = r.text
json_data = json.loads(json_string) #json.loads解析json格式数据
for abs in json_data['data']:
    print(abs.get('abstract','None'))
    if abs.get('abstracts','None') != 'None':
        abstracts.append(abs['abstract'])
    if abs.get('image_url','None') != 'None':
        images.append(abs['image_url'])
    if abs.get('title','None') != 'None':
        titles.append(abs['title'])

print(titles)
print(abstracts)
print(images)