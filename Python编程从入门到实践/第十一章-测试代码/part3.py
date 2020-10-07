import unittest
from part2 import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey的测试代码,测试函数必须以test开头'''
    def test_store_single_response(self):
        question = '你最先说的是哪种语言?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)


    '''多次测试'''
    def test_store_three_response(self):
        question = '您会多少种语言?'
        my_survey = AnonymousSurvey(question)
        responses = ['javaScript','Python','Node.js']
        for res in responses:
            my_survey.store_response(res)
            self.assertIn(res,my_survey.responses)

unittest.main()