
#while循环以及循环控制条件break,continue

sign = 10

while sign:
    sign -= 1
    print(sign)


user_input = '初始化文字'
while user_input :
    user_input = input('请输入你想输入的东西:\t')
    if user_input == '结束':
        print('程序结束!')
        break
    else:
        print('你说了:\t'+user_input)



number = 10

while number:
    number -= 1
    if number % 2 == 0:
        print('偶数:\t'+str(number))
        continue
    print('奇数:\t'+ str(number))
