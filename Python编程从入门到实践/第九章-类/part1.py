#类
#语法: class 你的类名，类名约定俗成的以大写字母开头来表示():

#例子:

class Dog():
    # __init__(self)函数类似于javaScript中的constructor,实例化对象的时候给对象赋值的一个内置函数
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 定义该类的方法
    def sit(self):
        print(f'{self.name}坐下了')



#例子:使用类创建实例

wangcai = Dog('旺财',6)

#实例可以调用类的方法,并具有类实例对象所传递的属性
print(wangcai.name)
wangcai.sit()