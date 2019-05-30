#coding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
# driver.get(r'D:\张亚军\WEB测试\Python File\学习了\接口自动化\test2.html')
# menu = driver.find_element_by_link_text('link1')
# webdriver.ActionChains(driver).move_to_element(menu).perform()
# sleep(1)
# WebDriverWait(driver,1).until(lambda dr:dr.find_element_by_class_name('dropdownlist').is_displayed)
#
# droplists = driver.find_element_by_class_name("dropdownlist").find_elements_by_tag_name('li')
# for li in droplists:
#     webdriver.ActionChains(driver).move_to_element(li).perform()
#     sleep(1)
#

driver.get('https://www.baidu.com')
setting = driver.find_element_by_link_text('设置')
webdriver.ActionChains(driver).move_to_element(setting).perform()
sleep(1)
WebDriverWait(driver,10).until(lambda dr:dr.find_element_by_class_name('bdnuarrow').is_displayed)
sleep(1)
# setting_list2 = driver.find_element_by_link_text('高级搜索').click()
# print(setting_list2)
setting_list1 = driver.find_element_by_link_text('搜索设置').click()
print(setting_list1)
sleep(1)
driver.quit()