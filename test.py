
from selenium import webdriver
from selenium.webdriver.common.by import By
from public.common import basepage


class  test(basepage.Page):

    def test1(self):
        base_url = 'https://mail.qq.com/'
        username = '2528229762'  # qq号码
        password = 'ZXcvbnm.123.'  # qq密码
        self.dr.get(base_url)
        self.dr.open.frame('login_frame') #切换到登录窗口的iframe
        self.dr.find_element(By.ID, "u").send_keys(username) #输入账号
        self.dr.find_element(By.ID, "p").send_keys(password) #输入密码
        self.dr.find_element(By.ID, "login_button").click()  #点击登录

def run():
    test().test1()

if __name__=='__mian__':
    run()