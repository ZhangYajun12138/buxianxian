#coding=utf-8
#elements表示操作一组元素

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get(r'D:\张亚军\WEB测试\Python File\学习了\接口自动化\test.html')

inputs = driver.find_elements_by_tag_name('input')
for inputtag in inputs:
    if inputtag.get_attribute('type') == 'checkbox':
        inputtag.click()
sleep(1)

checkboxs = driver.find_elements_by_css_selector('input[type=checkbox]')
print('the num of checkbox is',len(checkboxs))
for checkbox in checkboxs:
    checkbox.click()
sleep(1)

driver.find_elements_by_css_selector('input[type=radio')[-1].click()
driver.find_elements_by_css_selector('input[type=checkbox]')[1].click()
sleep(1)

driver.quit()