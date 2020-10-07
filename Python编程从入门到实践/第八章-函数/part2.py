#import 关键字可以导入模块
#import model 的意思是打开model文件,并将model文件所有的代码都复制到当前文件里
import model

#导入特定的函数
from model import make_pizza


#使用 as 可以为 模块或者函数指定别的名字

# from model import make_pizza as mk_food


#导入模块中所有函数
# from model import *