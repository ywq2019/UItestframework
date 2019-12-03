#coding=utf-8
from time import sleep
from public.common import mytest
from public.pages import liveIndexPage




class TestliveIndex(mytest.MyTest):
    """live后台登录"""


    def test_LIVE_orign(self):
        """live后台登录"""
        livepage = liveIndexPage.liveIndexPage(self.dr)
        livepage.into_live_page()
        sleep(2)
        # livepage.input_phone_number('zhongyanping')
        livepage.do(livepage.input_phone_number, 'zhongyanping')
        sleep(2)
        # livepage.input_password('123456')
        livepage.do(livepage.input_password, '123456')
        sleep(5)



