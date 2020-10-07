#json



#json.dump()存储json数据，接收两个参数 要存储的数据以及用于存储数据的文件对象

#用法:
import json

numbers = [1,3,4,6,7]
file_name = 'numbers.json'
with open(file_name,'w') as f_object:
    json.dump(numbers,f_object)