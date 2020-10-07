#函数语法: def 函数名:




#不确定有多少个参数的时候，可以使用 *形参名 方式,使得所有传入的参数为一个元组结构
def make_pizza(*something):
    print(something)


make_pizza('鱿鱼丝','果酱','番茄')
make_pizza('面包','黄油')