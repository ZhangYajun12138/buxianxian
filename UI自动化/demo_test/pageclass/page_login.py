# coding:utf-8

from .basepage import BasePage
from selenium.webdriver.common.by import By
import logging;logging.basicConfig(level=logging.INFO)

class PageLogin(BasePage):

    username_LOCATOR = (By.ID,'name')# 用户名
    password_LOCATOR = (By.ID,'password') # 密码
    rember_username_LOCATOR = (By.CLASS_NAME,'userchecked testlanguage') # 记住账号
    signup_LOCATOR = (By.ID,'signup') # 立即登陆
    forgetpwd_LOCATOR = (By.CLASS_NAME,'lostpossword testlanguage') # 忘记密码
    registerBtn_LOCATOR = (By.CLASS_NAME,'registerBtn') # 马上去注册

    def open_page_login(self,url):
        self.openpage(url)

    def
