# coding:utf-8
# 启动浏览器函数封装

from selenium import webdriver

def launch_brower(brower_name):
    if brower_name.lower() == 'chrome':
        return webdriver.Chrome()
    elif brower_name.lower() == 'ie':
        return webdriver.Ie()
    elif brower_name.lower() == 'firefox':
        return webdriver.Firefox()
    else:
        raise Exception("sorry,该浏览器不在启动范围内，请安装驱动并修改launch_browser函数")