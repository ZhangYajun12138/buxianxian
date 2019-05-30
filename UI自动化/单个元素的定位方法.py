#coding=utf-8

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://bing.com')
# driver.find_elements_by_id('sb_form_q').
# sleep(1)
# driver.find_element_by_name('q').send_keys('byname')
# sleep(1)
# driver.find_element_by_class_name('b_searchbox').send_keys('byclassname')
# sleep(1)
# driver.find_elements_by_tag_name('input').send_keys('bytagname')
# sleep(1)
# driver.find_element_by_css_selector('input#sb_from_q').send_keys('bycssselector')
# sleep(1)
# driver.find_element_by_xpath('//input[@class="b_searchbox"]').send_keys('byxpath')
# sleep(1)
driver.find_element_by_link_text('学术').click()
sleep(1)
driver.back()
driver.find_element_by_partial_link_text('词').click()
sleep(1)
driver.quit()