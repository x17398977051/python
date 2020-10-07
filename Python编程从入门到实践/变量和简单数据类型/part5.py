citys = ['北京','上海','郑州','湖州']


#列表的顺序从0开始,也就是说 0对应的是列表的第一位数字

#取值
first_element = citys[0]
second_element = citys[1]
third_element = citys[2]
#...
print(first_element,second_element,third_element)

#特殊用法 -1 代表反方向的第一个元素,即为列表的最后一个元素
last_element = citys[-1]
print(last_element)


#列表的增删改

schools = ['华北水利水电大学','郑州轻工业大学','郑州大学','河南财经政法大学']
#append()将元素添加到列表末尾
schools.append('河南工程学院')
print(schools)
#insert() 可在列表任意位置插入新元素，这种操作将插入位置之后的每个元素都像右移了一位
schools.insert(0,'郑州航空工业管理学院')
print(schools)
#del 根据列表索引从列表中删除元素
del schools[1]
print(schools)
#pop() 从列表中删除指定索引的元素，并返回他的值,默认删除最后一个
is_poped = schools.pop()
print(is_poped,schools)
#remove()根据值删除元素
schools.remove("郑州轻工业大学")
print(schools)
