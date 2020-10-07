import make_name
import unittest

class NameTestCase(unittest.TestCase):
    '''测试format_name'''
    def test_first_last_name(self):
        '''能够正确处理名字吗'''
        formatted = make_name.format_name('jam','xie')
        self.assertEqual(formatted,'Jam Xie')


unittest.main()