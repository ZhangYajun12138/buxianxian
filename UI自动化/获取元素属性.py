#coding=utf-8

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://cn.bing.com')

#打印logo文字
print("text of logo is",driver.find_element_by_class_name('hp_sw_logo').text)

search_box = driver.find_element_by_class_name('b_searchbox')
search_box.send_keys('selenium')
sleep(1)
search_box.clear()
sleep(1)
search_box.send_keys('apple')
sleep(1)
print('tag is',search_box.tag_name)
print('id is',search_box.id)
print('title is',search_box.get_attribute('title'))
print('searchbox isenabled',search_box.is_enabled())
print('searchbox displayed',search_box.is_displayed())
print('searchbox selected',search_box.is_selected())
button = driver.find_element_by_id('sb_form_go')
# button.submit()
# driver.quit()