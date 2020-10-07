#input()函数是可以让用户在终端输入内容的一个函数,返回值是一个字符串


name = input('What is your name?\n')
print('Your name is:\t'+name)


#使用 int()方法可以将输入类型为字符串类型的数字转化为数字类型

age = int(input('How old are you?'))
if age >= 18:
    print('成年人')
else:
    print('未成年')