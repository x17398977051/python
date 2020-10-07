#异常


#使用try-except代码块


#ZeroDivisionError 分母为0异常
try:
    print(5/0)
except ZeroDivisionError:
    print('Error:你不能用0作为分母,这是没有意义的一件事')
else:
    print('不出错误我会执行!')



#FileNotFoundError文件读取异常

file_name = 'alien.txt'

try:
    with open(file_name) as file_object:
        print(file_object.readlines())
except FileNotFoundError:
    print('文件不存在')
else:
    print('文件加载成功!')

#pass 语句可以跳过代码块，意为什么都不要做!