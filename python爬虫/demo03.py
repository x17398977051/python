import requests
key_dict = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data=key_dict)
print(r.text)