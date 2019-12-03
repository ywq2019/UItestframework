#coding=utf-8
import time
from public.common import publicfunction


class Page(object):
    """
    This is a base page class for Page Object.
    """
    def __init__(self, selenium_driver):
        self.dr = selenium_driver

#执行截图操作
    def do(self, func, *args):
        if args is not None:
            func(args)
        else:
            func()
        publicfunction.get_img(self.dr, '%s-%s.jpg' % (func.__name__, time.strftime('%Y-%m-%d_%H_%M_%S')))



