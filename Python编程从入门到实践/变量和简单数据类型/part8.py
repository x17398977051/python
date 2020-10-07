#遍历整个列表
dogs = ['柴犬','哈士奇','阿拉斯加','德牧','秋田犬','中华神犬']
for dog in dogs:
    message = '这个'+ dog +'加载完毕!'
    print(message)
print('所有的狗子加载完毕!')


#创建数值列表
#range()能让你轻松的生成一系列的数字。
for value in range(1,5):
    print('当亲value:'+str(value))



#直接使用list() 将range()转换成列表

range_to_list = list(range(1,11))
print(range_to_list)


#range()指定步长。
#range(1,10,2)指定步长为2,即每次增加2,直到最后的数字超出或等于10结束;
step2_range_to_list = list(range(1,10,2))
print(step2_range_to_list)
