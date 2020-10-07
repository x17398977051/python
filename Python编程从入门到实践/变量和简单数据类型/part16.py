user_0 = {
    'username':'谢绝',
    'first':'谢',
    'last':'绝'
}

#遍历字典
print( user_0.items())
#user_0.items() 返回的是一个列表:dict_items([('username', '谢绝'), ('first', '谢'), ('last', '绝')])
for key,value in user_0.items():
    print('key: '+key+' - '+'value: '+value)


#遍历字典中的所有键 类似javaScript中的Object.keys()
print(user_0.keys()) #dict_keys(['username', 'first', 'last'])
for key in user_0.keys():
    print(key)


#字典总是明确的记录着键和值，但是获取字典元素的顺序时,获取顺序时不可预测的。
#如果想要按顺序来获取字典中的键,则可以使用sorted

favorite_languages = {
    'XieZhanPeng':'JavaScript Python',
    'SongYuanXi':'Java Perl',
    'SongCi': 'Java Perl',
    'XieJue':'Node.js Ruby'
}

for name in sorted(favorite_languages.keys()):
    print('--->'+name)

#遍历字典中所有的值
for language in favorite_languages.values():
    print('语言: '+language)

#使用集合剔除无用项,集合中的每个元素都是独一无二的

print(set(favorite_languages.values())) #{'JavaScript Python', 'Node.js Ruby', 'Java Perl'}

