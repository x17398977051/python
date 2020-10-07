class Car ():
    '''通用汽车类'''
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year

    def get_details(self):
        details = f'一辆名叫:{self.name}的{self.model}牌子的,产自于{str(self.year)}年的汽车'
        print(details)