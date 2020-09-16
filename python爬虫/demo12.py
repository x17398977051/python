# 爬一下读者官网的数据
import requests
import json

url = 'https://www.duzhe.com/home/reader/magazine/list'
headers = {
    'Referer': 'https://www.duzhe.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}
offset = 1;
#使用requesrts库发送post请求时,如果传递参数是json格式的,需要指定json=xxx,而不是post=xxx,否则会报错!
def get_magzine(page,collection):
    key_dict = {'current': page, 'size': '12', 'month': '', 'year': ''}
    response = requests.post(url=url, headers=headers, json=key_dict)
    json_data = json.loads(response.text)
    json_magzine_list = json_data['data']['records']
    for mag in json_magzine_list:
        collection.append(mag)


def get_magzine_all():
    magzine_collection = []
    for num in range(1,61):
        get_magzine(num,magzine_collection)

    return magzine_collection

print(get_magzine_all())
