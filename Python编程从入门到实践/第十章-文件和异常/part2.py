#逐行读取

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())


#使用with关键字时,open()返回的文件对象只能在with代码块内使用。可以使用一个变量把每行内容存储起来
lines = []

with open(file_name) as file_object:
    lines = file_object.readlines()
    print(lines)

for line in lines:
    print(line)