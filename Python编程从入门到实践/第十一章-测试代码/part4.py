#使用setUp()函数简化测试代码

#setUp() 的作用:如果在TestCase类种定义了setUp()方法，Python将最先运行它

import unittest
from part2 import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = '你最先说的是哪种语言?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['javaScript','Python','Node.js']

    '''针对AnonymousSurvey的测试代码,测试函数必须以test开头'''
    def test_store_single_response(self):

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)


    '''多次测试'''
    def test_store_three_response(self):
        for res in self.responses:
            self.my_survey.store_response(res)
            self.assertIn(res,self.my_survey.responses)

unittest.main()