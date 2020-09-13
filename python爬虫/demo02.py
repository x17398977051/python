import requests
key_dict = {'key1':'value1','key2':'value2'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Host':'www.santostang.com'
}
r = requests.get('http://www.santostang.com/',params=key_dict)
print('文本编码:',r.encoding)
print('响应状态码:',r.status_code)
print('请求URL：',r.url)
# print('字符串方式的响应体:',r.text)