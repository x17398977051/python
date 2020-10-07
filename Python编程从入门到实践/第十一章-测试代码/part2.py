#测试类
class AnonymousSurvey():
    '''收集匿名调查问卷的答案'''
    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_response(self,new_response):
        '''存储单份调查答卷'''
        self.responses.append(new_response)

    def show_results(self):
        print('Servey results:')
        for res in self.responses:
            print('-' + res)