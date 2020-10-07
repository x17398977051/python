#open() 接受一个参数:要打开的文件名 返回一个文件对象
#with 表示在不再需要访问文件后将其关闭
#read()方法表示读取文件的全部内容，read函数读取到文件末尾时会返回一个空字符串

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)