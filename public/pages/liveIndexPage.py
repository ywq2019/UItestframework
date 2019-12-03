# coding=utf-8
from selenium.webdriver.common.keys import Keys
from public.common import basepage
from public.common.pyselenium import logger


class liveIndexPage(basepage.Page):


    def into_live_page(self):
        """live首页"""
        self.dr.open('http://liveadmin-test.61info.cn/#/login')
        logger.info("into live page")

    def input_phone_number(self, values):
        """输入手机号"""
        self.dr.clear_type('name->username', values, Keys.ENTER)

    def input_password(self, values):
        """输入密码并登录"""
        self.dr.clear_type('name->password', values, Keys.ENTER)
