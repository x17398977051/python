#元组 指的是一系列不可改变的值的总和

season_list = ('春','夏','秋','冬')

#使用索引来访问
spring = season_list[0]
print(spring)

#可迭代
for season in season_list:
    print('当前是: '+season)


#元组本身可以修改

season_list = ('spring','summer','autumn','winter')
first_element = season_list[0]
print(first_element)
