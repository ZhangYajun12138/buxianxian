#coding=utf-8
#切换窗口

from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.get('http://www.baidu.com')
dr.find_element_by_link_text('登录').click()
sleep(2)
dr.find_element_by_link_text('立即注册').click()
sleep(2)
origin_handle = dr.current_window_handle
print('当前窗口title：',dr.title)
handles = dr.window_handles

for handle in handles:
    if handle != origin_handle:
        dr.switch_to.window(handle)
        sleep(2)
        print('当前窗口title:',dr.title)
dr.switch_to.window(origin_handle)
print('当前窗口title：',dr.title)
sleep(2)
dr.quit()