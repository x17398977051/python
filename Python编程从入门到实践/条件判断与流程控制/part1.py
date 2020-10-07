cars = ['audi','bmw','toyota','subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('Applaction is done')


# 每条if语句的核心都是一个值为 True 或者 False 的表达式,这种表达式被称为 “条件测试”
# Python语句根据 True 还是 False 执行对应语句块中的语句



#条件判断
#相等 ==
#不相等 !=
#逻辑与 and
#逻辑或 or
#逻辑非 not

#检查特定值是否包含在列表内用关键字 in
one_car = '亚洲龙!'
print(one_car in cars) #False

#检查特定值是否不包含在列表中使用关键字 not in

print(one_car not in cars) #True
