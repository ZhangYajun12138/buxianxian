#coding=utf-8
#input标签上传图片

from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.get(r'D:\张亚军\WEB测试\Python File\学习了\接口自动化\test3.html')
dr.implicitly_wait(60)
iframe1=dr.find_element_by_id('iframe1')
dr.switch_to.frame(iframe1)

# dr.find_element_by_id('kw').send_keys('test')
# dr.find_element_by_id('su').click()
dr.find_element_by_class_name('soutu-btn').click()
dr.find_element_by_css_selector("input[type='file']").send_keys(r'D:\张亚军\WEB测试\Python File\学习了\接口自动化\16.jpg')
sleep(1)

# dr.switch_to.default_content()
# dr.find_element_by_id('bing').click()
# sleep(1)
#
# dr.quit()