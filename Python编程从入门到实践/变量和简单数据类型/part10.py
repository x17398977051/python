#列表解析

#语法:
    #首先指定一个描述性的列表名(这里是squares);然后,指定一个左方括号,并定义一个表达式,用于生成你要存储的值
    #接下来,编写一个for循环，用于给表达式提供值,再加上右方括号。
squares = [value+2 for value in range(1,11)]
print(squares)
