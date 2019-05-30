# coding:utf-8

from selenium import webdriver

dr = webdriver.Chrome()
dr.get("http://www.baidu.com")

assert ('百度') in dr.title,'test fail'
dr.find_element_by_id("kw").send_keys('assert')
dr.find_element_by_id("su").click()
print('pass')

assert '111' in dr.title,'test fail'
dr.find_element_by_id("kw").send_keys('assert')
dr.find_element_by_id("su").click()
print('pass')

dr.quit()