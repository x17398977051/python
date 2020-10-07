#例子1:通过函数range()创建一个列表，其中包含1~20以内的奇数
for num in range(1,22,2):
    print('奇数: '+str(num))
#例子2:通过列表解析创建存储每个数字的立方

cubes = [value**3 for value in range(1,10)]
print(cubes)